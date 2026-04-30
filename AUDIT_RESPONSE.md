# Audit response — `BINF4002_jupyterbook_site_audit.md`

A second-LLM review of the site found 7 P0 / P1.x items. The audit was performed against an old `site.zip` snapshot, so several findings are stale. This document tracks how each item was triaged.

## Status legend

- **fixed** — change made in this commit (and earlier commits).
- **stale** — item describes a problem that was already resolved before the audit. No action needed; the audit's `site.zip` predates the fix.
- **wontfix** — disagreement with the audit's recommendation, with reasoning.
- **partial** — addressed in part; full fix deferred or out of scope.

## Findings

| # | Audit finding | Status | Notes |
|---|---|---|---|
| **P0.1** | Missing `mind_map.md` | **stale** | `mind_map.md` was deliberately replaced by `concept_map.md` before the audit ran. `book/concept_map.md` exists and is in the TOC; `mind_map.md` is not referenced anywhere in the current repo. |
| **P0.2** | Missing `concept_map.md` | **stale** | `book/concept_map.md` exists and is the canonical mind-map / through-line page. Linked from the syllabus, intro, and L28. The audit was reading a `site.zip` that did not include this file. |
| **P0.3** | Lecture-table links to `Lectures/...` source folders | **stale** | Already fixed in earlier commit `cf56123`. Every row in "Lectures at a glance" links to `lectures/lecture-NN.md`, an in-book page. The `Lectures/` directory still exists in the repo (full source bundle), but no student-facing page links into it. |
| **P0.4** | Run book-build + link checker in CI | **partial** | A GitHub Actions workflow already exists at `.github/workflows/deploy.yml` that runs `uv run jupyter-book build book` on every push to `main`. A separate dedicated link checker is not yet added. |
| **P1.1** | `book/questions.md` should be removed | **stale** | `book/questions.md` was already removed (not in TOC, not on disk in `book/`). The audit was reading the old zip. |
| **P1.2** | Course-level syllabus says deployment is taught | **fixed** | Level-0 Topic, Summary, and Goal #7 in `book/syllabus.md` now state explicitly that deployment was *not* taught this cycle and is flagged for self-study. L28 page restated to match. |
| **P1.3** | L28 too thin to serve as recap | **fixed** | `book/lectures/lecture-28.md` rewritten as a real recap: course arc paragraph, full TL1-TL6 explanations with cross-references, lecture-to-through-line matrix, "what was not covered" self-study section, and an exam-checklist. |
| **P1.4** | README claims symlinks but ships copies | **stale** | The current `README.md` does not claim symlinks; it describes the layout as it actually is. The audit was reading an older README. |
| **P1.5** | Repo URL placeholder | **stale** | `book/_config.yml` already has `repository.url: https://github.com/mmcdermott/binf4002_jupyterbook` (the real repo). |
| **P1.6** | `.venv` shipped in zip | **stale** | `.venv/` is in `.gitignore`; not in any commit. The audit was reading an export that bundled the local venv. |
| **P1.7** | Notebooks claim outputs but have none | **fixed** | All 12 retained companion notebooks and 13 of 17 lab notebooks now have rendered outputs (committed in `cf56123`). Labs 13 / 14 timed out on heavy training cells; lab 16 has a few errors from a public dataset URL. The README and `_config.yml` reflect the current state. |
| **P1.8** | `pyproject.toml` lacks notebook deps | **wontfix** | Notebook dependencies are deliberately *not* in `pyproject.toml` — they are listed per-notebook in `scripts/notebook_extras.tsv` and installed into ephemeral isolated venvs by `scripts/execute_notebook.sh`. Putting all heavy ML/biology deps into the book's own pyproject would make `uv sync` huge and break the book-only Pages build. The labs intro now points students at `notebook_extras.tsv` for per-lab deps. |
| **P1.9** | Heavy notebooks have unconditional installs | **fixed** | `!pip install` and `get_ipython().system('pip install …')` lines were stripped from book-bundled notebooks by `scripts/post_swap_rerun.sh` (see `cf56123`). Per-notebook deps now come from the isolated venv. |
| **P1.10** | Labs intro overpromises Colab/GPU/TPU and pickle behavior | **fixed** | Labs intro rewritten with: (a) a per-lab runtime / GPU / network-download table, (b) explicit cross-lab dependency note (Lab 0's `processed_data.pkl` is needed for labs 1-11), (c) reference to `scripts/notebook_extras.tsv` for per-lab deps. |
| **P1.11** | "Same architecture" overclaim in L14/L27 | **fixed** | L14 cross-link to L27 reworded: protein/DNA models reuse the *paradigm* (sequence modeling, NLL, scale, transfer), not the literal architecture (long context, MSA-aware, equivariant heads change the model class). L27's "Why it matters" reworded similarly. Study guides updated. |
| **P1.12** | Coevolution overclaim in L27 | **fixed** | "Protein language models learn coevolutionary structure from sequence alone" → "Protein LMs learn statistical regularities that *correlate with* structural and evolutionary constraints; some attention heads and embeddings carry contact-relevant signal, but this is not the same as explicit MSA-derived coevolutionary couplings." Same change in study guide and notebook caveat. |
| **P1.13** | "Beats SIFT/PolyPhen on most benchmarks" overclaim | **fixed** | Reworded to "competitive with, and on some benchmarks outperforming, SIFT/PolyPhen; the conclusion depends on benchmark / split / endpoint." Study guide updated; notebook caveat added. |
| **P1.14** | BioMedLM PubMed-corpus / clinical-notes conflation | **partial / caveat-added** | Original notebook content is the *released student notebook*; we don't substantively edit it. Instead, a **caveat markdown cell** has been prepended to `nb-14-llm.ipynb` flagging the conflation explicitly: "PubMed sample text is *same broad biomedical-literature domain*, not necessarily the same corpus; clinical notes are a different genre." |
| **P1.15** | 4-bit memory estimate (≈700 MB) implausibly low | **partial / caveat-added** | Same approach: caveat cell at top of `nb-14-llm.ipynb` notes raw 4-bit weights for 2.7B parameters are ≈1.35 GB before metadata / activations / KV cache, and that practical GPU memory is higher. |
| **P1.16** | Decoding wording imprecise | **partial / caveat-added** | Caveat cell on `nb-14-llm.ipynb` reframes "no efficient algorithm" as "exact global maximum-probability decoding is exponential in sequence length in the general case; practical systems use approximate search or stochastic decoding." |
| **P1.17** | L27 simulated/real figure provenance mismatch | **partial / caveat-added** | Caveat cell on `nb-27-modern-bio-models.ipynb` flags illustrative figures and missing references. Full figure-by-figure relabeling deferred (would require rewriting the released notebook). |
| **P1.18** | ClinVar variant provenance missing | **partial / caveat-added** | Caveat cell on `nb-27-modern-bio-models.ipynb` says variants are "illustrative hand-picked examples; treat them as pedagogy, not as a benchmark — refer to ClinVar directly for any decision." |
| **P1.19** | Imaging-figure caption / windowing audit | **wontfix-now** | The audit asks for an audit, not a specific fix. Deferred: would need cell-by-cell verification of CT windowing values, image orientation, and shortcut-vs-content distinction in `nb-21` / `nb-22`. Not in scope for this round. |
| **P2.x** | Study checklists, bibliography, concept index, search affordances | **wontfix-now** | All are nice-to-have polish. Each lecture page already has a "Study tools" footer linking to its study guide and the concept map. A full bibliography migration to `references.bib` and a separate concept-index page are deferred. |
| **markmap date** | `Tue Jan 22, 2026` should be `Thu Jan 22` | **fixed** | Fixed in `syllabus_markmap.md` and re-rendered `concept_mindmap.html`. |

## Substantive disagreements with the audit

- **P1.8** (pyproject deps). The audit recommends declaring all notebook dependencies in `pyproject.toml`. We deliberately do not: notebooks have wildly different and conflicting heavy dependencies (PyTorch + torchvision + medmnist + transformers + datasets + RDKit + lifelines + scikit-survival + AIF360 + …). Putting them in the book's pyproject would make every CI build install ~3 GB of packages and would fight version constraints. The cleaner pattern is the one in this repo: `scripts/notebook_extras.tsv` declares per-notebook extras, and `scripts/execute_notebook.sh` installs them into ephemeral isolated venvs. This is documented in the labs intro.

- **P1.14-1.18** (in-notebook claims). The audit asks for source-cell rewrites of the released student notebooks. We add **caveat markdown cells** instead, because: (a) the notebooks were released to students in a specific form during the semester and re-publishing rewritten versions would break the historical record; (b) the caveat approach makes the wording calibration *explicitly visible* to readers, which is often more pedagogically useful than silently editing the source. Where the wording appears in the *book pages* (lecture markdown, study guides), it has been rewritten directly.

- **P1.19, P2.x**. Useful suggestions; deferred for a follow-up content pass.
