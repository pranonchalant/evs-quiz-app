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
- **Single Unified EVS FAT Revision Notes (18 Modules)**:
  - **Cheat Sheets & Numbers**:
    - *Module 1*: 30-statistic "Numbers, Targets & Values to Memorise" cheat sheet.
    - *Module 18*: Last-Minute Exam Tips & VIT Examiner Marking Criteria.
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
2. ⏱️ **Timed Mock Test (40 Questions — 40% Dates, Treaties & SDGs)**:
   - Official FAT Exam simulation: 40 randomly sampled questions with an increased **40% weighting (16 questions)** dedicated to Dates, Treaties, WHO guidelines & SDGs, combined with 24 core conceptual questions, live stopwatch tracking (`⏱️ MM:SS`), and pace analytics.
3. ⭐ **FAT Focus Bank (109 Important Questions — 46% Dates/Treaties)**:
   - Curated collection of the 109 most critical, high-frequency questions across all FAT modules, featuring an increased **46% focus (50 questions)** on core Environmental Laws, Treaties, WHO standards, and SDGs.
4. 🏛️ **Dates, Treaties, WHO & SDGs Drill (91 Targeted Questions)**:
   - Targeted rapid-fire exam drill testing ONLY historical dates & enactment years of environmental acts (Wildlife 1972, Water 1974, Air 1981, EPA 1986, Forest 1980, Biodiversity 2002), international treaties (Ramsar 1971, CITES 1973, Montreal 1987, Basel 1989, Rio 1992, Kyoto 1997, Stockholm 2001, Minamata 2013, Paris 2015, Kigali 2016), WHO health guidelines (PM2.5, arsenic, noise limits), and UN Sustainable Development Goals (all 17 SDGs, 169 targets).
5. 📖 **EVS FAT Revision Notes & Cheat Sheets**:
   - Integrated revision viewer with live search and 18 syllabus modules for comprehensive FAT exam preparation.
6. 🏷️ **Practice by Section**:
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
