# Context Budget Reference

Token cost estimates and budgeting guidelines for managing the 200K context window effectively.

## Context Window Anatomy

The ~200K token window is NOT all yours. Here's how it breaks down:

| Segment | Approx Tokens | Notes |
|---|---|---|
| System prompt + instructions | ~5,000-8,000 | Always present |
| Loaded skills | ~2,000-5,000 each | Stacks with multiple skills |
| Session summary (if continued) | ~3,000-10,000 | From prior session compaction |
| CLAUDE.md / project config | ~1,000-5,000 | Loaded at start |
| Memory index (MEMORY.md) | ~500-2,000 | Always loaded |
| **Available for conversation** | **~150,000-180,000** | What you actually have to work with |

### Effective Budget Rule
Assume you have **~150K usable tokens**. Plan for compaction at ~120K to leave headroom.

## Token Cost by Activity

### File Reading

| File Size | Lines | Approx Tokens | Context Impact |
|---|---|---|---|
| Small config | <50 lines | ~300-500 | Negligible |
| Single function | 50-100 lines | ~500-1,000 | Low |
| Medium file | 100-300 lines | ~1,000-3,000 | Moderate |
| Large file | 300-500 lines | ~3,000-5,000 | Significant |
| Very large file | 500-1000 lines | ~5,000-10,000 | Heavy |
| Huge file | 1000+ lines | ~10,000+ | Dangerous — use offset/limit |

### Tool Results

| Tool | Typical Result Size | Tokens |
|---|---|---|
| Glob (file list) | 10-50 files | ~200-500 |
| Grep (files_with_matches) | 5-20 files | ~100-300 |
| Grep (content, 10 matches) | 10-30 lines | ~200-400 |
| Grep (content, 50+ matches) | 100+ lines | ~1,000-2,000 |
| Bash (short command) | 5-20 lines | ~100-300 |
| Bash (test suite output) | 50-200 lines | ~500-2,000 |
| Bash (build output) | 100-500 lines | ~1,000-5,000 |
| Agent result | Varies | ~500-3,000 (contained) |

### Generation (Output)

| Output Type | Typical Size | Tokens |
|---|---|---|
| Short answer | 2-5 sentences | ~50-100 |
| Code edit (Edit tool) | 5-30 lines | ~100-400 |
| New file (Write tool) | 50-200 lines | ~500-2,000 |
| Large generation (PRD, doc) | 200-500 lines | ~2,000-5,000 |
| Full skill execution | Multiple outputs | ~5,000-15,000 total |

## Budget Tracking Heuristic

Since you can't see exact token counts, use this rough tracker:

### Per-Action Cost Estimates

| Action | Budget Points (1 point ~ 1K tokens) |
|---|---|
| Read a small file (<100 lines) | 1 |
| Read a medium file (100-300 lines) | 3 |
| Read a large file (300+ lines) | 5-10 |
| Grep with content (moderate results) | 1 |
| Grep with content (many results) | 2-3 |
| Glob search | 0.5 |
| Short Bash command | 0.5 |
| Long Bash output (tests, builds) | 2-5 |
| Generate a medium response | 1-2 |
| Generate a large artifact | 3-5 |
| Load a skill | 3-5 |
| Each conversation turn (user + assistant) | 1-3 |

### Session Budget

| Budget Points Used | Status | Action |
|---|---|---|
| 0-40 | Green | Proceed normally |
| 40-80 | Yellow | Apply lite optimization: subagents for research, offset/limit for reads |
| 80-120 | Red | Recommend /compact, persist critical state, go subagent-heavy |
| 120+ | Critical | Compaction is imminent or has fired. Save state, suggest new session for next phase |

### Rough Conversion
- **1 budget point ~ 1,000 tokens**
- **150 budget points ~ full usable context**
- Track mentally as you work. When you've done ~10 file reads and 15 conversation turns, you're probably at Yellow.

## Common Session Profiles

### Light Session (~30-50 points)
- User asks a question
- You read 2-3 files
- You make 1-2 edits
- 5-8 conversation turns
- **No optimization needed**

### Medium Session (~50-80 points)
- Multi-file task (feature, refactor)
- Read 5-8 files
- Multiple edits
- 10-15 conversation turns
- **Apply lite optimization midway**

### Heavy Session (~80-120 points)
- Full skill execution (PRD, architecture)
- Read 10+ files
- Large generation
- 15+ conversation turns
- **Will need compaction. Plan for it.**

### Marathon Session (~120+ points)
- Multiple skills in one session
- Deep codebase exploration
- Large artifacts generated
- 20+ turns
- **Will hit compaction multiple times. Use subagents aggressively. Consider splitting.**

## Optimization ROI

| Technique | Tokens Saved | Effort |
|---|---|---|
| Grep before Read (targeted read) | ~3,000-8,000 per file | Low — just add a grep step |
| Subagent for research | ~10,000-40,000 per delegation | Low — spawn and wait |
| offset/limit on large files | ~5,000-8,000 per file | Low — add params |
| Write to file instead of outputting | ~2,000-5,000 per generation | Low — use Write tool |
| /compact at Yellow | ~50,000-80,000 reclaimed | Medium — brief user disruption |
| Session split at Red | Full reset | Medium — requires state persistence |

## The Golden Rule

**Every token in context should be earning its keep.** If you read a 500-line file to find one function signature, you wasted 4,500 tokens of budget. Grep first, then read the 20 lines you need.
