# 🌿 EVS CAT-II Revision & High-Yield Exam Quiz App

An interactive, responsive multiple-choice quiz (MCQ) web application built for Environmental Studies (EVS) CAT-II exam preparation, powered by content from [masterdooom.github.io/evs](https://masterdooom.github.io/evs/) and high-yield exam question banks.

---

## 🎯 Features

- **Instant Right/Wrong Feedback**:
  - Highlights the chosen option in green (correct) or red (incorrect) the instant you click.
  - Automatically highlights the correct answer in green if you picked wrong.
  - Provides a concise 1–2 sentence explanation explaining *why* the answer is correct based on syllabus facts.
- **Answer Locking**: Options lock immediately upon answering to prevent changing answers.
- **Manual Advancement**: "Next Question →" button ensures you have all the time needed to review the explanation.
- **Live Progress & Scoring**:
  - Top header tracking `Question X of Y` with animated progress bar.
  - Real-time score counter (`Score: X / Y`).
- **Flexible Exam Modes**:
  - ⏱️ **Timed Mock Test (30 Random Questions)**: Generates 30 randomized questions sampled across the entire syllabus with a live stopwatch tracking time elapsed and pace per question.
  - 🌐 **Masterdooom Website Official Test**: The 63 official test questions directly from `masterdooom.github.io/evs`.
  - 📖 **Masterdooom 26 Topics Complete Bank**: 86 questions covering all 26 revision modules from the website.
  - ⭐ **Core Top 30 High-Yield Pack**: The essential top 30 questions to memorize for the exam.
  - 📚 **Master Mega Bank**: All 259 questions from all sources combined.
  - 🏷️ **Module Practice**: Filter and practice any specific exam topic.
- **Detailed Results Breakdown**:
  - Score total, accuracy percentage, and performance evaluation.
  - Full review list showing question text, your choice, correct answer, and explanation.
- **Zero Dependencies**: Pure HTML5, modern CSS, and vanilla JavaScript. Runs 100% offline.

---

## 📚 26 Syllabus Topics Covered

1. **Earth as a Life Support System** (Atmosphere layers, troposphere, stratosphere, ozonosphere, mesosphere, thermosphere, lithosphere)
2. **Ecosystem — Core Concepts** (Ernst Haeckel, ecological organization: organism to biosphere, natural vs. artificial ecosystems)
3. **Ecosystem Structure & Functions** (Producers, consumers, decomposers, abiotic/biotic components)
4. **Energy Flow in an Ecosystem** (Photosynthesis, GPP/NPP, 10% law, Lindeman's rule, thermodynamics, Eltonian pyramids)
5. **Ecological Succession** (Primary vs. secondary, pioneer lichens/mosses, sere types: hydrosere, xerosere, Clements' monoclimax, Tansley's polyclimax)
6. **Biodiversity — Definition & Levels** (Genetic, species, and ecosystem diversity; species richness vs. evenness)
7. **Species Interactions & Status** (Mutualism, commensalism, parasitism, amensalism, predation, competition, IUCN Red List)
8. **Conservation Strategies** (In-situ vs. ex-situ, Biosphere reserve zones: core/buffer/transition, Project Tiger, Project Elephant, CITES, Ramsar)
9. **Genetically Modified (GM) Crops** (Bacillus thuringiensis, Cry delta-endotoxins, Bt cotton, Bt brinjal moratorium, GEAC, refuge planting)
10. **Air Pollution** (Primary vs. secondary pollutants, photochemical smog, PAN, tropospheric ozone, acid rain pH < 5.6, AQI scale, ESP)
11. **Water Pollution** (Point vs. non-point sources, BOD/COD indicators, eutrophication, algal blooms, biomagnification)
12. **Soil Pollution** (Agrochemicals, heavy metal leaching into aquifers)
13. **Noise Pollution** (Decibel thresholds, hearing damage >85 dB, Noise Pollution Rules 2000, Silent Zone limits)
14. **Thermal Pollution** (Hot water discharge, inverse temperature-DO relationship, cooling towers)
15. **Water Management & Conservation** (IWRM, Jal Shakti Abhiyan, rainwater harvesting, drip irrigation)
16. **Circular Economy & Solid Waste** (Take-make-dispose linear model, 3Rs hierarchy, EPR, industrial symbiosis, urban mining, incineration, sanitary landfill)
17. **Environmental Hazards** (Natural vs. anthropogenic, hazard vs. risk formula)
18. **Chemical Hazards — BPA & Mercury** (Bisphenol A endocrine disruption, Minamata disease, methylmercury)
19. **Disaster Management** (Sendai Framework, pre-disaster preparedness/prevention vs. post-disaster response/recovery, earthquakes: epicenter vs. focus)
20. **Environmental Impact Assessment (EIA)** (Screening, scoping, Leopold Matrix, Environmental Management Plan - EMP, public hearings)
21. **Water Act, 1974** (First national pollution law, CPCB/SPCB creation, Section 24 prohibition, Section 25 consent)
22. **Environment Protection Act, 1986 & Air Act, 1981** (EPA umbrella law post-Bhopal MIC disaster under Article 253; Air Act 1981 and 1987 noise amendment)
23. **Forest Conservation Act, 1980 & Wildlife Protection Act, 1972** (Section 2 prior central approval, Godavarman 1996 judgment, protected area categories)
24. **Kyoto Protocol, 1997** (Annex I binding targets 5% below 1990 levels, 6 GHGs, 3 flexible mechanisms: CDM, JI, emissions trading)
25. **Paris Agreement, 2015** (Well below 2°C & pursue 1.5°C, Article 4 net-zero, bottom-up NDCs, Article 14 Global Stocktake every 5 years)
26. **Sustainable Development Goals (SDGs)** (17 goals, 169 targets agreed at UN in Sept 2015: SDG 6, 7, 12, 13, 14, 15, 17)

---

## 🚀 How to Run

Simply open `index.html` in your browser:

```bash
# macOS
open index.html

# Linux
xdg-open index.html

# Windows
start index.html
```

---

## 📁 Repository Files

- `index.html` — The standalone single-page quiz application
- `master_questions.json` — Complete combined questions dataset (259 MCQs)
- `website_mcqs.json` — Dedicated dataset from masterdooom.github.io/evs (86 MCQs)
- `build_website_mcqs.py` — Generator script extracting and generating questions from the website
- `merge_questions.py` — Merges all datasets
- `generate_final_html.py` — Compiles and builds `index.html`
