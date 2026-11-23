"""Build responsive slide derivatives without changing the original artwork."""

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image

_slides = {}


def on_pre_build(config):
    _slides.clear()


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
