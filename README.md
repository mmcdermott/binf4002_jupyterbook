# BINF 4002 — Machine Learning for Health (Jupyter Book)

A Sphinx-based Jupyter Book for the Spring 2026 BINF 4002 course at Columbia DBMI. Each lecture chapter is a student-facing review page that ends with a Study guide section (key terms, self-check questions, curated external resources); companion notebooks are first-class child pages that render with their original outputs; all 17 course labs are first-class chapters in their own Part. Every notebook page ships **"Open in Colab"** and **"Open in Binder"** launch buttons (active once this repo is public on GitHub).

## What's in this repo

```
.
├── pyproject.toml             # uv-managed dependencies (Jupyter Book pinned to <2.0)
├── book/                      # the book source tree
│   ├── _config.yml            #   Sphinx + Jupyter Book config (repo URL, launch buttons, …)
│   ├── _toc.yml               #   table of contents
│   ├── intro.md               #   landing page
│   ├── syllabus.md            #   full canonical hierarchical syllabus
│   ├── concept_map.md         #   prerequisite graph + 6 through-lines + interactive mind map
│   ├── concept_mindmap.html   #   the rendered Markmap (iframe target)
│   ├── parts/                 #   one overview page per Part (Parts 1-6)
│   ├── lectures/              #   28 lecture pages (each with a Study guide section) + 12 companion notebooks
│   └── labs/                  #   17 lab notebooks + an overview page
├── Lectures/                  # full per-lecture source bundle (PPTX/TeX/PDFs/figures/notebooks)
├── Labs/                      # canonical lab notebooks + solutions
├── .github/workflows/         # GitHub Actions deploy workflow
├── LICENSE-MIT, LICENSE-CC-BY-4.0
└── README.md                  # this file
```

The **`book/`** subtree is what `jupyter-book` builds. The **`Lectures/`** and **`Labs/`** subtrees are the original, ungroomed source bundle (full PPTX, LaTeX source, figures) — kept here so the repo is self-contained and students can clone the entire course in one go.

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

`book/_config.yml` is already set to point at this repository:

```yaml
repository:
  url: https://github.com/mmcdermott/binf4002_jupyterbook
  path_to_book: book
  branch: main
```

Once the repo is **public** on GitHub:

- **Each notebook page gets a rocket icon** at the top right that opens the notebook directly in Google Colab.
- **Each notebook page also gets a Binder option** (free, no GPU, slower than Colab).
- **Each markdown page gets an edit pencil** linking to the source on GitHub.

The Colab launcher constructs URLs of the form
`https://colab.research.google.com/github/mmcdermott/binf4002_jupyterbook/blob/main/book/labs/lab0_preprocessing.ipynb`
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

`book/_config.yml` sets `execute.execute_notebooks: "off"` — the *released* (pre-executed) notebooks ship with their original outputs and render as-is. To re-execute on build, change to `"force"` (slow, requires kernels) or `"cache"` (re-uses cached outputs).

## License

Course content (lecture text, syllabus, mind map) is licensed under [CC BY 4.0](LICENSE-CC-BY-4.0). Code (notebooks, build scripts) is under [MIT](LICENSE-MIT).

## Citing this course

```bibtex
@misc{mcdermott2026binf4002,
  author       = {Matthew McDermott},
  title        = {BINF 4002 — Machine Learning for Health (Spring 2026)},
  year         = {2026},
  howpublished = {\url{https://github.com/mmcdermott/binf4002_jupyterbook}}
}
```

## Acknowledgements

Course materials build on guest lectures from Di Liu (L7) and Florent Pollet (L8), and on the BINF 4002 teaching infrastructure at Columbia DBMI.
