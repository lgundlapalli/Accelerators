# PRD Writer Skill — Improvement Backlog

Gaps identified 2026-04-01 via review of SKILL.md + HealthRetail AI Search PRD (Path B).
v1.3 addressed gaps 3, 5, 7, and partial 1. Below are the remaining items.

---

## Gap 2 — No Definition of Done

**Problem:** The skill jumps from requirements → rollout with nothing between. Engineering has no acceptance criteria, no QA standard, no "what does done look like technically." The HealthRetail PRD is a complete requirements doc with no handoff contract for the build team.

**Fix:** Add a new section between Section 2 (Boundaries) and Section 3 (Success Measurement):

> **Section 2b: Build Contract**
> - Acceptance criteria: what must be true for engineering to call this done?
> - QA standard: what test coverage or review is required before launch?
> - Tech readiness gates: what infrastructure, data, or API dependencies must be confirmed before build begins?

**Checklist addition:**
- [ ] Acceptance criteria defined — engineering knows what "done" looks like

---

## Gap 4 — AI Section Missing Model/System Definition

**Problem:** Section 7 collects behavior contract and guardrails but never asks which AI system powers the feature, how it will be evaluated before launch, or what "confidence score" means technically. The HealthRetail PRD's fallback says "below [TBD threshold]" — making it unimplementable.

**Fix:** Add to Section 7, before Inputs Available:

> **Model / System**
> - Which AI model or system powers this feature? (name or describe)
> - How will the model be evaluated before launch? (human eval, automated test suite, task completion rate — name the method and pass threshold)
> - How is confidence/uncertainty measured? Define the confidence score or signal used for fallback routing.

**Checklist addition (AI-Specific):**
- [ ] Model or system named — not "AI layer" or "LLM"
- [ ] Evaluation method named with a pass threshold before launch
- [ ] Confidence threshold defined — fallback behavior is implementable

---

## Gap 6 — No Data / Logging Requirements

**Problem:** The regulatory gate asks about PHI/PII but doesn't ask what query data is logged, retained, or who has access. For AI features, search/query logs are a data handling question separate from PHI. The HealthRetail PRD has no answer to this because the skill never asked.

**Fix:** Add a prompt after the regulatory gate in Step 3b:

> **Data & Logging (ask for AI features):**
> "What user data does this feature log at inference time? How long is it retained? Who has access to query logs?"

If the user cannot answer → mark as `[TBD — Data/Privacy team]` and add as a dependency in Section 2 with status Unknown.

**Checklist addition:**
- [ ] Data retention policy stated or explicitly flagged as TBD with owner

---

## Notes

- Gap 1 (baseline collection) was partially addressed in v1.3 — a prompt was added at end of Step 3b. Full fix would also add a checklist item: `[ ] All guardrail metric baselines are real numbers, not TBD`.
- The HealthRetail PRD (Path B sample) should be updated to reflect v1.3 changes once the skill is stable.
