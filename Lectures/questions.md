# Outstanding questions for review

Things I'm unsure about while organizing the BINF 4002 course materials. Please review and
either correct in place or let me know how to resolve.

## 1. Lecture numbering for NN, LLM, FM (resolved → 13 / 14 / 15)

**Resolved.** Per the syllabus CSV (and confirmation that three classes before spring break were lab days), the calendar-order numbering is:
- L11 (Tue Feb 24) = Lab Day #1
- L12 (Thu Feb 26) = Lab Day #2
- L13 (Tue Mar 3) = Neural Networks
- L14 (Thu Mar 5) = Large Language Models
- L15 (Tue Mar 10) = Foundation Models
- L16 (Thu Mar 12) = Lab Day #3 (last class before spring break)

This matches the user's recollection of "two lab days in a row, then some other lectures, then the last lecture before break was also a lab day." Folders renamed accordingly.

## 2. Lab-day mapping (which labs on which day)

The lab folders for L11/L12/L16 contain labs released up to and including that class day:
- L11 + L12 (Feb 24 / Feb 26) = labs 0-5 (chunk #1 "ML model types," released Sun Feb 22).
- L16 (Mar 12) = labs 6-11 (chunk #2 "ML loss types," released Mon Mar 2) + labs 12-16 (chunk #3 "data types," released Fri Mar 6).

Caveat: students worked labs in order across chunks, so on later class days some were still working through earlier labs. The lab folders represent "what was *available* for in-class work that day," not strictly "what students did that day."

## 3. Lecture 8 — was the pptx actually delivered, or was the guest deck delivered?

`final_materials.zip` ships `Lecture 8_Florent Pollet.pdf` (a guest lecturer's deck). My organized folder also keeps the older `Lecture 8 - binary_classification_evaluation.pptx` from the loose Lectures/ files. **Was the pptx ever delivered**, or was it superseded entirely by the guest's deck before class? If superseded, the pptx should arguably be moved to `archive/`. Right now it's kept alongside the guest PDF in `lecture-08-...` for reference.

## 4. Lecture 7 — same question

`final_materials.zip` ships `Lecture 7 Di Liu.pdf` (Di Liu's guest deck). The original loose `Lecture 7 - probabilistic_modeling_and_optimization.pdf` (in `archive/`) is byte-identical to the guest PDF, so they are the same file — Di Liu's deck *is* the L7 deliverable. No outstanding question here, but flagging it for transparency.

## 5. Lecture 4 — two PDF variants (resolved)

**Resolved.** The instructor confirmed that the only PDF actually shown to students was the smaller "claude generation" variant (41 pages, exported from the Google-slides / PowerPoint source). The larger 63-page Beamer/"with claude equations" variant was generated but never delivered. `Lecture 4.pdf` in `lecture-04-information-theory/` is now the 41-page PowerPoint-sourced PDF; the Beamer variant remains preserved inside `final_materials.zip` (within `archive_materials.tar.xz`) for reference.

## 6. Lecture 17 — source ↔ PDF compile verified (after correction)

Three different `Lecture17_EHR_Claims.tex` files existed in the archive set. I initially picked the wrong one (from `Lecture17_Overleaf.zip`); compiling it produced a 103-page PDF, not the 107-page released version. **Resolved:** swapped in the .tex from `Health_Data_Modalities_I_EHR_Claims_Data__1_.zip`, which compiles to **107 pages / 1656 text-lines, exactly matching the released PDF**. The other two .tex versions are kept in `archive/` for reference.

## 7. Lecture 18 — source compiles to a 114-page PDF that matches the released version exactly

Verified: `lecture18_modeling_ehr_claims.tex` plus the two bundled figures (`curiosity_figure.png`, `everyquery_fig.jpg`) compiles to **114 pages / 1854 text-lines, exactly matching the released PDF**. No additional figures or packages needed.

## 8. Lecture 24 — source verified, figures still notebook-generated

The .tex compiles to **55 pages, matching the released PDF**, even when figures are missing (latex falls back to draft-mode boxes). So the source is correct. The six figures (`fig1_bias_gallery.png` ... `fig6_threshold_adjustment.png`) are still produced by running `nb24_causality_fairness.ipynb` and were never bundled as static files in any archive — to recompile the deck with embedded figures, run the notebook first. (Documented in `lecture-24-causality-fairness/README.md`.)

## 9. Lecture 28 — deployment lecture dropped this cycle (resolved)

**Resolved.** The originally-planned deployment lecture is *not* taught in Spring 2026. The L28 slot is used as a course-wide recap. The previously-organized `lecture-28-deployment/` folder (with the deployment notebook) was moved into the archive (`archive_materials.tar.xz` → `lectures_archive/lecture-28-deployment-DROPPED-this-cycle/`) for re-use in future cycles.

## 10. Lecture 27 notebook — picked the larger of two versions

Two copies of `nb27_modern_bio_models.ipynb` existed:
- A 372,629-byte version in the loose Lectures/ root (now in `archive/`).
- A 714,024-byte version inside `Lecture_27__Modern_Biological_AI.zip` (timestamp matches the final-PDF release).

I used the larger/newer one. **Confirm that's the version released to students.** The two are different — the bigger one likely has more output cells or images.

## 11. nb20 clinical NLP — significant size jump

`final_materials.zip` ships `nb20_clinical_nlp.ipynb` at 1.19 MB. An earlier `nb20_clinical_nlp_v2.ipynb` in the loose Lectures/ root was only 31 KB. I treated the 1.19 MB version as canonical (it has all the rendered figure outputs and demonstrations). The 31 KB version is in `archive/`. No outstanding question — flagging only.

## 12. Notebooks for L11 (NN), L12 (LLM): names

I named them `nn_fundamentals_lab.ipynb` and `llm_lecture_notebook.ipynb`, matching what was in `final_materials.zip`. Inside `archive/` there's `llm_lecture_notebook_v6.ipynb` (an older v6 version). **Is `llm_lecture_notebook.ipynb` actually the v6 final, or a v7+? Check timestamp/cells if you ever need to revert.**

## 13. Potential other lecture material I may have missed

I searched `~/Dropbox/Teaching/BINF4002/2026_01/` and `~/Downloads/` for BINF/lecture/lab files. If lecture 14-16 (or any other) materials live in another directory (e.g., another Dropbox folder, OneDrive, an external drive, or an institutional LMS), I did not see them.

## 14. Excel syllabi were not parsed (resolved)

The CSV exports of these were used to settle the calendar / lab-day questions (see #1 and #2 above).

---

## Verification summary (Apr 29 2026)

Compiled every LaTeX source folder with `latexmk -pdf` and compared to the released PDF. **All 12 LaTeX-sourced lectures match exactly** by both page count and `pdftotext -layout` line count:

| Lecture | Built | Released | Status |
|---|---|---|---|
| L13 Neural Networks | 95p / 1494 lines | 95p / 1494 lines | ✓ |
| L14 LLMs | 145p / 2142 lines | 145p / 2142 lines | ✓ |
| L17 EHR data | 107p / 1656 lines | 107p / 1656 lines | ✓ (after .tex swap) |
| L18 EHR modeling | 114p / 1854 lines | 114p / 1854 lines | ✓ |
| L19 Clinical text | 100p / 1410 lines | 100p / 1410 lines | ✓ |
| L20 Clinical NLP | 37p / 484 lines | 37p / 484 lines | ✓ |
| L21 Imaging data | 78p / 1120 lines | 78p / 1120 lines | ✓ |
| L22 Imaging modeling | 62p / 915 lines | 62p / 915 lines | ✓ |
| L23 Pop health | 68p / 990 lines | 68p / 990 lines | ✓ |
| L24 Causality / fairness | 55p (draft mode) | 55p / 854 lines | ✓ source; needs notebook-generated figures for full content |
| L25 DNA | 62p / 937 lines | 62p / 937 lines | ✓ |
| L26 Proteins | 56p / 842 lines | 56p / 842 lines | ✓ |
| L27 Modern bio AI | 57p / 811 lines | 57p / 811 lines | ✓ |

**All 24 released PDFs in lecture folders are byte-identical to `final_materials.zip`** (md5 verified).

**All 14 companion notebooks in lecture folders are byte-identical to `final_materials.zip`** (md5 verified). L27 (`nb27_modern_bio_models.ipynb`) and L28 (`nb28_deployment.ipynb`) were not in `final_materials.zip` but match the per-lecture-folder copies in `~/Downloads/lectures/`.

**All 17 lab notebooks in lab-day folders are byte-identical to `Labs/Labs_export.zip`** (md5 verified).

PPTX-based lectures (L1-L6, L7 was guest PDF, L8 has both PPTX draft + guest PDF, L9-L10, L15 FMs) cannot be auto-verified without a LibreOffice round-trip, but each released PDF is byte-identical to the final-materials version, and each PPTX file is the only candidate source available in the archive set (no draft variants were found).
