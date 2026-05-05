# Enterprise Architect Skill Modularization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Modularize the monolithic `enterprise-architect.md` skill into a two-tier structure with shared references, an interactive menu, context-guided sub-skills, and an ADD orchestration mode that sequences all 8 steps into a full Architecture Design Document.

**Architecture:** Thin orchestrator (`enterprise-architect.md`) routes to 11 capability sub-skills in `enterprise-architect/`. Shared behavioral guidelines, quality standards, and output formats live in `enterprise-architect/references/`. Six Abbott templates are extracted from `.docx` files and stored as `.md` reference files. ADD mode sequences sub-skills and tracks progress in `docs/architecture/.add-session.md`.

**Tech Stack:** Markdown skill files, python-docx for template extraction, bash for file sync to `~/.claude/commands/`

---

## File Structure

**Create:**
- `skills/enterprise-architect/references/behavioral-guidelines.md`
- `skills/enterprise-architect/references/quality-standards.md`
- `skills/enterprise-architect/references/output-formats.md`
- `skills/enterprise-architect/references/add-template.md` (extracted from docx)
- `skills/enterprise-architect/references/database-design-template.md` (extracted)
- `skills/enterprise-architect/references/interface-design-template.md` (extracted)
- `skills/enterprise-architect/references/detail-design-template.md` (extracted)
- `skills/enterprise-architect/references/test-design-template.md` (extracted)
- `skills/enterprise-architect/references/accuracy-document-template.md` (extracted)
- `skills/enterprise-architect/c4-diagrams.md`
- `skills/enterprise-architect/adr.md`
- `skills/enterprise-architect/solution-architecture.md`
- `skills/enterprise-architect/architecture-review.md`
- `skills/enterprise-architect/api-documentation.md`
- `skills/enterprise-architect/data-architecture.md`
- `skills/enterprise-architect/integration-architecture.md`
- `skills/enterprise-architect/deployment-architecture.md`
- `skills/enterprise-architect/technical-debt.md`
- `skills/enterprise-architect/target-architecture.md`
- `skills/enterprise-architect/gap-analysis.md`
- `skills/enterprise-architect/add-mode.md`

**Modify:**
- `skills/enterprise-architect.md` → rewrite as thin orchestrator with interactive menu

**Sync to:**
- `~/.claude/commands/enterprise-architect.md`
- `~/.claude/commands/enterprise-architect/` (all sub-skills and references)

---

## Task 1: Extract Abbott Templates from .docx Files

**Files:**
- Create: `skills/shared-scripts/extract_docx_to_md.py`
- Create: `skills/enterprise-architect/references/add-template.md`
- Create: `skills/enterprise-architect/references/database-design-template.md`
- Create: `skills/enterprise-architect/references/interface-design-template.md`
- Create: `skills/enterprise-architect/references/detail-design-template.md`
- Create: `skills/enterprise-architect/references/test-design-template.md`
- Create: `skills/enterprise-architect/references/accuracy-document-template.md`

- [ ] **Step 1: Write extraction script**

```python
# skills/shared-scripts/extract_docx_to_md.py
"""Extract .docx content to markdown for use as skill reference files."""
import sys
from pathlib import Path
from docx import Document

def extract_docx(input_path: str, output_path: str) -> None:
    doc = Document(input_path)
    lines = []
    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            lines.append("")
            continue
        style = para.style.name
        if style.startswith("Heading 1"):
            lines.append(f"# {text}")
        elif style.startswith("Heading 2"):
            lines.append(f"## {text}")
        elif style.startswith("Heading 3"):
            lines.append(f"### {text}")
        else:
            lines.append(text)
    # Extract tables
    for table in doc.tables:
        header = "| " + " | ".join(cell.text.strip() for cell in table.rows[0].cells) + " |"
        separator = "| " + " | ".join("---" for _ in table.rows[0].cells) + " |"
        rows = []
        for row in table.rows[1:]:
            rows.append("| " + " | ".join(cell.text.strip() for cell in row.cells) + " |")
        lines.extend(["", header, separator] + rows + [""])
    Path(output_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"Extracted: {output_path}")

if __name__ == "__main__":
    extract_docx(sys.argv[1], sys.argv[2])
```

- [ ] **Step 2: Run extraction for all 6 templates**

```bash
BASE="/Users/GUNDLLX/learn-claude/skills/enterprise-architect/references"
SCRIPT="/Users/GUNDLLX/learn-claude/skills/shared-scripts/extract_docx_to_md.py"

python3 "$SCRIPT" "$BASE/Architecture Design Document_ADD.docx" "$BASE/add-template.md"
python3 "$SCRIPT" "$BASE/BTSQC09.05-N v3_Database Design Document.docx" "$BASE/database-design-template.md"
python3 "$SCRIPT" "$BASE/BTSQC09.05-P v3_Interface Design Document.docx" "$BASE/interface-design-template.md"
python3 "$SCRIPT" "$BASE/BTSQC09.05-O v5 _Detailed Design Document.docx" "$BASE/detail-design-template.md"
python3 "$SCRIPT" "$BASE/BTSQC09.05-T v3 Test design accuracy.docx" "$BASE/test-design-template.md"
python3 "$SCRIPT" "$BASE/BTSQC09.05-R v2.docx" "$BASE/accuracy-document-template.md"
```

Expected output:
```
Extracted: .../add-template.md
Extracted: .../database-design-template.md
Extracted: .../interface-design-template.md
Extracted: .../detail-design-template.md
Extracted: .../test-design-template.md
Extracted: .../accuracy-document-template.md
```

- [ ] **Step 3: Verify each extracted file has content**

```bash
for f in add database-design interface-design detail-design test-design accuracy-document; do
  wc -l "/Users/GUNDLLX/learn-claude/skills/enterprise-architect/references/${f}-template.md"
done
```

Expected: each file shows > 10 lines

- [ ] **Step 4: Commit**

```bash
cd /Users/GUNDLLX/learn-claude
git add skills/shared-scripts/extract_docx_to_md.py skills/enterprise-architect/references/*.md
git commit -m "feat: extract Abbott design templates to markdown reference files"
```

---

## Task 2: Create Shared Reference Files

**Files:**
- Create: `skills/enterprise-architect/references/behavioral-guidelines.md`
- Create: `skills/enterprise-architect/references/quality-standards.md`
- Create: `skills/enterprise-architect/references/output-formats.md`

- [ ] **Step 1: Write behavioral-guidelines.md**

```markdown
# Behavioral Guidelines

Apply these rules on every enterprise-architect task.

## 1. Scope Discipline
Only perform the task explicitly requested. Do not produce unrequested artifacts or expand scope without approval.

## 2. Clarification First
If critical information is missing (scale requirements, existing technology stack, business constraints, integration points), ask targeted questions before proceeding. Show a context brief first, then ask gap-filling questions one at a time.

## 3. Structured Output
All output must be formatted as structured Markdown. Use H2/H3 headers, tables, bullet lists, numbered lists, and code blocks.

## 4. Diagrams with Mermaid
Use Mermaid syntax for all diagrams. Always wrap in fenced code blocks with the `mermaid` language identifier.

## 5. Architectural Rigor
Apply established patterns and frameworks. Reference TOGAF, C4 model, OpenAPI, AsyncAPI, ISO 42010 where appropriate. Justify decisions with rationale.

## 6. Risk Awareness
Proactively flag risks, trade-offs, and constraints. Use consistent risk taxonomy: High / Medium / Low with likelihood and impact.

## 7. Vendor Neutrality
Present options objectively. When recommending specific technologies, explain the reasoning and note alternatives.
```

Save to: `skills/enterprise-architect/references/behavioral-guidelines.md`

- [ ] **Step 2: Write quality-standards.md**

```markdown
# Quality Standards

Apply these standards to all enterprise-architect outputs.

- **Mermaid validity**: All Mermaid diagrams must be syntactically valid. Test by mentally parsing node → edge → node chains.
- **Language precision**: Use precise, unambiguous technical language. No vague qualifiers ("some", "various", "appropriate").
- **Traceability**: All recommendations must be traceable to a stated requirement or constraint. If you can't trace it, don't include it.
- **Terminology consistency**: Use the same term for the same concept throughout a document. Define terms on first use.
- **Assumption flagging**: When information is incomplete, explicitly flag assumptions with `> **Assumption:** ...` blockquote formatting.
- **Actionable output**: Every recommendation must name an owner, a next step, or a decision required. No passive observations.
```

Save to: `skills/enterprise-architect/references/quality-standards.md`

- [ ] **Step 3: Write output-formats.md**

Extract the four format templates from the existing `enterprise-architect.md` into this file:

```markdown
# Output Formats

## ADR Format
# ADR-[NUMBER]: [Title]
**Date**: [Date]
**Status**: [Proposed | Accepted | Deprecated | Superseded]
**Deciders**: [Stakeholders]

### Context
### Decision
### Consequences
#### Positive
#### Negative
#### Risks
### Alternatives Considered
### References

---

## Architecture Review Format
## Executive Summary
## Architecture Overview
## Findings
### Critical Risks
### High Risks
### Medium Risks
### Low Risks / Observations
## Technical Debt
## Recommendations
## Next Steps

---

## Gap Analysis Format
## Current State Summary
## Target State Summary
## Gap Analysis
| Capability | Current State | Target State | Gap | Priority |
## Migration Considerations
## Recommended Roadmap

---

## Solution Architecture Document Format
## Executive Summary
## Business Context & Goals
## Scope & Constraints
## Architecture Principles
## Solution Overview
## Component Architecture
## Integration Architecture
## Data Architecture
## Security Architecture
## Non-Functional Requirements & How They Are Met
## Deployment Architecture
## Risks & Mitigations
## Decision Log
## Appendix
```

Save to: `skills/enterprise-architect/references/output-formats.md`

- [ ] **Step 4: Commit**

```bash
cd /Users/GUNDLLX/learn-claude
git add skills/enterprise-architect/references/behavioral-guidelines.md \
        skills/enterprise-architect/references/quality-standards.md \
        skills/enterprise-architect/references/output-formats.md
git commit -m "feat: add shared reference files for enterprise-architect skill"
```

---

## Task 3: Create Sub-skill Files (Capability Skills)

**Files:** All 11 sub-skill files in `skills/enterprise-architect/`

Each sub-skill follows this template:
```markdown
---
name: enterprise-architect/<capability>
description: <one-line trigger>
---

## Purpose
<what this produces and when to use it>

## Context Brief
> To complete this I'll need: <comma-separated list of required inputs>
> Share what you have and I'll ask about anything missing.

## Gap Questions
Ask these one at a time, only if not already provided by the user:
1. <question 1>
2. <question 2>
3. <question 3>

## Process
<step-by-step execution instructions>

## Output
Produce output following the format in `references/output-formats.md` → [Section Name].
Apply all rules in `references/behavioral-guidelines.md` and `references/quality-standards.md`.
```

- [ ] **Step 1: Create adr.md**

```markdown
---
name: enterprise-architect/adr
description: Write a formal Architecture Decision Record documenting a specific architectural decision, its context, alternatives, and consequences.
---

## Purpose
Produces a structured ADR capturing a single architectural decision. Use when a significant technical choice has been made or needs to be documented for the record.

## Context Brief
> To write this ADR I'll need: the decision being made, the options considered, the key drivers (cost, risk, speed, compliance, scalability), and who the deciders are.
> Share what you have and I'll ask about anything missing.

## Gap Questions
Ask these one at a time, only if not already provided:
1. What is the specific decision being recorded? (e.g., "Use PostgreSQL over MongoDB for the primary data store")
2. What were the alternatives considered?
3. What are the key drivers or constraints that shaped this decision?
4. Who are the deciders / stakeholders?
5. What are the known risks or negative consequences of this decision?

## Process
1. Confirm the decision statement is precise and unambiguous
2. Document context — what forces led to this decision point
3. State the decision clearly in one sentence
4. List positive consequences, negative consequences, and risks separately
5. Document each alternative with a one-line rationale for why it was not chosen
6. Assign an ADR number (check existing ADRs in `docs/architecture/adr/` if present)

## Output
Use the ADR Format from `references/output-formats.md`.
Save to `docs/architecture/adr/ADR-[NUMBER]-[slug].md`.
Apply all rules in `references/behavioral-guidelines.md` and `references/quality-standards.md`.
```

- [ ] **Step 2: Create gap-analysis.md**

```markdown
---
name: enterprise-architect/gap-analysis
description: Perform a structured gap analysis comparing current state architecture to a defined target state, with a prioritized migration path.
---

## Purpose
Produces a gap analysis document mapping where the architecture is today versus where it needs to be, with prioritized gaps and a migration roadmap.

## Context Brief
> To perform this gap analysis I'll need: a description of the current architecture (or existing docs), the target state vision or requirements, and any known constraints (timeline, budget, compliance, technology lock-in).
> Share what you have and I'll ask about anything missing.

## Gap Questions
Ask these one at a time, only if not already provided:
1. How would you describe the current architecture? (paste docs, describe components, or share diagrams)
2. What does the target state look like? (business goals, target capabilities, or a reference architecture)
3. What are the hard constraints? (e.g., cannot replace X system, must be on Azure, must meet SOC2)
4. What is the migration timeline?
5. Which gaps are highest priority from a business perspective?

## Process
1. Summarize current state in 3-5 bullet points
2. Summarize target state in 3-5 bullet points
3. For each capability area, assess current vs target and identify the gap
4. Prioritize gaps by business impact and migration effort (High/Medium/Low)
5. Propose a phased migration roadmap with logical sequencing

## Output
Use the Gap Analysis Format from `references/output-formats.md`.
Save to `docs/architecture/gap-analysis-[date].md`.
Apply all rules in `references/behavioral-guidelines.md` and `references/quality-standards.md`.
```

- [ ] **Step 3: Create remaining 9 sub-skill files**

Create each file at `skills/enterprise-architect/<name>.md` using the same template structure. Content for each:

**c4-diagrams.md**
- Purpose: C4 context, container, component, and code-level diagrams using Mermaid
- Context brief needs: system name, key users/actors, external systems it integrates with, internal components if known
- Gap questions: What is the system? Who uses it? What external systems does it integrate with? What level of diagram (context/container/component/code)?

**solution-architecture.md**
- Purpose: Full Solution Architecture Document covering all functional, non-functional, and cross-cutting concerns
- Context brief needs: business problem, key functional requirements, non-functional requirements (scale, availability, security), technology constraints
- Gap questions: What problem does this solve? What are the top 3 functional requirements? What are the NFRs? What technology stack is in use or preferred?
- Output template: `references/add-template.md` (Abbott template)

**architecture-review.md**
- Purpose: Risk-focused review of an existing architecture identifying anti-patterns, SPOFs, scalability issues, security concerns
- Context brief needs: existing architecture description or docs, known pain points, scale requirements
- Gap questions: Share the architecture (docs/diagrams/description). What are the known pain points? What scale does it need to support?

**api-documentation.md**
- Purpose: RESTful, GraphQL, or event/message API contracts and design guidelines
- Context brief needs: API type (REST/GraphQL/event), resources/operations being documented, authentication method, consumers
- Gap questions: What type of API? What are the main resources/operations? How is it authenticated? Who are the consumers?

**data-architecture.md**
- Purpose: Data models, data flows, storage strategy, and governance considerations
- Context brief needs: key data entities, data volume/velocity, storage technology constraints, compliance requirements
- Gap questions: What are the core data entities? What are the volume/velocity requirements? Any compliance constraints (HIPAA, GDPR)? What storage technologies are in play?
- Output template: `references/database-design-template.md` (Abbott template)

**integration-architecture.md**
- Purpose: Integration patterns, middleware selection, event bus design, ESB/API gateway topology
- Context brief needs: systems being integrated, integration style (sync/async/event), data volumes, reliability requirements
- Gap questions: What systems need to integrate? Sync or async? What data volumes? What are the reliability/ordering requirements?
- Output template: `references/interface-design-template.md` (Abbott template)

**deployment-architecture.md**
- Purpose: Infrastructure topology, networking, cloud deployment view
- Context brief needs: cloud provider, deployment model (containers/VMs/serverless), environments needed, network/security requirements
- Gap questions: Which cloud provider? Container/VM/serverless? What environments (dev/staging/prod)? Any network segmentation or compliance requirements?

**technical-debt.md**
- Purpose: Catalog and prioritize existing technical debt with remediation recommendations
- Context brief needs: system or codebase description, known problem areas, business criticality
- Gap questions: What system are we assessing? What are the known pain points? What is the business criticality and tolerance for risk?

**target-architecture.md**
- Purpose: Future-state architecture proposal aligned to business goals
- Context brief needs: current state summary, business goals driving the change, constraints, horizon (1yr/3yr/5yr)
- Gap questions: What does today's architecture look like? What business goals are driving this? What constraints must be respected? What time horizon?

- [ ] **Step 4: Commit all sub-skill files**

```bash
cd /Users/GUNDLLX/learn-claude
git add skills/enterprise-architect/*.md
git commit -m "feat: add 11 enterprise-architect sub-skill files"
```

---

## Task 4: Create ADD Mode Orchestration File

**Files:**
- Create: `skills/enterprise-architect/add-mode.md`

- [ ] **Step 1: Write add-mode.md**

```markdown
---
name: enterprise-architect/add-mode
description: Orchestrates the full Architecture Design Document sequence, progressing through all 8 steps and tracking state in docs/architecture/.add-session.md
---

## Purpose
Produces a complete Architecture Design Document by sequencing 8 sub-skills in logical order. Tracks progress so sessions can be paused and resumed.

## ADD Sequence

| Step | Sub-skill | Output | Abbott Template |
|------|-----------|--------|-----------------|
| 1 | gap-analysis | Current vs target state, migration path | — |
| 2 | solution-architecture | Full solution design | add-template.md |
| 3 | c4-diagrams | Context + container diagrams minimum | — |
| 4 | integration-architecture | Integration layer design | interface-design-template.md |
| 5 | data-architecture | Data models, flows, storage | database-design-template.md |
| 6 | deployment-architecture | Infrastructure topology | — |
| 7 | adr | Decisions made during steps 1-6 | — |
| 8 | architecture-review | Risk check across full ADD | — |

## Session State File

On first invocation, create `docs/architecture/.add-session.md` in the working project:

```markdown
# ADD Session State
**Started**: [date]
**Project**: [project name]

## Progress
- [ ] Step 1: Gap Analysis
- [ ] Step 2: Solution Architecture
- [ ] Step 3: C4 Diagrams
- [ ] Step 4: Integration Architecture
- [ ] Step 5: Data Architecture
- [ ] Step 6: Deployment Architecture
- [ ] Step 7: ADRs
- [ ] Step 8: Architecture Review

## Decisions Log
(populated during session)

## Open Questions
(populated during session)

## Technology Stack
(populated during session)
\```

On each subsequent invocation, read this file and resume from the first unchecked step.

## Process
1. Check for existing `.add-session.md` — if found, show progress and ask "Resume from Step N or start over?"
2. For each step: load the sub-skill, run its context brief + gap question flow, produce the artifact, mark the step complete in the session file
3. After Step 7 (ADRs), consolidate all decisions made during the session and write them as ADRs
4. After Step 8 (Architecture Review), present a summary of the complete ADD with links to all artifacts
```

- [ ] **Step 2: Commit**

```bash
cd /Users/GUNDLLX/learn-claude
git add skills/enterprise-architect/add-mode.md
git commit -m "feat: add ADD mode orchestration sub-skill"
```

---

## Task 5: Rewrite Orchestrator (enterprise-architect.md)

**Files:**
- Modify: `skills/enterprise-architect.md`

- [ ] **Step 1: Rewrite the orchestrator**

Replace the full content of `skills/enterprise-architect.md` with:

```markdown
---
name: enterprise-architect
description: "Enterprise architecture skill with interactive menu. Supports 12 capabilities including full Architecture Design Document (ADD) generation. Use for C4 diagrams, ADRs, solution architecture, gap analysis, architecture reviews, API docs, data architecture, integration architecture, deployment diagrams, technical debt, target architecture, and full ADD mode."
model: sonnet
memory: user
---

## On Invocation

1. Check for `docs/architecture/.add-session.md` in the working project. If found, note the in-progress session.
2. Display the interactive menu below.
3. Route to the appropriate sub-skill based on user selection.
4. On every invocation, load `enterprise-architect/references/behavioral-guidelines.md` and `enterprise-architect/references/quality-standards.md`.

## Interactive Menu

Present this menu exactly:

---
**Enterprise Architect** — What would you like to do?

 1. Build a full Architecture Design Document (ADD)
 2. Create a C4 Diagram
 3. Write an Architecture Decision Record (ADR)
 4. Perform a Gap Analysis
 5. Review an existing architecture
 6. Document APIs
 7. Design data architecture
 8. Design integration architecture
 9. Create a deployment diagram
10. Identify technical debt
11. Propose a target architecture
12. Create a solution architecture document

Type a number, or describe what you need.

---

If an in-progress ADD session was found, prepend:
> **Note:** You have an in-progress ADD session. Select 1 to resume it.

## Routing

| Selection | Sub-skill to load |
|-----------|------------------|
| 1 | `enterprise-architect/add-mode` |
| 2 | `enterprise-architect/c4-diagrams` |
| 3 | `enterprise-architect/adr` |
| 4 | `enterprise-architect/gap-analysis` |
| 5 | `enterprise-architect/architecture-review` |
| 6 | `enterprise-architect/api-documentation` |
| 7 | `enterprise-architect/data-architecture` |
| 8 | `enterprise-architect/integration-architecture` |
| 9 | `enterprise-architect/deployment-architecture` |
| 10 | `enterprise-architect/technical-debt` |
| 11 | `enterprise-architect/target-architecture` |
| 12 | `enterprise-architect/solution-architecture` |

If the user describes their need in natural language instead of a number, map it to the closest sub-skill and confirm: "It sounds like you need [capability] — is that right?"

## Direct Invocation

If invoked with an argument (e.g., `/enterprise-architect adr`), skip the menu and load the matching sub-skill directly.

## Memory

Fix the memory path — use `/Users/GUNDLLX/.claude/projects/` not `/Users/kenwilson/`. Save cross-session preferences (technology stack defaults, diagram style preferences, ADD workflow notes) to the user's auto-memory.
```

- [ ] **Step 2: Commit**

```bash
cd /Users/GUNDLLX/learn-claude
git add skills/enterprise-architect.md
git commit -m "feat: rewrite enterprise-architect as thin orchestrator with interactive menu"
```

---

## Task 6: Sync to ~/.claude/commands/

**Files:**
- Sync: `skills/enterprise-architect.md` → `~/.claude/commands/enterprise-architect.md`
- Sync: `skills/enterprise-architect/` → `~/.claude/commands/enterprise-architect/`

- [ ] **Step 1: Write sync script**

```bash
# skills/shared-scripts/sync_skill.sh
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
```

Save to: `skills/shared-scripts/sync_skill.sh`

- [ ] **Step 2: Run sync**

```bash
chmod +x /Users/GUNDLLX/learn-claude/skills/shared-scripts/sync_skill.sh
/Users/GUNDLLX/learn-claude/skills/shared-scripts/sync_skill.sh enterprise-architect
```

Expected:
```
Synced: enterprise-architect
```

- [ ] **Step 3: Verify files are in place**

```bash
ls ~/.claude/commands/enterprise-architect/
ls ~/.claude/commands/enterprise-architect/references/
```

Expected: all 11 sub-skill `.md` files and 8 reference `.md` files visible.

- [ ] **Step 4: Commit sync script**

```bash
cd /Users/GUNDLLX/learn-claude
git add skills/shared-scripts/sync_skill.sh
git commit -m "feat: add sync script for installing skills to ~/.claude/commands"
```

---

## Task 7: Smoke Test

- [ ] **Step 1: Test standalone ADR invocation**

Start a new Claude Code session. Run:
```
/enterprise-architect adr
```
Expected: skill loads directly to ADR context brief, no menu shown.

- [ ] **Step 2: Test interactive menu**

Start a new Claude Code session. Run:
```
/enterprise-architect
```
Expected: numbered menu appears with 12 options.

- [ ] **Step 3: Test ADD mode from menu**

Select option 1. Expected: ADD mode loads, checks for session file, runs gap-analysis context brief first.

- [ ] **Step 4: Test natural language routing**

Type: "I need to document a decision we made about our database"
Expected: skill responds "It sounds like you need an Architecture Decision Record (ADR) — is that right?"

- [ ] **Step 5: Verify session file is created**

After starting ADD mode, check:
```bash
ls docs/architecture/.add-session.md
```
Expected: file exists with Step 1 marked in-progress.

- [ ] **Step 6: Commit final verification note**

```bash
cd /Users/GUNDLLX/learn-claude
git add .
git commit -m "feat: enterprise-architect skill modularization complete — smoke tests passed"
```
