# 🌿 EVS FAT Quiz — VIT Vellore Exam Revision & Practice Bank

An interactive, responsive multiple-choice quiz (MCQ) web application built for Environmental Sciences (EVS) FAT exam preparation at VIT Vellore, powered by the official FAT Question Bank (W5S1, W5S2, W5S3, W6S1, AI & IoT), core high-yield exam notes, and comprehensive topic revision.

---

## 🚀 Live App

- **Live Web App**: [pranonchalant.github.io/evs-quiz-app](https://pranonchalant.github.io/evs-quiz-app/)
- **Repository**: [github.com/pranonchalant/evs-quiz-app](https://github.com/pranonchalant/evs-quiz-app)

---

## 🎯 Features

- **Instant Right/Wrong Feedback**:
  - Highlights the chosen option in green (correct) or red (incorrect) the instant you click.
  - Automatically highlights the correct answer in green if you picked wrong.
  - Provides a concise 1–2 sentence explanation explaining *why* the answer is correct based on syllabus facts and lecture notes.
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
- **Dual-Source Comprehensive Revision Notes**:
  - **VIT Vellore FAT Cheat Sheets & Lecture Notes (Parts A–G)**:
    - *Part A*: 30-statistic "Numbers to Memorise" cheat sheet.
    - *Part B*: Climate Change Science & Global Warming (greenhouse physics, 4 evidence pillars, mitigation vs adaptation).
    - *Part C*: Carbon Footprint & Mitigation (Scopes 1/2/3, LCA, standards, sectoral shares, CCS/CCU/DAC).
    - *Part D*: Solar & Wind Energy (PV types, CSP, Indian schemes, wind cubic power law, Betz limit, HAWT vs VAWT).
    - *Part E*: Hydro & Geothermal Energy (energy chains, Tehri/Kadamparai, geothermal flash/binary cycles, Puga Valley).
    - *Part F*: AI & IoT in Environmental Monitoring (sensor matrix, LSTM, digital twins, IIT Kharagpur Ganga case study).
    - *Part G*: Last-Minute Exam Tips & VIT marking criteria.
  - **Masterdooom Syllabus Modules (26 Topics)**:
    - Complete, structured revision cards for Earth & Ecosystems, Biodiversity, Pollution, Waste, Hazards & Disasters, Indian Environmental Laws, and International Agreements (Kyoto, Paris, SDGs).
  - **Live Search & Category Filtering**: Instant real-time keyword search across all notes, formulas, and laws.
- **Zero Dependencies**: Pure HTML5, modern CSS, and vanilla JavaScript. Runs 100% offline.

---

## 📚 Exam Modes & Question Banks (420 MCQs Total)

1. 📚 **EVS FAT Master Bank (All 420 Questions)**:
   - Includes all old and new questions combined into one mega FAT preparation bank across Climate Change, Carbon Footprint, Renewables (Solar, Wind, Hydro, Geothermal), AI & IoT, Ecosystems, Biodiversity, and Environmental Laws.
2. ⏱️ **Timed Mock Test (40 Random Questions)**:
   - 40 randomly sampled questions from the full 420 question pool with live stopwatch tracking on top and average pace analytics.
3. ⭐ **FAT Focus Bank (65 Important Questions)**:
   - Curated collection of **ONLY the most critical, high-frequency questions** across all FAT modules and core environmental laws — 0% filler, 100% exam-critical.
4. 📖 **Complete EVS Revision Notes & Cheat Sheets**:
   - Integrated revision viewer with live search and dual-tab access for FAT Lecture Notes and all 26 Masterdooom modules.
5. 🏷️ **Practice by Section**:
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
