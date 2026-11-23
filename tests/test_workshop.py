"""Check the slide-to-page contract and the built workshop's navigation."""

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

import yaml
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"


class PageParser(HTMLParser):
    def __init__(self, content):
        super().__init__()
        self.tags = []
        self.feed(content)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


def workshop_pages():
    for source in (DOCS / "index.md", *sorted((DOCS / "chapters").glob("*.md"))):
        frontmatter = source.read_text().split("---", 2)[1]
        yield source, yaml.safe_load(frontmatter)


def built_page(source):
    relative = source.relative_to(DOCS)
    if relative.name == "index.md":
        return SITE / relative.with_suffix(".html")
    return SITE / relative.with_suffix("") / "index.html"


class WorkshopTests(unittest.TestCase):
    def test_every_original_slide_is_assigned_exactly_once(self):
        originals = {path.name for path in (DOCS / "assets").glob("*.png")}
        assignments = Counter(meta["hero"] for _, meta in workshop_pages())
        self.assertEqual(len(originals), 42)
        self.assertEqual(set(assignments), originals)
        self.assertTrue(all(count == 1 for count in assignments.values()))
        self.assertEqual(len(list((DOCS / "chapters").glob("*.md"))), 41)

    def test_heroes_are_accessible_responsive_and_bounded(self):
        for source, meta in workshop_pages():
            with self.subTest(page=source.name):
                parser = PageParser(built_page(source).read_text())
                heroes = [
                    attrs
                    for tag, attrs in parser.tags
                    if tag == "img" and attrs.get("fetchpriority") == "high"
                ]
                self.assertEqual(len(heroes), 1)
                hero = heroes[0]
                self.assertEqual(hero["alt"], meta["hero_alt"])
                self.assertGreater(len(hero["alt"]), 40)
                self.assertIn("sizes", hero)
                variants = hero["srcset"].split(", ")
                self.assertGreaterEqual(len(variants), 2)
                for variant in variants:
                    url, width = variant.rsplit(" ", 1)
                    image_path = built_page(source).parent / unquote(url)
                    self.assertTrue(image_path.is_file(), image_path)
                    with Image.open(image_path) as image:
                        self.assertEqual(image.width, int(width[:-1]))
                    if width == "640w":
                        self.assertLess(image_path.stat().st_size, 250_000)

    def test_all_pages_have_previous_home_and_next(self):
        sources = [source for source, _ in workshop_pages()] + [DOCS / "resources.md"]
        for index, source in enumerate(sources):
            with self.subTest(page=source.name):
                parser = PageParser(built_page(source).read_text())
                dialogs = [
                    attrs for _, attrs in parser.tags if attrs.get("role") == "dialog"
                ]
                self.assertTrue(dialogs)
                self.assertTrue(all(dialog.get("aria-label") for dialog in dialogs))
                links = [attrs for tag, attrs in parser.tags if tag == "a"]
                for direction in ("prev", "next"):
                    matches = [link for link in links if link.get("rel") == direction]
                    self.assertEqual(len(matches), 1)
                    offset = -1 if direction == "prev" else 1
                    expected = built_page(sources[(index + offset) % len(sources)]).parent
                    target = built_page(source).parent / unquote(matches[0]["href"])
                    self.assertEqual(target.resolve(), expected.resolve())
                self.assertTrue(
                    any(link.get("aria-label") == "Back to workshop Home" for link in links)
                )
                modes = [
                    attrs.get("title", "") + attrs.get("aria-label", "")
                    for tag, attrs in parser.tags
                    if tag == "label"
                ]
                self.assertTrue(any("dark mode" in mode for mode in modes))
                self.assertTrue(any("light mode" in mode for mode in modes))

    def test_built_internal_links_and_images_exist(self):
        self.assertTrue((SITE / "index.html").is_file(), "Build the site before testing")
        for html in SITE.rglob("*.html"):
            parser = PageParser(html.read_text())
            for tag, attrs in parser.tags:
                url = attrs.get("href") if tag == "a" else attrs.get("src")
                if not url:
                    continue
                parsed = urlsplit(url)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                # The custom 404 page uses site-root URLs on GitHub Pages.
                path = unquote(parsed.path)
                if path.startswith("/Agentic-AI-Developer-Course/"):
                    target = SITE / path.removeprefix("/Agentic-AI-Developer-Course/")
                elif path.startswith("/"):
                    target = SITE / path.lstrip("/")
                else:
                    target = html.parent / path
                self.assertTrue(target.exists(), f"{html.relative_to(SITE)} -> {url}")

    def test_resources_preserve_both_presenter_references(self):
        script = (ROOT / "GH-600 presenter scripts.md").read_text()
        references = re.findall(r"https://learn\.microsoft\.com/[^)]+", script)
        self.assertEqual(len(references), 2)
        resources = (DOCS / "resources.md").read_text()
        for reference in references:
            self.assertIn(reference, resources)
        for domain in ("scaling-guacamole.com", "linkedin.com", "bsky.app", "youtube.com"):
            self.assertIn(domain, resources)


if __name__ == "__main__":
    unittest.main()
