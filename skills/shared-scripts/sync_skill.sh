#!/bin/bash
SKILL=$1
SRC="/Users/GUNDLLX/learn-claude/skills/$SKILL"
DEST="/Users/GUNDLLX/.claude/commands"

cp "$SRC.md" "$DEST/$SKILL.md"
if [ -d "$SRC" ]; then
  mkdir -p "$DEST/$SKILL"
  cp -r "$SRC/"* "$DEST/$SKILL/"
fi
echo "Synced: $SKILL"
