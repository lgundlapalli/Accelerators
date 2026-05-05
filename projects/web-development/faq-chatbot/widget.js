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

  // ── Launcher toggle ───────────────────────────────────────────────────────
  const launcher = document.getElementById('chat-launcher');
  const chatbot = document.getElementById('chatbot');

  const openIcon = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>`;
  const closeIcon = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>`;

  launcher.addEventListener('click', () => {
    const isCollapsed = chatbot.classList.toggle('collapsed');
    launcher.innerHTML = isCollapsed ? openIcon : closeIcon;
  });

  // ── Init ──────────────────────────────────────────────────────────────────
  render();
  showState('home');
})();
