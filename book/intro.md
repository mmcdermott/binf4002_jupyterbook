# BINF 4002 — Machine Learning for Health

Welcome to the Spring 2026 course book for BINF 4002. This Jupyter Book is the student-facing companion to the lectures and labs.

## How to use this book

- The **[syllabus](syllabus.md)** is the single canonical reference. It maps the entire course as a hierarchy: course → part → section → lecture, with topic / summary / goals / takeaways / materials / references at every level.
- The **[concept map](concept_map.md)** is the "step back" view. It shows how lectures depend on each other (a prerequisite graph), traces six course-wide *through-lines* across the lectures they touch (an explicit cross-reference for each), and ends with an interactive zoom/pan/expand mind map of the whole syllabus. **Start here when you sit down to review for the final.**
- The **left sidebar** navigates to specific lectures and labs. Each lecture page is its own student-facing review (topic / why-it-matters / key takeaways / cross-references / reading list). When a companion notebook exists, it is a *child page* of the lecture and renders live in the book with original outputs.
- The **labs** Part contains the 17 lab notebooks released across the semester. Click the rocket icon at the top of any notebook page to open it in Google Colab (works once this repo is public on GitHub).

## Course arc in one paragraph

The course builds from mathematical and statistical foundations toward practical health AI. Part 1 (L1-L10) establishes vectors, probability, optimization, and empirical learning, and turns that machinery into model training and evaluation. Part 2 (L11-L16) introduces modern neural and foundation-model methods (NN, LLM, FM) interleaved with three in-class lab days. Parts 3-5 (L17-L27) apply the machinery modality by modality: EHR/claims, clinical text, imaging, population health, causality/fairness, genomics, proteins/molecules, modern biological AI. Part 6 (L28) is a course-wide recap. The recurring move across modalities is to map the modality onto generic ML, identify where that mapping breaks in health, and trace the breakage to task definition, representation, modeling, and evaluation.
