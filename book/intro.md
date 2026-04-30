# BINF 4002 — Machine Learning for Health

**Spring 2026 · Cornell**

This book is the student-facing companion to the Spring 2026 BINF 4002 lectures and labs. Everything you need to review for the course lives in these pages.

```{warning}
**This site was synthesized with the help of generative AI and is not fully authored or reviewed by course staff.** It is a study aid — not a primary source. The released slide decks, lecture recordings, and original notebooks are the authoritative course content. Specific factual claims, numerical estimates, citation details, and external-reference lists may contain errors; cross-check anything you plan to repeat in a paper or assignment, and trust lecture content over this site if the two disagree.
```

## Where to start

Pick the path that matches what you're trying to do.

```{admonition} I'm new to the book
:class: tip
Start with the **[syllabus](syllabus.md)** for the lecture-by-lecture map, then skim the **[concept map](concept_map.md)** to see how the lectures connect. The "Lectures at a glance" table at the top of the syllabus is clickable — every lecture title links straight to its review page.
```

```{admonition} I'm reviewing for the final
:class: tip
Open the **[concept map](concept_map.md)** first. Walk through the prerequisite graph and the six through-lines (TL1-TL6) — they are the cross-cutting picture. Then open each **Study Guide** (left sidebar) and run the self-check questions without notes. Anything you can't answer is where to focus next.
```

```{admonition} I missed a class and want to catch up
:class: tip
Open the **lecture page** for the missed lecture (left sidebar). Each lecture has a "What this lecture is about → Why it matters → Things you should walk away believing" structure that is meant to substitute for being there. The companion notebook (where one exists) is a child page that renders inline with outputs.
```

```{admonition} I want to actually run the labs
:class: tip
Click any lab in the **Labs** part of the left sidebar. The rocket icon at the top right of each notebook page opens the notebook in **Google Colab** with one click — no install needed. (Labs 0-5 in this book are the *solution* notebooks; labs 6-16 have inline solution cells at the bottom of each section.)
```

## What's in this book

| Part | Pages | What's there |
|---|---|---|
| **Course-wide** | 2 | The full hierarchical [syllabus](syllabus.md) and the [concept map](concept_map.md) (prerequisite graph + through-lines + interactive mind map). |
| **Parts 1-6** | 6 part overviews + 28 lecture pages | One overview per Part, then student-facing review pages per lecture. Companion notebooks for L13, L14, L17, L19-L27 are nested under their lecture. |
| **Study Guides** | 27 + 1 intro | Per-lecture key-terms tables, callout-box insights, self-check questions, and curated external resources. The fastest way to review for the final. |
| **Labs** | 17 + 1 intro | The 17 lab notebooks released across the semester, with full inline outputs. Open in Colab to run them yourself. |

## The course in one paragraph

The course builds from mathematical and statistical foundations toward practical health AI. Part 1 (L1-L10) establishes vectors, probability, optimization, and empirical learning, and turns that machinery into model training and evaluation. Part 2 (L11-L16) introduces modern neural and foundation-model methods (NN, LLM, FM) interleaved with three in-class lab days. Parts 3-5 (L17-L27) apply the machinery modality by modality: EHR/claims, clinical text, imaging, population health, causality/fairness, genomics, proteins/molecules, modern biological AI. Part 6 (L28) is a course-wide recap. The recurring move across modalities is to map the modality onto generic ML, identify where that mapping breaks in health, and trace the breakage to task definition, representation, modeling, and evaluation.

## How the pages relate

The **syllabus**, **concept map**, **lecture pages**, **study guides**, and **labs** are five views of the same content, each optimized for a different way of studying:

- **Syllabus** — the structured, hierarchical, *complete* statement of what each lecture covers. Reference document.
- **Concept map** — the *across-lecture* picture: prerequisites, through-lines, mind map. Use this when reviewing.
- **Lecture pages** — *narrative* per-lecture reviews ("what was the message of this lecture, and why does it matter?"). Use these when you missed a class or want a refresher in your own time.
- **Study guides** — *self-test* per-lecture material (key terms, self-check questions, resources). Use these when you want to actively recall, not passively read.
- **Labs** — *hands-on* work. The notebooks have full inline outputs in the book; click the rocket to run them yourself in Colab.

Cross-links are wired up: every lecture page points to its study guide and companion notebook; every study guide points back at the lecture page; every part-overview points at all of its child lectures.

## Citing or sharing this book

Course content is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); code is under MIT. To cite:

```bibtex
@misc{mcdermott2026binf4002,
  author       = {Matthew McDermott},
  title        = {BINF 4002 — Machine Learning for Health (Spring 2026)},
  year         = {2026},
  howpublished = {\url{https://github.com/mmcdermott/binf4002_jupyterbook}}
}
```
