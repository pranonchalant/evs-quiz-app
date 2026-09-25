# 🌿 EVS High-Yield Exam Prep Quiz App

An interactive, responsive multiple-choice quiz (MCQ) web application built for Environmental Studies (EVS) exam preparation. Features real-time, instant right/wrong feedback with 1–2 sentence rationale after every question.

---

## 🎯 Features

- **Instant Right/Wrong Feedback**:
  - Highlights correct option in green and incorrect in red the moment you click.
  - Automatically reveals the correct answer if an incorrect option was chosen.
  - Displays a concise 1–2 sentence explanation backed by high-yield exam facts.
- **Answer Locking**: Options lock immediately upon selection to prevent second guesses.
- **Controlled Advancement**: "Next Question" button ensures ample time to read the explanation.
- **Progress & Running Score**:
  - "Question X of Y" counter and animated progress bar.
  - Live accuracy score tracking throughout the session.
- **Multiple Exam Modes**:
  - ⭐ **PART A — Core Top 30 MCQs**: The 30 highest-yield exam preparation questions with matching answers.
  - 📚 **Full Practice Bank**: All 177 questions covering the complete syllabus.
  - 🏷️ **Topic Practice**: Filter by individual exam modules.
- **Comprehensive Results Breakdown**:
  - Final score, percentage, and performance evaluation.
  - Scrollable review of all questions with selected answers, correct answers, and explanations.
  - One-click quiz restart.
- **Zero Dependencies**: Pure HTML5, modern CSS, and vanilla JavaScript. Runs completely offline.

---

## 📚 Topics & Question Bank Structure

The app contains **177 verified MCQs** organized into key high-yield EVS exam topics:

1. **Environmental Studies & Ecosystems** (Ecosystem structure, abiotic/biotic components, trophic levels)
2. **Energy Flow & Food Chains** (10% law, Lindeman's rule, Eltonian pyramids, productivity)
3. **Ecological Succession** (Primary vs. secondary, pioneer species, Clements' monoclimax theory, nudation)
4. **Biodiversity & Species Status** (Levels of biodiversity, endemism, IUCN red list categories)
5. **Species Interactions** (Mutualism, commensalism, predation, competition)
6. **Conservation Strategies** (In-situ vs. ex-situ, Biosphere reserves, Project Tiger, Project Elephant, Ramsar, CBD)
7. **Circular Economy & Solid Waste Management** (3Rs hierarchy, linear vs. circular, EPR, industrial symbiosis, urban mining, incineration)
8. **Air Pollution & Control** (Primary vs. secondary pollutants, photochemical smog, acid rain, radon, BS-VI standards, ESP)
9. **Water Pollution & Management** (TDS/pH limits, point vs. non-point, eutrophication, biomagnification, Minamata disease, wastewater treatment stages, drip irrigation)
10. **Noise, Thermal & Soil Pollution** (Decibel thresholds, noise rules 2000, oxygen solubility, cooling towers)
11. **Environmental Hazards & Disaster Management** (Anthropogenic vs. natural, earthquake epicenter, Kedarnath, Sendai Framework)
12. **Genetically Modified Crops** (Bt cotton, Bt brinjal moratorium, GEAC regulations, refuge planting)
13. **Indian Environmental Legislation** (Wildlife Protection Act 1972, Water Act 1974, Air Act 1981, EPA 1986, Forest Conservation Act 1980, Biological Diversity Act 2002, NGT 2010, Bhopal Gas Tragedy & MIC)
14. **Global Treaties & SDGs** (Kyoto Protocol mechanisms & GHGs, Paris Agreement NDCs & Articles 2/4/7/9, 2030 Agenda & SDGs 6, 7, 13, 14, 15, 17)

---

## 🚀 How to Run

Simply open `index.html` in any web browser:

```bash
# macOS
open index.html

# Linux
xdg-open index.html

# Windows
start index.html
```

No build step, Node.js, or web server required!

---

## 📁 Repository Structure

```
├── index.html           # Standalone single-page quiz application
├── questions.json       # Structured JSON dataset containing all 177 questions & explanations
├── build_questions.py   # Python generator script compiling the verified question bank
├── generate_html.py     # Script to compile and inject questions into index.html
└── README.md            # Project documentation
```
