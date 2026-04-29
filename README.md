# BINF 4002 — Machine Learning for Health (Jupyter Book)

A Sphinx-based Jupyter Book for the Spring 2026 BINF 4002 course at Cornell. Each lecture chapter is a student-facing review page; the companion notebooks are first-class child pages that render with their original outputs; all 17 course labs are first-class chapters in their own Part. Every notebook page ships **"Open in Colab"** and **"Open in Binder"** launch buttons (active once this repo is public on GitHub).

> **Sister repo.** A second build of the same course content using **MkDocs Material** lives in a separate sibling repository. That build is search-first and lighter, but does not ship live launch buttons. Use this Jupyter Book build for course delivery to students.

## What's in this repo

```
repo_jupyterbook/
├── pyproject.toml             # uv-managed dependencies (Jupyter Book pinned to <2.0)
├── book/                      # the book source tree
│   ├── _config.yml            #   Sphinx + Jupyter Book config (repo URL, launch buttons, etc.)
│   ├── _toc.yml               #   table of contents (parts → chapters → notebook sub-pages)
│   ├── intro.md               #   landing page
│   ├── syllabus.md            #   full canonical syllabus
│   ├── mind_map.md            #   cross-cutting through-lines
│   ├── syllabus_markmap.md    #   compact Markmap-formatted version
│   ├── questions.md           #   open issues / verification log
│   ├── lectures/              #   28 lecture pages + 14 companion notebooks
│   └── labs/                  #   17 lab notebooks + an overview page
├── Lectures/                  # full per-lecture source bundle (PPTX/TeX/PDFs/figures/notebooks)
├── Labs/                      # canonical lab notebooks + solutions
└── README.md                  # this file
```

The **`book/`** subtree is what `jupyter-book` builds. The **`Lectures/`** and **`Labs/`** subtrees are the original, ungroomed source bundle (full PPTX, LaTeX source, figures, both released and editable forms) — kept here so the repo is self-contained.

## Build / preview locally

```bash
# One-time
uv sync

# Build the book to ./book/_build/html/
uv run jupyter-book build book

# Open the result
xdg-open book/_build/html/index.html
```

To force a clean rebuild:

```bash
uv run jupyter-book clean book && uv run jupyter-book build book
```

## Open in Colab / Open in Binder / Edit on GitHub

`book/_config.yml` ships with placeholder values for the GitHub repository URL:

```yaml
repository:
  url: https://github.com/mmcdermott/BINF4002-2026   # <-- update once the repo exists
  path_to_book: book
  branch: main
```

Replace `mmcdermott/BINF4002-2026` with this repository's actual URL once you push to GitHub. After that:

- **Each notebook page gets a rocket icon** at the top right that opens the notebook directly in Google Colab. Students click → run, no install needed.
- **Each notebook page also gets a Binder option** (free, no GPU, slower than Colab).
- **Each markdown page gets an edit pencil** linking to the source on GitHub.

The Colab launcher constructs URLs of the form
`https://colab.research.google.com/github/<your-user>/<this-repo>/blob/main/book/labs/lab0_preprocessing.ipynb`
automatically — no per-notebook configuration needed.

## Deploy to GitHub Pages

The included GitHub Actions workflow deploys automatically on every push to `main`:

```
.github/workflows/deploy.yml
```

1. Push this repo to GitHub.
2. In the repo settings, under **Pages**, set "Source: GitHub Actions."
3. Push to `main`. The workflow builds the book and publishes `book/_build/html/`.

## Notebook execution policy

`book/_config.yml` sets `execute.execute_notebooks: "off"` — the released (pre-executed) notebooks are rendered as-is, with their original outputs. To re-execute on build, change to `"force"` (slow, requires the right kernels installed) or `"cache"` (re-uses cached outputs).

## License

Course content (text, slides, lecture material) is under [CC BY 4.0](LICENSE-CC-BY-4.0). Code (notebooks, build scripts) is under [MIT](LICENSE-MIT).

## Citing this course

```
@misc{mcdermott2026binf4002,
  author       = {Matthew McDermott},
  title        = {BINF 4002 — Machine Learning for Health (Spring 2026)},
  year         = {2026},
  howpublished = {\url{https://github.com/<your-user>/<this-repo>}}
}
```

## Acknowledgements

Course materials build on guest lectures from Di Liu (L7) and Florent Pollet (L8), and on the BINF 4002 teaching infrastructure at Cornell.
