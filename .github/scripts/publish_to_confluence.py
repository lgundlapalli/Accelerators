#!/usr/bin/env python3
"""Publish FAQ Chatbot docs to Confluence Cloud."""

import os
import json
import re
import urllib3
import requests
from pathlib import Path

# Suppress SSL warnings on corporate networks with custom CA certs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
VERIFY_SSL = False

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
        verify=VERIFY_SSL,
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
        resp = requests.get(f"{API}/{existing_id}?expand=version", auth=AUTH, verify=VERIFY_SSL)
        resp.raise_for_status()
        version = resp.json()["version"]["number"] + 1
        payload["version"] = {"number": version}
        resp = requests.put(
            f"{API}/{existing_id}",
            auth=AUTH,
            headers=HEADERS,
            data=json.dumps(payload),
            verify=VERIFY_SSL,
        )
    else:
        resp = requests.post(API, auth=AUTH, headers=HEADERS, data=json.dumps(payload), verify=VERIFY_SSL)

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
        lambda m: (
            f'<ac:structured-macro ac:name="code">'
            f'<ac:parameter ac:name="language">{m.group(1) or "text"}</ac:parameter>'
            f'<ac:plain-text-body><![CDATA[{m.group(2)}]]></ac:plain-text-body>'
            f'</ac:structured-macro>'
        ),
        html,
        flags=re.DOTALL,
    )

    # Headings (process largest first to avoid partial matches)
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

    # Tables
    def convert_table(match):
        rows = [
            r.strip()
            for r in match.group(0).strip().split("\n")
            if "|" in r and not re.match(r"^\|[-| ]+\|$", r.strip())
        ]
        result = "<table><tbody>"
        for i, row in enumerate(rows):
            cells = [c.strip() for c in row.strip("|").split("|")]
            tag = "th" if i == 0 else "td"
            result += "<tr>" + "".join(f"<{tag}>{c}</{tag}>" for c in cells) + "</tr>"
        result += "</tbody></table>"
        return result

    html = re.sub(r"(\|.+\|\n)+", convert_table, html)

    # Paragraphs
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
        {
            "title": "How to Publish Documentation from Claude to Confluence",
            "path": repo_root / "docs/how-to-publish-claude-to-confluence.md",
            "type": "markdown",
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
