---
name: publish-to-confluence
description: Use when publishing project documentation to the Abbott Confluence space (devops-abbott.atlassian.net). Triggers when user asks to publish docs, sync to Confluence, or update Confluence pages from local markdown/HTML files.
---

# Publish to Confluence

## Overview

Publishes local documentation files to the Abbott Confluence space `ABTAIGAI` under **Architecture Experiments** using the Confluence REST API. Runs entirely from the terminal — no GitHub Actions required.

## When to Use

- User says "publish to Confluence", "sync docs to Confluence", "update Confluence"
- After completing a project and wanting to share design docs
- After updating a spec, skill doc, or test checklist

## Quick Reference

| What | Value |
|------|-------|
| Script | `.github/scripts/publish_to_confluence.py` |
| Shell wrapper | `publish_to_confluence.sh` |
| Space | `ABTAIGAI` |
| Base URL | `https://devops-abbott.atlassian.net` |
| Architecture Experiments folder ID | `54852222981` |
| Confluence email | `lalitha.gundlapalli@abbott.com` |

## How to Run

From the repo root (`/Users/GUNDLLX/learn-claude`):

```bash
CONFLUENCE_USER_EMAIL="lalitha.gundlapalli@abbott.com" \
CONFLUENCE_API_TOKEN="<token>" \
CONFLUENCE_BASE_URL="https://devops-abbott.atlassian.net" \
CONFLUENCE_SPACE_KEY="ABTAIGAI" \
CONFLUENCE_PARENT_FOLDER_ID="54852222981" \
python3 .github/scripts/publish_to_confluence.py
```

Or using the shell wrapper (prompts for credentials if not set):

```bash
./publish_to_confluence.sh
```

## API Token

Generate at: `https://id.atlassian.com/manage-profile/security/api-tokens`

Tokens expire — if you get a 401, generate a new one.

## Adding New Docs to Publish

Edit the `docs` list in `.github/scripts/publish_to_confluence.py`:

```python
docs = [
    {
        "title": "My Page Title",
        "path": repo_root / "path/to/file.md",
        "type": "markdown",   # or "html"
    },
    ...
]
```

- `type: "markdown"` — converts markdown to Confluence storage HTML
- `type: "html"` — extracts `<body>` content, strips scripts/styles

Pages are created under the **FAQ Chatbot Project** parent. To publish under a different parent, change the `parent_id` passed to `create_or_update_page`.

## SSL Note

Abbott's corporate network uses a custom CA. The script sets `verify=False` to bypass SSL verification errors. This is safe on the internal network.

## What Gets Published (Current Config)

| Local File | Confluence Page |
|-----------|----------------|
| `docs/superpowers/specs/2026-04-16-faq-chatbot-design.md` | FAQ Chatbot — Design Spec |
| `.github/skills/faq-chatbot/SKILL.md` | FAQ Chatbot — Skill Documentation |
| `Skill Test/faq-chatbot/test.html` | FAQ Chatbot — Test Checklist |

Parent page: **FAQ Chatbot Project** (under Architecture Experiments)
