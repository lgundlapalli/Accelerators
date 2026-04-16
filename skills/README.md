# Claude Code Skills

Read-only copies of skills for browsing and review. The live versions that Claude Code executes are in `~/.claude/commands/`.

## Skills

| Skill | Invoke With | Purpose |
|-------|-------------|---------|
| [notional-architecture](notional-architecture/) | `/notional-architecture` | Full 6-layer conceptual architecture from 10 strategic inputs |
| [capability-mapping](capability-mapping/) | `/notional-architecture:references:capability-mapping` | Map business capabilities to enablers, components, and layers |
| [enabler-catalog](enabler-catalog/) | `/notional-architecture:references:enabler-catalog` | Technology advisor — recommends platforms and tools with trade-offs |
| [output-formats](output-formats/) | `/notional-architecture:references:output-formats` | Generate architecture diagrams (Mermaid PNG/SVG or Miro board) |
| [presentation](presentation/) | `/presentation` | Structured presentations — architecture decks, pitches, briefings |
| [ddd-workshop](ddd-workshop/) | `/ddd-workshop` | DDD facilitator — event storming, domain storytelling, tactical modeling |
| [domain-model](domain-model/) | `/old-domain-model` | Legacy domain modeling skill (predecessor to ddd-workshop) |

## Shared Scripts

| Script | Location | Used By |
|--------|----------|---------|
| [extract_doc.py](shared-scripts/extract_doc.py) | `~/.claude/scripts/` | All skills — extracts text from .doc/.docx files |
| [extract_pptx.py](shared-scripts/extract_pptx.py) | `~/.claude/scripts/` | All skills — extracts text from .pptx files |

## Editing Skills

To edit a live skill, modify the file in `~/.claude/commands/<skill-name>/`. These copies in `skills/` are for browsing only — changes here won't affect skill execution.
