# Lecture 12 — Lab Day #2

**Thu Feb 26, 2026 · Part 2 — Modern AI & lab work**

## What this class meeting was about

Second of the two consecutive lab/Q&A days. No new lecture material. Students kept working through the first lab chunk (labs 0-5, released Sun Feb 22, covering ML model types). The second lab chunk — ML *losses* — would not release until the following Monday (Mar 2), so the labs in scope on this day are the same as on Lab Day #1.

What this day adds beyond Lab Day #1:

- **Time pressure to actually finish.** The next chunk lands Monday; carry-over is allowed but not encouraged.
- **Cross-comparison.** With a few days of work behind them, students can now compare results across model classes on the same dataset and start to *feel* the bias-variance picture from L10 rather than just believe it.
- **Clinic-style debugging.** This is the day where most students hit the "my logistic regression is doing weirdly poorly" or "my tree is at 100% training accuracy and 60% test accuracy" moments, and the in-class time is for debugging those rather than introducing new content.

## What you should walk away with

In addition to everything from Lab Day #1:

- A debugging muscle for "is this a data problem or a model problem?" — the single most useful skill in applied ML.
- A working comparison table for the six baselines (which performs best on your dataset, why, and how confident you are in that ranking).
- An understanding that *no single number* (accuracy, AUROC, F1) is the right summary of a binary classifier — connecting back to L8.

## How this connects to the rest of the course

- L13 (neural networks) is now the last NN-related lab you've seen plus the lecture you haven't. The contrast between "I trained a small NN in lab5 and it kind of worked" and "here is why architecture and optimization actually matter" is what L13 is built around.
- L16 (Lab Day #3) will pull in the loss-types chunk (lab 6-11) released the following Monday and the data-types chunk (lab 12-16) released on Mar 6; some carry-over from labs 0-5 is expected.

## Source files in this folder

- `labs/` — same six lab notebooks (labs 0-5) as in `lecture-11-lab-day-1/labs/`.
- `solutions/` — solution notebooks.

## To go deeper

Same references as Lab Day #1. In particular:

- **scikit-learn user guide** for the API.
- **Géron Ch. 2-7** for an applied companion.
- **ESL Chs. 2 and 9-10** for the classical statistical-learning lens on the same material.
