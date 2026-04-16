# FAQ Chatbot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a deterministic, multilingual FAQ chatbot as two standalone HTML files (chat widget + admin panel) with localStorage persistence and no external dependencies.

**Architecture:** Two HTML files share a `storage.js` module that handles all localStorage reads/writes and seed data initialization. The chat widget reads config and renders dynamically; the admin panel writes config and auto-saves on every change.

**Tech Stack:** Vanilla HTML5, CSS3, JavaScript (ES6+), localStorage API — no frameworks, no build tools.

---

## File Structure

| File | Responsibility |
|------|---------------|
| `projects/web-development/faq-chatbot/storage.js` | localStorage read/write, seed data, data model helpers |
| `projects/web-development/faq-chatbot/index.html` | Chat widget — all widget UI and matching logic |
| `projects/web-development/faq-chatbot/admin.html` | Admin panel — tabbed config UI, auto-saves to localStorage |
| `.github/skills/faq-chatbot/SKILL.md` | Skill documentation for this chatbot |
| `Skill Test/faq-chatbot/test.html` | Manual test checklist with in-browser verification steps |
| `.github/workflows/publish-confluence.yml` | GitHub Action — triggers on push to main, publishes docs to Confluence |
| `.github/scripts/publish_to_confluence.py` | Python script that converts docs to Confluence storage format and calls the API |

---

## Task 1: Project Scaffold + Data Layer

**Files:**
- Create: `projects/web-development/faq-chatbot/storage.js`

- [ ] **Step 1: Create the project directory and storage.js**

Create the file `projects/web-development/faq-chatbot/storage.js` with the full content below:

```javascript
// storage.js — FAQ Chatbot data layer
// All reads and writes to localStorage go through these functions.

const STORAGE_KEY = 'faq_config';

const SEED_DATA = {
  settings: {
    widgetTitle: { en: 'FAQ', ja: 'よくある質問' },
    welcomeMessage: { en: 'How can we help you today?', ja: 'ご質問をお選びください。' },
    theme: '#005A9C',
    fallbackMode: 'both',
    fallbackPhone: '0120-XXX-XXX',
    fallbackEmail: 'support@example.com',
    supportedLanguages: [
      { code: 'en', label: 'English' },
      { code: 'ja', label: '日本語' }
    ]
  },
  categories: [
    {
      id: 'cat_reimbursement',
      label: { en: 'Reimbursement', ja: '保険適用' },
      faqs: [
        {
          id: 'q_reimb_1',
          source: 'en',
          question: {
            en: 'What are the reimbursement criteria?',
            ja: '保険適用の基準は何ですか？'
          },
          answer: {
            en: 'Reimbursement is available for patients who meet the following criteria: confirmed diagnosis, prior authorization from a specialist, and prescription from a licensed physician.',
            ja: '以下の基準を満たす患者に保険が適用されます：確定診断、専門医による事前承認、および認定医師による処方。'
          }
        },
        {
          id: 'q_reimb_2',
          source: 'en',
          question: {
            en: 'How do I submit a reimbursement claim?',
            ja: '保険請求はどのように申請しますか？'
          },
          answer: {
            en: 'Submit the completed claim form along with supporting documentation to your regional insurance office within 30 days of treatment.',
            ja: '治療から30日以内に、必要書類とともに記入済みの申請書を地域の保険事務所に提出してください。'
          }
        },
        {
          id: 'q_reimb_3',
          source: 'en',
          question: {
            en: 'Which insurance plans are covered?',
            ja: 'どの保険プランが対象ですか？'
          },
          answer: {
            en: 'This product is covered under National Health Insurance (NHI) and most supplemental insurance plans. Please confirm with your specific insurer.',
            ja: 'この製品は国民健康保険および多くの補足保険プランの対象です。具体的な保険会社にご確認ください。'
          }
        }
      ]
    },
    {
      id: 'cat_prescription',
      label: { en: 'Prescription', ja: '処方' },
      faqs: [
        {
          id: 'q_presc_1',
          source: 'en',
          question: {
            en: 'Who can prescribe this medication?',
            ja: 'この薬を処方できるのは誰ですか？'
          },
          answer: {
            en: 'This medication must be prescribed by a licensed physician with appropriate specialist qualifications. General practitioners may prescribe with specialist consultation.',
            ja: 'この薬は適切な専門資格を持つ認定医師が処方する必要があります。一般開業医は専門医との相談のうえ処方することができます。'
          }
        },
        {
          id: 'q_presc_2',
          source: 'en',
          question: {
            en: 'What is the recommended dosage?',
            ja: '推奨用量は何ですか？'
          },
          answer: {
            en: 'Dosage should be determined by the prescribing physician based on the patient\'s individual clinical profile. Please refer to the approved prescribing information.',
            ja: '用量は処方医が患者の個別の臨床プロファイルに基づいて決定する必要があります。承認された処方情報を参照してください。'
          }
        },
        {
          id: 'q_presc_3',
          source: 'en',
          question: {
            en: 'Are there any contraindications?',
            ja: '禁忌事項はありますか？'
          },
          answer: {
            en: 'Yes, contraindications include hypersensitivity to the active substance and concurrent use of certain medications. Please review the full prescribing information for a complete list.',
            ja: 'はい、禁忌には活性物質に対する過敏症および特定の薬との併用が含まれます。完全なリストについては処方情報全文をご確認ください。'
          }
        }
      ]
    }
  ]
};

function loadConfig() {
  const raw = localStorage.getItem(STORAGE_KEY);
  if (!raw) {
    saveConfig(SEED_DATA);
    return SEED_DATA;
  }
  return JSON.parse(raw);
}

function saveConfig(config) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(config));
}

function getText(obj, lang) {
  if (typeof obj === 'string') return obj;
  return obj[lang] || obj['en'] || Object.values(obj)[0] || '';
}
```

- [ ] **Step 2: Verify the file was created**

Open `projects/web-development/faq-chatbot/storage.js` in the editor and confirm the `SEED_DATA`, `loadConfig`, `saveConfig`, and `getText` functions are present.

- [ ] **Step 3: Commit**

```bash
git init projects/web-development/faq-chatbot || true
cd projects/web-development/faq-chatbot
git add storage.js
git commit -m "feat: add data layer with localStorage persistence and seed data"
```

---

## Task 2: Chat Widget — HTML Structure + CSS

**Files:**
- Create: `projects/web-development/faq-chatbot/index.html`

- [ ] **Step 1: Create index.html with full structure and styles**

Create `projects/web-development/faq-chatbot/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>FAQ Chatbot</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Helvetica Neue', Arial, 'Hiragino Kaku Gothic ProN', sans-serif;
      background: #f4f6f9;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }

    #chatbot {
      width: 380px;
      max-width: 100%;
      border-radius: 12px;
      box-shadow: 0 4px 24px rgba(0,0,0,0.12);
      overflow: hidden;
      background: #fff;
      display: flex;
      flex-direction: column;
    }

    #chat-header {
      background: var(--theme, #005A9C);
      color: #fff;
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    #chat-header h1 {
      font-size: 17px;
      font-weight: 600;
    }

    #lang-toggle {
      display: flex;
      gap: 6px;
    }

    .lang-btn {
      background: rgba(255,255,255,0.2);
      border: 1px solid rgba(255,255,255,0.5);
      color: #fff;
      padding: 3px 8px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 12px;
      transition: background 0.2s;
    }

    .lang-btn.active {
      background: rgba(255,255,255,0.4);
      font-weight: 700;
    }

    #chat-body {
      padding: 20px;
      flex: 1;
      overflow-y: auto;
      max-height: 480px;
    }

    #welcome-msg {
      color: #555;
      font-size: 14px;
      margin-bottom: 16px;
      line-height: 1.5;
    }

    #search-bar {
      display: flex;
      gap: 8px;
      margin-bottom: 16px;
    }

    #search-input {
      flex: 1;
      border: 1px solid #ddd;
      border-radius: 6px;
      padding: 8px 12px;
      font-size: 14px;
      outline: none;
      transition: border-color 0.2s;
    }

    #search-input:focus { border-color: var(--theme, #005A9C); }

    #search-btn {
      background: var(--theme, #005A9C);
      color: #fff;
      border: none;
      border-radius: 6px;
      padding: 8px 14px;
      cursor: pointer;
      font-size: 13px;
    }

    .section-label {
      font-size: 12px;
      color: #888;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 8px;
    }

    .category-btn {
      display: block;
      width: 100%;
      text-align: left;
      background: #f0f4fa;
      border: none;
      border-radius: 8px;
      padding: 12px 16px;
      margin-bottom: 8px;
      cursor: pointer;
      font-size: 14px;
      color: #222;
      transition: background 0.2s;
    }

    .category-btn:hover { background: #dce8f7; }

    .faq-btn {
      display: block;
      width: 100%;
      text-align: left;
      background: none;
      border: 1px solid #e5e5e5;
      border-radius: 8px;
      padding: 11px 14px;
      margin-bottom: 8px;
      cursor: pointer;
      font-size: 14px;
      color: #333;
      transition: background 0.2s, border-color 0.2s;
    }

    .faq-btn:hover { background: #f7f9fc; border-color: var(--theme, #005A9C); }

    .back-btn {
      background: none;
      border: none;
      color: var(--theme, #005A9C);
      cursor: pointer;
      font-size: 13px;
      margin-bottom: 14px;
      padding: 0;
      display: flex;
      align-items: center;
      gap: 4px;
    }

    #answer-box {
      background: #f7f9fc;
      border-radius: 8px;
      padding: 16px;
      font-size: 14px;
      line-height: 1.7;
      color: #333;
      margin-bottom: 16px;
    }

    #answer-question {
      font-weight: 600;
      margin-bottom: 10px;
      color: #111;
    }

    #fallback-box {
      border-top: 1px solid #eee;
      padding-top: 14px;
      font-size: 13px;
      color: #555;
    }

    #fallback-box .fallback-label {
      margin-bottom: 8px;
    }

    #fallback-phone {
      font-weight: 600;
      color: #222;
      display: block;
      margin-bottom: 6px;
    }

    #fallback-email-btn {
      display: inline-block;
      background: var(--theme, #005A9C);
      color: #fff;
      padding: 7px 16px;
      border-radius: 6px;
      text-decoration: none;
      font-size: 13px;
    }

    .hidden { display: none !important; }
  </style>
</head>
<body>
<div id="chatbot">
  <div id="chat-header">
    <h1 id="header-title">FAQ</h1>
    <div id="lang-toggle"></div>
  </div>
  <div id="chat-body">
    <!-- Home State -->
    <div id="state-home">
      <p id="welcome-msg"></p>
      <div id="search-bar">
        <input id="search-input" type="text" placeholder="Search..." />
        <button id="search-btn">&#128269;</button>
      </div>
      <p class="section-label" id="categories-label">Topics</p>
      <div id="category-list"></div>
    </div>

    <!-- Category State -->
    <div id="state-category" class="hidden">
      <button class="back-btn" id="back-from-category">&#8592; <span id="back-label-cat">Back</span></button>
      <p class="section-label" id="faq-list-label">Questions</p>
      <div id="faq-list"></div>
    </div>

    <!-- Answer State -->
    <div id="state-answer" class="hidden">
      <button class="back-btn" id="back-from-answer">&#8592; <span id="back-label-ans">Back</span></button>
      <div id="answer-box">
        <p id="answer-question"></p>
        <p id="answer-text"></p>
      </div>
      <div id="fallback-box">
        <p class="fallback-label" id="fallback-label-text">Need more help?</p>
        <span id="fallback-phone" class="hidden"></span>
        <a id="fallback-email-btn" href="#" class="hidden"></a>
      </div>
    </div>
  </div>
</div>
<script src="storage.js"></script>
<script src="widget.js"></script>
</body>
</html>
```

- [ ] **Step 2: Commit**

```bash
git add index.html
git commit -m "feat: add chat widget HTML structure and CSS"
```

---

## Task 3: Chat Widget — JavaScript Logic

**Files:**
- Create: `projects/web-development/faq-chatbot/widget.js`

- [ ] **Step 1: Create widget.js**

Create `projects/web-development/faq-chatbot/widget.js`:

```javascript
// widget.js — Chat widget logic

(function () {
  let config = loadConfig();
  let lang = detectLang();
  let currentCategoryId = null;

  // ── Language detection ──────────────────────────────────────────────────
  function detectLang() {
    const supported = config.settings.supportedLanguages.map(l => l.code);
    const browser = (navigator.language || 'en').split('-')[0];
    return supported.includes(browser) ? browser : 'en';
  }

  function setLang(code) {
    lang = code;
    render();
  }

  // ── Matching logic ──────────────────────────────────────────────────────
  function normalize(str) {
    return str.toLowerCase().replace(/[^\w\s\u3000-\u9fff\uff00-\uffef]/g, '').trim();
  }

  function tokenize(str) {
    return normalize(str).split(/\s+/).filter(Boolean);
  }

  function findBestMatch(query) {
    const queryTokens = tokenize(query);
    if (queryTokens.length === 0) return null;

    let best = null;
    let bestScore = 0;

    config.categories.forEach(cat => {
      cat.faqs.forEach(faq => {
        const questionText = getText(faq.question, lang);
        const answerText = getText(faq.answer, lang);
        const haystack = normalize(questionText + ' ' + answerText);
        const haystackTokens = tokenize(haystack);

        let score = 0;
        queryTokens.forEach(token => {
          if (haystackTokens.includes(token)) score += 2;
          else if (haystack.includes(token)) score += 1;
        });

        if (score > bestScore) {
          bestScore = score;
          best = faq;
        }
      });
    });

    return bestScore > 0 ? best : null;
  }

  // ── State management ────────────────────────────────────────────────────
  function showState(stateName) {
    ['home', 'category', 'answer'].forEach(s => {
      document.getElementById('state-' + s).classList.toggle('hidden', s !== stateName);
    });
  }

  // ── Rendering ────────────────────────────────────────────────────────────
  function applyTheme() {
    document.documentElement.style.setProperty('--theme', config.settings.theme || '#005A9C');
  }

  function renderLangToggle() {
    const container = document.getElementById('lang-toggle');
    container.innerHTML = '';
    config.settings.supportedLanguages.forEach(l => {
      const btn = document.createElement('button');
      btn.className = 'lang-btn' + (l.code === lang ? ' active' : '');
      btn.textContent = l.label;
      btn.addEventListener('click', () => setLang(l.code));
      container.appendChild(btn);
    });
  }

  function renderHome() {
    document.getElementById('header-title').textContent = getText(config.settings.widgetTitle, lang);
    document.getElementById('welcome-msg').textContent = getText(config.settings.welcomeMessage, lang);
    document.getElementById('search-input').placeholder = lang === 'ja' ? '検索...' : 'Search...';
    document.getElementById('categories-label').textContent = lang === 'ja' ? 'トピック' : 'Topics';

    const list = document.getElementById('category-list');
    list.innerHTML = '';
    config.categories.forEach(cat => {
      const btn = document.createElement('button');
      btn.className = 'category-btn';
      btn.textContent = getText(cat.label, lang);
      btn.addEventListener('click', () => showCategory(cat.id));
      list.appendChild(btn);
    });
  }

  function renderCategory(catId) {
    const cat = config.categories.find(c => c.id === catId);
    if (!cat) return;
    currentCategoryId = catId;

    document.getElementById('header-title').textContent = getText(cat.label, lang);
    document.getElementById('back-label-cat').textContent = lang === 'ja' ? '戻る' : 'Back';
    document.getElementById('faq-list-label').textContent = lang === 'ja' ? '質問' : 'Questions';

    const list = document.getElementById('faq-list');
    list.innerHTML = '';
    cat.faqs.forEach(faq => {
      const btn = document.createElement('button');
      btn.className = 'faq-btn';
      btn.textContent = getText(faq.question, lang);
      btn.addEventListener('click', () => showAnswer(faq));
      list.appendChild(btn);
    });
  }

  function renderAnswer(faq) {
    document.getElementById('header-title').textContent = getText(config.settings.widgetTitle, lang);
    document.getElementById('back-label-ans').textContent = lang === 'ja' ? '戻る' : 'Back';
    document.getElementById('answer-question').textContent = getText(faq.question, lang);
    document.getElementById('answer-text').textContent = getText(faq.answer, lang);

    const s = config.settings;
    const phoneEl = document.getElementById('fallback-phone');
    const emailEl = document.getElementById('fallback-email-btn');
    const labelEl = document.getElementById('fallback-label-text');

    labelEl.textContent = lang === 'ja' ? 'さらにサポートが必要ですか？' : 'Need more help?';

    phoneEl.classList.toggle('hidden', s.fallbackMode === 'email');
    emailEl.classList.toggle('hidden', s.fallbackMode === 'phone');

    phoneEl.textContent = s.fallbackPhone;
    emailEl.href = 'mailto:' + s.fallbackEmail;
    emailEl.textContent = lang === 'ja' ? 'メールで問い合わせる' : 'Contact via Email';
  }

  function render() {
    config = loadConfig();
    applyTheme();
    renderLangToggle();
    renderHome();
  }

  // ── Navigation ───────────────────────────────────────────────────────────
  function showCategory(catId) {
    renderCategory(catId);
    showState('category');
  }

  function showAnswer(faq) {
    renderAnswer(faq);
    showState('answer');
  }

  // ── Events ────────────────────────────────────────────────────────────────
  document.getElementById('back-from-category').addEventListener('click', () => {
    renderHome();
    showState('home');
  });

  document.getElementById('back-from-answer').addEventListener('click', () => {
    if (currentCategoryId) {
      renderCategory(currentCategoryId);
      showState('category');
    } else {
      renderHome();
      showState('home');
    }
  });

  document.getElementById('search-btn').addEventListener('click', () => {
    const query = document.getElementById('search-input').value;
    const match = findBestMatch(query);
    if (match) {
      currentCategoryId = null;
      showAnswer(match);
    } else {
      // Show fallback in answer state with no specific answer
      currentCategoryId = null;
      const noMatch = {
        question: { en: 'No results found', ja: '該当する結果が見つかりませんでした' },
        answer: { en: 'We could not find an answer for your query. Please contact us directly.', ja: 'お問い合わせの回答が見つかりませんでした。直接お問い合わせください。' }
      };
      showAnswer(noMatch);
    }
  });

  document.getElementById('search-input').addEventListener('keydown', (e) => {
    if (e.key === 'Enter') document.getElementById('search-btn').click();
  });

  // ── Init ──────────────────────────────────────────────────────────────────
  render();
  showState('home');
})();
```

- [ ] **Step 2: Update index.html script reference**

In `index.html`, change:
```html
<script src="widget.js"></script>
```
This is already in the file from Task 2. Verify the line exists.

- [ ] **Step 3: Open index.html in browser and verify**

Open `projects/web-development/faq-chatbot/index.html` directly in a browser (file://).

Expected:
- Chat widget renders with blue header "FAQ"
- Two language buttons (English, 日本語) visible in header
- Welcome message visible
- Two category buttons: "Reimbursement" and "Prescription"
- Search input and button visible
- Clicking a category shows a list of FAQ questions
- Clicking a question shows the answer + fallback info
- Back button returns to previous state
- Language toggle switches all text instantly

- [ ] **Step 4: Commit**

```bash
git add widget.js index.html
git commit -m "feat: add chat widget logic — states, matching, language toggle"
```

---

## Task 4: Admin Panel — HTML Structure + CSS

**Files:**
- Create: `projects/web-development/faq-chatbot/admin.html`

- [ ] **Step 1: Create admin.html**

Create `projects/web-development/faq-chatbot/admin.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>FAQ Admin Panel</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Helvetica Neue', Arial, 'Hiragino Kaku Gothic ProN', sans-serif;
      background: #f0f2f5;
      color: #222;
    }

    header {
      background: #005A9C;
      color: #fff;
      padding: 16px 32px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    header h1 { font-size: 18px; font-weight: 600; }

    #save-indicator {
      font-size: 13px;
      background: rgba(255,255,255,0.15);
      padding: 4px 12px;
      border-radius: 4px;
      opacity: 0;
      transition: opacity 0.3s;
    }

    #save-indicator.visible { opacity: 1; }

    .container {
      max-width: 860px;
      margin: 32px auto;
      padding: 0 16px;
    }

    .tabs {
      display: flex;
      gap: 4px;
      margin-bottom: 0;
      border-bottom: 2px solid #ddd;
    }

    .tab-btn {
      padding: 10px 22px;
      border: none;
      background: none;
      cursor: pointer;
      font-size: 14px;
      color: #666;
      border-bottom: 3px solid transparent;
      margin-bottom: -2px;
      transition: color 0.2s;
    }

    .tab-btn.active {
      color: #005A9C;
      border-bottom-color: #005A9C;
      font-weight: 600;
    }

    .tab-panel { display: none; padding-top: 24px; }
    .tab-panel.active { display: block; }

    .card {
      background: #fff;
      border-radius: 10px;
      padding: 20px 24px;
      margin-bottom: 16px;
      box-shadow: 0 1px 4px rgba(0,0,0,0.07);
    }

    .card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
    }

    .card-title { font-size: 15px; font-weight: 600; }

    label {
      display: block;
      font-size: 13px;
      color: #555;
      margin-bottom: 4px;
      margin-top: 12px;
    }

    label:first-of-type { margin-top: 0; }

    input[type="text"], input[type="email"], input[type="tel"], input[type="color"], textarea, select {
      width: 100%;
      border: 1px solid #ddd;
      border-radius: 6px;
      padding: 8px 12px;
      font-size: 14px;
      outline: none;
      transition: border-color 0.2s;
      font-family: inherit;
    }

    input[type="color"] {
      padding: 2px 6px;
      height: 36px;
      cursor: pointer;
    }

    input:focus, textarea:focus, select:focus { border-color: #005A9C; }

    textarea { min-height: 80px; resize: vertical; }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 13px;
      cursor: pointer;
      border: none;
      transition: background 0.2s;
    }

    .btn-primary { background: #005A9C; color: #fff; }
    .btn-primary:hover { background: #004880; }
    .btn-danger { background: #e53e3e; color: #fff; }
    .btn-danger:hover { background: #c53030; }
    .btn-outline { background: #fff; color: #005A9C; border: 1px solid #005A9C; }
    .btn-outline:hover { background: #f0f6ff; }
    .btn-sm { padding: 5px 10px; font-size: 12px; }

    .lang-tabs { display: flex; gap: 4px; margin-bottom: 12px; }

    .lang-tab-btn {
      padding: 5px 14px;
      border-radius: 4px;
      border: 1px solid #ddd;
      background: #f7f7f7;
      cursor: pointer;
      font-size: 13px;
    }

    .lang-tab-btn.active { background: #005A9C; color: #fff; border-color: #005A9C; }

    .faq-item {
      border: 1px solid #eee;
      border-radius: 8px;
      padding: 14px;
      margin-bottom: 10px;
    }

    .faq-item-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 10px;
    }

    .faq-item-title { font-size: 13px; color: #888; }

    .lang-row { display: none; }
    .lang-row.active { display: block; }

    .field-row { display: flex; gap: 12px; align-items: flex-start; }
    .field-row > * { flex: 1; }

    .section-divider { border: none; border-top: 1px solid #eee; margin: 16px 0; }

    .lang-list-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 0;
      border-bottom: 1px solid #f0f0f0;
    }

    .lang-locked { color: #999; font-size: 12px; }

    #fallback-phone-row, #fallback-email-row { transition: opacity 0.2s; }
  </style>
</head>
<body>
<header>
  <h1>FAQ Admin Panel</h1>
  <span id="save-indicator">&#10003; Changes saved</span>
</header>

<div class="container">
  <div class="tabs">
    <button class="tab-btn active" data-tab="content">Content</button>
    <button class="tab-btn" data-tab="languages">Languages</button>
    <button class="tab-btn" data-tab="settings">Settings</button>
  </div>

  <!-- Content Tab -->
  <div class="tab-panel active" id="tab-content">
    <div style="display:flex; justify-content:flex-end; margin-bottom:12px;">
      <button class="btn btn-primary" id="add-category-btn">+ Add Category</button>
    </div>
    <div id="categories-container"></div>
  </div>

  <!-- Languages Tab -->
  <div class="tab-panel" id="tab-languages">
    <div class="card">
      <div class="card-header">
        <span class="card-title">Supported Languages</span>
      </div>
      <div id="lang-list-container"></div>
      <hr class="section-divider" />
      <p style="font-size:13px; color:#555; margin-bottom:12px;">Add a new language:</p>
      <div class="field-row">
        <div>
          <label>Language Code (e.g. fr, de, zh)</label>
          <input type="text" id="new-lang-code" placeholder="fr" maxlength="5" />
        </div>
        <div>
          <label>Display Name</label>
          <input type="text" id="new-lang-label" placeholder="Français" />
        </div>
      </div>
      <div style="margin-top:12px;">
        <button class="btn btn-primary" id="add-lang-btn">+ Add Language</button>
      </div>
    </div>
  </div>

  <!-- Settings Tab -->
  <div class="tab-panel" id="tab-settings">
    <div class="card">
      <p class="card-title" style="margin-bottom:16px;">UI Text</p>
      <div id="settings-ui-text"></div>
    </div>
    <div class="card">
      <p class="card-title" style="margin-bottom:16px;">Appearance</p>
      <label>Theme Color</label>
      <input type="color" id="theme-color" />
    </div>
    <div class="card">
      <p class="card-title" style="margin-bottom:16px;">Fallback / Contact</p>
      <label>Fallback Mode</label>
      <select id="fallback-mode">
        <option value="phone">Phone only</option>
        <option value="email">Email only</option>
        <option value="both">Phone + Email</option>
      </select>
      <div id="fallback-phone-row">
        <label>Phone Number</label>
        <input type="tel" id="fallback-phone" placeholder="0120-XXX-XXX" />
      </div>
      <div id="fallback-email-row">
        <label>Email Address</label>
        <input type="email" id="fallback-email" placeholder="support@example.com" />
      </div>
    </div>
  </div>
</div>

<script src="storage.js"></script>
<script src="admin.js"></script>
</body>
</html>
```

- [ ] **Step 2: Commit**

```bash
git add admin.html
git commit -m "feat: add admin panel HTML structure and CSS"
```

---

## Task 5: Admin Panel — JavaScript Logic

**Files:**
- Create: `projects/web-development/faq-chatbot/admin.js`

- [ ] **Step 1: Create admin.js**

Create `projects/web-development/faq-chatbot/admin.js`:

```javascript
// admin.js — Admin panel logic

(function () {
  let config = loadConfig();
  let activeLangPerFaq = {};

  // ── Utilities ─────────────────────────────────────────────────────────────
  function uid() {
    return 'id_' + Math.random().toString(36).slice(2, 9);
  }

  function showSaved() {
    const el = document.getElementById('save-indicator');
    el.classList.add('visible');
    setTimeout(() => el.classList.remove('visible'), 1800);
  }

  function persist() {
    saveConfig(config);
    showSaved();
  }

  // ── Tabs ──────────────────────────────────────────────────────────────────
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      document.getElementById('tab-' + btn.dataset.tab).classList.add('active');
    });
  });

  // ── Content Tab ───────────────────────────────────────────────────────────
  function getLangCodes() {
    return config.settings.supportedLanguages.map(l => l.code);
  }

  function getLangLabel(code) {
    const l = config.settings.supportedLanguages.find(x => x.code === code);
    return l ? l.label : code;
  }

  function renderLangTabs(faqId, container) {
    const codes = getLangCodes();
    const active = activeLangPerFaq[faqId] || codes[0];
    activeLangPerFaq[faqId] = active;

    const tabBar = document.createElement('div');
    tabBar.className = 'lang-tabs';

    codes.forEach(code => {
      const btn = document.createElement('button');
      btn.className = 'lang-tab-btn' + (code === active ? ' active' : '');
      btn.textContent = getLangLabel(code);
      btn.addEventListener('click', () => {
        activeLangPerFaq[faqId] = code;
        container.querySelectorAll('.lang-tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        container.querySelectorAll('.lang-row').forEach(r => {
          r.classList.toggle('active', r.dataset.lang === code);
        });
      });
      tabBar.appendChild(btn);
    });

    return tabBar;
  }

  function renderFaqItem(cat, faq) {
    const item = document.createElement('div');
    item.className = 'faq-item';
    item.dataset.faqId = faq.id;

    const header = document.createElement('div');
    header.className = 'faq-item-header';
    const title = document.createElement('span');
    title.className = 'faq-item-title';
    title.textContent = 'FAQ';
    const delBtn = document.createElement('button');
    delBtn.className = 'btn btn-danger btn-sm';
    delBtn.textContent = 'Delete';
    delBtn.addEventListener('click', () => {
      cat.faqs = cat.faqs.filter(f => f.id !== faq.id);
      persist();
      renderContent();
    });
    header.appendChild(title);
    header.appendChild(delBtn);
    item.appendChild(header);

    const tabsContainer = document.createElement('div');
    item.appendChild(renderLangTabs(faq.id, item));
    item.appendChild(tabsContainer);

    const codes = getLangCodes();
    const activeLang = activeLangPerFaq[faq.id] || codes[0];

    codes.forEach(code => {
      const row = document.createElement('div');
      row.className = 'lang-row' + (code === activeLang ? ' active' : '');
      row.dataset.lang = code;

      const qLabel = document.createElement('label');
      qLabel.textContent = 'Question (' + getLangLabel(code) + ')';
      const qInput = document.createElement('input');
      qInput.type = 'text';
      qInput.value = faq.question[code] || '';
      qInput.addEventListener('input', () => {
        faq.question[code] = qInput.value;
        persist();
      });

      const aLabel = document.createElement('label');
      aLabel.textContent = 'Answer (' + getLangLabel(code) + ')';
      const aInput = document.createElement('textarea');
      aInput.value = faq.answer[code] || '';
      aInput.addEventListener('input', () => {
        faq.answer[code] = aInput.value;
        persist();
      });

      row.appendChild(qLabel);
      row.appendChild(qInput);
      row.appendChild(aLabel);
      row.appendChild(aInput);
      item.appendChild(row);
    });

    return item;
  }

  function renderCategoryCard(cat) {
    const card = document.createElement('div');
    card.className = 'card';

    const header = document.createElement('div');
    header.className = 'card-header';

    const title = document.createElement('span');
    title.className = 'card-title';

    const codes = getLangCodes();
    const titleText = codes.map(code => {
      const inp = document.createElement('input');
      inp.type = 'text';
      inp.placeholder = 'Category name (' + getLangLabel(code) + ')';
      inp.value = cat.label[code] || '';
      inp.style.marginBottom = '6px';
      inp.addEventListener('input', () => {
        cat.label[code] = inp.value;
        persist();
      });
      return inp;
    });

    const labelWrap = document.createElement('div');
    labelWrap.style.flex = '1';
    titleText.forEach(inp => labelWrap.appendChild(inp));

    const delCatBtn = document.createElement('button');
    delCatBtn.className = 'btn btn-danger btn-sm';
    delCatBtn.style.marginLeft = '12px';
    delCatBtn.textContent = 'Delete Category';
    delCatBtn.addEventListener('click', () => {
      config.categories = config.categories.filter(c => c.id !== cat.id);
      persist();
      renderContent();
    });

    header.appendChild(labelWrap);
    header.appendChild(delCatBtn);
    card.appendChild(header);

    const faqContainer = document.createElement('div');
    cat.faqs.forEach(faq => {
      faqContainer.appendChild(renderFaqItem(cat, faq));
    });
    card.appendChild(faqContainer);

    const addFaqBtn = document.createElement('button');
    addFaqBtn.className = 'btn btn-outline btn-sm';
    addFaqBtn.textContent = '+ Add Question';
    addFaqBtn.addEventListener('click', () => {
      const newFaq = {
        id: uid(),
        source: 'en',
        question: {},
        answer: {}
      };
      cat.faqs.push(newFaq);
      persist();
      renderContent();
    });
    card.appendChild(addFaqBtn);

    return card;
  }

  function renderContent() {
    config = loadConfig();
    const container = document.getElementById('categories-container');
    container.innerHTML = '';
    config.categories.forEach(cat => {
      container.appendChild(renderCategoryCard(cat));
    });
  }

  document.getElementById('add-category-btn').addEventListener('click', () => {
    config = loadConfig();
    const newCat = { id: uid(), label: {}, faqs: [] };
    config.categories.push(newCat);
    persist();
    renderContent();
  });

  // ── Languages Tab ─────────────────────────────────────────────────────────
  function renderLangs() {
    config = loadConfig();
    const container = document.getElementById('lang-list-container');
    container.innerHTML = '';
    config.settings.supportedLanguages.forEach(l => {
      const item = document.createElement('div');
      item.className = 'lang-list-item';
      const info = document.createElement('span');
      info.textContent = l.label + ' (' + l.code + ')';

      if (l.code === 'en') {
        const locked = document.createElement('span');
        locked.className = 'lang-locked';
        locked.textContent = 'Source (locked)';
        item.appendChild(info);
        item.appendChild(locked);
      } else {
        const delBtn = document.createElement('button');
        delBtn.className = 'btn btn-danger btn-sm';
        delBtn.textContent = 'Remove';
        delBtn.addEventListener('click', () => {
          config.settings.supportedLanguages = config.settings.supportedLanguages.filter(x => x.code !== l.code);
          persist();
          renderLangs();
          renderContent();
        });
        item.appendChild(info);
        item.appendChild(delBtn);
      }
      container.appendChild(item);
    });
  }

  document.getElementById('add-lang-btn').addEventListener('click', () => {
    const code = document.getElementById('new-lang-code').value.trim().toLowerCase();
    const label = document.getElementById('new-lang-label').value.trim();
    if (!code || !label) return alert('Please enter both a language code and display name.');
    config = loadConfig();
    if (config.settings.supportedLanguages.find(l => l.code === code)) {
      return alert('Language code "' + code + '" already exists.');
    }
    config.settings.supportedLanguages.push({ code, label });
    persist();
    document.getElementById('new-lang-code').value = '';
    document.getElementById('new-lang-label').value = '';
    renderLangs();
    renderContent();
    renderSettings();
  });

  // ── Settings Tab ──────────────────────────────────────────────────────────
  function renderSettings() {
    config = loadConfig();
    const codes = getLangCodes();

    // UI Text
    const uiContainer = document.getElementById('settings-ui-text');
    uiContainer.innerHTML = '';

    ['widgetTitle', 'welcomeMessage'].forEach(field => {
      const fieldLabel = document.createElement('p');
      fieldLabel.style.cssText = 'font-size:13px;font-weight:600;margin-bottom:6px;margin-top:14px;';
      fieldLabel.textContent = field === 'widgetTitle' ? 'Widget Title' : 'Welcome Message';
      uiContainer.appendChild(fieldLabel);

      codes.forEach(code => {
        const lbl = document.createElement('label');
        lbl.textContent = getLangLabel(code);
        const inp = document.createElement('input');
        inp.type = 'text';
        inp.value = config.settings[field][code] || '';
        inp.addEventListener('input', () => {
          config.settings[field][code] = inp.value;
          persist();
        });
        uiContainer.appendChild(lbl);
        uiContainer.appendChild(inp);
      });
    });

    // Theme
    document.getElementById('theme-color').value = config.settings.theme || '#005A9C';

    // Fallback
    const mode = config.settings.fallbackMode || 'both';
    document.getElementById('fallback-mode').value = mode;
    document.getElementById('fallback-phone').value = config.settings.fallbackPhone || '';
    document.getElementById('fallback-email').value = config.settings.fallbackEmail || '';
    updateFallbackVisibility(mode);
  }

  function updateFallbackVisibility(mode) {
    document.getElementById('fallback-phone-row').style.opacity = mode === 'email' ? '0.3' : '1';
    document.getElementById('fallback-email-row').style.opacity = mode === 'phone' ? '0.3' : '1';
  }

  document.getElementById('theme-color').addEventListener('input', (e) => {
    config = loadConfig();
    config.settings.theme = e.target.value;
    persist();
  });

  document.getElementById('fallback-mode').addEventListener('change', (e) => {
    config = loadConfig();
    config.settings.fallbackMode = e.target.value;
    persist();
    updateFallbackVisibility(e.target.value);
  });

  document.getElementById('fallback-phone').addEventListener('input', (e) => {
    config = loadConfig();
    config.settings.fallbackPhone = e.target.value;
    persist();
  });

  document.getElementById('fallback-email').addEventListener('input', (e) => {
    config = loadConfig();
    config.settings.fallbackEmail = e.target.value;
    persist();
  });

  // ── Init ──────────────────────────────────────────────────────────────────
  renderContent();
  renderLangs();
  renderSettings();
})();
```

- [ ] **Step 2: Open admin.html in browser and verify**

Open `projects/web-development/faq-chatbot/admin.html` in a browser.

Expected:
- Three tabs: Content, Languages, Settings
- Content tab shows 2 categories with FAQ items, each with language tabs (English / 日本語)
- Editing any field shows "Changes saved" indicator
- Adding a category creates a new blank card
- Languages tab lists EN (locked) and 日本語 (removable)
- Adding a language via the form adds it to the list
- Settings tab shows title/welcome fields, color picker, fallback controls
- Changing fallback mode to "phone" fades out the email row

- [ ] **Step 3: Verify admin changes appear in widget**

1. In `admin.html`, change the widget title to "Test Title"
2. Open `index.html` in the same browser
3. Expected: header shows "Test Title"

- [ ] **Step 4: Commit**

```bash
git add admin.js admin.html
git commit -m "feat: add admin panel — content, language, and settings management"
```

---

## Task 6: Skill Documentation

**Files:**
- Create: `.github/skills/faq-chatbot/SKILL.md`

- [ ] **Step 1: Create skill file**

Create `.github/skills/faq-chatbot/SKILL.md`:

```markdown
# FAQ Chatbot Skill

## Overview

A deterministic, multilingual FAQ chatbot widget for embedding in web pages. No AI, no backend, no PII capture.

## Files

| File | Purpose |
|------|---------|
| `projects/web-development/faq-chatbot/index.html` | Chat widget — open in browser or embed in AEM |
| `projects/web-development/faq-chatbot/admin.html` | Admin panel — manage FAQ content, languages, and settings |
| `projects/web-development/faq-chatbot/storage.js` | Shared data layer (localStorage) |
| `projects/web-development/faq-chatbot/widget.js` | Widget rendering and interaction logic |
| `projects/web-development/faq-chatbot/admin.js` | Admin panel logic |

## Usage

1. Open `admin.html` to configure FAQ content, add languages, and set fallback contacts.
2. Open `index.html` to use the chat widget.
3. Both files share data via `localStorage` in the same browser.

## Adding Content

1. In Admin → Content tab, click **+ Add Category**
2. Enter category names for each language
3. Click **+ Add Question** inside a category
4. Fill in question and answer for each language tab

## Adding a Language

1. In Admin → Languages tab, enter the language code (e.g. `fr`) and display name (e.g. `Français`)
2. Click **+ Add Language**
3. Translation fields will appear in all FAQ items and settings

## AEM Embedding

To embed the widget in AEM:
1. Upload `storage.js`, `widget.js`, and `index.html` as assets
2. Reference `storage.js` and `widget.js` from the HTML component
3. The admin panel (`admin.html`) is not embedded — it is accessed directly by administrators
```

- [ ] **Step 2: Commit**

```bash
git add .github/skills/faq-chatbot/SKILL.md
git commit -m "docs: add FAQ chatbot skill documentation"
```

---

## Task 7: Test Checklist

**Files:**
- Create: `Skill Test/faq-chatbot/test.html`

- [ ] **Step 1: Create test.html**

Create `Skill Test/faq-chatbot/test.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>FAQ Chatbot — Test Checklist</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 720px; margin: 40px auto; padding: 0 20px; color: #222; }
    h1 { font-size: 22px; margin-bottom: 8px; }
    .subtitle { color: #666; font-size: 14px; margin-bottom: 32px; }
    h2 { font-size: 16px; margin: 28px 0 10px; border-bottom: 2px solid #005A9C; padding-bottom: 6px; color: #005A9C; }
    .test-case { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 10px; padding: 10px 14px; background: #f9f9f9; border-radius: 6px; }
    .test-case input[type="checkbox"] { margin-top: 3px; width: 16px; height: 16px; flex-shrink: 0; cursor: pointer; }
    .test-label { font-size: 14px; line-height: 1.5; }
    .test-label .step { color: #555; font-size: 12px; display: block; margin-top: 2px; }
    .pass { background: #f0fdf4; }
    .fail { background: #fff5f5; }
    #reset-btn { margin-top: 32px; padding: 8px 18px; background: #e53e3e; color: #fff; border: none; border-radius: 6px; cursor: pointer; font-size: 13px; }
    #reset-btn:hover { background: #c53030; }
    #progress { font-size: 14px; color: #555; margin-bottom: 20px; }
  </style>
</head>
<body>
  <h1>FAQ Chatbot — Manual Test Checklist</h1>
  <p class="subtitle">Open <code>index.html</code> and <code>admin.html</code> in the same browser to run these tests.</p>
  <p id="progress">0 / 0 passed</p>

  <h2>1. Widget — Initial Load</h2>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Widget renders with blue header and title "FAQ"<span class="step">Open index.html → check header</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Language toggle shows "English" and "日本語" buttons<span class="step">Check top-right of header</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Welcome message is visible below header<span class="step">Check body area</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Two category buttons visible: "Reimbursement" and "Prescription"<span class="step">Check home state</span></div></div>

  <h2>2. Widget — Category & Answer Navigation</h2>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Clicking "Reimbursement" shows 3 FAQ question buttons<span class="step">Click Reimbursement</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Clicking a question shows the answer text<span class="step">Click any question</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Back button from answer returns to category list<span class="step">Click ← Back</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Back button from category returns to home<span class="step">Click ← Back from category</span></div></div>

  <h2>3. Widget — Search</h2>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Searching "reimbursement" returns a relevant answer<span class="step">Type "reimbursement" → click search</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Searching "prescription" returns a relevant answer<span class="step">Type "prescription" → click search</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Searching a nonsense string shows no-results fallback<span class="step">Type "xyzabc123" → click search</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Pressing Enter in search box triggers search<span class="step">Type query → press Enter</span></div></div>

  <h2>4. Widget — Language Toggle</h2>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Clicking 日本語 switches all visible text to Japanese<span class="step">Click 日本語 on home screen</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Category labels switch to Japanese (保険適用, 処方)<span class="step">Check category buttons after switching</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">FAQ questions and answers display in Japanese after toggle<span class="step">Navigate to a question while in 日本語 mode</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Switching back to English restores English text<span class="step">Click English button</span></div></div>

  <h2>5. Widget — Fallback</h2>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Answer state shows phone number and email button (default: both)<span class="step">Click any answer → check bottom section</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Email button opens mailto link<span class="step">Click "Contact via Email"</span></div></div>

  <h2>6. Admin — Content Tab</h2>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Admin panel loads with 2 category cards<span class="step">Open admin.html → Content tab</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">"Changes saved" indicator appears after editing any field<span class="step">Edit a FAQ question field</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Changes to FAQ question in admin appear in widget immediately<span class="step">Edit a question → switch to index.html → navigate to that FAQ</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">+ Add Category creates a new empty card<span class="step">Click + Add Category</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Delete Category removes it from the list<span class="step">Delete the new category</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">+ Add Question adds a new FAQ item inside the category<span class="step">Click + Add Question in any category</span></div></div>

  <h2>7. Admin — Languages Tab</h2>
  <div class="test-case"><input type="checkbox" /><div class="test-label">English is listed as locked (Source)<span class="step">Check Languages tab</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Adding language code "fr" + "Français" adds it to the list<span class="step">Fill form and click + Add Language</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">New language appears as a tab in FAQ items in Content tab<span class="step">Switch to Content tab after adding fr</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Removing a language removes it from the list and FAQ tabs<span class="step">Remove "fr"</span></div></div>

  <h2>8. Admin — Settings Tab</h2>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Changing theme color updates widget header color on refresh<span class="step">Change color → open index.html</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Setting fallback mode to "phone" fades the email row<span class="step">Select "Phone only" in fallback dropdown</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Phone-only mode shows only phone number in widget answer state<span class="step">Open index.html → check answer fallback section</span></div></div>
  <div class="test-case"><input type="checkbox" /><div class="test-label">Email-only mode shows only email button in widget<span class="step">Set "Email only" → check widget</span></div></div>

  <button id="reset-btn">Reset All Checkboxes</button>

  <script>
    const checks = document.querySelectorAll('input[type="checkbox"]');
    const progress = document.getElementById('progress');

    function updateProgress() {
      const passed = Array.from(checks).filter(c => c.checked).length;
      progress.textContent = passed + ' / ' + checks.length + ' passed';
      checks.forEach(c => {
        c.closest('.test-case').classList.toggle('pass', c.checked);
        c.closest('.test-case').classList.toggle('fail', !c.checked);
      });
      localStorage.setItem('test_state', JSON.stringify(Array.from(checks).map(c => c.checked)));
    }

    // Restore state
    const saved = JSON.parse(localStorage.getItem('test_state') || '[]');
    checks.forEach((c, i) => { if (saved[i]) c.checked = true; });
    checks.forEach(c => c.addEventListener('change', updateProgress));

    document.getElementById('reset-btn').addEventListener('click', () => {
      checks.forEach(c => c.checked = false);
      localStorage.removeItem('test_state');
      updateProgress();
    });

    updateProgress();
  </script>
</body>
</html>
```

- [ ] **Step 2: Open test.html and run through all test cases**

Open `Skill Test/faq-chatbot/test.html` in browser. Work through each test case against `index.html` and `admin.html`. All 28 checkboxes should pass.

- [ ] **Step 3: Commit**

```bash
mkdir -p "Skill Test/faq-chatbot"
git add "Skill Test/faq-chatbot/test.html"
git commit -m "test: add manual test checklist for FAQ chatbot"
```

---

---

## Task 8: GitHub Action — Publish Docs to Confluence

**Files:**
- Create: `.github/workflows/publish-confluence.yml`
- Create: `.github/scripts/publish_to_confluence.py`

**What gets published:**
- Design spec (`docs/superpowers/specs/2026-04-16-faq-chatbot-design.md`) → Confluence page "FAQ Chatbot — Design Spec"
- Skill documentation (`.github/skills/faq-chatbot/SKILL.md`) → Confluence page "FAQ Chatbot — Skill Documentation"
- Test checklist (`Skill Test/faq-chatbot/test.html`) → Confluence page "FAQ Chatbot — Test Checklist"

All three pages are children of a dedicated parent page "FAQ Chatbot Project" created under the Architecture Experiments folder (ID `54852222981`).

**GitHub Secrets required (set in repo Settings → Secrets → Actions):**
- `CONFLUENCE_BASE_URL` = `https://devops-abbott.atlassian.net`
- `CONFLUENCE_USER_EMAIL` = your Atlassian account email
- `CONFLUENCE_API_TOKEN` = your Atlassian API token (generate at https://id.atlassian.com/manage-profile/security/api-tokens)
- `CONFLUENCE_SPACE_KEY` = `ABTAIGAI`
- `CONFLUENCE_PARENT_FOLDER_ID` = `54852222981`

- [ ] **Step 1: Create the Python publish script**

Create `.github/scripts/publish_to_confluence.py`:

```python
#!/usr/bin/env python3
"""Publish FAQ Chatbot docs to Confluence Cloud."""

import os
import sys
import json
import re
import requests
from pathlib import Path

BASE_URL = os.environ["CONFLUENCE_BASE_URL"].rstrip("/")
EMAIL = os.environ["CONFLUENCE_USER_EMAIL"]
API_TOKEN = os.environ["CONFLUENCE_API_TOKEN"]
SPACE_KEY = os.environ["CONFLUENCE_SPACE_KEY"]
FOLDER_ID = os.environ["CONFLUENCE_PARENT_FOLDER_ID"]

AUTH = (EMAIL, API_TOKEN)
HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}
API = f"{BASE_URL}/wiki/rest/api/content"


def get_page_id(title: str, parent_id: str) -> str | None:
    """Return page ID if a page with this title exists under parent_id, else None."""
    resp = requests.get(
        API,
        auth=AUTH,
        params={"spaceKey": SPACE_KEY, "title": title, "expand": "version,ancestors"},
    )
    resp.raise_for_status()
    results = resp.json().get("results", [])
    for r in results:
        ancestors = [a["id"] for a in r.get("ancestors", [])]
        if parent_id in ancestors or r["id"] == parent_id:
            return r["id"]
    return None


def create_or_update_page(title: str, body_html: str, parent_id: str) -> str:
    """Create or update a Confluence page. Returns the page ID."""
    existing_id = get_page_id(title, parent_id)

    payload = {
        "type": "page",
        "title": title,
        "space": {"key": SPACE_KEY},
        "ancestors": [{"id": parent_id}],
        "body": {
            "storage": {
                "value": body_html,
                "representation": "storage",
            }
        },
    }

    if existing_id:
        # Fetch current version number
        resp = requests.get(f"{API}/{existing_id}?expand=version", auth=AUTH)
        resp.raise_for_status()
        version = resp.json()["version"]["number"] + 1
        payload["version"] = {"number": version}
        resp = requests.put(
            f"{API}/{existing_id}",
            auth=AUTH,
            headers=HEADERS,
            data=json.dumps(payload),
        )
    else:
        resp = requests.post(API, auth=AUTH, headers=HEADERS, data=json.dumps(payload))

    resp.raise_for_status()
    page_id = resp.json()["id"]
    page_url = f"{BASE_URL}/wiki/spaces/{SPACE_KEY}/pages/{page_id}"
    print(f"  ✓ '{title}' → {page_url}")
    return page_id


def markdown_to_html(md: str) -> str:
    """Convert markdown to basic Confluence storage HTML (no external deps)."""
    html = md

    # Code blocks
    html = re.sub(
        r"```(\w*)\n(.*?)```",
        lambda m: f'<ac:structured-macro ac:name="code"><ac:parameter ac:name="language">{m.group(1) or "text"}</ac:parameter><ac:plain-text-body><![CDATA[{m.group(2)}]]></ac:plain-text-body></ac:structured-macro>',
        html,
        flags=re.DOTALL,
    )

    # Headings
    for level in range(4, 0, -1):
        html = re.sub(
            r"^#{" + str(level) + r"}\s+(.+)$",
            lambda m, l=level: f"<h{l}>{m.group(1)}</h{l}>",
            html,
            flags=re.MULTILINE,
        )

    # Bold
    html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html)

    # Inline code
    html = re.sub(r"`([^`]+)`", r"<code>\1</code>", html)

    # Table rows (simple)
    def convert_table(match):
        rows = [r.strip() for r in match.group(0).strip().split("\n") if "|" in r and not re.match(r"^\|[-| ]+\|$", r.strip())]
        result = "<table><tbody>"
        for i, row in enumerate(rows):
            cells = [c.strip() for c in row.strip("|").split("|")]
            tag = "th" if i == 0 else "td"
            result += "<tr>" + "".join(f"<{tag}>{c}</{tag}>" for c in cells) + "</tr>"
        result += "</tbody></table>"
        return result

    html = re.sub(r"(\|.+\|\n)+", convert_table, html)

    # Paragraphs (blank-line separated blocks not already in tags)
    lines = html.split("\n")
    output = []
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("<"):
            output.append(f"<p>{stripped}</p>")
        else:
            output.append(line)
    html = "\n".join(output)

    return html


def html_file_to_confluence_html(path: Path) -> str:
    """Extract body content from an HTML file for Confluence."""
    content = path.read_text(encoding="utf-8")
    body_match = re.search(r"<body[^>]*>(.*?)</body>", content, re.DOTALL | re.IGNORECASE)
    if body_match:
        # Strip scripts and styles
        body = re.sub(r"<script[^>]*>.*?</script>", "", body_match.group(1), flags=re.DOTALL)
        body = re.sub(r"<style[^>]*>.*?</style>", "", body, flags=re.DOTALL)
        return body.strip()
    return f"<p>Could not extract content from {path.name}</p>"


def main():
    repo_root = Path(__file__).parent.parent.parent

    print("Creating parent page 'FAQ Chatbot Project' under Architecture Experiments folder...")
    parent_id = create_or_update_page(
        title="FAQ Chatbot Project",
        body_html="<p>Documentation for the FAQ Chatbot project — deterministic multilingual chatbot for HCP regulatory queries.</p>",
        parent_id=FOLDER_ID,
    )

    docs = [
        {
            "title": "FAQ Chatbot — Design Spec",
            "path": repo_root / "docs/superpowers/specs/2026-04-16-faq-chatbot-design.md",
            "type": "markdown",
        },
        {
            "title": "FAQ Chatbot — Skill Documentation",
            "path": repo_root / ".github/skills/faq-chatbot/SKILL.md",
            "type": "markdown",
        },
        {
            "title": "FAQ Chatbot — Test Checklist",
            "path": repo_root / "Skill Test/faq-chatbot/test.html",
            "type": "html",
        },
    ]

    print("Publishing documentation pages...")
    for doc in docs:
        path = doc["path"]
        if not path.exists():
            print(f"  ⚠ Skipping '{doc['title']}' — file not found: {path}")
            continue
        if doc["type"] == "markdown":
            body = markdown_to_html(path.read_text(encoding="utf-8"))
        else:
            body = html_file_to_confluence_html(path)
        create_or_update_page(doc["title"], body, parent_id)

    print("\nAll pages published successfully.")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Create the GitHub Actions workflow**

Create `.github/workflows/publish-confluence.yml`:

```yaml
name: Publish Docs to Confluence

on:
  push:
    branches:
      - main
    paths:
      - 'docs/superpowers/specs/**'
      - '.github/skills/faq-chatbot/**'
      - 'Skill Test/faq-chatbot/**'

jobs:
  publish:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install requests

      - name: Publish docs to Confluence
        env:
          CONFLUENCE_BASE_URL: ${{ secrets.CONFLUENCE_BASE_URL }}
          CONFLUENCE_USER_EMAIL: ${{ secrets.CONFLUENCE_USER_EMAIL }}
          CONFLUENCE_API_TOKEN: ${{ secrets.CONFLUENCE_API_TOKEN }}
          CONFLUENCE_SPACE_KEY: ${{ secrets.CONFLUENCE_SPACE_KEY }}
          CONFLUENCE_PARENT_FOLDER_ID: ${{ secrets.CONFLUENCE_PARENT_FOLDER_ID }}
        run: python .github/scripts/publish_to_confluence.py
```

- [ ] **Step 3: Create the scripts directory and verify files**

```bash
mkdir -p .github/scripts
ls .github/scripts/publish_to_confluence.py
ls .github/workflows/publish-confluence.yml
```

Expected: both files exist.

- [ ] **Step 4: Add GitHub Secrets**

In your GitHub repository go to **Settings → Secrets and variables → Actions → New repository secret** and add:

| Secret Name | Value |
|-------------|-------|
| `CONFLUENCE_BASE_URL` | `https://devops-abbott.atlassian.net` |
| `CONFLUENCE_USER_EMAIL` | Your Atlassian account email |
| `CONFLUENCE_API_TOKEN` | Token from https://id.atlassian.com/manage-profile/security/api-tokens |
| `CONFLUENCE_SPACE_KEY` | `ABTAIGAI` |
| `CONFLUENCE_PARENT_FOLDER_ID` | `54852222981` |

- [ ] **Step 5: Commit and push to trigger the workflow**

```bash
git add .github/workflows/publish-confluence.yml .github/scripts/publish_to_confluence.py
git commit -m "feat: add GitHub Action to publish docs to Confluence"
git push origin main
```

- [ ] **Step 6: Verify in GitHub Actions and Confluence**

1. Go to your repo → **Actions** tab → confirm the workflow runs green
2. Open `https://devops-abbott.atlassian.net/wiki/spaces/ABTAIGAI/folder/54852222981`
3. Expected: "FAQ Chatbot Project" parent page with 3 child pages:
   - FAQ Chatbot — Design Spec
   - FAQ Chatbot — Skill Documentation
   - FAQ Chatbot — Test Checklist

- [ ] **Step 7: Commit**

Already committed in Step 5. Verify with:
```bash
git log --oneline -3
```

---

## Self-Review Notes

**Spec coverage check:**
- ✅ Rules-based deterministic matching (Task 3 — token scoring)
- ✅ Japanese + English support (Task 1 seed data, Task 3 language toggle)
- ✅ No PII, no backend, no external deps (all localStorage, vanilla JS)
- ✅ Fallback to contact centre (Task 3 fallback rendering)
- ✅ Admin: fallback mode config (Task 5 settings tab)
- ✅ Admin: FAQ content management (Task 5 content tab)
- ✅ Admin: UI settings — title, welcome message, theme (Task 5 settings tab)
- ✅ Admin: language management (Task 5 languages tab)
- ✅ Language auto-detect + manual toggle (Task 3)
- ✅ Seed data on first load (Task 1 storage.js)
- ✅ Skill documentation (Task 6)
- ✅ Test checklist (Task 7)

**Type/naming consistency:** `loadConfig`, `saveConfig`, `getText` defined in Task 1 and used consistently in Tasks 3 and 5. `uid()` defined in Task 5 admin.js. No cross-task naming conflicts.
