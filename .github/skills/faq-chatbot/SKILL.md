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
