# PRD Writer

**Version:** 1.5  
**Author:** Nitesh Luthra

---

## What It Does

Generates complete Product Requirements Documents (PRDs) for digital products and features. Supports two paths: Standard (from brief + OKRs) and Prototype Validated (from prototype learnings).

**Output:** .md + .docx files ready for engineering handoff

---

## When to Use

Use when you need to:
- Turn a product idea into a structured specification
- Document prototype validation and next steps
- Create engineering handoff document with metrics, rollout, risks, ownership

**Trigger phrases:** "write a PRD", "create a PRD", "generate product spec", "convert prototype to PRD"

---

## Quick Start

```
/prd-writer
```

The skill will guide you through:
1. Context gathering (existing docs, OKRs, research)
2. Path detection (Standard vs Prototype Validated)
3. Targeted questions (only what's needed)
4. PRD generation with anti-slop validation
5. Save as .md + .docx

---

## Two Paths

### Path A — Standard PRD
**When:** You have a brief, OKRs, and clear problem. No prototype yet.

**What you need:**
- Product/feature name
- User and problem statement
- Success metric + target
- Dependencies
- User research (optional)
- Competitive context (optional)

**Output includes:** Solution Approach section (concept, rationale, key components, alternatives considered)

### Path B — Prototype Validated PRD
**When:** You've built and evaluated prototypes. Ready to document the winner.

**What you need:**
- Which prototypes were built
- Which one survived and why
- What was validated/invalidated
- Residual unknowns
- Success metric + target

**Output includes:** Prototype Evidence section (what was tested, winner selection rationale)

---

## Key Features

**v1.5 Improvements:**
- ✅ **Reduced AI behavior examples** — 3-5 examples instead of 15-25 for readability
- ✅ **Scannable bullet format** — Behavior Contract uses clear query titles + bullet structure
- ✅ **Page count target** — 5-6 pages at 12-14pt font (.docx)
- ✅ **Detects .docx drafts** — searches both .md and .docx when looking for existing PRDs
- ✅ **Tight bullet formats** — AI Feature Readiness uses concise bullets, not Q&A

**v1.4 Improvements:**
- ✅ **Solution Approach** for Path A (concept, why, alternatives)
- ✅ **AI Activation Logic** (when AI triggers vs. fallback)
- ✅ **AI Feature Readiness** (data/systems/infrastructure dependencies)
- ✅ **Structured Evidence** (quantified research required)
- ✅ **Table Formats** (Dependencies, Guardrails, Risks)
- ✅ **High-Level Rollout** (timeline/phasing, not experiment design)
- ✅ **Universal Post-Ship** (living document for all PRDs)

**Quality Enforcement:**
- Anti-slop checklist (no banned phrases, specificity requirements)
- Baseline collection (no hollow metrics)
- Regulatory gate (Med-Tech/healthcare features)
- Named owners (no teams, one person accountable)

---

## PRD Structure

**Section 1:** Opportunity Framing (problem, hypothesis, evidence, solution approach)  
**Section 2:** Boundaries (scope, non-goals, dependencies, tradeoffs)  
**Section 3:** Success Measurement (primary metric, guardrails, kill criteria)  
**Section 4:** Rollout Plan (timeline, phasing, gates, kill switch)  
**Section 5:** Risk Management (top risks, detection, fallback)  
**Section 6:** Ownership + Action (owner, stakeholders, decision points, fail → action)  
**Section 7:** AI-Specific Additions (if applicable: tasks, activation logic, behavior contract)  
**Section 8:** Post-Ship (fill after launch: results, learnings, decision)

---

## Example Usage

### Standard PRD (Path A)
```
User: "Write a PRD for pharmacy inventory sync system"
```
Skill will ask for: problem, metric, dependencies, research, competitive context  
Output: PRD with Solution Approach section (concept, rationale, alternatives)

### Prototype Validated PRD (Path B)
```
User: "Create a PRD for semantic search - we tested 3 prototypes"
```
Skill will ask for: which prototypes, winner, validated/invalidated, residual unknowns  
Output: PRD with Prototype Evidence section

### AI Feature
For AI-powered features, skill automatically adds:
- AI Activation Logic (when does AI trigger?)
- AI Feature Readiness (data/systems/infrastructure check)
- Behavior Contract (15-25 Input → Expected examples)
- Guardrails and Fallback Behavior

---

## Files Created

**Location:** `.claude/skills/prd-writer/prds/`

**Format:** 
- `[ProductName]-PRD-[YYYY-MM-DD].md` (permanent reference)
- `[ProductName]-PRD-[YYYY-MM-DD].docx` (shareable)

---

## Pro Tips

1. **Gather docs first** — Paste briefs, OKRs, research before starting. Skill extracts context and asks fewer questions.

2. **Have baselines ready** — Skill requires baseline numbers for metrics. "Improve conversion" → rejected. "2.8% → 3.08%" → accepted.

3. **Name owners** — Skill enforces named individuals, not teams. Be ready with actual names.

4. **Path A needs solution concept** — Don't just describe problem. Have rough idea of what you're building and why.

5. **AI features need examples** — Prepare 15-25 realistic inputs. Generic templates rejected.

6. **Use with evaluator** — Run prd-evaluator after generation to confirm quality (target: 54-60/70 = 90%+).

---

## Quality Standard

**Target Score:** 54-60/70 (90%+) on PRD Evaluator

**Reference PRDs:**
- `HealthRetail-Search-Experience-Upgrade-PRD-2026-04-06-v4.md` (Path B, AI) — 54/60
- `Pharmacy-Inventory-Sync-PRD-2026-04-06-v1.md` (Path A, non-AI) — 54/60

---

## Company Context (Future: v1.6+)

**Current approach (v1.5):** prd-writer is **generic** — does not ask for company-specific context during PRD generation. Company context is handled **post-drafting** via prd-evaluator Track 7 (optional).

**Future enhancement:** Company/product/BU-specific reference data will be integrated into prd-writer for:
- **Strategic fit validation** — e.g., Abbott strategic imperatives (Instant Convenience, Enhanced Digital Experiences)
- **Regulatory gates** — e.g., PMA, 510(k), CE mark, HIPAA, GDPR requirements
- **Product-specific criteria** — e.g., FreeStyle Libre user personas, Mia platform architecture

**Reference file structure:**
- `references/companies/abbott-corporate.md` — Corporate context (strategic imperatives, regulatory, SLC)
- `references/companies/abbott-freestyle-libre.md` — FreeStyle Libre product context
- `references/companies/mia-platform.md` — Mia platform integration context

**How to use (when implemented):**
- Skill will ask: "Does this PRD need company-specific context?" (yes/no)
- If yes: load reference file or ask inline
- Company context feeds into Section 1 (Strategy Fit) and Section 6 (Stakeholder Sign-off)

**For now:** Use prd-evaluator Track 7 for company-specific assessment after PRD is drafted.

---

## See Also

- **prd-evaluator** — Companion skill to assess PRD quality
- **CREATION-LOG.md** — Full TDD process documentation
- **skill-inference.md** — Writing style guide for skill outputs
