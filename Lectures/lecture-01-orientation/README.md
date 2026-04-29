# Lecture 1 — Course orientation

**Tue Jan 20, 2026 · Part 1 — Foundations**

## What this lecture is about

The first day of class is not really about course logistics — it is about setting up an *attitude* you'll need for the rest of the semester. This is a course about machine learning *for health*, and almost every claim we'll examine over the next 14 weeks comes with an asterisk that says "...but in this clinical setting, it might not be that simple."

The lecture introduces a stance you should keep through the whole course: **healthy epistemic uncertainty.** When a paper says "our model achieves 0.94 AUROC on ICU mortality prediction," your first reflex should not be "great" — it should be "AUROC against what label, on which patients, generalizing where, evaluated by whom, deployed how?" That habit of asking is the most durable thing this course tries to build, more durable than any specific algorithm or library.

## Why it matters

A pattern repeats across health AI failures: a model is technically excellent, gets through validation, gets deployed, and then either degrades, harms a subgroup, gets gamed, or simply solves the wrong problem because nobody asked what problem it was actually solving. The math of ML is rarely the limiting factor; the question-framing is.

Because tools change quickly (the libraries we'll use this semester are not the libraries you'll use in five years), we don't optimize the course for tool-specific recipes. We optimize for a few enduring habits: *what is the data actually measuring*, *what is the loss actually rewarding*, *what is the deployment context actually doing to the data-generating process*. Those questions outlive any particular framework.

## Things you should walk away believing

- ML for health is not generic ML applied to health-shaped tables. The data, the labels, the deployment, and the consequences are all different in ways that affect modeling choices.
- Conceptual understanding is the stable target; tool fluency is the moving target. We will favor the former over the latter when they conflict.
- Skepticism is not pessimism. It is the move that lets you trust the *right* claims while ignoring the noise.
- The course expects independent reading. The lectures are a backbone; the readings make you fluent.

## How this connects to the rest of the course

Every later lecture has a "where this can go wrong in health" subsection. L1 is what justifies that pattern. In particular:

- L8-L10's emphasis on calibration, decision-curve analysis, and domain shift comes from this stance.
- L17-L18 (EHR data) is a long argument that "data are generated, not given."
- L24 (causality and fairness) is the formal version of "asking what problem the model is actually solving."
- L28 (course recap) returns to this orientation to ask: did we earn the skepticism we promised on day one?

## Source files in this folder

- `Lecture 1.pdf` — the slides as released to students.
- `Lecture 1 - Intros_and_overview.pptx` — editable PowerPoint source.

## To go deeper

- **Beam & Kohane, "Big Data and Machine Learning in Health Care," _JAMA_ 319(13), 2018.** A short, opinionated piece on what ML for health is and isn't. Good companion to this lecture's framing.
- **Topol, "High-performance medicine: the convergence of human and artificial intelligence," _Nat Med_ 25, 2019.** A panoramic survey — useful for getting a sense of where the field thinks it is going.
- **Wiens et al., "Do no harm: a roadmap for responsible machine learning for health care," _Nat Med_ 25, 2019.** The "epistemic humility" version of this lecture, written as a checklist.
