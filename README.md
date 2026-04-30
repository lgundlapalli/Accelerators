# Learn Claude Workspace

This workspace is the source of truth for custom Claude Code skills built for Abbott BTS-DTS. Skills are authored here, then synced to `~/.claude/commands/` for use in any Claude Code session.

---

## Quick Start

**Invoke any skill in Claude Code:**
```
/enterprise-architect     ← architecture documents, ADRs, C4 diagrams
/ux-design                ← UX artifacts from a confirmed idea
/presentation             ← executive presentations and slide decks
/notional-architecture    ← notional architecture diagrams
/ddd-workshop             ← domain-driven design facilitation
```

**Sync a skill after editing:**
```bash
./skills/shared-scripts/sync_skill.sh <skill-name>
# Example:
./skills/shared-scripts/sync_skill.sh enterprise-architect
./skills/shared-scripts/sync_skill.sh ux-design
```

---

## Workspace Structure

```
learn-claude/
├── skills/                         ← skill source files (edit here)
│   ├── enterprise-architect.md     ← orchestrator
│   ├── enterprise-architect/       ← sub-skills + references
│   ├── ux-design.md                ← orchestrator (Phase 1)
│   ├── ux-design/                  ← sub-skills + references
│   ├── presentation/               ← presentation skill
│   ├── notional-architecture/      ← notional architecture skill
│   ├── ddd-workshop/               ← DDD workshop skill
│   ├── context-manager/            ← context window management
│   └── shared-scripts/             ← sync_skill.sh, extract_docx_to_md.py
│
├── docs/
│   └── superpowers/
│       ├── specs/                  ← design specs for each skill
│       └── plans/                  ← implementation plans
│
├── projects/                       ← project-specific work
│   └── web-development/
│       └── faq-chatbot/            ← FAQ chatbot project
│
└── Skill Test/                     ← skill output test artifacts
    └── presentation/
        └── why-ai-fails/           ← cultural debt presentation
```

---

## Skills

### `/enterprise-architect`
Modular enterprise architecture skill with interactive menu. Supports 12 capabilities including full Architecture Design Document (ADD) generation.

**Capabilities:**
| Command | What it does |
|---|---|
| `/enterprise-architect` | Interactive menu — pick a capability |
| `/enterprise-architect add` | Full ADD mode — sequences all 8 steps |
| `/enterprise-architect adr` | Write an Architecture Decision Record |
| `/enterprise-architect c4-diagrams` | C4 context/container/component diagrams |
| `/enterprise-architect gap-analysis` | Current vs target state analysis |
| `/enterprise-architect architecture-review` | Risk and anti-pattern review |
| `/enterprise-architect solution-architecture` | Full solution architecture document |
| `/enterprise-architect data-architecture` | Data models, flows, storage strategy |
| `/enterprise-architect integration-architecture` | Integration patterns and topology |
| `/enterprise-architect deployment-architecture` | Infrastructure and cloud deployment |
| `/enterprise-architect technical-debt` | Technical debt catalog and roadmap |
| `/enterprise-architect target-architecture` | Future-state architecture proposal |
| `/enterprise-architect api-documentation` | REST, GraphQL, event API contracts |

**Abbott templates wired in:**
- ADD → `add-template.md`
- Data architecture → `database-design-template.md`
- Integration → `interface-design-template.md`
- Detail design → `detail-design-template.md`
- Test design → `test-design-template.md`

---

### `/ux-design` *(Phase 1)*
Adaptive UX design skill. Takes a confirmed idea or vision/scope document and produces UX artifacts based on complexity — from a quick user story + flow set to a full design package.

**Artifacts:**
| Artifact | When produced |
|---|---|
| Personas | Multi-user or complex ideas |
| User Journeys | Multi-step workflows or new platforms |
| User Stories | Always |
| Mermaid Flows | Always (navigation + interaction + error states) |
| Interaction Patterns | Complex or platform-level ideas |

**Phases:**
- Phase 1 *(built)* — Markdown artifacts + Mermaid flows
- Phase 2 *(planned)* — HTML prototype generator
- Phase 3 *(planned)* — PPTX deck output via pptx-generator

---

### `/presentation`
Executive presentation builder. Generates structured `.md` slide files and editable `.pptx` decks. Supports Abbott BTS-DTS brand template.

**Types:** Architecture deck, stakeholder pitch, general presentation, executive briefing, adaptive.

---

### `/notional-architecture`
Notional architecture designer. Takes business capabilities and strategic inputs and produces architecture diagrams and documentation.

---

### `/ddd-workshop`
Domain-Driven Design workshop facilitator. Guides teams through event storming, domain storytelling, and tactical/strategic DDD patterns.

---

### `/context-manager`
Context window health monitor. Proactively manages token budget and delegates work to subagents to keep sessions healthy.

---

## Development Workflow

All skill development follows this cycle:

```
Brainstorm → Spec → Plan → Build (subagent-driven) → Sync → Test
```

1. **Brainstorm** — `/superpowers:brainstorming` to design the skill
2. **Spec** — saved to `docs/superpowers/specs/YYYY-MM-DD-<skill>-design.md`
3. **Plan** — saved to `docs/superpowers/plans/YYYY-MM-DD-<skill>.md`
4. **Build** — subagent-driven development via `/superpowers:subagent-driven-development`
5. **Sync** — `./skills/shared-scripts/sync_skill.sh <skill-name>`
6. **Test** — new Claude Code session, invoke the skill

---

## Abbott Design Templates

Located in `skills/enterprise-architect/references/`:

| File | Source Document |
|---|---|
| `add-template.md` | Architecture Design Document (ADD) |
| `database-design-template.md` | Database Design Document |
| `interface-design-template.md` | Interface Design Document |
| `detail-design-template.md` | Detailed Design Document |
| `test-design-template.md` | Test Design Accuracy Document |
| `accuracy-document-template.md` | Source Code Review Template |
