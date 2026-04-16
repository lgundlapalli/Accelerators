# Architecture Deck Template

## When to Use
- Presenting a new or revised technical architecture to stakeholders
- Architecture review boards
- Technical strategy presentations to leadership
- Cross-team alignment on system design

## Audience Calibration

| Audience         | Lead With            | Diagram Depth     | Language             |
|-----------------|----------------------|-------------------|----------------------|
| C-Suite         | Business impact      | 1 high-level only | Zero jargon          |
| VP Engineering  | Trade-offs + risk    | 2-3 layered       | Technical shorthand OK|
| Architects      | Design decisions     | Full detail       | Precise terminology  |
| Mixed           | Capability story     | Progressive reveal| Define terms inline  |

## Slide Structure

### Slide 1: Title + The One Thing
- Architecture name / initiative
- Single sentence: what this enables for the business
- **Speaker Notes**: Set context in 30 seconds. Why are we here today?

### Slide 2: Executive Summary
- 3-4 bullets maximum:
  - What we're building and why NOW
  - Key architectural decision and its business impact
  - What we need (approval / resources / alignment)
  - Timeline headline

### Slide 3: Business Context Drives Architecture
- What business capabilities does this architecture enable?
- Connect each capability to a revenue/cost/risk/speed outcome
- Use a simple table: Capability | Business Outcome | Priority

### Slide 4: Current State Pain Points (if applicable)
- Frame as business problems, not technical debt
- "Customer checkout fails 3% of the time" not "Monolith coupling causes race conditions"
- Maximum 3 pain points — each tied to a metric

### Slide 5: Architecture Overview (The Diagram)
- ONE high-level diagram (Mermaid recommended)
- Label components with business capabilities, not technical names
- Color-code by: new vs. existing, or by domain/team ownership
- **Speaker Notes**: Walk the audience through ONE user journey on the diagram

### Slide 6: Key Design Decisions
- Table format: Decision | Options Considered | Choice | Why
- Maximum 3-4 decisions — the ones that matter to THIS audience
- Frame "why" in business terms: cost, speed, risk, compliance

### Slide 7: What Changes (Before/After)
- Side-by-side or table comparison
- Focus on outcomes: latency, cost, reliability, capability
- Include at least one metric for each change

### Slide 8: Journey Traceability (Optional)
- Pick 1-2 critical user journeys
- Show how they flow through the architecture
- Sequence diagram (Mermaid) connecting user action to system response

### Slide 9: Risk and Mitigation
- Table: Risk | Impact | Likelihood | Mitigation
- Maximum 4 risks — the ones leadership would ask about
- Show you've thought about failure, not just success

### Slide 10: Implementation Roadmap
- Phase-based timeline (not Gantt charts for executives)
- Each phase: what ships, what it enables, key milestone
- Call out decision points where leadership input is needed

### Slide 11: The Ask
- Exactly what you need: approval, funding amount, team allocation, priority call
- By when
- What happens if we proceed vs. if we don't

### Slide 12: Next Steps + Owners + Dates
- 3-5 concrete next steps with named owners and dates
- Include the first checkpoint/review date

### Appendix Slides
- Detailed technical diagrams
- Component inventory
- Non-functional requirements matrix
- Cost modeling details
- Security / compliance mapping

## Mermaid Diagram Guidelines for Architecture Decks

```
- Use `graph TB` for layered architectures (top-to-bottom)
- Use `graph LR` for flow/pipeline architectures (left-to-right)
- Use `sequenceDiagram` for journey traceability
- Subgraphs for layers or bounded contexts
- Dotted lines (-.->`) for async / eventual consistency
- Solid lines (-->`) for synchronous / direct
- Color-code with style statements for new vs existing
```

## Tone Calibration

- **To executives**: "This architecture enables us to enter 3 new markets by Q4"
- **To engineers**: "This architecture separates read/write paths using CQRS with eventual consistency"
- **To mixed**: "This design lets us scale to 10x current volume — here's how the pieces fit together"
