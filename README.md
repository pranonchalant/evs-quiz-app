# 🌿 EVS FAT Quiz — VIT Vellore Exam Revision & Practice Bank (40-Mark MCQ Pattern)

An interactive, responsive multiple-choice quiz (MCQ) web application built specifically for the **official 40-mark MCQ Environmental Sciences (EVS) FAT exam pattern** at VIT Vellore. Powered by the official FAT Question Bank (W5S1, W5S2, W5S3, W6S1, AI & IoT), core high-yield exam notes, and comprehensive topic revision.

> [!IMPORTANT]
> **Official VIT EVS FAT Exam Pattern**: Strictly a **40-question, 40-mark MCQ examination** (1 mark per question = 40 marks total, zero subjective/theory writing, zero diagrams to draw). All theoretical concepts, numerical values, and environmental policies are tested exclusively through multiple-choice questions.

---

## 🚀 Live App

- **Live Web App**: [pranonchalant.github.io/evs-quiz-app](https://pranonchalant.github.io/evs-quiz-app/)
- **Repository**: [github.com/pranonchalant/evs-quiz-app](https://github.com/pranonchalant/evs-quiz-app)

---

## 🎯 Features

- **Interactive Question Navigator & Colour-Coded Palette**:
  - Full CBT-style Question Grid displaying all question numbers (e.g. 1–40 in Mock Tests) for complete visual tracking and instant navigation.
  - **Colour-Coded Status Boxes**:
    - 🟩 **Answered (Green)**: Questions that have been answered.
    - 🟧 **Watched / Visited (Amber / Orange)**: Questions that have been visited/viewed or explicitly marked for review with `[👁️ Watch Question]`.
    - ⬜ **Unanswered (Neutral Slate)**: Questions that have not been visited or answered yet.
    - 🟦 **Current Question (Glowing Cyan Ring)**: The active question currently in view.
  - Live summary counter pills: `✔ X Answered`, `👁️ Y Watched`, and `⏳ Z Unanswered`.
  - Jump directly to any question by clicking its number box, or navigate using `← Prev`, `Skip to Next →`, or keyboard arrows `<kbd>←</kbd>` / `<kbd>→</kbd>`.
  - **Results Screen Review Palette**: Full grid showing Correct (Green) vs Incorrect/Skipped (Red); clicking any box smoothly scrolls right to that question's syllabus explanation.
- **Instant Right/Wrong Feedback**:
  - Highlights the chosen option in green (correct) or red (incorrect) the instant you click.
  - Automatically highlights the correct answer in green if you picked wrong.
  - Provides a concise 1–2 sentence explanation explaining *why* the answer is correct based on syllabus facts and lecture notes.
- **Fast Keyboard Shortcuts**:
  - Press `1`, `2`, `3`, or `4` (standard or numpad keys) to instantly select Option A, B, C, or D without touching the mouse.
  - Press `Enter ↵` to immediately advance to the next question (or submit and view final results on the last question).
  - Clean visual badges `[1]`, `[2]`, `[3]`, `[4]` and helper banner keep controls visible and intuitive.
  - Smart input isolation: keyboard navigation automatically disables while typing in the FAT Notes search bar.
- **Dynamic Randomization**:
  - **Shuffled Options**: Option choices (A, B, C, D) are randomly shuffled for every question using the Fisher-Yates algorithm.
  - **Randomized Question Sequence**: The sequence of questions is shuffled on every attempt.
- **Live Stopwatch**:
  - Real-time stopwatch (`⏱️ MM:SS`) in the top navigation bar during tests.
  - Summarizes **Total Time Taken** and **Average Pace per Question** on the final results screen.
- **Answer Locking & Review**:
  - Options lock immediately upon answering to prevent changing answers.
  - "Next Question →" button ensures ample time to read the rationale.
  - Scrollable results breakdown with right/wrong indicators and explanations.
- **Single Unified EVS FAT Revision Notes (18 Modules)**:
  - **Cheat Sheets & Numbers**:
    - *Module 1*: 30-statistic "Numbers, Targets & Values to Memorise" cheat sheet.
    - *Module 18*: 40-Mark MCQ Exam Strategy & Last-Minute FAT Scoring Guide.
  - **Climate Science & Carbon Accounting**:
    - *Module 2*: Climate Change Science & Global Warming (greenhouse physics, 4 evidence pillars, mitigation vs adaptation).
    - *Module 3*: Carbon Footprint & Mitigation (Scopes 1/2/3, LCA, standards, sectoral shares, CCS/CCU/DAC, offsets).
  - **Renewable Energy Technologies**:
    - *Module 4*: Solar Energy & Photovoltaic Engineering (PV types, CSP, Indian schemes).
    - *Module 5*: Wind Energy & Betz Limit (cubic power relation, Betz limit 59.3%, HAWT vs VAWT, NIWE).
    - *Module 6*: Hydroelectric Power Engineering (energy conversion chain, Tehri, run-of-river, pumped storage).
    - *Module 7*: Geothermal Energy & Thermodynamic Cycles (geothermal gradient, flash vs binary cycles, Puga Valley).
  - **Emerging Technologies**:
    - *Module 8*: AI & IoT in Environmental Monitoring (sensor matrix, LSTM AQI forecasting, digital twins, IIT Kharagpur case study).
  - **Foundations, Biodiversity, Pollution & Laws**:
    - *Modules 9–17*: Earth as a Life Support System, Ecosystem Dynamics & 10% Law, Biodiversity & Conservation, Air/Water/Soil Pollution, Noise & Thermal Pollution, Circular Economy & Solid Waste (3Rs, EPR), Environmental Hazards & Disasters (BPA, Minamata, Bhopal), Indian Environmental Laws (Water Act 1974 & CPCB, Air Act, EPA 1986, Wildlife), and International Treaties (Montreal, Kyoto, Paris 1.5°C/2°C) & SDGs.
  - **Live Search & Category Filtering**: Instant real-time keyword search across all notes, formulas, and laws.
- **Zero Dependencies**: Pure HTML5, modern CSS, and vanilla JavaScript. Runs 100% offline.

---

## 📚 Exam Modes & Question Banks (435 MCQs Total)

1. 📚 **EVS FAT Master Bank (All 435 Questions)**:
   - Includes all questions combined into one mega FAT preparation bank across Climate Change, Carbon Footprint, Renewables (Solar, Wind, Hydro, Geothermal), AI & IoT, Ecosystems, Biodiversity, and Environmental Laws.
2. ⏱️ **Normal FAT Mock Test (40 Marks — Balanced Syllabus)**:
   - Official 40-Mark Exam Simulation: 40 questions (1 mark each) sampled completely at random across the entire 435-question syllabus with live stopwatch tracking (`⏱️ MM:SS`), official grade predictions (S/A/B/C/D), and pace analytics.
3. 🏛️⏱️ **Dates & Treaties Weighted Mock Test (40 Marks — 40% Dates/Treaties)**:
   - Targeted 40-Mark Exam Simulation: 40 questions (1 mark each) with a guaranteed **40% weighting (16 marks)** dedicated to Dates, Treaties, WHO guidelines & SDGs, combined with 24 marks from core conceptual questions.
4. ⭐ **FAT Focus Bank (109 Important Questions — 46% Dates/Treaties)**:
   - Curated collection of the 109 most critical, high-frequency questions across all FAT modules, featuring an increased **46% focus (50 questions)** on core Environmental Laws, Treaties, WHO standards, and SDGs.
5. 🏛️ **Dates, Treaties, WHO & SDGs Drill (91 Targeted Questions)**:
   - Targeted rapid-fire exam drill testing ONLY historical dates & enactment years of environmental acts (Wildlife 1972, Water 1974, Air 1981, EPA 1986, Forest 1980, Biodiversity 2002), international treaties (Ramsar 1971, CITES 1973, Montreal 1987, Basel 1989, Rio 1992, Kyoto 1997, Stockholm 2001, Minamata 2013, Paris 2015, Kigali 2016), WHO health guidelines (PM2.5, arsenic, noise limits), and UN Sustainable Development Goals (all 17 SDGs, 169 targets).
6. 📖 **EVS FAT Revision Notes & Cheat Sheets (18 Modules)**:
   - Integrated revision viewer with live search and 18 syllabus modules for comprehensive FAT exam preparation (including full W5S1, W5S2, W5S3, W6S1, W6L2, AI & IoT lecture notes).
7. 🏷️ **Practice by Section**:
   - Filter and focus on individual syllabus sections (Climate Change, Carbon Footprint, Solar Energy, Wind Energy, Hydro & Geothermal, AI & IoT, etc.).

---

## 🚀 How to Run Locally

Open `index.html` in your browser:

```bash
# macOS
open index.html

# Linux
xdg-open index.html

# Windows
start index.html
```
