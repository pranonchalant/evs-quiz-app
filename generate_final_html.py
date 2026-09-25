import json

with open("/Users/pran/devjams26/master_questions.json") as f:
    master_data = json.load(f)

json_str = json.dumps(master_data, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>EVS CAT-II & High-Yield Exam Quiz</title>
  <style>
    /* ── Reset & Color Scheme ─────────────────────────────── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg-color: #0b1120;
      --card-bg: #131d35;
      --card-header: #1a2644;
      --border-color: #24355a;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --accent: #38bdf8;
      --accent-gradient: linear-gradient(135deg, #6366f1, #06b6d4);
      --site-badge: #10b981;
      --correct-bg: #064e3b;
      --correct-border: #10b981;
      --wrong-bg: #451010;
      --wrong-border: #ef4444;
      --timer-color: #f59e0b;
      --timer-bg: rgba(245, 158, 11, 0.12);
      --timer-border: rgba(245, 158, 11, 0.35);
    }

    body {
      font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--bg-color);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 1.5rem 1rem 3.5rem;
      background-image: 
        radial-gradient(ellipse 80% 50% at 50% -20%, rgba(99, 102, 241, 0.18), transparent),
        radial-gradient(ellipse 60% 40% at 50% 120%, rgba(6, 182, 212, 0.12), transparent);
    }

    /* ── Card Container ───────────────────────────────────── */
    .quiz-card {
      width: 100%;
      max-width: 780px;
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 1.25rem;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.55), 0 0 0 1px rgba(255, 255, 255, 0.05);
      overflow: hidden;
      margin-top: 1rem;
    }

    /* ── Top Navigation Bar ───────────────────────────────── */
    .quiz-nav-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1.15rem 1.75rem;
      background: var(--card-header);
      border-bottom: 1px solid var(--border-color);
      font-size: 0.92rem;
      font-weight: 600;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .mode-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: rgba(56, 189, 248, 0.12);
      color: var(--accent);
      padding: 0.35rem 0.8rem;
      border-radius: 2rem;
      font-size: 0.8rem;
      border: 1px solid rgba(56, 189, 248, 0.3);
      max-width: 220px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    /* Stopwatch Badge */
    .stopwatch-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: var(--timer-bg);
      color: var(--timer-color);
      border: 1px solid var(--timer-border);
      padding: 0.35rem 0.8rem;
      border-radius: 2rem;
      font-size: 0.85rem;
      font-weight: 700;
      font-variant-numeric: tabular-nums;
      letter-spacing: 0.04em;
      box-shadow: 0 0 12px rgba(245, 158, 11, 0.15);
      transition: all 0.2s ease;
    }

    .stopwatch-badge.running {
      animation: timerPulse 2s infinite ease-in-out;
    }

    @keyframes timerPulse {
      0%, 100% { border-color: rgba(245, 158, 11, 0.3); }
      50% { border-color: rgba(245, 158, 11, 0.7); box-shadow: 0 0 14px rgba(245, 158, 11, 0.3); }
    }

    .live-score {
      color: #34d399;
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 0.35rem 0.8rem;
      border-radius: 2rem;
      font-size: 0.82rem;
      font-weight: 700;
      white-space: nowrap;
    }

    /* ── Progress Bar ─────────────────────────────────────── */
    .progress-track {
      height: 6px;
      background: #182442;
      position: relative;
    }
    .progress-fill {
      height: 100%;
      background: var(--accent-gradient);
      transition: width 0.35s ease;
    }

    /* ── Main Quiz Body ───────────────────────────────────── */
    .quiz-body {
      padding: 2.25rem 2rem;
    }

    .meta-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.75rem;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .source-tag {
      display: inline-block;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--accent);
      background: rgba(56, 189, 248, 0.1);
      padding: 0.25rem 0.65rem;
      border-radius: 0.4rem;
      font-weight: 700;
    }

    .random-tag {
      font-size: 0.72rem;
      color: #94a3b8;
      background: #17233f;
      border: 1px solid #283a63;
      padding: 0.2rem 0.55rem;
      border-radius: 1rem;
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
    }

    .question-title {
      font-size: 1.25rem;
      font-weight: 600;
      line-height: 1.55;
      margin-bottom: 1.75rem;
      color: #ffffff;
    }

    /* ── Option Buttons ───────────────────────────────────── */
    .options-grid {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }

    .option-btn {
      width: 100%;
      text-align: left;
      padding: 1.1rem 1.35rem;
      font-size: 1rem;
      font-family: inherit;
      color: var(--text-main);
      background: #17233f;
      border: 1.5px solid #283a63;
      border-radius: 0.85rem;
      cursor: pointer;
      transition: all 0.18s ease;
      display: flex;
      align-items: center;
      gap: 1rem;
      line-height: 1.4;
    }

    .option-btn:hover:not(.locked) {
      background: #203157;
      border-color: #6366f1;
      transform: translateY(-1px);
      box-shadow: 0 4px 14px rgba(99, 102, 241, 0.2);
    }

    .option-badge {
      flex-shrink: 0;
      width: 2.1rem;
      height: 2.1rem;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 0.55rem;
      background: #253966;
      font-weight: 700;
      font-size: 0.9rem;
      color: var(--text-muted);
      transition: all 0.18s ease;
    }

    /* Highlight feedback states */
    .option-btn.correct {
      background: var(--correct-bg) !important;
      border-color: var(--correct-border) !important;
      color: #ffffff !important;
      box-shadow: 0 0 16px rgba(16, 185, 129, 0.3);
    }
    .option-btn.correct .option-badge {
      background: #10b981;
      color: #064e3b;
    }

    .option-btn.incorrect {
      background: var(--wrong-bg) !important;
      border-color: var(--wrong-border) !important;
      color: #ffffff !important;
      box-shadow: 0 0 16px rgba(239, 68, 68, 0.3);
    }
    .option-btn.incorrect .option-badge {
      background: #ef4444;
      color: #451010;
    }

    .option-btn.locked {
      cursor: default;
    }
    .option-btn.locked:not(.correct):not(.incorrect) {
      opacity: 0.45;
    }

    /* ── Explanation Box ──────────────────────────────────── */
    .feedback-box {
      margin-top: 1.75rem;
      padding: 1.25rem 1.5rem;
      border-radius: 0.85rem;
      animation: slideUp 0.25s ease forwards;
      background: #17233f;
      border: 1px solid #283a63;
      border-left: 5px solid #6366f1;
    }

    .feedback-box.is-correct {
      border-left-color: #10b981;
      background: rgba(16, 185, 129, 0.08);
    }

    .feedback-box.is-wrong {
      border-left-color: #ef4444;
      background: rgba(239, 68, 68, 0.08);
    }

    .feedback-status {
      font-weight: 700;
      font-size: 1.05rem;
      margin-bottom: 0.4rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .feedback-status.correct { color: #34d399; }
    .feedback-status.wrong { color: #f87171; }

    .explanation-text {
      font-size: 0.95rem;
      line-height: 1.6;
      color: #cbd5e1;
    }

    @keyframes slideUp {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* ── Action Rows & Buttons ────────────────────────────── */
    .action-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 1.75rem;
      padding-top: 1.25rem;
      border-top: 1px solid var(--border-color);
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.85rem 1.75rem;
      font-size: 0.98rem;
      font-family: inherit;
      font-weight: 600;
      color: #ffffff;
      background: var(--accent-gradient);
      border: none;
      border-radius: 0.75rem;
      cursor: pointer;
      transition: all 0.2s ease;
      box-shadow: 0 4px 14px rgba(99, 102, 241, 0.35);
    }

    .btn:hover {
      opacity: 0.92;
      transform: translateY(-1px);
      box-shadow: 0 6px 20px rgba(99, 102, 241, 0.45);
    }

    .btn-secondary {
      background: #203157;
      color: #cbd5e1;
      border: 1px solid var(--border-color);
      box-shadow: none;
    }
    .btn-secondary:hover {
      background: #283d6d;
      color: #ffffff;
      box-shadow: none;
    }

    /* ── Mode Selection Screen ────────────────────────────── */
    .start-screen {
      padding: 2.5rem 2rem;
      text-align: center;
    }

    .start-screen h1 {
      font-size: 1.85rem;
      font-weight: 800;
      margin-bottom: 0.5rem;
      background: linear-gradient(135deg, #ffffff, #94a3b8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .start-subtitle {
      color: var(--text-muted);
      font-size: 0.98rem;
      margin-bottom: 2rem;
      line-height: 1.5;
    }

    .features-pill-row {
      display: flex;
      justify-content: center;
      gap: 0.6rem;
      margin-bottom: 1.75rem;
      flex-wrap: wrap;
    }

    .feature-pill {
      font-size: 0.78rem;
      color: var(--accent);
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.25);
      padding: 0.25rem 0.75rem;
      border-radius: 1rem;
      font-weight: 600;
    }

    .mode-cards {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1rem;
      margin-bottom: 2rem;
      text-align: left;
    }

    .mode-card {
      background: #17233f;
      border: 2px solid #283a63;
      border-radius: 1rem;
      padding: 1.25rem 1.5rem;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
    }

    .mode-card:hover {
      border-color: #38bdf8;
      background: #1c2a4d;
      transform: translateY(-2px);
    }

    .mode-card.mock-featured {
      border-color: #f59e0b;
      background: linear-gradient(145deg, #17233f, #2e2311);
    }

    .mode-card.featured {
      border-color: #10b981;
      background: linear-gradient(145deg, #17233f, #132e3b);
    }

    .mode-card.featured-blue {
      border-color: #6366f1;
      background: linear-gradient(145deg, #17233f, #1e2448);
    }

    .mode-card h3 {
      font-size: 1.05rem;
      font-weight: 700;
      margin-bottom: 0.25rem;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .mode-card p {
      font-size: 0.85rem;
      color: var(--text-muted);
      line-height: 1.4;
    }

    .mode-badge-count {
      background: #253966;
      color: var(--accent);
      padding: 0.35rem 0.8rem;
      border-radius: 2rem;
      font-size: 0.8rem;
      font-weight: 700;
      white-space: nowrap;
    }

    .mode-card.mock-featured .mode-badge-count {
      color: #fbbf24;
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.35);
    }

    .mode-card.featured .mode-badge-count {
      color: #34d399;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.3);
    }

    .topic-select-row {
      margin: 1.5rem 0 2rem;
      text-align: left;
    }

    .topic-select-row label {
      display: block;
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 0.5rem;
    }

    .topic-dropdown {
      flex: 1;
      padding: 0.85rem 1rem;
      background: #17233f;
      color: #ffffff;
      border: 1.5px solid #283a63;
      border-radius: 0.65rem;
      font-size: 0.95rem;
      font-family: inherit;
      cursor: pointer;
    }

    /* ── Results Screen ───────────────────────────────────── */
    .results-screen {
      padding: 2.75rem 2rem;
      text-align: center;
    }

    .results-badge {
      font-size: 3.5rem;
      margin-bottom: 0.5rem;
    }

    .results-score-big {
      font-size: 3.8rem;
      font-weight: 900;
      background: var(--accent-gradient);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      line-height: 1;
      margin: 0.75rem 0;
    }

    .results-pct {
      font-size: 1.25rem;
      color: var(--text-muted);
      font-weight: 600;
      margin-bottom: 1.25rem;
    }

    .time-stats-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      background: var(--timer-bg);
      border: 1px solid var(--timer-border);
      color: #fbbf24;
      padding: 0.5rem 1.25rem;
      border-radius: 2rem;
      font-size: 0.92rem;
      font-weight: 600;
      margin-bottom: 2rem;
    }

    .review-section {
      text-align: left;
      margin: 2.5rem 0 1.5rem;
      border-top: 1px solid var(--border-color);
      padding-top: 1.75rem;
    }

    .review-section h3 {
      font-size: 1.15rem;
      margin-bottom: 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .review-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
      max-height: 480px;
      overflow-y: auto;
      padding-right: 0.5rem;
    }

    .review-list::-webkit-scrollbar {
      width: 6px;
    }
    .review-list::-webkit-scrollbar-thumb {
      background: #2a3d6d;
      border-radius: 4px;
    }

    .review-item {
      background: #17233f;
      border-radius: 0.75rem;
      padding: 1rem 1.25rem;
      border: 1px solid #283a63;
      border-left: 4px solid #94a3b8;
      font-size: 0.92rem;
    }

    .review-item.is-correct {
      border-left-color: #10b981;
    }

    .review-item.is-wrong {
      border-left-color: #ef4444;
    }

    .review-q {
      font-weight: 600;
      margin-bottom: 0.5rem;
      color: #ffffff;
    }

    .review-ans {
      font-size: 0.85rem;
      margin-top: 0.25rem;
      color: #94a3b8;
    }

    .review-ans strong {
      color: #cbd5e1;
    }

    .review-explanation {
      margin-top: 0.5rem;
      padding-top: 0.5rem;
      border-top: 1px dashed #283a63;
      font-size: 0.82rem;
      color: #38bdf8;
    }

    /* ── Responsive adjustments ───────────────────────────── */
    @media (max-width: 600px) {
      body { padding: 0.75rem 0.5rem 2rem; }
      .quiz-body { padding: 1.5rem 1.25rem; }
      .quiz-nav-bar { padding: 1rem 1.25rem; }
      .question-title { font-size: 1.1rem; }
      .option-btn { font-size: 0.93rem; padding: 0.9rem 1.1rem; }
      .results-score-big { font-size: 3rem; }
    }
  </style>
</head>
<body>

<div class="quiz-card" id="quizCard">
  <!-- Dynamic UI injected via JavaScript -->
</div>

<script>
// ── Master Question Bank (Website + PDF Sources) ───────────────
const masterQuestions = __INJECTED_MASTER_QUESTIONS__;

// ── Application State ──────────────────────────────────────────
let currentMode = "mock"; 
let currentTopic = "";
let activeQuestions = [];
let currentIndex = 0;
let score = 0;
let answered = false;
let userAnswers = [];

// ── Stopwatch State ────────────────────────────────────────────
let timerInterval = null;
let timerStartTime = null;
let elapsedSeconds = 0;

const app = document.getElementById("quizCard");
const letters = ["A", "B", "C", "D"];

// ── Randomization Helpers (Fisher-Yates) ────────────────────────
function shuffleArray(array) {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// Shuffles both the question sequence AND each question's 4 options
function prepareQuizQuestions(rawQuestionList) {
  const shuffledList = shuffleArray(rawQuestionList);
  return shuffledList.map(q => ({
    ...q,
    options: shuffleArray(q.options)
  }));
}

// Samples random count and shuffles options
function getRandomSample(array, count) {
  const sampled = shuffleArray(array).slice(0, Math.min(count, array.length));
  return sampled.map(q => ({
    ...q,
    options: shuffleArray(q.options)
  }));
}

// ── Stopwatch Helper Functions ─────────────────────────────────
function startStopwatch() {
  stopStopwatch();
  elapsedSeconds = 0;
  timerStartTime = Date.now();
  timerInterval = setInterval(() => {
    elapsedSeconds = Math.floor((Date.now() - timerStartTime) / 1000);
    updateStopwatchUI();
  }, 1000);
}

function stopStopwatch() {
  if (timerInterval) {
    clearInterval(timerInterval);
    timerInterval = null;
  }
}

function formatStopwatch(sec) {
  const m = Math.floor(sec / 60).toString().padStart(2, "0");
  const s = (sec % 60).toString().padStart(2, "0");
  return `${m}:${s}`;
}

function updateStopwatchUI() {
  const el = document.getElementById("stopwatchDisplay");
  if (el) {
    el.textContent = formatStopwatch(elapsedSeconds);
  }
}

// ── Screen: Mode Selection ─────────────────────────────────────
function renderStartScreen() {
  stopStopwatch();
  const categories = [...new Set(masterQuestions.map(q => q.category))].sort();

  app.innerHTML = `
    <div class="start-screen">
      <div style="font-size:2.5rem; margin-bottom: 0.5rem;">⏱️ 🔀 🌿</div>
      <h1>EVS CAT-II Revision & Practice Bank</h1>
      <p class="start-subtitle">
        Powered by questions and syllabus topics from <strong style="color:var(--accent);">masterdooom.github.io/evs</strong> + High-Yield PDF exam pack.
      </p>

      <div class="features-pill-row">
        <span class="feature-pill">🔀 Randomized Question Order</span>
        <span class="feature-pill">🎲 Shuffled Option Positions</span>
        <span class="feature-pill">⏱️ Live Stopwatch</span>
        <span class="feature-pill">💡 Instant Explanation</span>
      </div>

      <div class="mode-cards">
        <!-- Mock Test Mode Card -->
        <div class="mode-card mock-featured" onclick="startQuiz('mock')">
          <div>
            <h3>⏱️ Timed Mock Test (30 Random Questions)</h3>
            <p>Pulls 30 randomized questions across the entire syllabus with both question order and answer options dynamically shuffled on every attempt.</p>
          </div>
          <span class="mode-badge-count">⏱️ 30 Random · Timed</span>
        </div>

        <div class="mode-card featured" onclick="startQuiz('website_official')">
          <div>
            <h3>🌐 Masterdooom Website Official Test</h3>
            <p>The 63 multiple choice questions from masterdooom.github.io/evs with randomized order and shuffled options.</p>
          </div>
          <span class="mode-badge-count">63 Questions</span>
        </div>

        <div class="mode-card featured-blue" onclick="startQuiz('website_all')">
          <div>
            <h3>📖 Masterdooom 26 Topics Complete Bank</h3>
            <p>Comprehensive MCQs generated across all 26 revision modules from the website with randomized options.</p>
          </div>
          <span class="mode-badge-count">86 Questions</span>
        </div>

        <div class="mode-card" onclick="startQuiz('top30')">
          <div>
            <h3>⭐ Core Top 30 High-Yield Pack</h3>
            <p>The 30 essential questions to memorize for high-yield exam preparation with randomized answer choices.</p>
          </div>
          <span class="mode-badge-count">30 Questions</span>
        </div>

        <div class="mode-card" onclick="startQuiz('all')">
          <div>
            <h3>📚 Master Mega Bank (All Sources)</h3>
            <p>Complete combined collection covering all 259 questions in randomized practice order.</p>
          </div>
          <span class="mode-badge-count">${masterQuestions.length} Questions</span>
        </div>
      </div>

      <div class="topic-select-row">
        <label for="topicSelect">Or Practice by Specific Syllabus Module:</label>
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
          <select id="topicSelect" class="topic-dropdown">
            ${categories.map(c => {
              const count = masterQuestions.filter(q => q.category === c).length;
              return `<option value="${c}">${c} (${count} questions)</option>`;
            }).join("")}
          </select>
          <button class="btn btn-secondary" onclick="startTopicQuiz()">Practice Module</button>
        </div>
      </div>

      <button class="btn" style="width:100%; justify-content:center; font-size:1.05rem;" onclick="startQuiz('mock')">
        🚀 Launch Timed Mock Test (30 Questions)
      </button>
    </div>
  `;
}

function startTopicQuiz() {
  const select = document.getElementById("topicSelect");
  const topic = select.value;
  currentMode = "topic";
  currentTopic = topic;
  const filtered = masterQuestions.filter(q => q.category === topic);
  activeQuestions = prepareQuizQuestions(filtered);
  initQuizState();
}

function startQuiz(mode) {
  currentMode = mode;
  if (mode === "mock") {
    activeQuestions = getRandomSample(masterQuestions, 30);
  } else if (mode === "website_official") {
    const pool = masterQuestions.filter(q => q.isWebsiteOfficial63);
    activeQuestions = prepareQuizQuestions(pool);
  } else if (mode === "website_all") {
    const pool = masterQuestions.filter(q => q.isWebsiteGenerated);
    activeQuestions = prepareQuizQuestions(pool);
  } else if (mode === "top30") {
    const pool = masterQuestions.filter(q => q.isTop30);
    activeQuestions = prepareQuizQuestions(pool);
  } else {
    activeQuestions = prepareQuizQuestions(masterQuestions);
  }
  initQuizState();
}

function initQuizState() {
  currentIndex = 0;
  score = 0;
  userAnswers = [];
  answered = false;
  startStopwatch();
  renderQuestion();
}

// ── Screen: Question View ──────────────────────────────────────
function renderQuestion() {
  answered = false;
  const q = activeQuestions[currentIndex];
  const progressPct = ((currentIndex) / activeQuestions.length) * 100;
  
  let modeLabel = "Timed Mock Test";
  if (currentMode === "website_official") modeLabel = "Masterdooom 63";
  else if (currentMode === "website_all") modeLabel = "26 Topics Bank";
  else if (currentMode === "top30") modeLabel = "Top 30 Pack";
  else if (currentMode === "all") modeLabel = "Mega Bank (259)";
  else if (currentMode === "topic") modeLabel = currentTopic;

  app.innerHTML = `
    <div class="quiz-nav-bar">
      <span class="mode-badge" title="${modeLabel}">🎯 ${modeLabel}</span>
      <span class="stopwatch-badge running" title="Elapsed Time">
        ⏱️ <span id="stopwatchDisplay">${formatStopwatch(elapsedSeconds)}</span>
      </span>
      <span>Question ${currentIndex + 1} of ${activeQuestions.length}</span>
      <span class="live-score">Score: ${score} / ${currentIndex}</span>
    </div>

    <div class="progress-track">
      <div class="progress-fill" style="width:${progressPct}%"></div>
    </div>

    <div class="quiz-body">
      <div class="meta-row">
        <span class="source-tag">${escapeHtml(q.category)}</span>
        <span class="random-tag">🔀 Shuffled Options</span>
      </div>
      <h2 class="question-title">${escapeHtml(q.question)}</h2>

      <ul class="options-grid" id="optionsList">
        ${q.options.map((opt, i) => `
          <li>
            <button class="option-btn" data-value="${escapeHtml(opt)}">
              <span class="option-badge">${letters[i]}</span>
              <span>${escapeHtml(opt)}</span>
            </button>
          </li>
        `).join("")}
      </ul>

      <div id="feedbackContainer"></div>

      <div class="action-row" id="actionRow" style="display:none;">
        <button class="btn btn-secondary" onclick="renderStartScreen()">Quit to Menu</button>
        <button class="btn" id="nextBtn">
          ${currentIndex === activeQuestions.length - 1 ? "Finish & View Results 🏆" : "Next Question →"}
        </button>
      </div>
    </div>
  `;

  document.querySelectorAll(".option-btn").forEach(btn => {
    btn.addEventListener("click", () => handleSelection(btn));
  });
}

function handleSelection(btn) {
  if (answered) return;
  answered = true;

  const selected = btn.dataset.value;
  const q = activeQuestions[currentIndex];
  const isCorrect = (selected === q.correctAnswer);

  if (isCorrect) {
    score++;
  }

  userAnswers.push({
    question: q.question,
    selected: selected,
    correct: q.correctAnswer,
    isCorrect: isCorrect,
    explanation: q.explanation,
    category: q.category
  });

  // Update score badge
  app.querySelector(".live-score").textContent = `Score: ${score} / ${currentIndex + 1}`;

  // Highlight and lock (correct answer highlighted regardless of slot)
  document.querySelectorAll(".option-btn").forEach(b => {
    b.classList.add("locked");
    if (b.dataset.value === q.correctAnswer) {
      b.classList.add("correct");
    }
    if (b === btn && !isCorrect) {
      b.classList.add("incorrect");
    }
  });

  // Instant explanation
  const feedbackContainer = document.getElementById("feedbackContainer");
  feedbackContainer.innerHTML = `
    <div class="feedback-box ${isCorrect ? "is-correct" : "is-wrong"}">
      <div class="feedback-status ${isCorrect ? "correct" : "wrong"}">
        ${isCorrect ? "✅ Correct!" : "❌ Incorrect. The correct answer is: " + escapeHtml(q.correctAnswer)}
      </div>
      <div class="explanation-text">${escapeHtml(q.explanation)}</div>
    </div>
  `;

  // Show Next button
  const actionRow = document.getElementById("actionRow");
  actionRow.style.display = "flex";

  document.getElementById("nextBtn").addEventListener("click", () => {
    currentIndex++;
    if (currentIndex < activeQuestions.length) {
      renderQuestion();
    } else {
      renderResults();
    }
  });
}

// ── Screen: Results Breakdown ──────────────────────────────────
function renderResults() {
  stopStopwatch();
  const total = activeQuestions.length;
  const pct = Math.round((score / total) * 100);
  const timeStr = formatStopwatch(elapsedSeconds);
  const avgSecPerQ = total > 0 ? Math.round(elapsedSeconds / total) : 0;

  let emoji = "🏆";
  let verdict = "Outstanding Mastery!";
  if (pct >= 85) {
    emoji = "🌟";
    verdict = "Outstanding Mastery! Exam Ready!";
  } else if (pct >= 70) {
    emoji = "🎯";
    verdict = "Great Performance! Strong grasp of concepts.";
  } else if (pct >= 50) {
    emoji = "📖";
    verdict = "Good Effort! Review your missed questions below.";
  } else {
    emoji = "💡";
    verdict = "Keep Practicing! Review the explanations below.";
  }

  app.innerHTML = `
    <div class="quiz-nav-bar">
      <span>Session Complete</span>
      <span class="stopwatch-badge">⏱️ Time: ${timeStr}</span>
      <span class="live-score">${score} / ${total} Correct</span>
    </div>
    <div class="progress-track">
      <div class="progress-fill" style="width:100%"></div>
    </div>

    <div class="results-screen">
      <div class="results-badge">${emoji}</div>
      <h2 style="font-size:1.75rem; font-weight:800;">${verdict}</h2>
      <div class="results-score-big">${score} / ${total}</div>
      <div class="results-pct">${pct}% Accuracy</div>

      <div class="time-stats-pill">
        <span>⏱️ Total Time: <strong>${timeStr}</strong></span>
        <span>•</span>
        <span>⚡ Pace: <strong>${avgSecPerQ}s</strong> / question</span>
      </div>

      <div style="display:flex; justify-content:center; gap:0.75rem; flex-wrap:wrap; margin-bottom: 2rem;">
        <button class="btn" onclick="startQuiz(currentMode)">🔄 Retake with Fresh Reshuffle</button>
        <button class="btn btn-secondary" onclick="renderStartScreen()">🏠 Switch Topic/Mode</button>
      </div>

      <div class="review-section">
        <h3>
          <span>Detailed Answer Review</span>
          <span style="font-size:0.85rem; color:var(--text-muted); font-weight:normal;">${userAnswers.filter(a => !a.isCorrect).length} mistakes</span>
        </h3>
        
        <ul class="review-list">
          ${userAnswers.map((item, idx) => `
            <li class="review-item ${item.isCorrect ? "is-correct" : "is-wrong"}">
              <div class="review-q">
                <span style="color:${item.isCorrect ? "#34d399" : "#f87171"}">${item.isCorrect ? "✔" : "✘"}</span>
                Q${idx + 1}: ${escapeHtml(item.question)}
              </div>
              <div class="review-ans">
                <strong>Your answer:</strong> ${escapeHtml(item.selected)} 
                ${!item.isCorrect ? `&bull; <strong style="color:#34d399">Correct:</strong> ${escapeHtml(item.correct)}` : ""}
              </div>
              <div class="review-explanation">
                💡 <strong>Why:</strong> ${escapeHtml(item.explanation)}
              </div>
            </li>
          `).join("")}
        </ul>
      </div>
    </div>
  `;
}

function escapeHtml(str) {
  if (!str) return "";
  return String(str).replace(/&/g, "&amp;")
                    .replace(/</g, "&lt;")
                    .replace(/>/g, "&gt;")
                    .replace(/"/g, "&quot;")
                    .replace(/'/g, "&#039;");
}

// ── Initialize App ─────────────────────────────────────────────
renderStartScreen();
</script>
</body>
</html>
"""

html_final = html_template.replace("__INJECTED_MASTER_QUESTIONS__", json_str)

with open("/Users/pran/devjams26/index.html", "w") as f:
    f.write(html_final)

print("Updated /Users/pran/devjams26/index.html with full question & option randomization.")
