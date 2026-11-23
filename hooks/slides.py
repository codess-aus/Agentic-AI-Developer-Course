"""Build responsive slide derivatives without changing the original artwork."""

from concurrent.futures import ThreadPoolExecutor
from html import escape
from pathlib import Path

from mkdocs.structure.pages import Page
from mkdocs.utils import get_relative_url
from mkdocs.utils.meta import get_data
from PIL import Image

GALLERY_MARKER = "<!-- chapter-gallery -->"
THUMBNAIL_WIDTH = 640

_slides = {}
_nav = None


def on_pre_build(config):
    _slides.clear()


def on_nav(nav, config, files):
    global _nav
    _nav = nav
    return nav


def _gallery_card(chapter, page, config):
    # Other pages' front matter is not parsed yet, so read it directly.
    _, meta = get_data(Path(chapter.file.abs_src_path).read_text(encoding="utf-8"))
    with Image.open(Path(config.docs_dir) / "assets" / meta["hero"]) as image:
        height = round(image.height * THUMBNAIL_WIDTH / image.width)
    thumbnail = f"assets/slides/{chapter.file.name}-{THUMBNAIL_WIDTH}.webp"
    number = chapter.file.name.split("-", 1)[0]
    # The image is decorative: the link text already names the chapter.
    return (
        f'<li><a class="chapter-thumb" href="{escape(get_relative_url(chapter.url, page.url))}">'
        f'<img src="{escape(get_relative_url(thumbnail, page.url))}" alt="" '
        f'width="{THUMBNAIL_WIDTH}" height="{height}" loading="lazy" decoding="async">'
        f'<span class="chapter-thumb__number">Chapter {number}</span>'
        f'<span class="chapter-thumb__title">{escape(chapter.title)}</span>'
        "</a></li>"
    )


def on_page_markdown(markdown, page, config, files):
    if GALLERY_MARKER not in markdown:
        return markdown

    sections = []
    for section in _nav.items:
        chapters = [item for item in section.children or [] if isinstance(item, Page)]
        if not chapters:
            continue
        cards = "".join(_gallery_card(chapter, page, config) for chapter in chapters)
        sections.append(
            f"### {section.title}\n\n"
            f'<ul class="chapter-gallery">{cards}</ul>\n'
        )
    return markdown.replace(GALLERY_MARKER, "\n".join(sections))


def on_page_context(context, page, config, nav):
    if "hero" not in page.meta:
        return context

    source = Path(config.docs_dir) / "assets" / page.meta["hero"]
    with Image.open(source) as image:
        width, height = image.size

    variants = [
        {
            "url": f"assets/slides/{page.file.name}-{size}.webp",
            "width": size,
        }
        for size in sorted({min(size, width) for size in (640, 1280, width)})
    ]
    _slides[source] = variants
    context.update(
        hero_sources=variants,
        hero_width=width,
        hero_height=height,
    )
    return context


def on_post_build(config):
    def render_slide(item):
        source, variants = item
        with Image.open(source) as image:
            for variant in variants:
                width = variant["width"]
                height = round(image.height * width / image.width)
                destination = Path(config.site_dir) / variant["url"]
                destination.parent.mkdir(parents=True, exist_ok=True)
                # Resize the entire slide, never crop text or diagram content.
                resized = image.resize((width, height), Image.Resampling.LANCZOS)
                resized.save(destination, "WEBP", quality=86, method=4)

    # Propagate encoding errors so broken hero assets fail the build.
    with ThreadPoolExecutor(max_workers=4) as executor:
        list(executor.map(render_slide, _slides.items()))
