import sys
from pathlib import Path
import importlib.util
spec = importlib.util.spec_from_file_location(
    "abc",
    Path.home() / '.claude/commands/pptx-generator/references/abbott-brand-constants.py'
)
abc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(abc)
for k, v in vars(abc).items():
    if not k.startswith('_'):
        globals()[k] = v

prs = create_presentation()

# ── Slide 1: Title ──────────────────────────────────────────
slide = add_title_slide(
    prs,
    title="EPD Marketer of the Future",
    subtitle="Capability Gap Analysis & Future State Roadmap",
    tagline="AI-Empowered. Human-Led.",
    org_date="Abbott EPD Marketing  |  May 2026"
)
add_notes(slide, "Open by framing this as a strategic inflection point. Abbott EPD is moving from humans using AI tools to AI-empowered strategic orchestrators. This deck maps where we are, where we need to go, and what we need to discover first.")

# ── Slide 2: Agenda ─────────────────────────────────────────
slide = add_agenda_slide(prs, "Agenda", [
    ("01", "The Burning Platform", "Why EPD marketing must transform — five systemic gaps"),
    ("02", "Five AI Agents", "The future state model covering the full marketing lifecycle"),
    ("03", "Capability Gap Analysis", "Current vs future state across all 20 capabilities"),
    ("04", "Validation Workplan", "What we need to discover before making tool decisions"),
    ("05", "Next Steps", "Three actions to move from assessment to architecture"),
], 2)
add_notes(slide, "Walk through the agenda briefly. Emphasize that this is a working document — the gap analysis will be updated once the validation workplan is complete.")

# ── Slide 3: Section 1 divider ──────────────────────────────
slide = add_section_divider(prs, "01", "The Burning Platform", "Why we must change — now")
add_notes(slide, "Set the context. EPD marketing is not broken — but it is structurally limited. The five gaps on the next slide are systemic, not tactical.")

# ── Slide 4: Five Systemic Gaps ─────────────────────────────
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.65),
         "Five Systemic Gaps Are Holding EPD Marketing Back",
         font_size=26, bold=True, color=NAVY)
add_text(slide, Inches(0.6), Inches(1.0), Inches(12), Inches(0.4),
         "These are root causes — not symptoms. Each has a named AI agent designed to close it.",
         font_size=13, color=NEAR_BLACK)

data = [
    ["Gap", "What It Means Today", "Business Impact"],
    ["Fragmentation", "Data, tools, and teams operate in silos", "Disconnected insights, missed signals"],
    ["Reactive Mode", "Static annual planning, unable to pivot", "Late to market, missed opportunities"],
    ["Bottlenecks", "Manual production and review cycles", "3–5 day briefs, 4–6 revision cycles"],
    ["Mass Reach", "Cannot scale personalized content", "One-size-fits-all campaigns"],
    ["Compliance Gating", "MLR viewed as a blocker, not an enabler", "Slow approvals, compliance risk"],
]
add_table(slide, Inches(0.6), Inches(1.5), Inches(12), Inches(3.5),
          rows=6, cols=3, data=data,
          col_widths=[Inches(2.5), Inches(5.0), Inches(4.5)], font_size=12)
add_callout_bar(slide, "Every gap has a named AI agent. The question is not whether to act — it is how fast.", y=Inches(5.2))
add_footer(slide, 4)
add_notes(slide, "Ask the room: how many of these gaps does your team feel every week? Let the table do the work. These are confirmed systemic issues from the EPD strategy document — not opinions.")

# ── Slide 5: ALICE Metrics ───────────────────────────────────
slide = add_big_numbers_slide(
    prs,
    title="The Baseline Is Broken — and Measurable",
    subtitle="ALICE has already proven what AI transformation delivers at scale",
    metrics=[
        ("8.9/10", "New Quality Baseline", "Up from 6.2/10. Excellence becomes the floor."),
        ("95%", "Faster Execution", "1–2 hours vs 3–5 days per brief"),
        ("750", "Days Reclaimed", "Equivalent to ~3 FTEs freed for strategic work"),
        ("3 Weeks", "Faster to Market", "From brief to campaign activation"),
    ],
    callout="43% quality elevation. Every brief now starts at excellence — not average.",
    sources="Source: ALICE deployment results — Abbott EPD AI transformation program",
    page_num=5
)
add_notes(slide, "These are real numbers from ALICE deployment. Use the 750 days reclaimed figure — it translates AI impact into business language that resonates with leadership. Brief quality from 6.2 to 8.9 means the floor of quality rose, not just the ceiling.")

# ── Slide 6: Section 2 divider ──────────────────────────────
slide = add_section_divider(prs, "02", "Five AI Agents", "The future state model for EPD marketing")
add_notes(slide, "Introduce the five agents as an ecosystem, not a toolbox. They are designed to work together — ALICE feeds CRAFTS, CRAFTS feeds SPARK, BRANDS provides strategy to all.")

# ── Slide 7: Five Agents Overview ───────────────────────────
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.65),
         "Five Purpose-Led Agents Cover the Full Marketing Lifecycle",
         font_size=26, bold=True, color=NAVY)
add_text(slide, Inches(0.6), Inches(0.95), Inches(12), Inches(0.4),
         "Each agent targets a specific systemic gap with AI-native capabilities.",
         font_size=13, color=NEAR_BLACK)

data = [
    ["Agent", "Full Name", "Core Job"],
    ["ALICE", "AI-Led Intelligent Creative Engine", "Brief optimization, concept scoring, persona-targeted creative at scale"],
    ["BRANDS", "Brand Strategy Planning System", "Global brand plan, regional localization, market archetype navigation"],
    ["CRAFTS", "Content Lifecycle Management Agent", "Modular assets, MLR acceleration, pre-launch content testing"],
    ["SPARK", "Intelligent Customer Engagement Agent", "NBA, HCP segmentation, omnichannel personalization, patient engagement"],
    ["ACCESS", "AI-Powered Market Access Agent", "Competitive intelligence, HTA dossiers, patient support automation"],
]
add_table(slide, Inches(0.6), Inches(1.5), Inches(12), Inches(3.6),
          rows=6, cols=3, data=data,
          col_widths=[Inches(1.5), Inches(3.5), Inches(7.0)], font_size=12)
add_callout_bar(slide, "These are not separate tools — they are a connected intelligence ecosystem.", y=Inches(5.3))
add_footer(slide, 7)
add_notes(slide, "Walk the table row by row. Emphasize that each agent name is memorable by design: ALICE creates, BRANDS strategizes, CRAFTS produces, SPARK engages, ACCESS penetrates markets. Draw the data flow connections verbally as you present.")

# ── Slide 8: Section 3 divider ──────────────────────────────
slide = add_section_divider(prs, "03", "Capability Gap Analysis", "Current vs future state — 20 capabilities across 5 agents")
add_notes(slide, "Set expectations: the current state column shows 'Investigation for Validation' for all 20 capabilities. This is intentional — we do not yet have a confirmed tool inventory for EPD. The validation workplan in section 4 fixes this.")

# ── Slide 9: ALICE Gap Table ─────────────────────────────────
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.55),
         "ALICE — Creative Excellence: Capability Gap",
         font_size=24, bold=True, color=NAVY)
add_text(slide, Inches(0.6), Inches(0.9), Inches(12), Inches(0.35),
         "Creative production must shift from agency-dependent to AI-accelerated.",
         font_size=13, color=NEAR_BLACK)
data = [
    ["#", "Capability", "Current State", "Future Tool", "Status"],
    ["1", "Creative Generation", "Investigation for Validation", "Adobe Firefly / GenStudio", "TBD"],
    ["2", "Brief Intelligence", "Investigation for Validation", "Persado", "TBD"],
    ["3", "Copy & Claim Generation", "Investigation for Validation", "Writer.com", "TBD"],
    ["4", "Creative Ops & Workflow", "Investigation for Validation", "Adobe Workfront", "TBD"],
]
add_table(slide, Inches(0.6), Inches(1.35), Inches(12), Inches(2.5),
          rows=5, cols=5, data=data,
          col_widths=[Inches(0.5), Inches(2.5), Inches(2.8), Inches(3.5), Inches(2.7)], font_size=11)
add_text(slide, Inches(0.6), Inches(4.1), Inches(12), Inches(0.35),
         "Known pain points: Manual briefs  |  Agency-dependent  |  4–6 revision cycles  |  Limited localization",
         font_size=11, italic=True, color=LIGHT_GRAY)
add_callout_bar(slide, "ALICE transforms a 3–5 day brief cycle into 1–2 hours. The gap here is urgent.", y=Inches(4.7))
add_footer(slide, 9)
add_notes(slide, "The 'Investigation for Validation' status is not a gap in our analysis — it is the first action item. We need to confirm what Abbott EPD already licenses before recommending any new tools. Persado and Writer.com are market leaders in pharma-compliant copy generation.")

# ── Slide 10: BRANDS Gap Table ───────────────────────────────
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.55),
         "BRANDS — Brand Strategy: Capability Gap",
         font_size=24, bold=True, color=NAVY)
add_text(slide, Inches(0.6), Inches(0.9), Inches(12), Inches(0.35),
         "From intuition-based annual planning to real-time, data-driven strategy.",
         font_size=13, color=NEAR_BLACK)
data = [
    ["#", "Capability", "Current State", "Future Tool", "Status"],
    ["5", "Market Intelligence", "Investigation for Validation", "Deepsights", "TBD"],
    ["6", "Social Listening", "Investigation for Validation", "Brandwatch / Synthesio", "TBD"],
    ["7", "Commercial Strategy Modeling", "Investigation for Validation", "McKinsey Lilli / ZS ZAIDYN", "TBD"],
    ["8", "Synthetic Research / Digital Twins", "Investigation for Validation", "Synthetic Audiences", "TBD"],
]
add_table(slide, Inches(0.6), Inches(1.35), Inches(12), Inches(2.5),
          rows=5, cols=5, data=data,
          col_widths=[Inches(0.5), Inches(2.7), Inches(2.8), Inches(3.3), Inches(2.7)], font_size=11)
add_text(slide, Inches(0.6), Inches(4.1), Inches(12), Inches(0.35),
         "Known pain points: Static insights  |  2–3 month workshops  |  Annual plans  |  Intuition-based decisions",
         font_size=11, italic=True, color=LIGHT_GRAY)
add_callout_bar(slide, "Synthetic audiences are a top 2026 pharma trend — message testing without traditional recruitment timelines.", y=Inches(4.7))
add_footer(slide, 10)
add_notes(slide, "The biggest unlock here is replacing 2–3 month workshop cycles with continuous AI-driven insight generation. Deepsights (formerly Greenbook AI) is the market leader for pharma brand strategy synthesis.")

# ── Slide 11: CRAFTS Gap Table ───────────────────────────────
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.55),
         "CRAFTS — Content Excellence: Capability Gap",
         font_size=24, bold=True, color=NAVY)
add_text(slide, Inches(0.6), Inches(0.9), Inches(12), Inches(0.35),
         "MLR must become an integrated AI enabler — not a manual gatekeeper.",
         font_size=13, color=NEAR_BLACK)
data = [
    ["#", "Capability", "Current State", "Future Tool", "Status"],
    ["9", "MLR Review & Compliance", "Investigation for Validation", "Veeva Vault PromoMats + AI", "TBD"],
    ["10", "Compliance Detection", "Investigation for Validation", "Indegene AI Compliance Engine", "TBD"],
    ["11", "Modular Content Creation", "Investigation for Validation", "Writer.com / Adobe AEM", "TBD"],
    ["12", "Content Testing & Optimization", "Investigation for Validation", "Optimizely / VWO AI", "TBD"],
]
add_table(slide, Inches(0.6), Inches(1.35), Inches(12), Inches(2.5),
          rows=5, cols=5, data=data,
          col_widths=[Inches(0.5), Inches(2.7), Inches(2.8), Inches(3.3), Inches(2.7)], font_size=11)
add_text(slide, Inches(0.6), Inches(4.1), Inches(12), Inches(0.35),
         "Known pain points: Slow MLR reviews  |  Manual coordination  |  Linear rollouts  |  One-size-fits-all",
         font_size=11, italic=True, color=LIGHT_GRAY)
add_callout_bar(slide, "Veeva PromoMats AI Agents (Dec 2025): up to 75% MLR cycle time reduction. Available now.", y=Inches(4.7))
add_footer(slide, 11)
add_notes(slide, "Veeva PromoMats AI Agents launched December 2025 — Moderna is the first live customer. 38% of MLR is projected to be AI-driven by 2028. This is not future speculation — these tools are available today. The question is whether Abbott EPD already has a PromoMats license.")

# ── Slide 12: SPARK Gap Table ────────────────────────────────
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.55),
         "SPARK — Customer Engagement: Capability Gap",
         font_size=24, bold=True, color=NAVY)
add_text(slide, Inches(0.6), Inches(0.9), Inches(12), Inches(0.35),
         "From mass reach to intelligent, personalized HCP and patient journeys.",
         font_size=13, color=NEAR_BLACK)
data = [
    ["#", "Capability", "Current State", "Future Tool", "Status"],
    ["13", "Next-Best-Action (NBA)", "Investigation for Validation", "Aktana / PharmaForceIQ", "TBD"],
    ["14", "CRM & HCP Journey Orchestration", "Investigation for Validation", "Veeva Vault CRM AI Agents", "TBD"],
    ["15", "Patient Engagement", "Investigation for Validation", "Conversa Health", "TBD"],
    ["16", "Omnichannel Personalization", "Investigation for Validation", "Adobe Sensei / Marketing Cloud", "TBD"],
]
add_table(slide, Inches(0.6), Inches(1.35), Inches(12), Inches(2.5),
          rows=5, cols=5, data=data,
          col_widths=[Inches(0.5), Inches(2.9), Inches(2.8), Inches(3.3), Inches(2.5)], font_size=11)
add_text(slide, Inches(0.6), Inches(4.1), Inches(12), Inches(0.35),
         "Known pain points: Mass reach  |  Broad segments  |  Reactive planning  |  Disconnected data silos",
         font_size=11, italic=True, color=LIGHT_GRAY)
add_callout_bar(slide, "Aktana / PharmaForceIQ (merged Jan 2026): 36% NBRx lift, 100M+ field AI suggestions.", y=Inches(4.7))
add_footer(slide, 12)
add_notes(slide, "The NBA (Next-Best-Action) capability is the highest-ROI gap in the SPARK agent. Aktana and PharmaForceIQ merged in January 2026 — the combined platform has delivered 36% NBRx lift across pharma clients. This is the strongest ROI signal in the entire tool landscape.")

# ── Slide 13: ACCESS Gap Table ───────────────────────────────
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.55),
         "ACCESS — Market Access: Capability Gap",
         font_size=24, bold=True, color=NAVY)
add_text(slide, Inches(0.6), Inches(0.9), Inches(12), Inches(0.35),
         "From reactive payer response to proactive, AI-simulated access strategy.",
         font_size=13, color=NEAR_BLACK)
data = [
    ["#", "Capability", "Current State", "Future Tool", "Status"],
    ["17", "Competitive Intelligence", "Investigation for Validation", "IQVIA Market Edge AI", "TBD"],
    ["18", "HTA & Value Dossier", "Investigation for Validation", "Payer Sciences / ZS ZAIDYN Access", "TBD"],
    ["19", "Patient Support Programs", "Investigation for Validation", "ConnectiveRx AI Platform", "TBD"],
    ["20", "Regulatory & Access Compliance", "Investigation for Validation", "RegASK / Veripharm", "TBD"],
]
add_table(slide, Inches(0.6), Inches(1.35), Inches(12), Inches(2.5),
          rows=5, cols=5, data=data,
          col_widths=[Inches(0.5), Inches(2.7), Inches(2.8), Inches(3.6), Inches(2.4)], font_size=11)
add_text(slide, Inches(0.6), Inches(4.1), Inches(12), Inches(0.35),
         "Known pain points: Reactive payer response  |  Siloed data  |  Post-campaign analysis only",
         font_size=11, italic=True, color=LIGHT_GRAY)
add_callout_bar(slide, "Value dossier automation can compress HTA submission timelines from months to weeks.", y=Inches(4.7))
add_footer(slide, 13)
add_notes(slide, "Market access is often the last function to adopt AI — and often the highest ROI opportunity. HTA dossier automation and economic model simulation can dramatically compress timelines that today take months of manual work.")

# ── Slide 14: Section 4 divider ─────────────────────────────
slide = add_section_divider(prs, "04", "Validation Workplan", "What we need to discover before building")
add_notes(slide, "Frame this section as discipline, not delay. The fastest path to the right technology decisions is knowing what we already have. Buying redundant tools is the most common and expensive MarTech mistake.")

# ── Slide 15: Validation Workplan ───────────────────────────
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.55),
         "Before We Build, We Must Discover",
         font_size=26, bold=True, color=NAVY)
add_text(slide, Inches(0.6), Inches(0.9), Inches(12), Inches(0.35),
         "Six discovery actions unlock the full gap analysis and prevent duplicate investment.",
         font_size=13, color=NEAR_BLACK)
data = [
    ["Priority", "Action", "Owner", "Why It Matters"],
    ["P1", "Inventory current MarTech tools across EPD regions", "Marketing Ops", "Avoid buying what we already own"],
    ["P1", "Identify existing Veeva, Salesforce, Adobe licenses", "IT / Procurement", "Major platforms may already be licensed"],
    ["P1", "Map current MLR process and tooling", "Medical / Regulatory", "MLR is the highest-impact gap to close"],
    ["P2", "Assess CRM maturity (Veeva vs Salesforce vs other)", "Commercial IT", "CRM determines SPARK architecture"],
    ["P2", "Review existing analytics and data platforms", "Data & Analytics", "Data foundation drives all 5 agents"],
    ["P3", "Identify regional variation in tool usage", "Regional Marketing Leads", "Markets may differ significantly"],
]
add_table(slide, Inches(0.6), Inches(1.4), Inches(12), Inches(4.2),
          rows=7, cols=4, data=data,
          col_widths=[Inches(1.0), Inches(4.5), Inches(2.8), Inches(3.7)], font_size=11)
add_callout_bar(slide, "Validation unlocks mapping. Mapping unlocks architecture. Architecture unlocks procurement.", y=Inches(5.8))
add_footer(slide, 15)
add_notes(slide, "Assign P1 actions immediately. These three discovery activities are the critical path. Until we know what is already licensed, we cannot make defensible tool recommendations. Target 4 weeks to complete P1 items.")

# ── Slide 16: Section 5 divider ─────────────────────────────
slide = add_section_divider(prs, "05", "Next Steps", "Three actions to move from assessment to architecture")
add_notes(slide, "Close with clarity and urgency. These three actions have a clear sequence — each one unlocks the next.")

# ── Slide 17: Next Steps ─────────────────────────────────────
slide = add_action_cards_slide(
    prs,
    title="Three Actions to Move from Assessment to Architecture",
    actions=[
        (
            "1.  Complete the Validation Workplan",
            "Run tool inventory across EPD regions and confirm existing licenses for Veeva, Salesforce, and Adobe.",
            "Target: 4 weeks  |  P1 items: Marketing Ops, IT/Procurement, Medical/Regulatory",
            "Owner: EPD Marketing Ops + IT / Procurement"
        ),
        (
            "2.  Run Current State → Future State Capability Mapping",
            "Update gap analysis with validated current tools. Confirm which gaps are real vs already addressed.",
            "Target: 2 weeks post-validation  |  Produces: Updated gap analysis with confirmed tool inventory",
            "Owner: EPD Architect + Marketing Ops"
        ),
        (
            "3.  Build Integration & Target Architecture",
            "Design how the 5 agents connect, share data, and integrate with Abbott's existing technology stack.",
            "Target: 4 weeks post-mapping  |  Produces: Integration architecture + target architecture diagrams",
            "Owner: EPD Architect"
        ),
    ],
    closing_line="Disciplined discovery first. Architecture second. Procurement third. This sequence protects Abbott's investment.",
    page_num=17
)
add_notes(slide, "End by confirming owners in the room. Who owns the validation workplan? Who runs the capability mapping? Who owns the architecture? These three questions should have answers before the meeting ends.")

# ── Slide 18: Q&A ────────────────────────────────────────────
slide = add_qa_slide(
    prs,
    title="Questions This Deck Is Designed to Answer",
    questions=[
        ("What are the 5 AI agents?", "ALICE (Creative), BRANDS (Strategy), CRAFTS (Content/MLR), SPARK (Engagement), ACCESS (Market Access). Each closes a specific systemic gap."),
        ("What capabilities do we need?", "20 capabilities across 5 agents — covering creative, strategy, content, engagement, and market access."),
        ("What tools should we evaluate?", "Market leaders identified for each capability. Final recommendations depend on validation workplan outcomes."),
        ("Why is current state unknown?", "No confirmed tool inventory exists for EPD. The validation workplan is the first priority."),
        ("What are the next 3 actions?", "Validation (4 weeks) → Capability mapping (2 weeks) → Architecture (4 weeks)."),
    ],
    page_num=18
)
add_notes(slide, "Use this slide as a reference sheet. If questions come up during the presentation that aren't on this list, capture them as inputs for the validation workplan.")

# ── Save ─────────────────────────────────────────────────────
output_path = "/Users/GUNDLLX/learn-claude/projects/Marketing Future/EPD-Marketer-of-the-Future-Capability-Gap-Analysis-2026-05-05.pptx"
prs.save(output_path)
print(f"Saved: {output_path}")
print(f"Total slides: {len(prs.slides)}")
for i, slide in enumerate(prs.slides, 1):
    for shape in slide.shapes:
        if shape.has_text_frame:
            title_text = shape.text_frame.paragraphs[0].text.strip()
            if title_text:
                print(f"  Slide {i}: {title_text[:70]}")
                break
