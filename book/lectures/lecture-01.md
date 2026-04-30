# Lecture 1 — Course orientation

> ⚠️ **AI-synthesized; not fully reviewed by course staff. Treat as a study aid; released slides, notebooks, and lecture recordings are authoritative.**

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

---

## Study guide

*Key terms, self-check questions, and additional resources for active recall.*

### Core Ideas

- The course prioritizes **mathematical and computational intuition** over direct practical readiness. Intuitions outlast any specific technology stack.
- ML/AI for health is **meaningfully different** from general ML/AI; this difference is a recurring theme.
- **Independent learning** is expected; AI tools (ChatGPT, etc.) can help you explore background material — use them as scaffolding, not as a crutch.
- **Epistemic humility** — being confidently uncertain, and being happy to be wrong — is a core scientific skill and an explicit course goal.

### Key Concept: Epistemic Humility

```{admonition} What is epistemic humility?
:class: tip
The ability to hold beliefs with appropriate confidence — neither overconfident nor paralyzed by uncertainty. In ML/health, this means recognizing when a model's output should be trusted vs. questioned, and always being able to articulate the limits of your own knowledge.
```

### Course Roadmap

| Phase | When | What |
|---|---|---|
| **Phase 1** | through February | Math background: linear algebra, probability, calculus |
| **Phase 2** | through spring break | ML fundamentals: optimization, evaluation, training, data types, models |
| **Phase 3** | after spring break | ML for health: health data differences, model differences, deployment |

### Self-Check Questions

1. What does it mean to have "healthy epistemic uncertainty" about an ML model's output in a clinical setting?
2. Why might building intuition matter more than learning a specific framework or library?
3. How does ML for health differ from ML in other domains? (You will revisit this throughout the course — jot down your initial answer now.)

### Additional Resources

- [3Blue1Brown — Essence of Linear Algebra (playlist)](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — visual intuition for the math covered in L2-L6.
- [Calling Bullshit (Bergstrom & West)](https://www.callingbullshit.org/) — companion on epistemic humility and reasoning about data.
- [The Alignment Problem (Brian Christian)](https://brianchristian.org/the-alignment-problem/) — accessible intro to why ML for health is different.
- [Beam & Kohane, "Big Data and Machine Learning in Health Care," _JAMA_ 319(13), 2018](https://jamanetwork.com/journals/jama/fullarticle/2675024) — short, opinionated; good companion to the course's framing.
