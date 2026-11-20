import json

with open("/Users/pran/devjams26/master_questions.json", "r", encoding="utf-8") as f:
    master_data = json.load(f)

with open("/Users/pran/devjams26/unified_fat_notes.json", "r", encoding="utf-8") as f:
    fat_notes_data = json.load(f)

questions_json_str = json.dumps(master_data, ensure_ascii=False)
notes_json_str = json.dumps(fat_notes_data, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>EVS FAT Quiz & Revision Notes — VIT Vellore Exam Revision Bank</title>
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
      --fat-gold: #f59e0b;
      --fat-gradient: linear-gradient(135deg, #f59e0b, #ef4444);
      --site-badge: #10b981;
      --correct-bg: #064e3b;
      --correct-border: #10b981;
      --wrong-bg: #451010;
      --wrong-border: #ef4444;
      --timer-color: #f59e0b;
      --timer-bg: rgba(245, 158, 11, 0.12);
      --timer-border: rgba(245, 158, 11, 0.35);
      --notes-purple: #8b5cf6;
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
      max-width: 820px;
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 1.25rem;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.55), 0 0 0 1px rgba(255, 255, 255, 0.05);
      overflow: hidden;
      margin-top: 1rem;
      transition: max-width 0.25s ease;
    }

    .quiz-card.wide-mode {
      max-width: 960px;
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

    .brand-title {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #ffffff;
      font-size: 1rem;
      cursor: pointer;
    }
    .brand-title span.badge {
      background: var(--fat-gradient);
      color: #ffffff;
      font-size: 0.72rem;
      padding: 0.15rem 0.45rem;
      border-radius: 0.4rem;
      font-weight: 700;
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      flex-wrap: wrap;
    }

    .nav-notes-btn {
      background: rgba(139, 92, 246, 0.18);
      color: #c4b5fd;
      border: 1px solid rgba(139, 92, 246, 0.35);
      padding: 0.35rem 0.85rem;
      border-radius: 2rem;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      text-decoration: none;
    }
    .nav-notes-btn:hover {
      background: rgba(139, 92, 246, 0.32);
      color: #ffffff;
      transform: translateY(-1px);
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
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.1);
      padding: 0.25rem 0.65rem;
      border-radius: 0.5rem;
      border: 1px solid rgba(56, 189, 248, 0.2);
    }
    .source-tag.fat-tag {
      color: #fbbf24;
      background: rgba(245, 158, 11, 0.12);
      border-color: rgba(245, 158, 11, 0.3);
    }

    .random-tag {
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 500;
    }

    .question-title {
      font-size: 1.25rem;
      font-weight: 700;
      line-height: 1.5;
      margin-bottom: 1.75rem;
      color: #ffffff;
    }

    /* ── Options List ─────────────────────────────────────── */
    .options-grid {
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
      list-style: none;
    }

    .option-btn {
      width: 100%;
      text-align: left;
      padding: 1.05rem 1.25rem;
      background: #17233f;
      border: 1.5px solid #283a63;
      border-radius: 0.85rem;
      color: var(--text-main);
      font-size: 0.98rem;
      font-family: inherit;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      display: flex;
      align-items: flex-start;
      gap: 0.85rem;
      line-height: 1.4;
      user-select: none;
    }

    .option-btn:hover:not(:disabled) {
      background: #1e2c4f;
      border-color: #38bdf8;
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(56, 189, 248, 0.15);
    }

    .option-badge {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 1.75rem;
      height: 1.75rem;
      border-radius: 0.45rem;
      background: #253966;
      color: #cbd5e1;
      font-size: 0.85rem;
      font-weight: 700;
      flex-shrink: 0;
      margin-top: -0.1rem;
    }

    .option-btn:disabled {
      cursor: not-allowed;
    }

    /* Correct / Incorrect states */
    .option-btn.selected-correct {
      background: var(--correct-bg) !important;
      border-color: var(--correct-border) !important;
      color: #ecfdf5 !important;
      box-shadow: 0 0 15px rgba(16, 185, 129, 0.3) !important;
    }
    .option-btn.selected-correct .option-badge {
      background: #10b981;
      color: #ffffff;
    }

    .option-btn.selected-wrong {
      background: var(--wrong-bg) !important;
      border-color: var(--wrong-border) !important;
      color: #fef2f2 !important;
      box-shadow: 0 0 15px rgba(239, 68, 68, 0.3) !important;
    }
    .option-btn.selected-wrong .option-badge {
      background: #ef4444;
      color: #ffffff;
    }

    .option-btn.highlight-correct {
      background: rgba(16, 185, 129, 0.18) !important;
      border-color: #10b981 !important;
      color: #a7f3d0 !important;
    }
    .option-btn.highlight-correct .option-badge {
      background: #10b981;
      color: #ffffff;
    }

    .option-btn.faded {
      opacity: 0.45;
    }

    /* ── Instant Feedback Box ─────────────────────────────── */
    .feedback-box {
      margin-top: 1.5rem;
      padding: 1.25rem 1.35rem;
      border-radius: 0.85rem;
      font-size: 0.95rem;
      line-height: 1.55;
      animation: fadeIn 0.25s ease-out;
      border-left: 4px solid;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .feedback-box.is-correct {
      background: rgba(6, 78, 59, 0.35);
      border-left-color: #10b981;
      color: #d1fae5;
    }

    .feedback-box.is-wrong {
      background: rgba(69, 16, 16, 0.4);
      border-left-color: #ef4444;
      color: #fee2e2;
    }

    .feedback-status {
      font-weight: 800;
      font-size: 1.05rem;
      margin-bottom: 0.35rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .feedback-explanation {
      color: #cbd5e1;
      font-size: 0.92rem;
    }

    /* ── Action Buttons ───────────────────────────────────── */
    .action-row {
      margin-top: 1.75rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      flex-wrap: wrap;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.85rem 1.6rem;
      border-radius: 0.75rem;
      font-size: 0.98rem;
      font-weight: 700;
      font-family: inherit;
      cursor: pointer;
      border: none;
      background: var(--accent-gradient);
      color: #ffffff;
      box-shadow: 0 4px 15px rgba(6, 182, 212, 0.3);
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(6, 182, 212, 0.45);
    }

    .btn-fat {
      background: var(--fat-gradient);
      box-shadow: 0 4px 15px rgba(245, 158, 11, 0.3);
    }
    .btn-fat:hover {
      box-shadow: 0 6px 20px rgba(245, 158, 11, 0.45);
    }

    .btn-secondary {
      background: #17233f;
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

    .brand-hero {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 0.75rem;
    }
    .brand-hero h1 {
      font-size: 2.2rem;
      font-weight: 900;
      letter-spacing: -0.03em;
      background: linear-gradient(135deg, #ffffff, #cbd5e1);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .brand-hero .fat-pill {
      background: var(--fat-gradient);
      color: #ffffff;
      font-size: 0.9rem;
      font-weight: 800;
      padding: 0.25rem 0.65rem;
      border-radius: 0.5rem;
      text-transform: uppercase;
      box-shadow: 0 2px 10px rgba(245, 158, 11, 0.3);
    }

    .start-subtitle {
      color: var(--text-muted);
      font-size: 0.98rem;
      margin-bottom: 1.5rem;
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
    .feature-pill.notes-pill-top {
      color: #c4b5fd;
      background: rgba(139, 92, 246, 0.12);
      border-color: rgba(139, 92, 246, 0.35);
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

    /* FAT Featured All 420 Questions */
    .mode-card.fat-featured {
      border-color: #f59e0b;
      background: linear-gradient(145deg, #17233f, #2e2311);
    }

    /* Timed Mock 40 Questions */
    .mode-card.mock-featured {
      border-color: #6366f1;
      background: linear-gradient(145deg, #17233f, #1e2448);
    }

    .mode-card.featured {
      border-color: #10b981;
      background: linear-gradient(145deg, #17233f, #132e3b);
    }

    /* Dates, Treaties, WHO & SDGs Card */
    .mode-card.treaties-featured {
      border-color: #06b6d4;
      background: linear-gradient(145deg, #17233f, #0c2b3a);
    }
    .mode-card.treaties-featured:hover {
      border-color: #22d3ee;
      background: #113649;
    }
    .mode-card.treaties-featured .mode-badge-count {
      color: #22d3ee;
      background: rgba(6, 182, 212, 0.15);
      border: 1px solid rgba(6, 182, 212, 0.35);
    }

    /* Notes Card */
    .mode-card.notes-card {
      border-color: #8b5cf6;
      background: linear-gradient(145deg, #17233f, #231942);
    }
    .mode-card.notes-card:hover {
      border-color: #a78bfa;
      background: #241d4c;
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

    .mode-card.fat-featured .mode-badge-count {
      color: #fbbf24;
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.35);
    }

    .mode-card.mock-featured .mode-badge-count {
      color: #38bdf8;
      background: rgba(99, 102, 241, 0.15);
      border: 1px solid rgba(99, 102, 241, 0.35);
    }

    .mode-card.featured .mode-badge-count {
      color: #34d399;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.3);
    }

    .mode-card.notes-card .mode-badge-count {
      color: #c4b5fd;
      background: rgba(139, 92, 246, 0.15);
      border: 1px solid rgba(139, 92, 246, 0.35);
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

    /* ── Single Unified FAT Notes Viewer Screen ───────────── */
    .notes-screen {
      padding: 2.25rem 2rem;
      text-align: left;
    }

    .notes-header {
      margin-bottom: 1.5rem;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 1.25rem;
    }

    .notes-header-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.5rem;
      flex-wrap: wrap;
      gap: 0.75rem;
    }

    .notes-header h2 {
      font-size: 1.6rem;
      font-weight: 800;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .notes-header p {
      font-size: 0.92rem;
      color: var(--text-muted);
      line-height: 1.45;
    }

    /* Search Box */
    .notes-search-container {
      position: relative;
      margin-bottom: 1.25rem;
    }

    .notes-search-input {
      width: 100%;
      padding: 0.85rem 1.2rem 0.85rem 2.6rem;
      background: #17233f;
      border: 1.5px solid #283a63;
      border-radius: 0.75rem;
      color: #ffffff;
      font-size: 0.95rem;
      font-family: inherit;
      outline: none;
      transition: all 0.2s ease;
    }

    .notes-search-input:focus {
      border-color: #38bdf8;
      box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.15);
    }

    .notes-search-icon {
      position: absolute;
      left: 0.9rem;
      top: 50%;
      transform: translateY(-50%);
      font-size: 1rem;
      color: var(--text-muted);
    }

    /* Category Pill Filters */
    .notes-pills {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      margin-bottom: 1.5rem;
    }

    .notes-pill {
      font-size: 0.78rem;
      font-weight: 600;
      padding: 0.35rem 0.8rem;
      border-radius: 2rem;
      border: 1px solid #283a63;
      background: #17233f;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .notes-pill:hover, .notes-pill.active {
      background: rgba(245, 158, 11, 0.18);
      color: #fbbf24;
      border-color: rgba(245, 158, 11, 0.4);
    }

    /* Note Card & Section Layout */
    .note-item {
      background: #17233f;
      border: 1px solid #283a63;
      border-radius: 1rem;
      padding: 1.5rem;
      margin-bottom: 1.25rem;
      transition: all 0.2s ease;
    }

    .note-item-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 0.75rem;
      gap: 0.75rem;
      flex-wrap: wrap;
    }

    .note-item-title {
      font-size: 1.18rem;
      font-weight: 700;
      color: #ffffff;
    }

    .note-item-sub {
      font-size: 0.88rem;
      color: var(--text-muted);
      margin-bottom: 1rem;
      line-height: 1.45;
    }

    .note-tag {
      font-size: 0.72rem;
      font-weight: 700;
      padding: 0.2rem 0.55rem;
      border-radius: 0.35rem;
      text-transform: uppercase;
      letter-spacing: 0.03em;
      background: rgba(245, 158, 11, 0.18);
      color: #fbbf24;
      border: 1px solid rgba(245, 158, 11, 0.35);
    }

    /* Tables in Notes */
    .notes-table-wrap {
      overflow-x: auto;
      margin: 1rem 0;
      border-radius: 0.65rem;
      border: 1px solid #283a63;
    }

    .notes-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.86rem;
      text-align: left;
    }

    .notes-table th {
      background: #1e2e50;
      color: #cbd5e1;
      padding: 0.75rem 1rem;
      font-weight: 700;
      border-bottom: 1px solid #283a63;
      white-space: nowrap;
    }

    .notes-table td {
      padding: 0.75rem 1rem;
      border-bottom: 1px solid #203155;
      color: #e2e8f0;
      vertical-align: top;
      line-height: 1.45;
    }

    .notes-table tr:last-child td {
      border-bottom: none;
    }

    .notes-table tr:hover td {
      background: rgba(56, 189, 248, 0.04);
    }

    /* Bullet List in Notes */
    .note-bullets {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.55rem;
      margin-top: 0.75rem;
    }

    .note-bullets li {
      position: relative;
      padding-left: 1.4rem;
      font-size: 0.9rem;
      color: #cbd5e1;
      line-height: 1.5;
    }

    .note-bullets li::before {
      content: "•";
      position: absolute;
      left: 0.4rem;
      color: #f59e0b;
      font-weight: 900;
    }

    .note-section-block {
      margin-top: 1.25rem;
      padding-top: 1.25rem;
      border-top: 1px dashed #283a63;
    }
    .note-section-block:first-child {
      margin-top: 0;
      padding-top: 0;
      border-top: none;
    }
    .note-section-heading {
      font-size: 1rem;
      font-weight: 700;
      color: #38bdf8;
      margin-bottom: 0.5rem;
    }
    .note-section-content {
      font-size: 0.9rem;
      color: #cbd5e1;
      line-height: 1.55;
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
      font-size: 1.2rem;
      font-weight: 700;
      margin-bottom: 1.25rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: #ffffff;
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
      .notes-screen { padding: 1.5rem 1rem; }
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
// ── Master Question Bank (All 420 Questions Combined) ──────────
const masterQuestions = __QUESTIONS_JSON__;

// ── Unified FAT Revision Notes Data ────────────────────────────
const fatNotesData = __NOTES_JSON__;

// ── Application State ──────────────────────────────────────────
let activeQuestions = [];
let currentIndex = 0;
let score = 0;
let answered = false;
let userAnswers = [];
let currentMode = "fat_all";
let currentTopic = "";

// Notes viewer state (One unified FAT Notes section)
let notesActivePill = "all";
let notesSearchTerm = "";

// Stopwatch State
let elapsedSeconds = 0;
let timerInterval = null;
let timerStartTime = null;

const app = document.getElementById("quizCard");
const letters = ["A", "B", "C", "D"];

// ── Fisher-Yates Array Shuffle ─────────────────────────────────
function shuffleArray(origArray) {
  const arr = [...origArray];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// Shuffles both question sequence and each question's 4 options
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
  app.classList.remove("wide-mode");
  const categories = [...new Set(masterQuestions.map(q => q.category))].sort();

  app.innerHTML = `
    <div class="start-screen">
      <div class="brand-hero">
        <div style="font-size:2.2rem;">🌿</div>
        <h1>EVS FAT Quiz</h1>
        <span class="fat-pill">FAT 2026</span>
      </div>
      <p class="start-subtitle">
        Comprehensive EVS FAT Exam Bank combining all 420 questions with high-yield focus revision, 40-Q timed mock tests, and a dedicated FAT revision notes section.
      </p>

      <div class="features-pill-row">
        <span class="feature-pill">🎓 435 Total MCQs</span>
        <span class="feature-pill">⭐ 65 High-Yield Focus</span>
        <span class="feature-pill" style="color:#22d3ee; border-color:rgba(6,182,212,0.35); background:rgba(6,182,212,0.12); cursor:pointer;" onclick="startQuiz('dates_treaties_sdg')">🏛️ Dates & Treaties Drill</span>
        <span class="feature-pill">⏱️ 40-Q Timed Mock</span>
        <span class="feature-pill notes-pill-top" onclick="renderNotesScreen()" style="cursor:pointer;">📖 FAT Notes (18 Modules)</span>
        <span class="feature-pill">🔀 Shuffled Options</span>
      </div>

      <div class="mode-cards">
        <!-- 1. FAT All Questions Combined (Old + New) -->
        <div class="mode-card fat-featured" onclick="startQuiz('fat_all')">
          <div>
            <h3>🎓 EVS FAT Master Bank (All 435 Questions)</h3>
            <p>Includes all old and new questions combined: Climate Change, Carbon Footprint, Solar & Wind, Hydro, Geothermal, AI & IoT, Ecosystems, Biodiversity, and Environmental Laws.</p>
          </div>
          <span class="mode-badge-count">435 Questions</span>
        </div>

        <!-- 2. Timed Mock Test (40 Questions) -->
        <div class="mode-card mock-featured" onclick="startQuiz('mock')">
          <div>
            <h3>⏱️ Timed Mock Test (40 Random Questions)</h3>
            <p>Generates 40 randomized questions sampled across the entire syllabus with live stopwatch tracking on top and average pace analytics.</p>
          </div>
          <span class="mode-badge-count">⏱️ 40 Random · Timed</span>
        </div>

        <!-- 3. FAT Focus Bank (Only Important Questions) -->
        <div class="mode-card featured" onclick="startQuiz('fat_focus')">
          <div>
            <h3>⭐ FAT Focus Bank (Important Questions Only)</h3>
            <p>Curated bank of ONLY the 65 most critical, frequently tested questions across Climate Change, Carbon Accounting, Renewables (Solar, Wind, Hydro, Geothermal), AI/IoT, and Core Environmental Laws.</p>
          </div>
          <span class="mode-badge-count">⭐ 65 Important MCQs</span>
        </div>

        <!-- 4. Dates, Treaties, WHO & SDGs Drill -->
        <div class="mode-card treaties-featured" onclick="startQuiz('dates_treaties_sdg')">
          <div>
            <h3>🏛️ Dates, Treaties, WHO & SDGs Bank (91 Questions)</h3>
            <p>Targeted exam drill testing ONLY historical dates & enactment years of environmental acts, international climate treaties (Paris, Kyoto, Montreal, Kigali, Basel, Stockholm, Minamata, Ramsar, CITES), WHO health standards, and UN Sustainable Development Goals.</p>
          </div>
          <span class="mode-badge-count">🏛️ 91 Target MCQs</span>
        </div>

        <!-- 5. Single Unified FAT Notes Section -->
        <div class="mode-card notes-card" onclick="renderNotesScreen()">
          <div>
            <h3>📖 EVS FAT Revision Notes (All 18 Modules & Cheat Sheets)</h3>
            <p>Comprehensive FAT revision notes covering all 18 modules: Numbers Cheat Sheet, Climate Science, Carbon Accounting, Renewables (Solar, Wind, Hydro, Geothermal), AI & IoT, Ecosystems, Biodiversity, Pollution, Environmental Laws, and Exam Tips.</p>
          </div>
          <span class="mode-badge-count">📖 FAT Notes</span>
        </div>
      </div>

      <div class="topic-select-row">
        <label for="topicSelect">Or Practice by Specific Exam Section:</label>
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
          <select id="topicSelect" class="topic-dropdown">
            ${categories.map(c => {
              const count = masterQuestions.filter(q => q.category === c).length;
              return `<option value="${c}">${c} (${count} questions)</option>`;
            }).join("")}
          </select>
          <button class="btn btn-secondary" onclick="startTopicQuiz()">Practice Section</button>
        </div>
      </div>

      <div style="display:flex; gap:0.75rem; justify-content:center; flex-wrap:wrap;">
        <button class="btn btn-fat" style="flex:1; min-width:200px; justify-content:center; font-size:1.02rem;" onclick="startQuiz('fat_all')">
          🚀 Start All 435 Questions
        </button>
        <button class="btn" style="flex:1; min-width:200px; justify-content:center; font-size:1.02rem;" onclick="startQuiz('mock')">
          ⏱️ Launch 40-Q Mock Test
        </button>
        <button class="btn btn-secondary" style="flex:1; min-width:200px; justify-content:center; font-size:1.02rem;" onclick="startQuiz('fat_focus')">
          ⭐ Launch 65-Q Focus Bank
        </button>
        <button class="btn btn-secondary" style="flex:1; min-width:200px; justify-content:center; font-size:1.02rem; background:rgba(6,182,212,0.18); border-color:#06b6d4; color:#22d3ee;" onclick="startQuiz('dates_treaties_sdg')">
          🏛️ Launch Dates & Treaties
        </button>
        <button class="btn btn-secondary" style="flex:1; min-width:200px; justify-content:center; font-size:1.02rem; background:rgba(139,92,246,0.2); border-color:#8b5cf6; color:#c4b5fd;" onclick="renderNotesScreen()">
          📖 Read FAT Notes
        </button>
      </div>
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
    // Exactly 40 random questions sampled across entire bank
    activeQuestions = getRandomSample(masterQuestions, 40);
  } else if (mode === "fat_focus") {
    // Only the curated 65 important questions
    const pool = masterQuestions.filter(q => q.isFatFocus);
    activeQuestions = prepareQuizQuestions(pool);
  } else if (mode === "dates_treaties_sdg") {
    // Dedicated quiz for Dates, Treaties, WHO, and SDGs (91 questions)
    const pool = masterQuestions.filter(q => q.isDatesTreatiesSdg);
    activeQuestions = prepareQuizQuestions(pool);
  } else {
    // All old + new questions combined together (435 questions)
    activeQuestions = prepareQuizQuestions(masterQuestions);
  }
  initQuizState();
}

function initQuizState() {
  app.classList.remove("wide-mode");
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
  
  let modeLabel = "EVS FAT Quiz";
  if (currentMode === "fat_all") modeLabel = "FAT All 435 MCQs";
  else if (currentMode === "mock") modeLabel = "40-Q Timed Mock";
  else if (currentMode === "fat_focus") modeLabel = "FAT Focus (65 Qs)";
  else if (currentMode === "dates_treaties_sdg") modeLabel = "Dates & Treaties (91 Qs)";
  else if (currentMode === "topic") modeLabel = currentTopic;

  const isFat = q.isFatExam;

  app.innerHTML = `
    <div class="quiz-nav-bar">
      <div class="brand-title" onclick="renderStartScreen()">
        <span>EVS FAT Quiz</span>
        <span class="badge">FAT</span>
      </div>
      <div class="nav-actions">
        <button class="nav-notes-btn" onclick="renderNotesScreen()" title="Open FAT Revision Notes">📖 FAT Notes</button>
        <span class="mode-badge" title="${modeLabel}">🎯 ${modeLabel}</span>
        <span class="stopwatch-badge running" title="Elapsed Time">
          ⏱️ <span id="stopwatchDisplay">${formatStopwatch(elapsedSeconds)}</span>
        </span>
        <span>Q${currentIndex + 1}/${activeQuestions.length}</span>
        <span class="live-score">Score: ${score}</span>
      </div>
    </div>

    <div class="progress-track">
      <div class="progress-fill" style="width:${progressPct}%"></div>
    </div>

    <div class="quiz-body">
      <div class="meta-row">
        <span class="source-tag ${isFat ? 'fat-tag' : ''}">${escapeHtml(q.category)}</span>
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

  // Attach option click listeners
  const optionButtons = document.querySelectorAll(".option-btn");
  optionButtons.forEach(btn => {
    btn.addEventListener("click", () => handleSelectOption(btn, q));
  });
}

function handleSelectOption(selectedBtn, q) {
  if (answered) return;
  answered = true;

  const selectedValue = selectedBtn.getAttribute("data-value");
  const isCorrect = (selectedValue === q.correctAnswer);

  if (isCorrect) score++;

  userAnswers.push({
    question: q.question,
    selected: selectedValue,
    correct: q.correctAnswer,
    isCorrect: isCorrect,
    explanation: q.explanation
  });

  const buttons = document.querySelectorAll(".option-btn");
  buttons.forEach(btn => {
    btn.disabled = true;
    const val = btn.getAttribute("data-value");

    if (val === q.correctAnswer) {
      if (isCorrect) {
        btn.classList.add("selected-correct");
      } else {
        btn.classList.add("highlight-correct");
      }
    } else if (val === selectedValue && !isCorrect) {
      btn.classList.add("selected-wrong");
    } else {
      btn.classList.add("faded");
    }
  });

  // Render Instant Feedback Box
  const feedbackBox = document.getElementById("feedbackContainer");
  feedbackBox.innerHTML = `
    <div class="feedback-box ${isCorrect ? 'is-correct' : 'is-wrong'}">
      <div class="feedback-status">
        ${isCorrect ? "✔ Correct!" : "✘ Incorrect"}
      </div>
      <div class="feedback-explanation">
        ${escapeHtml(q.explanation)}
      </div>
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
  app.classList.remove("wide-mode");
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
      <div class="brand-title" onclick="renderStartScreen()">
        <span>EVS FAT Quiz</span>
        <span class="badge">FAT</span>
      </div>
      <div class="nav-actions">
        <button class="nav-notes-btn" onclick="renderNotesScreen()">📖 FAT Notes</button>
        <span class="stopwatch-badge">⏱️ Time: ${timeStr}</span>
        <span class="live-score">${score} / ${total} Correct</span>
      </div>
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
        <button class="btn btn-fat" onclick="startQuiz('mock')">⏱️ Start Another 40-Q Mock Test</button>
        <button class="btn btn-secondary" onclick="startQuiz('fat_focus')">⭐ Practice FAT Focus Bank</button>
        <button class="btn btn-secondary" style="border-color:#06b6d4; color:#22d3ee;" onclick="startQuiz('dates_treaties_sdg')">🏛️ Practice Dates, Treaties & SDGs</button>
        <button class="btn btn-secondary" style="border-color:#8b5cf6; color:#c4b5fd;" onclick="renderNotesScreen()">📖 Read FAT Revision Notes</button>
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

// ── Screen: Single Unified EVS FAT Revision Notes Viewer ───────
function renderNotesScreen() {
  stopStopwatch();
  app.classList.add("wide-mode");

  app.innerHTML = `
    <div class="quiz-nav-bar">
      <div class="brand-title" onclick="renderStartScreen()">
        <span>EVS FAT Quiz</span>
        <span class="badge">FAT</span>
      </div>
      <div class="nav-actions">
        <button class="btn btn-secondary" style="padding:0.35rem 0.85rem; font-size:0.82rem;" onclick="renderStartScreen()">← Back to Quiz</button>
      </div>
    </div>

    <div class="notes-screen">
      <div class="notes-header">
        <div class="notes-header-top">
          <h2>📖 EVS FAT Revision Notes & Cheat Sheets</h2>
          <button class="btn btn-secondary" style="font-size:0.85rem; padding:0.4rem 0.9rem;" onclick="renderStartScreen()">← Return to Quiz Modes</button>
        </div>
        <p>
          Complete, unified revision notes covering all 18 exam modules: Numbers Cheat Sheet, Climate Science, Carbon Accounting, Renewables (Solar, Wind, Hydro, Geothermal), AI & IoT, Ecosystems, Biodiversity, Pollution, Environmental Laws, and Exam Tips.
        </p>
      </div>

      <!-- Real-time Search Box -->
      <div class="notes-search-container">
        <span class="notes-search-icon">🔍</span>
        <input 
          type="text" 
          id="notesSearchInput" 
          class="notes-search-input" 
          placeholder="Search any keyword, formula, standard, or law (e.g. 'Paris', 'Scope 3', 'Betz', 'Bhopal', 'Inverter', 'Tehri', 'Minamata', '10%', 'pH')..." 
          value="${escapeHtml(notesSearchTerm)}"
          oninput="handleNotesSearch(this.value)"
        />
      </div>

      <!-- Category Filter Pills -->
      <div class="notes-pills" id="notesPillsContainer">
        <!-- Rendered dynamically -->
      </div>

      <!-- Notes Content Container -->
      <div id="notesCardsContainer">
        <!-- Rendered dynamically -->
      </div>
    </div>
  `;

  renderNotesPills();
  renderNotesContent();
}

function renderNotesPills() {
  const container = document.getElementById("notesPillsContainer");
  if (!container) return;

  const categories = [
    { id: "all", label: "All Modules (18)" },
    { id: "Cheat Sheet & Numbers", label: "📌 Numbers & Cheat Sheet" },
    { id: "Climate & Carbon", label: "🌡️ Climate & Carbon" },
    { id: "Renewable Energy", label: "☀️ Renewable Energy" },
    { id: "AI & IoT", label: "🤖 AI & IoT Monitoring" },
    { id: "Earth & Ecosystems", label: "🌿 Earth & Ecosystems" },
    { id: "Biodiversity", label: "🦋 Biodiversity" },
    { id: "Pollution & Waste", label: "🏭 Pollution & Waste" },
    { id: "Waste & Circular", label: "🔄 Circular Economy" },
    { id: "Hazards & Disasters", label: "⚠️ Hazards & Disasters" },
    { id: "Environmental Laws", label: "⚖️ Environmental Laws" },
    { id: "International Treaties", label: "🌐 Treaties & SDGs" }
  ];

  container.innerHTML = categories.map(c => `
    <button class="notes-pill ${notesActivePill === c.id ? 'active' : ''}" onclick="selectNotesPill('${c.id}')">
      ${c.label}
    </button>
  `).join("");
}

function selectNotesPill(pillId) {
  notesActivePill = pillId;
  renderNotesPills();
  renderNotesContent();
}

function handleNotesSearch(term) {
  notesSearchTerm = term.trim().toLowerCase();
  renderNotesContent();
}

function renderNotesContent() {
  const container = document.getElementById("notesCardsContainer");
  if (!container) return;

  let items = fatNotesData;
  if (notesActivePill !== "all") {
    items = items.filter(n => n.category === notesActivePill);
  }

  const term = notesSearchTerm;
  if (term) {
    items = items.filter(n => {
      const textToSearch = (
        n.title + " " + n.category + " " + n.summary + " " +
        JSON.stringify(n.tableRows || []) + " " +
        JSON.stringify(n.sections || []) + " " +
        JSON.stringify(n.bullets || [])
      ).toLowerCase();
      return textToSearch.includes(term);
    });
  }

  if (items.length === 0) {
    container.innerHTML = `
      <div style="text-align:center; padding:3rem 1rem; color:var(--text-muted);">
        <div style="font-size:2.5rem; margin-bottom:0.75rem;">🔍</div>
        <h3>No matching FAT notes found for "${escapeHtml(notesSearchTerm)}"</h3>
        <p style="margin-top:0.5rem; font-size:0.9rem;">Try a broader keyword or select 'All Modules' above.</p>
      </div>
    `;
    return;
  }

  container.innerHTML = items.map(n => renderUnifiedNoteCard(n)).join("");
}

function renderUnifiedNoteCard(n) {
  let innerHtml = "";

  if (n.type === "table") {
    innerHtml = `
      <div class="notes-table-wrap">
        <table class="notes-table">
          <thead>
            <tr>
              ${n.tableHeaders.map(h => `<th>${escapeHtml(h)}</th>`).join("")}
            </tr>
          </thead>
          <tbody>
            ${n.tableRows.map(row => `
              <tr>
                <td style="font-weight:600; color:#38bdf8; min-width:240px;">${escapeHtml(row[0])}</td>
                <td>${escapeHtml(row[1])}</td>
              </tr>
            `).join("")}
          </tbody>
        </table>
      </div>
    `;
  } else if (n.type === "sections") {
    innerHtml = n.sections.map(sec => `
      <div class="note-section-block">
        <div class="note-section-heading">${escapeHtml(sec.heading)}</div>
        ${sec.content ? `<div class="note-section-content">${sec.content}</div>` : ""}
        ${sec.tableHeaders ? `
          <div class="notes-table-wrap">
            <table class="notes-table">
              <thead>
                <tr>
                  ${sec.tableHeaders.map(h => `<th>${escapeHtml(h)}</th>`).join("")}
                </tr>
              </thead>
              <tbody>
                ${sec.tableRows.map(row => `
                  <tr>
                    <td style="font-weight:600; color:#38bdf8; min-width:180px;">${escapeHtml(row[0])}</td>
                    <td>${escapeHtml(row[1])}</td>
                    ${row[2] ? `<td>${escapeHtml(row[2])}</td>` : ""}
                  </tr>
                `).join("")}
              </tbody>
            </table>
          </div>
        ` : ""}
      </div>
    `).join("");
  } else if (n.type === "bullets") {
    innerHtml = `
      <ul class="note-bullets">
        ${n.bullets.map(b => `<li>${escapeHtml(b)}</li>`).join("")}
      </ul>
    `;
  }

  return `
    <div class="note-item">
      <div class="note-item-header">
        <div>
          <span class="note-tag">${escapeHtml(n.category)}</span>
          <h3 class="note-item-title" style="margin-top:0.4rem;">${escapeHtml(n.title)}</h3>
        </div>
        <span class="note-tag" style="background:#24355a; color:#cbd5e1;">${escapeHtml(n.badge)}</span>
      </div>
      <p class="note-item-sub">${escapeHtml(n.summary)}</p>
      ${innerHtml}
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

final_html = html_template.replace("__QUESTIONS_JSON__", questions_json_str).replace("__NOTES_JSON__", notes_json_str)

output_path = "/Users/pran/devjams26/index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Generated {output_path} successfully ({len(final_html)} bytes).")
