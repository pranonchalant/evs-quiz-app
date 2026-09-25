import json

with open("/Users/pran/devjams26/questions.json") as f:
    questions_data = json.load(f)

json_str = json.dumps(questions_data, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>EVS High-Yield Exam Prep Quiz</title>
  <style>
    /* ── Reset & Variables ────────────────────────────────── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg-color: #090d16;
      --card-bg: #131b2e;
      --card-header: #1a243b;
      --border-color: #23314e;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --accent: #38bdf8;
      --accent-gradient: linear-gradient(135deg, #6366f1, #06b6d4);
      --correct-bg: #064e3b;
      --correct-border: #10b981;
      --correct-text: #a7f3d0;
      --wrong-bg: #451010;
      --wrong-border: #ef4444;
      --wrong-text: #fecaca;
    }

    body {
      font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--bg-color);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 1.5rem 1rem 3rem;
      background-image: 
        radial-gradient(ellipse 80% 50% at 50% -20%, rgba(99, 102, 241, 0.15), transparent),
        radial-gradient(ellipse 60% 40% at 50% 120%, rgba(6, 182, 212, 0.1), transparent);
    }

    /* ── Quiz Card Container ──────────────────────────────── */
    .app-card {
      width: 100%;
      max-width: 760px;
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 1.25rem;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.05);
      overflow: hidden;
      margin-top: 1rem;
    }

    /* ── Header ───────────────────────────────────────────── */
    .quiz-nav-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1.15rem 1.75rem;
      background: var(--card-header);
      border-bottom: 1px solid var(--border-color);
      font-size: 0.92rem;
      font-weight: 600;
    }

    .mode-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: rgba(56, 189, 248, 0.12);
      color: var(--accent);
      padding: 0.3rem 0.75rem;
      border-radius: 2rem;
      font-size: 0.8rem;
      border: 1px solid rgba(56, 189, 248, 0.3);
    }

    .live-score {
      color: #34d399;
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 0.3rem 0.75rem;
      border-radius: 2rem;
      font-size: 0.82rem;
      font-weight: 700;
    }

    /* ── Progress Bar ─────────────────────────────────────── */
    .progress-track {
      height: 6px;
      background: #182239;
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

    .category-tag {
      display: inline-block;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
      margin-bottom: 0.6rem;
      font-weight: 700;
    }

    .question-title {
      font-size: 1.25rem;
      font-weight: 600;
      line-height: 1.55;
      margin-bottom: 1.75rem;
      color: #ffffff;
    }

    /* ── Options ──────────────────────────────────────────── */
    .options-grid {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }

    .option-btn {
      width: 100%;
      text-align: left;
      padding: 1.05rem 1.35rem;
      font-size: 1rem;
      font-family: inherit;
      color: var(--text-main);
      background: #182239;
      border: 1.5px solid #283756;
      border-radius: 0.85rem;
      cursor: pointer;
      transition: all 0.18s ease;
      display: flex;
      align-items: center;
      gap: 1rem;
      line-height: 1.4;
    }

    .option-btn:hover:not(.locked) {
      background: #202d4b;
      border-color: #4f46e5;
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(99, 102, 241, 0.15);
    }

    .option-badge {
      flex-shrink: 0;
      width: 2.1rem;
      height: 2.1rem;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 0.55rem;
      background: #253350;
      font-weight: 700;
      font-size: 0.9rem;
      color: var(--text-muted);
      transition: all 0.18s ease;
    }

    /* Selected Correct */
    .option-btn.correct {
      background: var(--correct-bg) !important;
      border-color: var(--correct-border) !important;
      color: #ffffff !important;
      box-shadow: 0 0 16px rgba(16, 185, 129, 0.25);
    }
    .option-btn.correct .option-badge {
      background: #10b981;
      color: #064e3b;
    }

    /* Selected Incorrect */
    .option-btn.incorrect {
      background: var(--wrong-bg) !important;
      border-color: var(--wrong-border) !important;
      color: #ffffff !important;
      box-shadow: 0 0 16px rgba(239, 68, 68, 0.25);
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

    /* ── Instant Feedback Explanation Box ─────────────────── */
    .feedback-box {
      margin-top: 1.75rem;
      padding: 1.25rem 1.5rem;
      border-radius: 0.85rem;
      animation: slideUp 0.25s ease forwards;
      background: #182239;
      border: 1px solid #283756;
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

    /* ── Next Button & Action Bars ─────────────────────────── */
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
      background: #202d4b;
      color: #cbd5e1;
      border: 1px solid var(--border-color);
      box-shadow: none;
    }
    .btn-secondary:hover {
      background: #2a3b61;
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
      font-size: 1rem;
      margin-bottom: 2rem;
      line-height: 1.5;
    }

    .mode-cards {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1rem;
      margin-bottom: 2rem;
      text-align: left;
    }

    .mode-card {
      background: #182239;
      border: 2px solid #283756;
      border-radius: 1rem;
      padding: 1.25rem 1.5rem;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .mode-card:hover, .mode-card.active {
      border-color: #38bdf8;
      background: #1c2945;
      transform: translateY(-2px);
    }

    .mode-card.featured {
      border-color: #6366f1;
      background: linear-gradient(145deg, #182239, #1e2448);
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
    }

    .mode-badge-count {
      background: #253350;
      color: var(--accent);
      padding: 0.35rem 0.75rem;
      border-radius: 2rem;
      font-size: 0.8rem;
      font-weight: 700;
      white-space: nowrap;
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
      background: #182239;
      color: #ffffff;
      border: 1.5px solid #283756;
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
      background: #2a3b61;
      border-radius: 4px;
    }

    .review-item {
      background: #182239;
      border-radius: 0.75rem;
      padding: 1rem 1.25rem;
      border: 1px solid #283756;
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
      border-top: 1px dashed #283756;
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

<div class="app-card" id="quizCard">
  <!-- Dynamic Views Injected via JavaScript -->
</div>

<script>
// ── Complete Question Bank from EVS High-Yield Exam Prep PDF (177 MCQs) ──
const rawQuestions = __INJECTED_QUESTIONS_JSON__;

// ── State Management ───────────────────────────────────────────
let currentMode = "top30"; // "top30" | "all" | "topic"
let currentTopic = "";
let activeQuestions = [];
let currentIndex = 0;
let score = 0;
let answered = false;
let userAnswers = []; // records { question, selected, correct, isCorrect, explanation }

const app = document.getElementById("quizCard");
const letters = ["A", "B", "C", "D"];

// ── Screen: Mode Selection ─────────────────────────────────────
function renderStartScreen() {
  const topics = [...new Set(rawQuestions.map(q => q.category))].sort();

  app.innerHTML = `
    <div class="start-screen">
      <div style="font-size:2.5rem; margin-bottom: 0.5rem;">🌿 📝</div>
      <h1>EVS MCQ High-Yield Question Bank</h1>
      <p class="start-subtitle">
        30 Core High-Yield Exam MCQs + 147 Extended Practice Questions with Instant Rationale.
      </p>

      <div class="mode-cards">
        <div class="mode-card featured" onclick="startQuiz('top30')">
          <div>
            <h3>⭐ PART A — Core Top 30 MCQs</h3>
            <p>The 30 highest-yield exam preparation questions with instant answers & explanations.</p>
          </div>
          <span class="mode-badge-count">30 Questions</span>
        </div>

        <div class="mode-card" onclick="startQuiz('all')">
          <div>
            <h3>📚 Full Practice Bank</h3>
            <p>Every single question from the exam preparation pack (Questions 1 to 177).</p>
          </div>
          <span class="mode-badge-count">177 Questions</span>
        </div>
      </div>

      <div class="topic-select-row">
        <label for="topicSelect">Or Practice by Specific Exam Section:</label>
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
          <select id="topicSelect" class="topic-dropdown">
            ${topics.map(t => {
              const count = rawQuestions.filter(q => q.category === t).length;
              return `<option value="${t}">${t} (${count} questions)</option>`;
            }).join("")}
          </select>
          <button class="btn btn-secondary" onclick="startTopicQuiz()">Practice Topic</button>
        </div>
      </div>

      <button class="btn" style="width:100%; justify-content:center; font-size:1.05rem;" onclick="startQuiz('top30')">
        🚀 Start Core Top 30 Exam Quiz
      </button>
    </div>
  `;
}

function startTopicQuiz() {
  const select = document.getElementById("topicSelect");
  const topic = select.value;
  currentMode = "topic";
  currentTopic = topic;
  activeQuestions = rawQuestions.filter(q => q.category === topic);
  initQuizState();
}

function startQuiz(mode) {
  currentMode = mode;
  if (mode === "top30") {
    activeQuestions = rawQuestions.filter(q => q.isTop30);
  } else {
    activeQuestions = [...rawQuestions];
  }
  initQuizState();
}

function initQuizState() {
  currentIndex = 0;
  score = 0;
  userAnswers = [];
  answered = false;
  renderQuestion();
}

// ── Screen: Question View ──────────────────────────────────────
function renderQuestion() {
  answered = false;
  const q = activeQuestions[currentIndex];
  const progressPct = ((currentIndex) / activeQuestions.length) * 100;
  
  let modeLabel = "Core Top 30";
  if (currentMode === "all") modeLabel = "All 177 Questions";
  if (currentMode === "topic") modeLabel = currentTopic;

  app.innerHTML = `
    <div class="quiz-nav-bar">
      <span class="mode-badge">🎯 ${modeLabel}</span>
      <span>Question ${currentIndex + 1} of ${activeQuestions.length}</span>
      <span class="live-score">Score: ${score} / ${currentIndex}</span>
    </div>

    <div class="progress-track">
      <div class="progress-fill" style="width:${progressPct}%"></div>
    </div>

    <div class="quiz-body">
      <span class="category-tag">${q.category}</span>
      <h2 class="question-title">${q.question}</h2>

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

  // Update header score pill
  app.querySelector(".live-score").textContent = `Score: ${score} / ${currentIndex + 1}`;

  // Highlight choices and lock
  document.querySelectorAll(".option-btn").forEach(b => {
    b.classList.add("locked");
    if (b.dataset.value === q.correctAnswer) {
      b.classList.add("correct");
    }
    if (b === btn && !isCorrect) {
      b.classList.add("incorrect");
    }
  });

  // Show immediate 1-2 sentence explanation
  const feedbackContainer = document.getElementById("feedbackContainer");
  feedbackContainer.innerHTML = `
    <div class="feedback-box ${isCorrect ? "is-correct" : "is-wrong"}">
      <div class="feedback-status ${isCorrect ? "correct" : "wrong"}">
        ${isCorrect ? "✅ Correct!" : "❌ Incorrect. The right answer is: " + escapeHtml(q.correctAnswer)}
      </div>
      <div class="explanation-text">${q.explanation}</div>
    </div>
  `;

  // Show the Next button
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
  const total = activeQuestions.length;
  const pct = Math.round((score / total) * 100);

  let emoji = "🏆";
  let verdict = "Outstanding Mastery!";
  if (pct >= 85) {
    emoji = "🌟";
    verdict = "Outstanding Mastery! Ready for the exam!";
  } else if (pct >= 70) {
    emoji = "🎯";
    verdict = "Great Job! Solid grasp of high-yield concepts.";
  } else if (pct >= 50) {
    emoji = "📖";
    verdict = "Good Effort! Review your missed concepts below.";
  } else {
    emoji = "💡";
    verdict = "Keep Practicing! Review the high-yield facts below.";
  }

  app.innerHTML = `
    <div class="quiz-nav-bar">
      <span>Exam Session Complete</span>
      <span class="live-score">${score} of ${total} Correct</span>
    </div>
    <div class="progress-track">
      <div class="progress-fill" style="width:100%"></div>
    </div>

    <div class="results-screen">
      <div class="results-badge">${emoji}</div>
      <h2 style="font-size:1.75rem; font-weight:800;">${verdict}</h2>
      <div class="results-score-big">${score} / ${total}</div>
      <div class="results-pct">${pct}% Accuracy</div>

      <div style="display:flex; justify-content:center; gap:0.75rem; flex-wrap:wrap; margin-bottom: 2rem;">
        <button class="btn" onclick="initQuizState()">🔄 Retake This Quiz</button>
        <button class="btn btn-secondary" onclick="renderStartScreen()">🏠 Change Exam Section</button>
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
                <strong>Your pick:</strong> ${escapeHtml(item.selected)} 
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

html_final = html_template.replace("__INJECTED_QUESTIONS_JSON__", json_str)

with open("/Users/pran/devjams26/index.html", "w") as f:
    f.write(html_final)

print("index.html compiled successfully with all 177 questions from PDF!")
