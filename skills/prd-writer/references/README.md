# PRD Writer — References

Store context documents here organized by project or product name. When running the PRD Writer skill, point to the relevant subfolder so the skill reads existing context before asking questions.

## Folder Convention

```
references/
  [project-or-product-name]/
    brief.md
    okrs.md
    journey-map.md
    capability-map.md
    prototype-results.md
    competitive-notes.md
    [any other relevant context]
```

## How to Use

When starting a PRD, tell the skill:
> "Reference documents are in `.claude/skills/prd-writer/references/[project-name]/`"

The skill will read all files in that folder before asking any questions. Anything already answered in the reference docs will not be re-asked.

## What to Store Here

- Product briefs
- OKR docs
- Journey maps (output from Journey Builder skill)
- Capability maps (output from Capability Mapper skill)
- Prototype evaluation results (output from Prototype Evaluator skill)
- Competitive analysis notes
- User research summaries
- Stakeholder alignment notes
