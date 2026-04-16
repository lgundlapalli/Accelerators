#!/bin/bash
# publish_to_confluence.sh
# Run this from the repo root to publish FAQ Chatbot docs to Confluence.
# Usage: ./publish_to_confluence.sh

set -e

# ── Credentials ───────────────────────────────────────────────────────────────
# Fill these in once, or set them as environment variables before running.

CONFLUENCE_BASE_URL="https://devops-abbott.atlassian.net"
CONFLUENCE_SPACE_KEY="ABTAIGAI"
CONFLUENCE_PARENT_FOLDER_ID="54852222981"

# Leave blank to be prompted each run (more secure)
CONFLUENCE_USER_EMAIL="${CONFLUENCE_USER_EMAIL:-}"
CONFLUENCE_API_TOKEN="${CONFLUENCE_API_TOKEN:-}"

# ── Prompt for credentials if not set ────────────────────────────────────────
if [ -z "$CONFLUENCE_USER_EMAIL" ]; then
  read -rp "Atlassian email: " CONFLUENCE_USER_EMAIL
fi

if [ -z "$CONFLUENCE_API_TOKEN" ]; then
  read -rsp "Atlassian API token: " CONFLUENCE_API_TOKEN
  echo
fi

# ── Run the Python script ─────────────────────────────────────────────────────
export CONFLUENCE_BASE_URL
export CONFLUENCE_USER_EMAIL
export CONFLUENCE_API_TOKEN
export CONFLUENCE_SPACE_KEY
export CONFLUENCE_PARENT_FOLDER_ID

python3 .github/scripts/publish_to_confluence.py
