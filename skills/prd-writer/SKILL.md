---
name: prd-writer
description: Generates a Product Requirements Document (PRD) for digital products and features. Use when the user says "write a PRD", "create a PRD", "build a requirements doc", "convert prototype to PRD", "generate product spec", or when a product idea or prototype needs to be turned into a structured specification for engineering handoff. Supports two paths — Standard (from brief + OKRs) and Prototype Validated (from prototype learnings). Includes regulatory/compliance gate for Med-Tech and enterprise contexts.
license: Nitesh Luthra
metadata:
  author: Nitesh Luthra
  version: "1.8"
  created: "2026-03-31"
  updated: "2026-04-09"
  changelog:
    - "v1.8 (2026-04-09): Added Step 0a auto-detection — detects Abbott signals from user's initial request (3+ signals = auto-load, 1-2 = ask confirmation, 0 = generic). Silent context loading already present from v1.7. Matches prd-evaluator UX improvements."
    - "v1.7 (2026-04-09): Integrated centralized context system with two-level hierarchy (company + project). Abbott context loads automatically when selected. New projects auto-create context file as byproduct of PRD work. Updated to reference `.claude/context/` for strategic priorities, regulatory frameworks, org structure, AI governance, and platform context."
    - "v1.6 (2026-04-07): Added background execution option before Step 4 — user can choose to run PRD generation in background while continuing work, or foreground for progress visibility"
    - "v1.5 (2026-04-06): Reduced AI behavior examples from 15-25 to 3-5, added scannable bullet format for examples, page count target (5-6 pages), search .docx files for drafts, AI Feature Readiness tight bullet format, anti-slop checklist marked internal-only"
    - "v1.4 (2026-04-06): Added Solution Approach for Path A, AI activation logic, AI Feature Readiness dependencies, structured evidence/competitive sections, simplified rollout, table formats for dependencies/risks, updated anti-slop checklist, universal Post-Ship section"
    - "v1.3 (2026-04-01): Kill Criteria vs Fail → Action distinction, baseline collection"
  acknowledgements: "Aakash Gupta (product-growth.com) — Prototype-First PRD Template, 5 Lenses Prototype Evaluation Framework, Elements of a Great PRD"
---

# PRD Writer

## What This Skill Does

Generates a Product Requirements Document (PRD) in the modern AI-prototyping era. A PRD is a **decision record**, not a permission slip. It answers: what did we learn, what are we shipping, how will we know it worked, and when will we pull the plug.

Two paths:
- **Path A — Standard**: You have a brief, OKRs, and a clear problem. No prototype yet.
- **Path B — Prototype Validated**: You have run a prototype, evaluated it, and are ready to write the spec for the winner.

---

## Critical Guidance — Read Before Starting

**This PRD must not read like it was written by an AI.**

Every claim needs a number. Every metric needs a threshold. Every risk needs a named owner. If a sentence could apply to any product at any company, delete it and rewrite it for this specific product, this specific user, this specific bet.

Banned phrases: *robust*, *seamless*, *leverage*, *world-class*, *cutting-edge*, *significant improvement*, *better experience*, *empower users*, *holistic*, *synergy*.

If a section cannot be filled with specifics, mark it `[TBD — owner: name]` rather than writing a generic placeholder. Honest gaps are better than confident vagueness.

---

## Trigger

Activate when the user says: "write a PRD", "create a PRD", "build a requirements doc", "convert prototype to PRD", "generate product spec".

---

**Start with overview:**

> "This is PRD Writer. I'll help you build a Product Requirements Document following a structured process:
> 
> **What I do:**
> - Problem framing, boundaries, success metrics, rollout plan, risks, ownership
> - AI behavior contract (if applicable)
> 
> **Two paths:**
> - **Path A — Standard PRD**: You have a brief, OKRs, clear problem. No prototype yet.
> - **Path B — Prototype-Validated PRD**: You built prototypes, evaluated them, ready to spec the winner.
> 
> **Process:**
> 1. Gather context — any docs you have
> 2. Detect path — standard or prototype-validated
> 3. Ask targeted questions — only what I need
> 4. Draft all sections — with anti-slop checklist
> 5. Save as .md + .docx
> 
> Let's start."

---

## Step 0a — Auto-Detect Company Context

**Run immediately after user request, before asking any questions.**

**Auto-detect Abbott from user's request:**

Check for Abbott signals in user's initial message or context documents:
- Abbott program names (Mia, AI COE, Marketing GenAI, Regulatory Drafting Lighthouse)
- Abbott systems (Veeva, ServiceNow, Salesforce Health Cloud)
- Abbott divisions (ARDx, BTS, Nutrition, Core Lab Diagnostics, ADC)
- Abbott people (Nitesh Luthra, team members mentioned)
- Abbott-specific terms (MLR compliance, Abbott SSO, CoreDX, FreeStyle Libre, GxP)

**If 3+ Abbott signals detected:**
- Skip Step 0b, proceed directly to Abbott project selection
- Silently load Abbott context (do not announce to user)

**If 1-2 Abbott signals (unclear):**
- Proceed to Step 0b (ask user to confirm)

**If no Abbott signals:**
- Skip Abbott context, proceed with generic PRD

---

## Step 0b — Context Selection (if needed)

**Only run if Step 0a detected 1-2 Abbott signals (unclear) or no auto-detection possible.**

Ask user:

> "Is this PRD for:
> 1. **Abbott project** (load Abbott context)
> 2. **Generic** (no company-specific context)
> 
> Reply with a number."

**If Abbott project (1) OR auto-detected in Step 0a:**

Silently load Abbott company context (do not announce to user):
- `.claude/context/strategic-priorities.md`
- `.claude/context/company/abbott-corporate.md`
- `.claude/context/company/abbott-governance.md`
- `.claude/context/regulatory/frameworks.md`
- `.claude/context/ai/abbott-genai-work.md`
- `.claude/context/platforms/tech-stack.md`

Then ask:

> "Which Abbott project?
> - **Mia** (load Mia-specific context)
> - **Marketing GenAI** (load Marketing GenAI context)
> - **Regulatory Drafting** (load Regulatory Drafting context)
> - **Generic Abbott** (no project-specific context)
> - **[Type new project name]** (I'll create context file after PRD is complete)
> 
> Type the project name or 'Generic Abbott'."

**If existing project:**
- Mia → Silently load `.claude/context/projects/mia.md`
- Marketing GenAI → Silently load `.claude/context/projects/marketing-genai.md`
- Regulatory Drafting → Silently load `.claude/context/projects/regulatory-drafting.md`
- Generic Abbott → Just company context, no project-specific

**If new project name (e.g., "ABCD"):**
- Internally note project name for Step 7 (don't mention to user)
- Continue with company context only

**If Generic (2):**
- No context loading
- PRD runs without company/project framing

---

## Step 1 — Accept Context Documents

Ask two questions — one at a time:

**Question 1:**
> "Do you have any existing documents to reference? This could include a brief, OKRs, prototype results, competitive analysis, or a previous PRD draft. Paste text, share a file, or describe what you have."

If provided — read them. Extract: problem statement, hypothesis, metrics, decisions already made. Do not re-ask for anything already answered.

**Note:** When searching for existing PRDs, use both `*.md` and `*.docx` patterns. Users may have draft PRDs in .docx format.

**Question 2:**
> "Do you have a journey map or capability map for this product that I should pull pain points and gaps from? If yes, share the file or point me to the references folder."

This is opt-in — do not automatically read journey maps or capability maps. Only pull from them if the user explicitly says yes. If yes:
- **From journey maps**: extract confirmed pain points and moments of truth → feed into Section 1 (Opportunity Framing) and Section 5 (Risk Management)
- **From capability maps**: extract capability gaps and differentiator ratings → feed into Section 2 (Boundaries / Dependencies)

The PRD skill is standalone. It does not assume other skills have been run.

---

## Step 2 — Detect Path

Ask one question:

> "Have you built and evaluated a prototype for this? (Yes / No)"

- **No** → Path A (Standard)
- **Yes** → Path B (Prototype Validated)

If Path B, ask one additional question:

> "Do you have prototype screenshots or design images you'd like included in the PRD? If yes, paste them here and I'll save them to the prds folder and embed them in the document."

If images are provided — save each image to `docs/prds/` with a descriptive filename (e.g., `prototype-p1-standard-search.png`). Reference them in the PRD under a **Prototype Screens** section at the top, before Section 1. If no images are provided — add placeholder captions noting where each prototype screen should be inserted.

---

## Step 3 — Gather Inputs

### Path A — Standard Inputs
Ask only what was not already provided in Step 1:
1. What is the product or feature name?
2. Who is the primary user and what is their core problem?
3. What OKR or strategic bet does this unlock?
4. What is the one metric that defines success, and what is the target?
5. What is explicitly out of scope?
6. What dependencies must be true before this ships?
7. Any user research to include? (paste text, share a file, drop a deck, or describe findings — say "none" to skip)
8. Any competitive context? (same — doc, deck, or a quick description of what competitors do — say "none" to skip)

### Path B — Prototype Validated Inputs
Ask only what was not already provided in Step 1:
1. What prototypes were built? (how many, what variations)
2. Which one survived evaluation and why?
3. What was validated? What was invalidated?
4. What residual unknowns remain going into build?
5. What OKR or strategic bet does this unlock?
6. What is the one metric that defines success, and what is the target?
7. Any user research beyond the prototype evaluation? (paste text, share a file, drop a deck, or describe findings — say "none" to skip)
8. Any competitive context? (doc, deck, or quick description — say "none" to skip)

---

## Step 3b — Regulatory & Compliance Gate

After gathering all inputs, ask:

> "Before I write the PRD — does this feature: (a) make a clinical claim about health outcomes, (b) handle patient health information (PHI) or personally identifiable data, (c) modify a regulated workflow or device function, or (d) apply to a market with regulatory oversight (FDA, CE, GDPR, HIPAA)?"

- **If yes to any** → add a mandatory dependency in Section 2: `Regulatory / Compliance Review — Owner: [Legal / Regulatory Affairs / Privacy team] — Status: [not started]`. Flag it in the anti-slop checklist. Do not treat this as optional.
- **If no** → proceed. Note "Regulatory: Not applicable" in Section 2 Dependencies.

In a Med-Tech context, clinical claims include: accuracy statements, outcome improvements, diagnostic support, or any language that could constitute device labeling.

**Baseline Collection (ask before drafting)**

Before writing Section 3, ask:

> "What are the current baseline numbers for your primary metric and any guardrail metrics you care about? Even rough estimates are fine — I need these to write kill criteria and graduate conditions that aren't hollow."

If the user cannot provide any baselines, mark each as `[TBD — required before PRD approval]` and flag on the anti-slop checklist. A PRD with no baselines has mathematically empty success criteria.

---

## Step 4 — Build the PRD

**Before generation, ask user about execution preference:**

> "I have everything needed. I can generate PRD in background so you can continue working, or run in foreground. Prefer?"

- **Background**: User can work while PRD generates, notified on completion
- **Foreground**: User sees generation progress, waits for completion

Proceed based on user choice.

---

Generate all 7 sections. Use the real inputs gathered. Do not invent numbers, personas, or metrics.

**Target length:** 5-6 pages at 12-14pt font when converted to .docx. Prioritize conciseness in all sections—use tight bullet formats for AI Feature Readiness, scannable bullet structure for Behavior Contract examples, and keep all prose sections focused.

---

### Section 1: Opportunity Framing

**Core Problem**
One sentence. Name the user, the friction, and the measurable consequence.
Format: *[User] experiences [friction] which causes [measurable outcome].*

**Hypothesis**
One sentence in if/then/because format.
Format: *If we [intervention], then [metric] will [change by X%] because [mechanism].*

**Strategy Fit**
Which OKR or initiative does this unlock? Name it specifically.

**Solution Approach** *(Path A only)*
For non-prototyped features, describe the solution concept and rationale:

*What we're building:*
1-2 sentence description of the solution concept. What is the user experience or system behavior?

*Why this approach:*
Rationale for this solution — why does it fit? (e.g., reuses existing infrastructure, fits architecture, aligns with strategic initiative, avoids tight coupling)

*Key components:*
High-level list of what needs to be built (3-5 components). Not implementation detail, just major pieces.

*Alternatives considered:*
List 2-3 alternative approaches that were discussed and rejected. For each, state the specific reason for rejection (not just "too complex" but "adds ML complexity without solving root cause of X").

**Evidence**
Structure the evidence with explicit questions to ensure quantified, actionable findings:

**User Research:**
- What did users say or do? Include % or sample size if available (e.g., "N=45 interviews, 67% reported X")
- What's the top friction or unmet need? (quote or observed behavior)
- What validates the hypothesis? (specific finding that supports the intervention)

If nothing was provided, mark as `[TBD — owner: Product/Research]` — do not skip.

**Competitive Snapshot:**
- What do the top 2-3 competitors do in this space? (1 sentence per competitor)
- Where is our gap or differentiator? (explicit statement: "Our gap: X. Our differentiator: Y.")

**Prototype Evidence** *(Path B only)*
- Prototypes built: [list]
- Winner: [name/version] — survived because [specific reason]
- Validated: [what the prototype confirmed]
- Invalidated: [what was ruled out]
- Residual unknowns: [what we still don't know]

---

### Section 2: Boundaries

**In Scope**
Bullet list — specific features, user segments, platforms, timeframes.

**Non-Goals**
Only list things someone would genuinely argue for. If no one would push back, it is not a real non-goal.

**Dependencies**
What must be true before this ships? Use table format for scannability:

| Dependency | Owner | Status |
|---|---|---|
| [Dependency description] | [Name/Team] | [Confirmed / At risk / Not started] |
| [Second dependency] | [Name/Team] | [Status] |

**AI Feature Readiness** *(AI features only — add as subsection under Dependencies)*

For any feature where AI makes decisions or generates content, systematically surface data, system, and infrastructure readiness. **Use tight bullet format, not Q&A paragraphs.**

*Data Sources:*
- Document what data AI needs, if it exists, owner, and timeline for readiness (e.g., "12K AdPromo docs in Veeva (exist), metadata alignment in progress (Abir, 30-day timeline)")

*System Integrations:*
- Document what system integrations required, if endpoints exist, owner, and timeline (e.g., "Veeva API endpoints exist (sandbox confirmed), SSO integrated")

*Infrastructure:*
- Document what infrastructure needed, if it exists, owner, and timeline (e.g., "Mia storage/compute exists, current ingestion 2000 docs/day = 6-day load, Aaron assessing additional capacity (3mo ramp-up)")

Add each readiness item to the Dependencies table above with owner and status.

**Tradeoffs Accepted**
What are we explicitly giving up to ship this? Name the tradeoff and the reasoning.

---

### Section 3: Success Measurement

**Primary Metric**
One number. One threshold. This is the single metric that determines if this shipped successfully.
Format: *[Metric] [direction] [X%] vs [baseline] over [timeframe]*

**Guardrail Metrics**
Metrics that must NOT get worse. Use table format:

| Metric | Baseline | Acceptable Floor |
|---|---|---|
| [Metric name] | [Current value] | [Minimum acceptable — specific threshold] |
| [Second metric] | [Baseline] | [Floor] |

**Kill Criteria**
The operational trigger for rollback — fast and automatic. At what specific threshold does the system or on-call team act immediately, without a strategy meeting?
Format: *Roll back if [metric] drops below [X] or [event] occurs within [timeframe].*

> Note: Kill Criteria is not the same as Fail → Action (Section 6). Kill Criteria = automatic rollback threshold. Fail → Action = strategic response if primary metric underperforms over the evaluation window. Set different thresholds for each — if they reference the same number, one of them is redundant.

**Graduate When**
For rollout experiments: what specific condition moves this from limited to full rollout?

---

### Section 4: Rollout Plan

**PRD-level rollout plan is high-level** — detailed experiment design (MDE, statistical power, randomization mechanics) belongs in the technical specification document, not the PRD.

**Timeline**
When is the rollout happening? Use quarters or months:
- **Q2 2026:** Initial launch (pilot or limited rollout)
- **Q3 2026:** Expansion if criteria met
- **Q4 2026:** Full rollout

**Phasing Strategy**
What are the stages? Describe progression:
- **Stage 1:** X% of users or Y pilot locations
- **Stage 2:** Expand to Z% if gates met
- **Stage 3:** Full rollout (100%)

Name specific cohorts, locations, or segments for each stage.

**Gates for Expansion**
What must be true to move from one stage to the next?
- Primary metric threshold (e.g., conversion ≥ X%)
- Guardrail metrics within acceptable range
- No P0/P1 incidents
- Approvals required (Product, Engineering, Ops leads)

**Kill Switch**
- **Mechanism:** How is the feature disabled? (feature flag, configuration change)
- **Owner:** Who can trigger it? (name and role)
- **Speed:** How fast can it be executed? (< X minutes)

---

### Section 5: Risk Management

**Top Risks**
Use table format for scannability:

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| [What could go wrong — specific scenario] | High/Medium/Low | High/Medium/Low | [Specific action to prevent or reduce impact] |
| [Second risk] | [Likelihood] | [Impact] | [Mitigation] |

Limit to top 4-5 risks. Be specific — not "system might fail" but "POS event stream unreliable causes inventory sync lag."

**Detection**
How will we know when something is going wrong? Name the signal, the threshold, and the monitoring mechanism.

**Fallback & Kill Switch**
- Fallback: What happens to users if the feature is disabled?
- Kill switch: Who can trigger it? How fast can it be executed?

---

### Section 6: Ownership + Action

**Primary Owner**
Name and role of the accountable person. One person, not a team.

**Stakeholder Sign-off**
Who needs to approve before this ships? Build the table from the inputs gathered and the regulatory gate in Step 2b. Only include stakeholders whose approval is genuinely required — not everyone who should be informed.

| Stakeholder | Team | Decision Needed | Status |
|---|---|---|---|
| [Name] | Product | PRD approval | Not started |
| [Name] | Engineering | Feasibility sign-off | Not started |
| [Name] | Legal / Regulatory | Compliance review | Not started |
| [Name] | Privacy / Security | Data handling review | Not started |
| [Name] | Clinical Affairs | Clinical claim review *(if applicable)* | Not started |

Remove rows that do not apply. Add rows specific to the product (e.g., Supply Chain, HCP Advisory, Market Access).

**Decision Points**
When will we revisit or adjust? Name the dates and the trigger conditions.
Format: *[Date / milestone] — Decision: [what will be decided] — Owner: [name]*

**Fail → Action**
The strategic response if the primary metric underperforms over the full evaluation window — slower, human-led, involves a decision. If primary metric is not met by [date], the action is [specific next step], owned by [name].

> Note: This threshold should be different from Kill Criteria (Section 3). Kill Criteria triggers immediate rollback. Fail → Action triggers a strategy conversation. If both reference the same number, collapse them into one.

---

### Section 7: AI-Specific Additions *(only if this is an AI-powered feature)*

**Primary Tasks**
Number each task the AI is performing. Be specific — not "classify intent" but "classify return reason into 8 defined categories."

**Inputs Available**
What data does the AI have access to at inference time? List each input type (e.g., "user search query (text)", "catalog metadata (product descriptions, category taxonomy)", "search context (active filters, session data)").

**Activation Logic**
When does the AI activate vs. when does the system use non-AI fallback?

*When AI activates:*
- [Condition 1 — be specific: "query contains 3+ words with no product name detected"]
- [Condition 2]
- [Condition 3]

*When system uses non-AI fallback:*
- [Condition 1 — be specific: "query is specific product name or brand"]
- [Condition 2]

*Examples:*
Provide 3-5 examples showing which path is taken:

| Input Example | Path Taken | Why |
|---|---|---|
| "headache relief safe during pregnancy" | AI | Natural language, health intent, requires interpretation |
| "Tylenol 500mg" | Non-AI | Specific product name, keyword match sufficient |

**Behavior Contract**
Provide 3–5 labeled examples using **Input → Expected** format. Each example must be specific to this product, not generic. **Use scannable bullet format with clear query titles.**

Format per example:
```
**Query [N]: [Descriptive title for this scenario]**

- **Input:** [specific realistic user input]
- **Expected:**
  - [First expected behavior or check]
  - [Second expected behavior]
  - [Third expected behavior - use bullets if multiple steps]
- **Edge case:** [Yes/No — if yes, explain why this is non-obvious or safety-critical]
```

**Optional Training Supplement:**
For training purposes only, you may also provide GOOD/BAD/REJECT patterns as a supplement (not replacement) to Input → Expected:
- **GOOD:** [what the AI should do]
- **BAD:** [what the AI might do wrong]
- **REJECT:** [what the AI must never do]

**Edge Cases** *(Path B — populate from prototype testing)*
Specific scenarios that surfaced during prototype testing where the system behaved unexpectedly or users did something unanticipated. These are not hypothetical — they are observed. List each with what happened and how the production system should handle it.

**Guardrails**
Constraints the AI must never violate. Use bullet list:
- [Constraint 1 — e.g., "No clinical claims: AI must never suggest a product treats, cures, or prevents a disease"]
- [Constraint 2]

**Fallback Behavior**
What happens when the AI is uncertain or fails?

*When AI is uncertain (confidence score < X):*
- [Specific fallback path — e.g., "Revert to standard keyword search"]
- [What user sees]
- [What gets logged]

*Handoff path:* [Name the non-AI system that takes over]  
*Trigger threshold:* [Specific condition — e.g., "Confidence score < 0.6 OR latency > 500ms"]

---

### Section 8: Post-Ship *(applies to all PRDs — leave blank at PRD creation, fill in after launch)*

This section turns the PRD into a living document. Populate it after the first rollout evaluation.

*[Leave blank until first evaluation — fill after pilot or initial rollout completes]*

**Results doc link**
*[Link to dashboard or experiment results]*

**What surprised us?**
*[What did users do that we didn't expect? What did data show that we didn't anticipate?]*

**What will we change?**
*[Based on results — changes to scope, metrics, rollout strategy, or behavior contract]*

**New examples to add to behavior contract** *(AI features only)*
*[Real production inputs that should be added as examples for next iteration]*

**Decision**
- ○ Iterate — continue with changes
- ○ Scale — expand rollout as planned
- ○ Retire — stop and document why

---

## Step 5 — Anti-Slop Checklist

Before finalising the PRD, verify every item below. Flag any that fail.

**IMPORTANT:** This checklist is for internal validation only. **DO NOT include the anti-slop checklist section in the final PRD markdown file.** It bloats the document and is not meant for readers—it's a quality gate for drafting.

**Specificity**
- [ ] Every metric has a number and a threshold — no "improve", "increase", "reduce" without a target
- [ ] The hypothesis names the specific mechanism, not just the outcome
- [ ] Non-goals list only genuinely contested items — if no one would argue for them, remove them
- [ ] Kill criteria has a specific number, not "if metrics degrade"

**Ownership**
- [ ] Every dependency has a named owner and a status
- [ ] Primary owner is one person, not a team or role
- [ ] Every decision point has a date or milestone and an owner
- [ ] Fail → Action names a specific next step and a named person
- [ ] Stakeholder sign-off table is populated — rows without real owners removed
- [ ] Regulatory gate was answered — either a compliance dependency is listed or "Not applicable" is explicitly noted

**Honesty**
- [ ] Tradeoffs Accepted names something real that was given up
- [ ] Gaps are marked [TBD — owner: name] rather than filled with vague placeholders
- [ ] No banned phrases present: robust, seamless, leverage, world-class, cutting-edge, significant improvement, better experience, empower users, holistic, synergy

**Evidence & Context (v1.4)**
- [ ] User research includes quantified findings (%, sample size, or specific observation) — not just "users want X"
- [ ] Competitive snapshot explicitly states gap and differentiator — not just "competitors do X"
- [ ] Solution Approach present for Path A — includes concept, rationale, components, alternatives rejected

**AI-Specific (if applicable)**
- [ ] AI activation conditions are explicit — when does AI trigger vs. fallback?
- [ ] AI Feature Readiness dependencies identified — data sources, system integrations, infrastructure with owners and timelines
- [ ] Inputs Available lists actual data fields, not categories ("user search query (text)" not "user input")
- [ ] Behavior Contract uses Input → Expected format with 3-5 examples in scannable bullet format with query titles
- [ ] Fallback behavior names a specific handoff path and trigger threshold

**Format & Structure (v1.4)**
- [ ] Dependencies use table format (dependency | owner | status)
- [ ] Guardrail Metrics use table format (metric | baseline | acceptable floor)
- [ ] Top Risks use table format (risk | likelihood | impact | mitigation)
- [ ] Rollout plan is high-level (timeline Q2/Q3, phasing %, gates) — not detailed experiment design (MDE, power, randomization)

If any item fails — fix it before saving.

---

## Step 6 — Save Output

Save the PRD in both formats. Both are permanent outputs — not just intermediaries.

**Filename format:** `[ProductName]-PRD-[YYYY-MM-DD]`
**Save location:** `docs/prds/`

Steps:
1. Create directory if needed: `mkdir -p docs/prds`
2. Write the full PRD content to `docs/prds/[ProductName]-PRD-[YYYY-MM-DD].md` — this is a permanent reference copy
3. If prototype images were provided in Step 2, ensure they are saved to `docs/prds/` folder and the image references in the .md point to the correct filenames
4. Run: `cd docs/prds && pandoc [filename].md -o [filename].docx`
5. Confirm both files exist
6. Inform the user: "Saved as [filename].md and [filename].docx in `docs/prds/`"

**Note on prototype images in .docx:** If images were provided, pandoc will embed them in the .docx automatically if the image files are in the same folder as the .md. If images are missing, pandoc will replace them with the alt-text description — note this to the user and ask them to drop the image files into the `docs/prds/` folder for a clean embed.

---

## Step 7 — Capture Project Context (If New Abbott Project)

**Only run this step if:** User selected "Abbott project" in Step 0 AND provided a new project name (not Mia, Marketing GenAI, or Regulatory Drafting).

**Purpose:** Create a reusable project context file so future PRDs for this project can load project-specific context automatically.

**Steps:**

1. Create file: `.claude/context/projects/[project-name].md` (lowercase, hyphenated)

2. Populate with information captured during PRD creation:

```markdown
# [Project Name] — Project Context

**Status:** [Active/Pilot/Planning]  
**Owner:** [Primary owner from Section 6]  
**Last Updated:** [Today's date]

---

## Overview

[Problem statement from Section 1, 2-3 sentences]

**Solution:** [Solution overview from Section 1, 2-3 sentences]

---

## Key Stakeholders

[From Section 6 Stakeholder Sign-off table]

| Role | Name | Responsibility |
|---|---|---|
| [Role] | [Name] | [What they approve/review] |

---

## Strategic Fit

[From Section 1 Strategy Fit]

**OKRs:** [List OKRs this project maps to]

---

## Dependencies & Integrations

[From Section 2 Dependencies table]

| Dependency | Owner | Status |
|---|---|---|
| [System/Platform] | [Owner] | [Status] |

---

## Regulatory Considerations

[From Step 3b Regulatory Gate and Section 2]

- **Regulatory classification:** [GxP / Non-GxP / Clinical / etc.]
- **Compliance requirements:** [HIPAA / GDPR / FDA / etc.]
- **Approvals needed:** [List regulatory stakeholders]

---

## How to Use This Context

**For future PRDs:**
- Load this file when writing PRDs for [Project Name]
- Reference stakeholders, dependencies, regulatory requirements
- Check strategic fit alignment

**For other skills:**
- competitive-intel: Reference when analyzing competitors in this domain
- prd-evaluator: Use for Track 7 scoring (strategic alignment, regulatory awareness)
- requirements-spec-writer: Reference for requirement classification
```

3. Notify user:

> "Created project context file at `.claude/context/projects/[project-name].md`. Future PRDs for [Project Name] will automatically load this context."

---

## Rules

- Never fill a section with generic text when specifics are missing — ask or mark as TBD
- Path B PRDs must include Prototype Evidence in Section 1 — do not skip it
- The AI-Specific section is mandatory for any feature where AI makes a decision or generates content
- The anti-slop checklist runs every time — it is not optional
- One primary metric only — if the user gives multiple, ask them to choose one
- Save as .docx every time — do not deliver PRD only in chat
