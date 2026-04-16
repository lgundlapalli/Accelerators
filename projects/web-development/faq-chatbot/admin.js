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

    item.appendChild(renderLangTabs(faq.id, item));

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

    const codes = getLangCodes();

    const labelWrap = document.createElement('div');
    labelWrap.style.flex = '1';
    codes.forEach(code => {
      const inp = document.createElement('input');
      inp.type = 'text';
      inp.placeholder = 'Category name (' + getLangLabel(code) + ')';
      inp.value = cat.label[code] || '';
      inp.style.marginBottom = '6px';
      inp.addEventListener('input', () => {
        cat.label[code] = inp.value;
        persist();
      });
      labelWrap.appendChild(inp);
    });

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

    document.getElementById('theme-color').value = config.settings.theme || '#005A9C';

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
