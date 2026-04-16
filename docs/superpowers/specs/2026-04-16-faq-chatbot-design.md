# FAQ Chatbot — Design Spec
**Date:** 2026-04-16  
**Status:** Approved

---

## Problem Statement

A lightweight, web-based FAQ chatbot to support a regulatory announcement (mid-May) impacting reimbursement and prescription queries from HCPs. Provides a compliant, deterministic way to access pre-approved answers and reduce call centre volume.

---

## Constraints

- Rules-based, deterministic — no AI, no generative responses
- Japanese + English language support (extensible to others)
- No PII capture, no data storage, no backend integrations
- Web-based, embeddable in AEM
- No external dependencies — pure HTML/CSS/JS
- Very short timeline (targeting mid-May)

---

## Architecture

**Two files, `localStorage` persistence:**

| File | Purpose |
|------|---------|
| `index.html` | Chat widget — what HCPs see |
| `admin.html` | Admin panel — separate URL, no authentication (security by obscurity) |

All configuration and FAQ content is stored in `localStorage` key `faq_config`. No external files, no backend.

---

## Data Model

Stored in `localStorage` as `faq_config`:

```json
{
  "settings": {
    "widgetTitle": { "en": "FAQ", "ja": "よくある質問" },
    "welcomeMessage": { "en": "How can we help?", "ja": "ご質問をお選びください。" },
    "theme": "#005A9C",
    "fallbackMode": "both",
    "fallbackPhone": "0120-XXX-XXX",
    "fallbackEmail": "support@example.com",
    "supportedLanguages": ["en", "ja"]
  },
  "categories": [
    {
      "id": "cat1",
      "label": { "en": "Reimbursement", "ja": "保険適用" },
      "faqs": [
        {
          "id": "q1",
          "source": "en",
          "question": { "en": "What is the reimbursement criteria?", "ja": "保険適用の基準は何ですか？" },
          "answer": { "en": "...", "ja": "..." }
        }
      ]
    }
  ]
}
```

**Language model:**
- English (`en`) is the canonical source language — locked, cannot be removed
- `supportedLanguages` array controls which languages appear in the widget picker
- All UI strings and FAQ content are fully translatable per language code
- Adding a new language in the admin panel adds it to `supportedLanguages` and exposes translation fields for all existing content

---

## Chat Widget (`index.html`)

### States

| State | Description |
|-------|-------------|
| Home | Welcome message + category buttons + free-text search input |
| Category | FAQ question list for selected category + Back button |
| Answer | Matched question + full answer + Back button + fallback prompt |

### Language Handling

- On load: detect `navigator.language`, match against `supportedLanguages`, default to `en` if no match
- Language toggle in header (e.g., `EN | 日本語`) — only languages in `supportedLanguages` shown
- Switching language re-renders the current state instantly (no page reload)

### Matching Logic (free-text search)

1. Normalize input: lowercase, strip punctuation
2. Score each FAQ question by counting matching tokens against the input (within active language)
3. Top score > 0 → show answer state
4. Top score = 0 → trigger fallback

### Fallback Display

Driven by `settings.fallbackMode`:

| Mode | Display |
|------|---------|
| `phone` | Show phone number text |
| `email` | Show email button (`mailto:`) |
| `both` | Show phone number + email button |

---

## Admin Panel (`admin.html`)

### Access

Separate URL (`admin.html`). No authentication. Security by obscurity — URL shared only with admins.

### Tabs

**1. Content**
- Add / rename / delete categories
- Per category: add / edit / delete FAQ entries
- Per FAQ entry: language tabs (EN | 日本語 | ...) to switch between translation fields
- English is always the first/source tab

**2. Languages**
- List active languages with display name and language code
- Add new language (code + display name)
- Remove language (except `en`)
- Adding a language appends it to `supportedLanguages` and reveals translation fields across all content

**3. Settings**
- Widget title and welcome message — per-language text fields
- Theme color picker
- Fallback mode selector: `phone` / `email` / `both`
- Phone number field (visible when mode is `phone` or `both`)
- Email field (visible when mode is `email` or `both`)

### Persistence

- Auto-save to `localStorage` on every input change
- "Changes saved" indicator shown after each save
- No explicit Save button required

### Seed Data

On first load, if `localStorage` is empty, populate with:
- 2 categories (Reimbursement / Prescription)
- 3–4 sample FAQs per category in both English and Japanese
- Default settings (theme, fallback mode, contact placeholders)

---

## Out of Scope

- Backend / API integrations
- PII capture or analytics
- Authentication for admin panel
- AEM integration (widget is designed to be embeddable but AEM setup is out of scope)
- Machine learning or AI-based matching
