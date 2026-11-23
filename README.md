# Agentic AI Workshop

A slide-led, self-paced GitHub Pages workshop following the two Microsoft Learn
GH-600 learning paths. Join Michelle and Coda to explore agent architecture,
tools, orchestration, memory, evaluation, and governance.

**Workshop:** <https://codess-aus.github.io/Agentic-AI-Developer-Course/>

## Run locally

Use Python 3.12 or newer:

```bash
# Keep the workshop's Python dependencies isolated.
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m mkdocs serve
```

Open the local address printed by MkDocs. For a production build and structural checks:

```bash
python -m mkdocs build --strict
python -m unittest discover -s tests -v
```

## Publish

In **Settings > Pages > Build and deployment**, select **GitHub Actions**.
The `Workshop Pages` workflow validates pull requests and publishes pushes to
`main`. It can also be started manually from the Actions tab. Only the deployment
job receives Pages write permissions. Configure any required deployment reviewers
on the `github-pages` environment.

## Edit the workshop

- `docs/index.md`: welcome, prerequisites, and module map.
- `docs/chapters/`: one Markdown lesson per slide, in presenter-script order.
- `docs/resources.md`: original learning paths, GitHub references, and author links.
- `mkdocs.yml`: lesson order, theme, search, and social links.
- `overrides/main.html`: shared hero and Previous / Home / Next navigation.
- `hooks/slides.py`: responsive WebP heroes generated only into the build output.
- `docs/stylesheets/workshop.css`: slide-inspired colors and responsive layout.
- `GH-600 presenter scripts.md`: the original content guide, preserved unchanged.

Each slide is assigned once through a page's `hero` metadata. Include descriptive
`hero_alt` text and explain the visual's teaching points in the lesson body.
Keep examples scoped to a disposable practice repository. Product capabilities
vary by Copilot surface, plan, and organization policy; link to current GitHub
documentation instead of presenting workshop guardrails as universal platform limits.

Mona Sans is self-hosted under its SIL Open Font License in
`docs/assets/fonts/OFL.txt`, from the official `github/mona-sans` source at
revision `4bc6ba8b354c36b4fb66d32cd67b4c1f2beb0a06`.
No external font service or analytics is required. Original PNG slides remain
unchanged; the build generates smaller WebP variants without cropping the artwork.

Material for MkDocs currently announces end of life on May 5, 2027, with critical
and security fixes until then. This workshop uses its current stable MkDocs theme;
review the upstream maintenance status before that date.
