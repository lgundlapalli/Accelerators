"""
CONSOLIDATED DECK: From AI-First Strategy to Transforming AI with People, Culture & Mindset
============================================================================================
Merges the Cultural Debt framing + Six Sources of Influence framework into one unified
presentation. Three storylines: Culture, Change Management, Leadership.

Uses the /pptx-generator skill's Abbott brand constants library.
"""

import sys
from pathlib import Path

# Import the shared Abbott brand library
sys.path.insert(0, str(Path.home() / '.claude/commands/pptx-generator/references'))
from abbott_brand_constants import *  # noqa: F403, F401

# Rename to avoid shadowing with local function calls
_prs = create_presentation()

pg = [0]  # page counter


def next_pg():
    pg[0] += 1
    return pg[0]


# ============================================================
# SLIDE 1: Title
# ============================================================
slide = add_title_slide(
    _prs,
    "From AI-First Strategy",
    "To Transforming AI with People, Culture & Mindset",
    tagline="Why AI initiatives fail \u2014 and how to fix the human system, not the technology",
    org_date="BTS-DTS Architecture  |  April 2026"
)
add_notes(slide, """OPENING:
"We have an AI-First strategy. The technology is powerful. But the data is clear: the vast majority of AI initiatives fail \u2014 and technology is almost never the reason. Today I want to show you what IS the reason, give you a diagnostic framework, and propose three concrete actions."

Don't read the slide. Set the room with conviction.

TRANSITION: "Let me give you the full picture in one slide."
""")

# ============================================================
# SLIDE 2: Executive Summary
# ============================================================
slide = _prs.slides.add_slide(_prs.slide_layouts[6])
p = next_pg()
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.6),
         "Executive Summary", font_size=32, color=NAVY)
add_text(slide, Inches(0.6), Inches(0.9), Inches(12), Inches(0.5),
         "AI-First is the right strategy. But strategy without cultural readiness produces investment without return.",
         font_size=14, color=NEAR_BLACK)

data = [
    ["The Problem", "The Root Cause", "The Path Forward"],
    ["70-85%", "Cultural Debt", "People, Culture & Mindset"],
    ["AI initiative failure rate. Technology is rarely the cause. The organization doesn\u2019t change.",
     "Accumulated resistance, misaligned incentives, and eroded trust that compound with every failed attempt.",
     "Three storylines \u2014 Culture, Change Management, and Leadership \u2014 addressed through the Six Sources of Influence framework."],
    ["What\u2019s failing", "What\u2019s compounding", "What works"],
    ["Not the models. Not the data. Not the platforms. The human system surrounding them.",
     "Each failure breeds cynicism and shadow processes. Second attempts face 3x higher resistance.",
     "Organizations that invest in cultural readiness before technology see 2-3x higher adoption and 10x faster behavioral change."],
]
add_table(slide, Inches(0.6), Inches(1.6), Inches(12), Inches(4.2), 5, 3, data,
          col_widths=[Inches(4), Inches(4), Inches(4)], font_size=11)

add_source(slide, "Sources: McKinsey (2023); Gartner (2024); MIT CISR (2024); Crucial Learning (2026); Shelly Palmer (2026)")
add_footer(slide, p)

add_notes(slide, """This is the "read only this slide" slide.

"Three columns: 70-85% failure rate \u2014 not technology. Cultural debt \u2014 it compounds. And the path forward: People, Culture & Mindset, diagnosed through a research-backed framework called Six Sources of Influence."

TRANSITION: "Here\u2019s what we\u2019ll cover."
""")

# ============================================================
# SLIDE 3: Agenda
# ============================================================
add_agenda_slide(_prs, "What We\u2019ll Decide Today", [
    ("01", "The Numbers", "Why 70-85% of AI initiatives fail \u2014 and technology isn\u2019t the reason"),
    ("02", "Cultural Debt", "The hidden force that compounds with every failed attempt"),
    ("03", "Six Sources of Influence", "A diagnostic framework for where adoption actually breaks"),
    ("04", "Three Storylines", "Culture, Change Management, and Leadership \u2014 the transformation opportunities"),
    ("05", "The Actions", "What we do this quarter to start paying down cultural debt"),
], next_pg())

# ============================================================
# SECTION 01: THE NUMBERS
# ============================================================
add_section_divider(_prs, "01", "The Numbers")

# Slide: Big Numbers
slide = add_big_numbers_slide(_prs,
    "70-85% of AI Initiatives Fail \u2014 Technology Isn\u2019t the Reason",
    "The technology works. The organization doesn\u2019t change.",
    [
        ("70-85%", "Fail to deliver\nexpected value", "Consistent across industries,\ncompany sizes, and geographies"),
        ("<15%", "Failures attributed\nto technology", "Models work. Infrastructure works.\nThe organization doesn\u2019t adopt."),
        ("#1 Cause", "Organizational and\ncultural resistance", "Change resistance, skill gaps,\nmisaligned incentives, lack of trust"),
        ("$4.6T", "Projected global AI\ninvestment by 2027", "The majority at risk of\ndelivering no return"),
    ],
    "AI tools are advancing rapidly. Human systems are not. The gap is where value dies.",
    "Sources: McKinsey (2023); BCG (2024); IDC (2025); HBR (2025)",
    next_pg()
)
add_notes(slide, """Walk left to right. Let each number land.

70-85%: "Seven to eight out of ten AI initiatives don\u2019t deliver."
<15%: "Less than 15% of failures are technology. The models work."
#1 Cause: "Organizational and cultural resistance. People."
$4.6T: "The stakes: $4.6 trillion at risk."

Point to the callout bar. Pause.

TRANSITION: "If it\u2019s not technology, what is it?"
""")

# ============================================================
# SECTION 02: CULTURAL DEBT
# ============================================================
add_section_divider(_prs, "02", "Cultural Debt", "The hidden force behind the failures")

# Slide: Definition (Side-by-Side)
slide = add_side_by_side_slide(_prs,
    "Cultural Debt Compounds Like Technical Debt \u2014 But No One Tracks It",
    "Technical Debt",
    [
        "Shortcuts in code that create future rework",
        "Visible in code reviews, build times, bug rates",
        "Tracked, measured, budgeted for",
        "Compounds as system complexity grows",
        "Fix: refactor the code",
    ],
    "Cultural Debt",
    [
        "Shortcuts in change management that create future resistance",
        "Invisible until the next initiative stalls",
        "Untracked, unmeasured, unbudgeted",
        "Compounds as organizational cynicism grows",
        "Fix: rebuild trust, realign incentives, invest in people",
    ],
    "Cultural debt accrues every time an organization deploys technology without investing in the humans who must adopt it.",
    next_pg()
)
add_notes(slide, """Definitional slide \u2014 creates the vocabulary.

"Everyone here understands technical debt. Cultural debt is the parallel. But it\u2019s invisible, unmeasured, and unbudgeted."

Pause on row 3: "Tracked vs. untracked. That\u2019s the core problem."

TRANSITION: "And it compounds."
""")

# Slide: Compounding Cycle
slide = _prs.slides.add_slide(_prs.slide_layouts[6])
p = next_pg()
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.7),
         "Every Failed AI Initiative Makes the Next One Harder", font_size=28, color=NAVY)

cycle_items = [
    (Inches(1.5), Inches(1.8), "AI Initiative\nLaunched"),
    (Inches(5.0), Inches(1.8), "Adoption\nStalls"),
    (Inches(8.5), Inches(1.8), "Leadership\nDeclares Failure"),
    (Inches(8.5), Inches(3.8), "Cynicism\nDeepens"),
    (Inches(5.0), Inches(3.8), "Shadow Processes\nHarden"),
    (Inches(1.5), Inches(3.8), "Next Initiative Faces\nHigher Resistance"),
]
for x, y, text in cycle_items:
    add_box(slide, x, y, Inches(2.8), Inches(1.2), LAVENDER)
    add_text(slide, x + Inches(0.1), y + Inches(0.15), Inches(2.6), Inches(0.9),
             text, font_size=14, bold=True, color=NAVY, alignment=PP_ALIGN.CENTER)

arrows = [
    (Inches(4.3), Inches(2.2), "\u2192"), (Inches(7.8), Inches(2.2), "\u2192"),
    (Inches(10.2), Inches(3.2), "\u2193"), (Inches(7.8), Inches(4.2), "\u2190"),
    (Inches(4.3), Inches(4.2), "\u2190"), (Inches(1.8), Inches(3.2), "\u2191"),
]
for x, y, arrow in arrows:
    add_text(slide, x, y, Inches(0.6), Inches(0.5),
             arrow, font_size=28, bold=True, color=NAVY, alignment=PP_ALIGN.CENTER)

add_box(slide, Inches(0.6), Inches(5.3), Inches(12), Inches(1.3), SOFT_LAVENDER)
stages = [
    ("Cycle 1:", "Healthy skepticism \u2014 \u201cLet\u2019s see if this works\u201d"),
    ("Cycle 2:", "Active resistance \u2014 \u201cWe tried this before\u201d"),
    ("Cycle 3:", "Organizational antibodies \u2014 \u201cAI doesn\u2019t work here\u201d"),
    ("Cycle 4:", "Structural inability \u2014 the best people have stopped engaging"),
]
for i, (label, desc) in enumerate(stages):
    y = Inches(5.4) + Inches(i * 0.28)
    add_text(slide, Inches(1), y, Inches(1.5), Inches(0.3),
             label, font_size=11, bold=True, color=NAVY)
    add_text(slide, Inches(2.5), y, Inches(9.5), Inches(0.3),
             desc, font_size=11, color=NEAR_BLACK)
add_footer(slide, p)

add_notes(slide, """Walk the cycle slowly. Each loop is worse.

By Cycle 3, resistance is unconscious \u2014 "organizational antibodies."
By Cycle 4, the best people have stopped engaging entirely.

TRANSITION: "So how do we diagnose exactly where it\u2019s breaking?"
""")

# ============================================================
# SECTION 03: SIX SOURCES OF INFLUENCE
# ============================================================
add_section_divider(_prs, "03", "Six Sources of Influence", "A diagnostic framework for where adoption breaks")

# Slide: The Framework Grid
slide = _prs.slides.add_slide(_prs.slide_layouts[6])
p = next_pg()
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.6),
         "Behavior Is Shaped by Six Forces \u2014 Miss One, Adoption Stalls", font_size=24, color=NAVY)
add_text(slide, Inches(0.6), Inches(0.85), Inches(12), Inches(0.4),
         "Leaders who engage all 6 sources are 10x more likely to drive rapid behavioral change.",
         font_size=13, bold=True, color=MED_BLUE)

# Headers
add_box(slide, Inches(2.6), Inches(1.5), Inches(5), Inches(0.5), NAVY)
add_text(slide, Inches(2.6), Inches(1.5), Inches(5), Inches(0.5),
         "MOTIVATION", font_size=14, bold=True, color=WHITE, alignment=PP_ALIGN.CENTER)
add_box(slide, Inches(7.8), Inches(1.5), Inches(5), Inches(0.5), NAVY)
add_text(slide, Inches(7.8), Inches(1.5), Inches(5), Inches(0.5),
         "ABILITY", font_size=14, bold=True, color=WHITE, alignment=PP_ALIGN.CENTER)

row_labels = [("PERSONAL", Inches(2.2)), ("SOCIAL", Inches(3.8)), ("STRUCTURAL", Inches(5.4))]
for label, y in row_labels:
    add_box(slide, Inches(0.6), y, Inches(1.8), Inches(1.4), NAVY)
    add_text(slide, Inches(0.6), y + Inches(0.4), Inches(1.8), Inches(0.5),
             label, font_size=11, bold=True, color=WHITE, alignment=PP_ALIGN.CENTER)

sources = [
    (Inches(2.6), Inches(2.2), "Source 1: Personal Motivation",
     "Do people WANT to use AI?\nFear of replacement, loss of identity, distrust"),
    (Inches(7.8), Inches(2.2), "Source 2: Personal Ability",
     "Do people KNOW HOW to use AI?\nPrompting skills, output validation, workflow integration"),
    (Inches(2.6), Inches(3.8), "Source 3: Social Motivation",
     "Do peers and leaders MODEL AI use?\nOr is adoption seen as optional / risky?"),
    (Inches(7.8), Inches(3.8), "Source 4: Social Ability",
     "Do teams SUPPORT each other in adoption?\nOr is everyone figuring it out alone?"),
    (Inches(2.6), Inches(5.4), "Source 5: Structural Motivation",
     "Do INCENTIVES reward AI adoption?\nOr do they reward the old way of working?"),
    (Inches(7.8), Inches(5.4), "Source 6: Structural Ability",
     "Does the ENVIRONMENT make AI easy?\nOr is AI bolted on outside core workflows?"),
]

for x, y, title, desc in sources:
    add_box(slide, x, y, Inches(5), Inches(1.4), LAVENDER)
    add_text(slide, x + Inches(0.2), y + Inches(0.1), Inches(4.6), Inches(0.4),
             title, font_size=11, bold=True, color=NAVY)
    add_text(slide, x + Inches(0.2), y + Inches(0.5), Inches(4.6), Inches(0.8),
             desc, font_size=10, color=NEAR_BLACK)
add_footer(slide, p)

add_notes(slide, """THIS IS THE KEY SLIDE. Spend 60-90 seconds.

Walk the grid top to bottom:
- PERSONAL: "Do they want to? Do they know how?"
- SOCIAL: "Do the people around them model it? Do they support each other?"
- STRUCTURAL: "Do incentives reward it? Does the environment make it easy?"

"If even ONE source is misaligned, adoption stalls. Training alone covers Source 2. You still have five pulling against you."

TRANSITION: "Now let me show you where cultural debt hides in each source."
""")

# Slide: Diagnosis Table
slide = _prs.slides.add_slide(_prs.slide_layouts[6])
p = next_pg()
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.6),
         "Cultural Debt Shows Up in Every Source \u2014 Here\u2019s Where to Look", font_size=24, color=NAVY)

data = [
    ["Source", "The Cultural Debt", "What It Looks Like", "Signal"],
    ["1. Personal\nMotivation", "Fear and distrust",
     "\u201cAI will replace my role\u201d \u2014 silent resistance", "Low voluntary usage despite access"],
    ["2. Personal\nAbility", "Skill gaps disguised\nas skepticism",
     "\u201cAI isn\u2019t reliable\u201d = \u201cI don\u2019t know how\u201d", "Inconsistent quality across teams"],
    ["3. Social\nMotivation", "No visible role models",
     "No leader publicly using AI in decisions", "\u201cPromising but premature\u201d verdicts"],
    ["4. Social\nAbility", "No peer support\nstructure",
     "Everyone figures it out alone", "Isolated pockets, no scaling"],
    ["5. Structural\nMotivation", "Incentives reward\nthe old way",
     "Promotions based on pre-AI metrics", "Rational sabotage by process owners"],
    ["6. Structural\nAbility", "AI bolted on,\nnot embedded",
     "Tools outside core workflows", "High license cost, low actual usage"],
]
add_table(slide, Inches(0.6), Inches(1.1), Inches(12.1), Inches(5.0), 7, 4, data,
          col_widths=[Inches(1.8), Inches(2.5), Inches(4.5), Inches(3.3)], font_size=11)

add_box(slide, Inches(0.6), Inches(6.3), Inches(12), Inches(0.5), LAVENDER)
add_text(slide, Inches(1), Inches(6.35), Inches(11), Inches(0.4),
         "If even one source is misaligned, adoption stalls. If several are misaligned, it fails entirely.",
         font_size=13, bold=True, color=NAVY)
add_footer(slide, p)

add_notes(slide, """Walk each row. Make it concrete.

Source 5 (Structural Motivation) is the big one: "Incentives reward the old way. Process owners whose authority depends on current workflows have every rational reason to slow adoption."

Ask: "How many of these are misaligned in your organization right now?"

TRANSITION: "The good news: these six sources map directly to three storylines we can act on."
""")

# ============================================================
# SECTION 04: THREE STORYLINES
# ============================================================
add_section_divider(_prs, "04", "Three Storylines", "Culture, Change Management, and Leadership")

# Slide: The Three Storylines Overview
slide = _prs.slides.add_slide(_prs.slide_layouts[6])
p = next_pg()
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.7),
         "Three Storylines Transform AI-First Strategy into AI-First Reality", font_size=26, color=NAVY)
add_text(slide, Inches(0.6), Inches(0.9), Inches(12), Inches(0.4),
         "Each storyline addresses specific sources of influence where cultural debt accumulates.",
         font_size=14, color=NEAR_BLACK)

# Three columns
storylines = [
    ("Culture", "Sources 1 & 2", Inches(0.6),
     "From permission culture\nto experimentation culture",
     ["\u2022 Psychological safety to experiment",
      "\u2022 Reframe AI as multiplier, not threat",
      "\u2022 Build skills through practice, not theater",
      "\u2022 Celebrate learning from failure"],
     "Addresses: Fear, distrust,\nand skill gaps"),
    ("Change Management", "Sources 3 & 4", Inches(4.6),
     "From 2-of-6-source programs\nto full Six Sources approach",
     ["\u2022 Co-design adoption with users",
      "\u2022 Create cross-functional AI councils",
      "\u2022 Build peer support networks",
      "\u2022 Measure adoption, not deployment"],
     "Addresses: No role models,\nno peer support, no scaling"),
    ("Leadership", "Sources 5 & 6", Inches(8.6),
     "From sponsorship-in-committee\nto visible, active modeling",
     ["\u2022 Executives use tools publicly",
      "\u2022 Tie adoption to promotion criteria",
      "\u2022 Embed AI into core workflows",
      "\u2022 Redesign incentives for new behaviors"],
     "Addresses: Misaligned incentives,\nAI bolted on, invisible leadership"),
]

for title, sources_label, x, shift, bullets, addresses in storylines:
    add_box(slide, x, Inches(1.5), Inches(3.8), Inches(4.8), LAVENDER)
    add_text(slide, x + Inches(0.2), Inches(1.55), Inches(3.4), Inches(0.35),
             title, font_size=20, bold=True, color=NAVY)
    add_text(slide, x + Inches(0.2), Inches(1.9), Inches(3.4), Inches(0.3),
             sources_label, font_size=10, bold=True, color=MED_BLUE)
    add_box(slide, x + Inches(0.15), Inches(2.3), Inches(3.5), Inches(0.65), SOFT_LAVENDER)
    add_text(slide, x + Inches(0.25), Inches(2.35), Inches(3.3), Inches(0.55),
             shift, font_size=10, bold=True, color=NAVY)
    for i, bullet in enumerate(bullets):
        add_text(slide, x + Inches(0.2), Inches(3.1) + Inches(i * 0.4), Inches(3.4), Inches(0.35),
                 bullet, font_size=11, color=NEAR_BLACK)
    add_text(slide, x + Inches(0.2), Inches(4.8), Inches(3.4), Inches(0.5),
             addresses, font_size=10, italic=True, color=MED_BLUE)

add_box(slide, Inches(0.6), Inches(6.5), Inches(12), Inches(0.5), NAVY)
add_text(slide, Inches(1), Inches(6.55), Inches(11), Inches(0.4),
         "AI-First is the technology strategy. People, Culture & Mindset is the adoption strategy. You need both.",
         font_size=13, bold=True, color=WHITE, italic=True)
add_footer(slide, p)

add_notes(slide, """THIS IS THE PIVOT SLIDE \u2014 where the two framings merge.

"The Six Sources framework reveals three natural storylines:
- CULTURE addresses the personal sources \u2014 fear, skills, experimentation safety.
- CHANGE MANAGEMENT addresses the social sources \u2014 role models, peer support, community.
- LEADERSHIP addresses the structural sources \u2014 incentives, environment, visible commitment."

Read the bottom bar: "AI-First is the technology strategy. People, Culture & Mindset is the adoption strategy."

TRANSITION: "Let me show you what each storyline looks like in practice."
""")

# Slide: Storyline 1 \u2014 Culture
slide = _prs.slides.add_slide(_prs.slide_layouts[6])
p = next_pg()
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.7),
         "Culture: From Permission Culture to Experimentation Culture", font_size=26, color=NAVY)
add_text(slide, Inches(0.6), Inches(0.9), Inches(12), Inches(0.4),
         "Addresses Personal Motivation (Source 1) and Personal Ability (Source 2)",
         font_size=13, bold=True, color=MED_BLUE)

data = [
    ["From (Cultural Debt)", "To (Cultural Infrastructure)", "How (Research-Proven)"],
    ["AI as threat \u2014 \u201cthis will replace me\u201d",
     "AI as multiplier \u2014 \u201cthis makes me better\u201d",
     "Share stories where AI = strategic advantage. Energy firm: AI anomaly detection reframed from \u201ctool\u201d to \u201csafeguard\u201d"],
    ["Skills theater \u2014 attend training, return to old habits",
     "Apprenticeship \u2014 learn by doing, build real capability",
     "Hands-on workshops with real scenarios. Services firm: confidence and adoption up in one quarter"],
    ["Permission culture \u2014 wait for approval to experiment",
     "Experimentation culture \u2014 safe to try, safe to fail",
     "Google Project Aristotle: psychological safety is the #1 predictor of team effectiveness"],
    ["Fear of failure \u2014 mistakes are career risk",
     "Learning from failure \u2014 mistakes are data",
     "Celebrate experiments that didn\u2019t work. Name what was learned. Normalize \u201cI tried X and it didn\u2019t work because Y\u201d"],
]
add_table(slide, Inches(0.6), Inches(1.4), Inches(12), Inches(4.0), 5, 3, data,
          col_widths=[Inches(3.5), Inches(3.5), Inches(5)], font_size=11)

add_callout_bar(slide,
    "Culture isn\u2019t a soft topic. It\u2019s the difference between teams who experiment and teams who hide.",
    y=Inches(5.6))
add_footer(slide, p)

add_notes(slide, """Walk each row. The "From/To/How" structure makes it actionable.

"Skills theater is the most common trap. Everyone went to the AI training. Nobody changed how they work Monday morning. The fix is apprenticeship \u2014 pair people with AI on real work."

"The energy firm story is powerful: when AI anomaly detection prevented millions in equipment downtime, the narrative shifted from 'experimental tool' to 'strategic safeguard.' Stories change identity."
""")

# Slide: Storyline 2 \u2014 Change Management
slide = _prs.slides.add_slide(_prs.slide_layouts[6])
p = next_pg()
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.7),
         "Change Management: From 2-of-6 Source Programs to Full Adoption Strategy", font_size=24, color=NAVY)
add_text(slide, Inches(0.6), Inches(0.9), Inches(12), Inches(0.4),
         "Addresses Social Motivation (Source 3) and Social Ability (Source 4)",
         font_size=13, bold=True, color=MED_BLUE)

data = [
    ["From (Cultural Debt)", "To (Cultural Infrastructure)", "How (Research-Proven)"],
    ["Traditional change management \u2014 covers\n2 of 6 sources (training + communication)",
     "Six Sources approach \u2014 all 6 aligned",
     "Traditional CM has a 70% failure rate. The missing 4 sources are exactly where adoption stalls."],
    ["No visible role models \u2014 adoption\nfelt optional or risky",
     "Respected leaders publicly model AI use\nin real decisions",
     "Retail org: regional leaders using AI forecasts shifted adoption from \u201coptional\u201d to \u201chow high performers operate\u201d"],
    ["Everyone figures it out alone \u2014\nno shared practices, no community",
     "Cross-functional AI councils and peer\nsupport networks",
     "Manufacturing org: compliance + business heads reviewing AI together reduced fear, increased trust, accelerated adoption"],
    ["Measure deployment, not adoption \u2014\nteams ship models no one uses",
     "Measure adoption and impact \u2014\ntime-to-value, not time-to-production",
     "Microsoft AI transformation: shifted KPIs from deployment to outcome \u2014 adoption jumped 40%"],
]
add_table(slide, Inches(0.6), Inches(1.4), Inches(12), Inches(4.2), 5, 3, data,
          col_widths=[Inches(3.5), Inches(3.5), Inches(5)], font_size=10)

add_callout_bar(slide,
    "Change management isn\u2019t failing. It\u2019s incomplete. Covering 2 of 6 sources is like running a 6-cylinder engine on 2 spark plugs.",
    y=Inches(5.8))
add_footer(slide, p)

add_notes(slide, """This is the "upgrade your change management" slide.

"Traditional change management covers communication and training \u2014 Sources 2 and 4. That\u2019s why it has a 70% failure rate. The missing four sources are where adoption actually stalls."

The Microsoft stat lands: "They shifted KPIs from 'models deployed' to 'business outcomes improved.' Adoption jumped 40%. What gets measured gets done."
""")

# Slide: Storyline 3 \u2014 Leadership
slide = _prs.slides.add_slide(_prs.slide_layouts[6])
p = next_pg()
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.7),
         "Leadership: From Sponsorship-in-Committee to Visible, Active Modeling", font_size=24, color=NAVY)
add_text(slide, Inches(0.6), Inches(0.9), Inches(12), Inches(0.4),
         "Addresses Structural Motivation (Source 5) and Structural Ability (Source 6)",
         font_size=13, bold=True, color=MED_BLUE)

data = [
    ["From (Cultural Debt)", "To (Cultural Infrastructure)", "How (Research-Proven)"],
    ["Incentives reward the old way \u2014\npromotions based on pre-AI metrics",
     "Adoption tied to promotion criteria \u2014\nresponsible AI use is a leadership expectation",
     "Financial services firm: incorporated responsible AI use into promotion criteria. Adoption became a career advantage, not a risk."],
    ["AI bolted on \u2014 exists outside\ncore workflows, requires extra steps",
     "AI embedded \u2014 integrated into the tools\npeople already use, every day",
     "Healthcare system: AI risk alerts embedded in EMR workflow, requiring review before chart close. Adoption became automatic."],
    ["Sponsorship lives in a steering committee \u2014\ndoesn\u2019t reach the teams doing the work",
     "Executives use the tools publicly, share\nfailures openly, model the behavior",
     "MIT CISR: executive engagement is the strongest predictor of digital transformation success. Permission flows downward."],
    ["\u201cBureaucratic antibodies\u201d \u2014 narrow scope,\nexpand criteria, declare \u201cpremature\u201d",
     "Structural redesign \u2014 remove friction,\nredesign processes around AI capability",
     "Ask: \u201cWould this step exist if we built from scratch?\u201d If not, it\u2019s cultural debt encoded in process."],
]
add_table(slide, Inches(0.6), Inches(1.4), Inches(12), Inches(4.2), 5, 3, data,
          col_widths=[Inches(3.5), Inches(3.5), Inches(5)], font_size=10)

add_callout_bar(slide,
    "If you\u2019re asking 2026 technology to operate inside a 2019 culture, the culture will win every time. \u2014 Shelly Palmer",
    y=Inches(5.8))
add_footer(slide, p)

add_notes(slide, """This is the "leadership accountability" slide.

"Source 5 is the most lethal: incentives reward the old way. Process owners have every rational reason to slow adoption. Palmer calls them 'bureaucratic antibodies' \u2014 they\u2019re not saboteurs, they\u2019re rational actors."

"The healthcare example is the gold standard for Source 6: embed AI into the existing workflow so adoption becomes automatic, not optional."

Read the Palmer quote. Let it land.
""")

# ============================================================
# SECTION 05: THE ACTIONS
# ============================================================
add_section_divider(_prs, "05", "The Actions", "What we do this quarter")

# Slide: Urgency
slide = _prs.slides.add_slide(_prs.slide_layouts[6])
p = next_pg()
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.7),
         "Cultural Debt Grows Quarterly \u2014 Every Delay Compounds the Cost", font_size=28, color=NAVY)

timeline = [
    ("Quarter 1", "Skepticism", "\u201cLet\u2019s wait and see\u201d", "Low cost to address", LAVENDER),
    ("Quarter 2", "Resistance", "\u201cThis didn\u2019t work last time\u201d", "Moderate cost", SOFT_LAVENDER),
    ("Quarter 4", "Antibodies", "\u201cAI isn\u2019t for us\u201d", "High cost \u2014 visible reset", LIGHT_ORANGE),
    ("Year 2", "Structural Lock-in", "Best people stopped engaging", "Requires org redesign", LIGHT_PEACH),
]
for i, (period, stage, quote, cost, color) in enumerate(timeline):
    x = Inches(0.6) + Inches(i * 3.1)
    add_box(slide, x, Inches(1.5), Inches(2.8), Inches(3.5), color)
    add_text(slide, x + Inches(0.2), Inches(1.6), Inches(2.4), Inches(0.4),
             period, font_size=14, bold=True, color=NAVY, alignment=PP_ALIGN.CENTER)
    add_text(slide, x + Inches(0.2), Inches(2.1), Inches(2.4), Inches(0.5),
             stage, font_size=22, bold=True, color=NAVY, alignment=PP_ALIGN.CENTER)
    add_text(slide, x + Inches(0.2), Inches(2.8), Inches(2.4), Inches(0.5),
             quote, font_size=12, italic=True, color=NEAR_BLACK, alignment=PP_ALIGN.CENTER)
    add_text(slide, x + Inches(0.2), Inches(3.6), Inches(2.4), Inches(0.5),
             cost, font_size=11, bold=True, color=MED_BLUE, alignment=PP_ALIGN.CENTER)

for i in range(3):
    x = Inches(3.4) + Inches(i * 3.1)
    add_text(slide, x, Inches(2.5), Inches(0.6), Inches(0.5),
             "\u2192", font_size=32, bold=True, color=NAVY, alignment=PP_ALIGN.CENTER)

add_box(slide, Inches(0.6), Inches(5.4), Inches(12), Inches(1.0), NAVY)
add_text(slide, Inches(1), Inches(5.5), Inches(11), Inches(0.35),
         "The math is simple:", font_size=14, color=LIGHT_NAVY)
add_text(slide, Inches(1), Inches(5.9), Inches(11), Inches(0.4),
         "Addressing cultural debt in Q1 costs a leadership conversation. Addressing it in Year 2 costs a transformation program.",
         font_size=16, bold=True, color=WHITE)
add_footer(slide, p)

add_notes(slide, """Urgency slide. Walk left to right. Colors darken.

"Every quarter unaddressed, the cost roughly doubles. Not because the problem gets harder \u2014 because the cynicism gets deeper."

TRANSITION: "Three actions, mapped to the three storylines."
""")

# Slide: Three Actions mapped to storylines
slide = _prs.slides.add_slide(_prs.slide_layouts[6])
p = next_pg()
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.7),
         "Three Actions This Quarter \u2014 One Per Storyline", font_size=28, color=NAVY)

actions = [
    ("1. Culture: Audit the Cultural Balance Sheet (Sources 1 & 2)",
     "Run a cultural readiness assessment before the next AI investment. Name the debt. Map the five failure patterns.",
     "Survey team sentiment on AI. Map the last 3 failed initiatives. Score against the Cultural Debt Assessment Framework.",
     "Executive Sponsor + HR  |  Within 30 days"),
    ("2. Change Management: Realign the Scorecard (Sources 3 & 4)",
     "Change how you measure AI success from \u201cdeployed\u201d to \u201cadopted and delivering value.\u201d Create peer support structures.",
     "Rewrite KPIs for the current AI portfolio. Launch a cross-functional AI council. Add adoption and outcome metrics.",
     "Business Unit Leads + Transformation Office  |  Within 30 days"),
    ("3. Leadership: Make It Visible (Sources 5 & 6)",
     "Executives use the tools publicly, share what they learned, and tie adoption to promotion criteria.",
     "One executive shares an AI experiment at the next all-hands. Incorporate AI use into next performance cycle.",
     "C-Suite + HR  |  Next all-hands + next performance cycle"),
]

for i, (title, desc, detail, owner) in enumerate(actions):
    y = Inches(1.2) + Inches(i * 1.65)
    color = LAVENDER if i % 2 == 0 else SOFT_LAVENDER
    add_box(slide, Inches(0.6), y, Inches(12), Inches(1.45), color)
    add_text(slide, Inches(1), y + Inches(0.05), Inches(11), Inches(0.35),
             title, font_size=14, bold=True, color=NAVY)
    add_text(slide, Inches(1), y + Inches(0.4), Inches(11), Inches(0.35),
             desc, font_size=12, color=NEAR_BLACK)
    add_text(slide, Inches(1), y + Inches(0.75), Inches(11), Inches(0.35),
             detail, font_size=11, color=NEAR_BLACK)
    add_text(slide, Inches(1), y + Inches(1.1), Inches(11), Inches(0.3),
             owner, font_size=10, bold=True, color=MED_BLUE)

add_box(slide, Inches(0.6), Inches(6.2), Inches(12), Inches(0.55), NAVY)
add_text(slide, Inches(1), Inches(6.25), Inches(11), Inches(0.45),
         "The question is not whether you\u2019ve invested in AI. The question is whether you\u2019ve invested in the human system required to make it work.",
         font_size=13, bold=True, color=WHITE, italic=True)
add_footer(slide, p)

add_notes(slide, """End with action. Each action maps to one storyline and two sources.

"Culture: Audit the debt. Name it. If you can\u2019t measure it, you can\u2019t fix it."
"Change Management: Change the metric. What gets measured gets done."
"Leadership: Model the behavior. Until the C-suite uses the tools publicly, everything else is policy without practice."

Read the closing line. Pause.

Ask: "Who in this room owns the first one?"
""")

# Slide: Next Steps
slide = _prs.slides.add_slide(_prs.slide_layouts[6])
p = next_pg()
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.6),
         "Next Steps", font_size=32, color=NAVY)

data = [
    ["Action", "Storyline", "Owner", "By When"],
    ["Circulate deck + cultural debt framework", "All", "[Presenter]", "This week"],
    ["Run cultural readiness assessment", "Culture", "[Exec Sponsor] + HR", "30 days"],
    ["Audit AI KPIs \u2014 flag deployment-only metrics", "Change Mgmt", "BU Leads", "30 days"],
    ["Launch cross-functional AI council", "Change Mgmt", "Transformation Office", "30 days"],
    ["Schedule leadership AI \u201cshow and tell\u201d", "Leadership", "[C-Suite Champion]", "Next all-hands"],
    ["Incorporate AI use into promotion criteria", "Leadership", "HR + C-Suite", "Next perf cycle"],
    ["Reconvene: review findings, agree on plan", "All", "[Presenter] + Steering", "45 days"],
]
add_table(slide, Inches(0.6), Inches(1.2), Inches(12), Inches(4.2), 8, 4, data,
          col_widths=[Inches(5), Inches(1.8), Inches(3), Inches(2.2)], font_size=11)
add_footer(slide, p)

add_notes(slide, """Read actions, not the table. 30-day window is critical.

"Can we schedule the readiness assessment before we leave today?"

If the next meeting isn\u2019t calendared before people leave the room, it won\u2019t happen.
""")

# ============================================================
# APPENDIX
# ============================================================
add_appendix_divider(_prs)

# Appendix: Research Sources
slide = _prs.slides.add_slide(_prs.slide_layouts[6])
p = next_pg()
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.6),
         "The Research Behind This Presentation", font_size=28, color=NAVY)

data = [
    ["Source", "Finding", "Year"],
    ["McKinsey Global Institute", "70% of AI transformations fail to reach stated goals", "2023"],
    ["Gartner", "85% of AI projects deliver erroneous outcomes", "2024"],
    ["BCG & MIT Sloan", "Only 10% of companies report significant financial benefit from AI", "2024"],
    ["HBR \u2014 De Cremer et al.", "95% of AI initiatives fail; leaders default to \u201ctechnosolutionism\u201d", "2025"],
    ["Crucial Learning", "Organizations using all 6 sources are 12x faster at behavioral change", "2026"],
    ["Shelly Palmer", "Cultural debt: \u201cbureaucratic antibodies\u201d and the 40-year electrification parallel", "2026"],
    ["MIT Sloan Mgmt Review", "Leaders engaging all 6 sources are 10x more likely to drive change", "2008"],
]
add_table(slide, Inches(0.6), Inches(1.2), Inches(12), Inches(4.5), 8, 3, data,
          col_widths=[Inches(3.5), Inches(6.5), Inches(2)], font_size=11)
add_footer(slide, p)

add_notes(slide, """Backup for "where did you get that number?" questions.""")

# Appendix: Assessment Framework
slide = _prs.slides.add_slide(_prs.slide_layouts[6])
p = next_pg()
add_text(slide, Inches(0.6), Inches(0.3), Inches(12), Inches(0.6),
         "Cultural Debt Assessment Framework", font_size=28, color=NAVY)
add_text(slide, Inches(0.6), Inches(0.85), Inches(12), Inches(0.4),
         "Rate 1-5 on each dimension. Below 15 = significant cultural debt.", font_size=13, italic=True, color=NEAR_BLACK)

data = [
    ["Dimension", "Storyline", "1 (High Debt)", "5 (Low Debt)"],
    ["Experimentation Safety", "Culture", "Failures punished or hidden", "Failures shared and learned from"],
    ["Skill Building", "Culture", "Annual classroom training", "Continuous, embedded in work"],
    ["Peer Support", "Change Mgmt", "Everyone figures it out alone", "AI councils and shared practices"],
    ["Adoption Metrics", "Change Mgmt", "Success = model deployed", "Success = outcome improved"],
    ["Incentive Alignment", "Leadership", "Promotions reward old behaviors", "AI adoption in promotion criteria"],
    ["Leadership Visibility", "Leadership", "Leaders talk about AI, don\u2019t use it", "Leaders demo AI usage regularly"],
]
add_table(slide, Inches(0.6), Inches(1.4), Inches(12), Inches(3.5), 7, 4, data,
          col_widths=[Inches(2.5), Inches(1.8), Inches(3.85), Inches(3.85)], font_size=11)

scoring = [
    ("25-30:", "Strong \u2014 invest in technology with confidence", GREEN_ACCENT),
    ("18-24:", "Moderate debt \u2014 address gaps before scaling", MED_BLUE),
    ("12-17:", "Significant \u2014 pause tech investment, invest in people", AMBER_ACCENT),
    ("6-11:", "Critical \u2014 organizational redesign needed", RED_ACCENT),
]
for i, (score, desc, color) in enumerate(scoring):
    y = Inches(5.2) + Inches(i * 0.35)
    add_text(slide, Inches(1), y, Inches(1.5), Inches(0.3),
             score, font_size=11, bold=True, color=color)
    add_text(slide, Inches(2.5), y, Inches(9.5), Inches(0.3),
             desc, font_size=11, color=NEAR_BLACK)
add_footer(slide, p)

add_notes(slide, """Most actionable appendix slide. Offer to facilitate.

Dimensions now map to the three storylines. The conversation the rating provokes is more valuable than the score.""")

# Appendix: Anticipated Questions
add_qa_slide(_prs, "Anticipated Questions", [
    ("\u201cIsn\u2019t this just change management?\u201d",
     "Traditional CM covers 2 of 6 sources. That\u2019s why it has a 70% failure rate. This framework covers all six \u2014 it\u2019s an upgrade, not a replacement."),
    ("\u201cWe can\u2019t slow down our AI roadmap.\u201d",
     "Cultural debt IS the bottleneck. Every initiative into a high-debt org has 70-85% chance of failing and making the next harder. One quarter of assessment is cheaper than failing again."),
    ("\u201cHow do we measure cultural debt?\u201d",
     "Three proxies: (1) Time from pilot to production. (2) Process steps no one can explain. (3) Gap between \u2018AI deployed\u2019 vs. \u2018AI used weekly.\u2019 Use the assessment framework."),
    ("\u201cAre middle managers the problem?\u201d",
     "No \u2014 their incentives are (Source 5). Redesign incentives and the antibody response disappears. It\u2019s structural, not personal."),
    ("\u201cHow does this connect to AI-First?\u201d",
     "AI-First defines WHAT we build. People, Culture & Mindset defines WHETHER it gets adopted. One without the other produces investment without return."),
], next_pg())

# ============================================================
# SAVE
# ============================================================
output = "/Users/GUNDLLX/learn-claude/Skill Test/presentation/why-ai-fails/ai-first-to-people-culture-mindset.pptx"
_prs.save(output)
print(f"Saved: {output}")
print(f"Slides: {len(_prs.slides)}")
