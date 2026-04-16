# General Presentation Template

## When to Use
- Team alignment on a topic, process, or decision
- Knowledge sharing / brown bag sessions
- Project kickoffs or retrospectives
- Training or onboarding sessions
- Status updates to peers or cross-functional teams

## The Inform-Align-Act Framework

General presentations should still drive action. Structure around:

1. **Inform**: What does the audience need to know?
2. **Align**: What should they think or believe after this?
3. **Act**: What should they do differently as a result?

If you can't answer #3, question whether a presentation is the right format — maybe a document or email suffices.

## Slide Structure

### Slide 1: Title + Purpose
- Title states the topic AND the angle: "API Redesign: What Changes for Your Team"
- Subtitle: Why this matters to THIS audience right now
- **Speaker Notes**: Open with a question or a surprising fact — not "Today I'm going to talk about..."

### Slide 2: What We'll Decide / Learn Today
- Replace the traditional "Agenda" with outcome-oriented framing
- 3-4 bullets: "By the end of this session, you'll know..."
- Set expectations for interaction: "I'll pause for questions after section 2"

### Slide 3: Context Setting (Keep It Short)
- Maximum 2 slides of background
- Only include context the audience DOESN'T already have
- If they know the background, skip straight to the new information
- **Anti-pattern**: Don't recap the entire project history for a team that lived it

### Slides 4-N: Content Slides
Each content slide follows these rules:
- **Title = Takeaway**: "Latency Dropped 40% After Migration" not "Performance Results"
- **One idea per slide**: If you have two points, use two slides
- **5x5 rule**: 5 bullets max, 5-8 words each
- **Visual > Text**: Diagram, chart, or table when possible
- **Speaker Notes**: Include what you'll SAY — slides are visual aids, not scripts

### Content Slide Patterns

**Pattern: The Comparison**
| Before | After |
|--------|-------|
| metric | metric |
Best for: showing impact, justifying changes

**Pattern: The Framework**
- Introduce a mental model with 3-4 components
- One diagram showing relationships
Best for: teaching concepts, establishing shared vocabulary

**Pattern: The Evidence**
- Claim as title
- 2-3 supporting data points
- Source attribution
Best for: persuading, building consensus

**Pattern: The Demo/Example**
- Show, don't tell
- Screenshot, code snippet, or live walkthrough
- Annotate what to look at
Best for: making abstract concepts concrete

**Pattern: The Decision**
- Frame the choice
- Options with trade-offs (table format)
- Recommendation highlighted
Best for: driving alignment, getting buy-in

### Transition Slides (Optional)
- Use sparingly — only between major sections
- State what's coming AND why it matters
- "Now that we know the problem, here's what we're doing about it"

### Slide N-1: Key Takeaways
- 3-5 bullets maximum
- Each one a complete, actionable sentence
- Test: if someone only sees this slide, do they get the message?

### Slide N: Next Steps + Actions
- Specific actions with owners and dates
- Include "what you can do starting tomorrow"
- End with where to find more information or who to contact

## Engagement Techniques

### For Longer Presentations (30+ min)
- Insert a question or poll every 10 minutes
- Use "raise your hand if..." or "in the chat, share..."
- Alternate between telling and asking

### For Remote/Virtual
- More slides, less text per slide (keep visual pace)
- Explicitly call on people by name for input
- Use chat for parallel Q&A

### For In-Person
- Fewer slides, more whiteboarding moments
- Plan 2-3 "put down your laptop" moments
- Use physical movement (stand, walk to whiteboard) to signal transitions

## Visual Design in Markdown

### Diagrams (Mermaid)
- Use `flowchart` for processes
- Use `sequenceDiagram` for interactions
- Use `pie` for proportions
- Use `gantt` for timelines (sparingly)
- Keep diagrams to 5-8 nodes maximum per slide

### Tables
- Preferred over bullet lists for any comparison
- Bold the key column or row
- Maximum 5 rows visible (put rest in appendix)

### Code Snippets
- Maximum 10 lines per slide
- Highlight the relevant 2-3 lines
- Always explain what to look at BEFORE showing the code

## Common Mistakes

- **Reading slides aloud**: If you're reading, the audience is reading ahead and tuning out
- **Too much context**: Get to the new information fast
- **No clear ask**: Even informational presentations should end with "here's what to do next"
- **Skipping speaker notes**: Your future self (or someone inheriting the deck) needs them
- **Dense slides for "completeness"**: The appendix exists — use it
