# Delegation Patterns Reference

Decision tree and patterns for when and how to delegate work to subagents to protect main context.

## The Delegation Decision Tree

```
Is this task the user's PRIMARY request?
├── YES → Do it in main context
│   └── But does it require reading 3+ files first?
│       ├── YES → Delegate the RESEARCH to a subagent, then implement in main
│       └── NO → Proceed in main context
└── NO → Is it independent of the current task?
    ├── YES → Delegate to background subagent
    └── NO → Is it a prerequisite?
        ├── YES → Delegate to foreground subagent, wait for result
        └── NO → Defer until needed
```

## Pattern Catalog

### Pattern 1: Research-Then-Act

**When:** You need to understand the codebase before making changes.

**Anti-pattern:** Read 8 files into main context, then make a 3-line edit.

**Correct pattern:**
```
1. Spawn Explore subagent: "Find all files that [criteria]. Report: file paths, relevant line ranges, and the pattern used."
2. Receive report (compact summary, not raw file contents)
3. Read ONLY the specific lines you need to edit
4. Make the edit
```

**Token savings:** ~80% — subagent reads 8 files (~40K tokens) but only returns a 200-word summary (~300 tokens) to main context.

### Pattern 2: Parallel Investigation

**When:** The user's request requires checking multiple independent things.

**Example:** "Is this function used anywhere? And check if the tests pass."

**Correct pattern:**
```
1. Spawn subagent A (foreground): "Search for all usages of [function] across the codebase"
2. Spawn subagent B (background): "Run the test suite and report results"
3. Both run in parallel
4. Use results as they arrive
```

### Pattern 3: Generate-and-Validate

**When:** You're generating a large artifact (code, docs, PRD) that needs validation.

**Correct pattern:**
```
1. Generate the artifact in main context (write to file)
2. Spawn background subagent: "Review [file] for [criteria]. Report issues only."
3. Continue with next task while validation runs
4. Address issues when subagent reports back
```

### Pattern 4: Multi-File Edit

**When:** A change touches 5+ files (e.g., renaming, refactoring, API changes).

**Correct pattern:**
```
1. In main context: Edit the primary file (the source of truth)
2. Spawn subagent: "Update all references to [old] → [new] in these files: [list]"
3. Review subagent's changes
```

### Pattern 5: Context Recovery

**When:** Auto-compaction has fired and you need information from earlier in the session.

**Anti-pattern:** Re-read all the files from earlier.

**Correct pattern:**
```
1. Check memory files — was anything saved before compaction?
2. Check todo list — does it capture the key decisions?
3. If still missing info, spawn Explore subagent to re-gather ONLY what you need
4. Capture the critical facts in your response text (so they survive future compaction)
```

### Pattern 6: Skill Execution Isolation

**When:** The user's task requires running a heavy skill (e.g., notional-architecture, ddd-workshop).

**Correct pattern:**
```
1. Run the skill's interactive steps in main context (questions, confirmations)
2. Delegate the skill's GENERATION step to a subagent if the output is large
3. Or: save progress to memory, suggest /compact, then generate
```

## Subagent Type Selection

| Task | Subagent Type | Why |
|---|---|---|
| Find files, search code, answer codebase questions | `Explore` | Fast, specialized for search |
| Multi-step implementation, complex edits | `general-purpose` | Full tool access |
| Architecture/design review | `Plan` | Read-only analysis |
| Code quality check after implementation | `superpowers:code-reviewer` | Specialized review |
| Independent parallel tasks | `general-purpose` with `run_in_background: true` | Non-blocking |

## Prompt Engineering for Subagents

When spawning a subagent, always include:

1. **What to find/do** — specific, not vague
2. **What to report back** — "Report file paths and line numbers" not "tell me what you find"
3. **What NOT to include** — "Don't include full file contents, just the relevant excerpts"
4. **Size constraint** — "Keep your report under 300 words" or "Report in a table"

**Good prompt:**
> "Search the codebase for all usages of the `correlateGlucose` function. Report: each file path, the line number, and a 1-line description of how it's used. Don't include the full surrounding code. Table format."

**Bad prompt:**
> "Look into how correlateGlucose works and tell me about it."

The bad prompt will return a 2000-word essay. The good prompt returns a 10-row table.
