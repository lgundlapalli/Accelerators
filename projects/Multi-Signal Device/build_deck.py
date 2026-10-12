"""
Build Multi-Signal Device Business Deck using python-pptx
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import copy

# Colors
NAVY = RGBColor(0x1F, 0x35, 0x64)
TEAL = RGBColor(0x00, 0x70, 0xC0)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_BLUE = RGBColor(0xD9, 0xE1, 0xF2)
DARK_GRAY = RGBColor(0x40, 0x40, 0x40)
MID_GRAY = RGBColor(0x60, 0x60, 0x60)

# Slide dimensions (widescreen 13.33" x 7.5")
W = Inches(13.33)
H = Inches(7.5)

prs = Presentation()
prs.slide_width = W
prs.slide_height = H

blank_layout = prs.slide_layouts[6]  # blank

def add_rect(slide, left, top, width, height, fill_color, line_color=None):
    shape = slide.shapes.add_shape(1, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if line_color:
        shape.line.color.rgb = line_color
    else:
        shape.line.fill.background()
    return shape

def add_text_box(slide, text, left, top, width, height,
                 font_name="Calibri", font_size=18, bold=False,
                 color=DARK_GRAY, align=PP_ALIGN.LEFT, italic=False,
                 word_wrap=True):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    txBox.word_wrap = word_wrap
    tf = txBox.text_frame
    tf.word_wrap = word_wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.name = font_name
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return txBox

def add_accent_bar_top(slide, color=TEAL, height=Inches(0.08)):
    add_rect(slide, 0, 0, W, height, color)

def add_accent_bar_left(slide, color=NAVY, width=Inches(0.12)):
    add_rect(slide, 0, 0, width, H, color)

def add_heading(slide, text, top=Inches(0.35), color=NAVY, size=28):
    add_text_box(slide, text, Inches(0.5), top, Inches(12.3), Inches(0.7),
                 font_size=size, bold=True, color=color)

def add_footer_bar(slide):
    bar = add_rect(slide, 0, H - Inches(0.4), W, Inches(0.4), NAVY)
    add_text_box(slide, "Multi-Signal Device Platform  |  Confidential",
                 Inches(0.5), H - Inches(0.38), Inches(10), Inches(0.35),
                 font_size=10, color=WHITE, align=PP_ALIGN.LEFT)

# ─────────────────────────────────────────────
# SLIDE 1 — Title
# ─────────────────────────────────────────────
slide = prs.slides.add_slide(blank_layout)

# Navy background
add_rect(slide, 0, 0, W, H, NAVY)

# Teal accent bar (left strip)
add_rect(slide, 0, 0, Inches(0.35), H, TEAL)

# Title
add_text_box(slide, "Continuous Multi-Signal\nPatient Monitoring",
             Inches(1.0), Inches(1.8), Inches(11), Inches(2.0),
             font_size=40, bold=True, color=WHITE, align=PP_ALIGN.LEFT)

# Subtitle
add_text_box(slide,
             "A Next-Generation Wearable Platform for Clinical Decision Support",
             Inches(1.0), Inches(3.9), Inches(10), Inches(0.8),
             font_size=22, bold=False, color=LIGHT_BLUE, align=PP_ALIGN.LEFT)

# Tagline box
tb = add_rect(slide, Inches(1.0), Inches(5.1), Inches(7), Inches(0.7), TEAL)
add_text_box(slide, "From Device to Decision — in Seconds",
             Inches(1.15), Inches(5.12), Inches(6.7), Inches(0.65),
             font_size=20, bold=True, color=WHITE, align=PP_ALIGN.LEFT)

# ─────────────────────────────────────────────
# SLIDE 2 — The Problem
# ─────────────────────────────────────────────
slide = prs.slides.add_slide(blank_layout)
add_accent_bar_top(slide)
add_footer_bar(slide)

add_heading(slide, "Patients Deteriorate Between Check-ins", top=Inches(0.25))

pain_points = [
    "Clinicians see patients for minutes.\nRisks develop over hours.",
    "Fragmented point-in-time vitals miss\nearly warning signs.",
    "Escalation decisions rely on intuition —\nnot continuous signal data.",
]

colors = [NAVY, TEAL, RGBColor(0x2E, 0x74, 0xB5)]

for i, (pt, col) in enumerate(zip(pain_points, colors)):
    box_left = Inches(0.5 + i * 4.2)
    box_top = Inches(1.5)
    box_w = Inches(3.9)
    box_h = Inches(4.2)
    add_rect(slide, box_left, box_top, box_w, box_h, LIGHT_BLUE)
    add_rect(slide, box_left, box_top, box_w, Inches(0.12), col)
    add_text_box(slide, pt,
                 box_left + Inches(0.2), box_top + Inches(0.35),
                 box_w - Inches(0.4), box_h - Inches(0.5),
                 font_size=18, bold=True, color=NAVY, align=PP_ALIGN.LEFT)

# ─────────────────────────────────────────────
# SLIDE 3 — Our Solution
# ─────────────────────────────────────────────
slide = prs.slides.add_slide(blank_layout)
add_accent_bar_top(slide)
add_footer_bar(slide)

add_heading(slide, "One Wearable. Six Signals. Real-Time Clinical Intelligence.")

signals = [
    ("Bio-impedance", "Fluid / Tissue"),
    ("Pressure", "Hemodynamic"),
    ("pH", "Tissue Acidity"),
    ("SpO₂", "Oxygen"),
    ("H₂O₂", "Oxidative Stress"),
    ("Temperature", "Fever"),
]

col_count = 3
row_count = 2
cell_w = Inches(3.8)
cell_h = Inches(1.8)
start_x = Inches(0.7)
start_y = Inches(1.3)
gap_x = Inches(0.25)
gap_y = Inches(0.25)

for idx, (name, desc) in enumerate(signals):
    r = idx // col_count
    c = idx % col_count
    cx = start_x + c * (cell_w + gap_x)
    cy = start_y + r * (cell_h + gap_y)
    add_rect(slide, cx, cy, cell_w, cell_h, LIGHT_BLUE)
    add_rect(slide, cx, cy, Inches(0.1), cell_h, TEAL)
    add_text_box(slide, name, cx + Inches(0.25), cy + Inches(0.25),
                 cell_w - Inches(0.3), Inches(0.65),
                 font_size=18, bold=True, color=NAVY)
    add_text_box(slide, desc, cx + Inches(0.25), cy + Inches(0.9),
                 cell_w - Inches(0.3), Inches(0.6),
                 font_size=14, bold=False, color=MID_GRAY)

# Tagline
tagline_y = start_y + row_count * (cell_h + gap_y) + Inches(0.1)
tl_box = add_rect(slide, Inches(0.5), tagline_y, Inches(12.3), Inches(0.65), NAVY)
add_text_box(slide,
             "Continuous monitoring  →  AI risk scoring  →  Actionable insight inside your EMR",
             Inches(0.7), tagline_y + Inches(0.08), Inches(12.0), Inches(0.55),
             font_size=16, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

# ─────────────────────────────────────────────
# SLIDE 4 — How It Works
# ─────────────────────────────────────────────
slide = prs.slides.add_slide(blank_layout)
add_accent_bar_top(slide)
add_footer_bar(slide)

add_heading(slide, "Simple for Clinicians. Powerful Under the Hood.")

steps = [
    ("1", "Wear", "Patient wears device.\nSignals stream continuously."),
    ("2", "Analyze", "AI computes risk score (0–100)\nand generates a clinical summary."),
    ("3", "Act", "Risk scores, SOAP notes, and escalation\nalerts appear inside Epic or Cerner —\nno new app to learn."),
]

box_colors = [NAVY, TEAL, RGBColor(0x2E, 0x74, 0xB5)]
step_w = Inches(3.7)
step_h = Inches(4.5)
step_y = Inches(1.5)
start_x = Inches(0.7)

for i, (num, title, body) in enumerate(steps):
    bx = start_x + i * (step_w + Inches(0.35))
    add_rect(slide, bx, step_y, step_w, step_h, box_colors[i])
    # Step number circle (use small rect)
    add_text_box(slide, num, bx + Inches(0.2), step_y + Inches(0.3),
                 Inches(0.8), Inches(0.8),
                 font_size=32, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_text_box(slide, title, bx + Inches(0.2), step_y + Inches(1.1),
                 step_w - Inches(0.4), Inches(0.7),
                 font_size=24, bold=True, color=WHITE, align=PP_ALIGN.LEFT)
    add_text_box(slide, body, bx + Inches(0.2), step_y + Inches(1.9),
                 step_w - Inches(0.4), Inches(2.2),
                 font_size=16, bold=False, color=LIGHT_BLUE, align=PP_ALIGN.LEFT)

# Arrow connectors (simple text)
for i in range(2):
    ax = start_x + (i + 1) * (step_w + Inches(0.35)) - Inches(0.45)
    add_text_box(slide, "→", ax, step_y + Inches(1.8), Inches(0.5), Inches(0.6),
                 font_size=28, bold=True, color=TEAL, align=PP_ALIGN.CENTER)

# ─────────────────────────────────────────────
# SLIDE 5 — Key Differentiators
# ─────────────────────────────────────────────
slide = prs.slides.add_slide(blank_layout)
add_accent_bar_top(slide)
add_footer_bar(slide)

add_heading(slide, "Why This Platform Is Different")

diffs = [
    ("Works Inside\nYour EMR",
     "No new login. Clinicians see insights in Epic, Cerner, or any FHIR system they already use."),
    ("Patient Privacy\nby Design",
     "No patient records stored on our platform. Zero PII. Fully HIPAA-aligned."),
    ("AI That Explains\nItself",
     "Every risk score comes with cited signal evidence — not a black box."),
    ("Grows With You",
     "Start with 2 signals. Add 4 more as clinical validation expands. Pay for what you use."),
]

cell_w = Inches(5.8)
cell_h = Inches(2.4)
gap = Inches(0.25)
positions = [
    (Inches(0.5), Inches(1.4)),
    (Inches(6.55), Inches(1.4)),
    (Inches(0.5), Inches(4.0)),
    (Inches(6.55), Inches(4.0)),
]

for (cx, cy), (title, body) in zip(positions, diffs):
    add_rect(slide, cx, cy, cell_w, cell_h, LIGHT_BLUE)
    add_rect(slide, cx, cy, cell_w, Inches(0.1), TEAL)
    add_text_box(slide, title, cx + Inches(0.2), cy + Inches(0.2),
                 cell_w - Inches(0.3), Inches(0.85),
                 font_size=18, bold=True, color=NAVY)
    add_text_box(slide, body, cx + Inches(0.2), cy + Inches(1.1),
                 cell_w - Inches(0.3), Inches(1.1),
                 font_size=14, color=DARK_GRAY)

# ─────────────────────────────────────────────
# SLIDE 6 — Generational Roadmap
# ─────────────────────────────────────────────
slide = prs.slides.add_slide(blank_layout)
add_accent_bar_top(slide)
add_footer_bar(slide)

add_heading(slide, "A Phased Path to Full Clinical Intelligence")

gens = [
    ("Gen 1", "Foundation", NAVY,
     "Bio-impedance + Temperature",
     ["Threshold alerting", "Patient mobile app", "Device fleet monitoring"]),
    ("Gen 2", "Intelligence", TEAL,
     "+ pH + SpO₂",
     ["AI risk scoring", "LLM clinical summaries", "SOAP draft notes", "EMR embedding"]),
    ("Gen 3", "Population Scale", RGBColor(0x2E, 0x74, 0xB5),
     "+ H₂O₂",
     ["Full composite risk", "Oxidative stress detection", "Population health analytics"]),
]

col_w = Inches(3.9)
col_h = Inches(5.4)
col_y = Inches(1.3)
col_xs = [Inches(0.5), Inches(4.6), Inches(8.7)]

for (col_x, (gen, subtitle, col, signals_txt, bullets)) in zip(col_xs, gens):
    add_rect(slide, col_x, col_y, col_w, col_h, LIGHT_BLUE)
    add_rect(slide, col_x, col_y, col_w, Inches(0.9), col)
    add_text_box(slide, gen, col_x + Inches(0.2), col_y + Inches(0.05),
                 col_w - Inches(0.3), Inches(0.4),
                 font_size=20, bold=True, color=WHITE)
    add_text_box(slide, subtitle, col_x + Inches(0.2), col_y + Inches(0.5),
                 col_w - Inches(0.3), Inches(0.35),
                 font_size=14, bold=False, color=WHITE)
    add_text_box(slide, signals_txt, col_x + Inches(0.2), col_y + Inches(1.05),
                 col_w - Inches(0.3), Inches(0.55),
                 font_size=14, bold=True, color=NAVY)
    for bi, bullet in enumerate(bullets):
        add_text_box(slide, f"• {bullet}",
                     col_x + Inches(0.2), col_y + Inches(1.7) + bi * Inches(0.7),
                     col_w - Inches(0.3), Inches(0.6),
                     font_size=14, color=DARK_GRAY)

# ─────────────────────────────────────────────
# SLIDE 7 — Who It Serves
# ─────────────────────────────────────────────
slide = prs.slides.add_slide(blank_layout)
add_accent_bar_top(slide)
add_footer_bar(slide)

add_heading(slide, "Designed for Every Member of the Care Team")

personas = [
    ("Patient",           "Plain-language vitals and\nalerts on their phone"),
    ("Clinician",         "Risk scores and AI summaries\nwhere they already work"),
    ("Care Team",         "Shared visibility into\npatient status in real time"),
    ("Researcher",        "Anonymized signal data\nfor clinical studies"),
    ("Hospital Admin",    "Fleet oversight, utilization\nreports, and compliance"),
    ("Corporate Admin",   "Enterprise configuration,\nsecurity, and audit controls"),
]

p_col_count = 3
p_col_w = Inches(3.8)
p_col_h = Inches(2.2)
p_start_x = Inches(0.7)
p_start_y = Inches(1.4)
p_gap_x = Inches(0.25)
p_gap_y = Inches(0.3)
p_colors = [NAVY, TEAL, RGBColor(0x2E, 0x74, 0xB5), NAVY, TEAL, RGBColor(0x2E, 0x74, 0xB5)]

for idx, ((name, desc), col) in enumerate(zip(personas, p_colors)):
    r = idx // p_col_count
    c = idx % p_col_count
    cx = p_start_x + c * (p_col_w + p_gap_x)
    cy = p_start_y + r * (p_col_h + p_gap_y)
    add_rect(slide, cx, cy, p_col_w, p_col_h, LIGHT_BLUE)
    add_rect(slide, cx, cy, p_col_w, Inches(0.12), col)
    add_text_box(slide, name, cx + Inches(0.2), cy + Inches(0.2),
                 p_col_w - Inches(0.3), Inches(0.55),
                 font_size=18, bold=True, color=NAVY)
    add_text_box(slide, desc, cx + Inches(0.2), cy + Inches(0.8),
                 p_col_w - Inches(0.3), Inches(1.2),
                 font_size=14, color=DARK_GRAY)

# ─────────────────────────────────────────────
# SLIDE 8 — EMR Integration
# ─────────────────────────────────────────────
slide = prs.slides.add_slide(blank_layout)
add_accent_bar_top(slide)
add_footer_bar(slide)

add_heading(slide, "Works With Any Hospital System — Out of the Box")

# Three EMR boxes
emrs = ["Epic", "Oracle Cerner", "Any FHIR R4 System"]
emr_w = Inches(3.5)
emr_h = Inches(1.8)
emr_y = Inches(1.6)
emr_xs = [Inches(0.9), Inches(4.7), Inches(8.5)]

for ex, name in zip(emr_xs, emrs):
    add_rect(slide, ex, emr_y, emr_w, emr_h, NAVY)
    add_text_box(slide, name, ex, emr_y, emr_w, emr_h,
                 font_size=22, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

# Key message box
msg = ("SMART on FHIR standard — mandated by the 21st Century Cures Act — means no custom "
       "integration per hospital. One certification works everywhere.")
add_rect(slide, Inches(0.5), Inches(3.9), Inches(12.3), Inches(2.2), LIGHT_BLUE)
add_rect(slide, Inches(0.5), Inches(3.9), Inches(0.12), Inches(2.2), TEAL)
add_text_box(slide, msg, Inches(0.8), Inches(4.05), Inches(11.8), Inches(1.9),
             font_size=18, color=NAVY, align=PP_ALIGN.LEFT)

# ─────────────────────────────────────────────
# SLIDE 9 — Clinical Impact
# ─────────────────────────────────────────────
slide = prs.slides.add_slide(blank_layout)
add_accent_bar_top(slide)
add_footer_bar(slide)

add_heading(slide, "Outcomes That Matter")

metrics = [
    ("<30 seconds",  "from signal observation\nto risk score"),
    ("<60 seconds",  "from AI alert to care\nteam escalation"),
    ("Zero PII",     "stored on the platform"),
    ("3 Generations","of expanding clinical\ncapability"),
]

m_w = Inches(2.8)
m_h = Inches(3.8)
m_y = Inches(1.6)
m_xs = [Inches(0.5 + i * (m_w + Inches(0.45))) for i in range(4)]
m_colors = [NAVY, TEAL, RGBColor(0x2E, 0x74, 0xB5), NAVY]

for mx, (big, small), col in zip(m_xs, metrics, m_colors):
    add_rect(slide, mx, m_y, m_w, m_h, col)
    add_text_box(slide, big, mx + Inches(0.15), m_y + Inches(0.7),
                 m_w - Inches(0.2), Inches(1.4),
                 font_size=28, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_text_box(slide, small, mx + Inches(0.15), m_y + Inches(2.3),
                 m_w - Inches(0.2), Inches(1.1),
                 font_size=15, color=LIGHT_BLUE, align=PP_ALIGN.CENTER)

# ─────────────────────────────────────────────
# SLIDE 10 — Call to Action
# ─────────────────────────────────────────────
slide = prs.slides.add_slide(blank_layout)

# Navy background
add_rect(slide, 0, 0, W, H, NAVY)
add_rect(slide, 0, 0, Inches(0.35), H, TEAL)

add_text_box(slide,
             "Let's Build the Future of\nContinuous Care Together",
             Inches(1.0), Inches(0.5), Inches(11), Inches(1.8),
             font_size=32, bold=True, color=WHITE, align=PP_ALIGN.LEFT)

next_steps = [
    ("1  Clinical Pilot",
     "Select a hospital partner for Gen 2 validation"),
    ("2  EMR Certification",
     "Submit Epic App Orchard application"),
    ("3  Regulatory",
     "Initiate FDA SaMD determination for CDS outputs"),
]

for i, (title, body) in enumerate(next_steps):
    sy = Inches(2.5) + i * Inches(1.3)
    add_rect(slide, Inches(1.0), sy, Inches(11.0), Inches(1.1), RGBColor(0x28, 0x45, 0x78))
    add_rect(slide, Inches(1.0), sy, Inches(0.1), Inches(1.1), TEAL)
    add_text_box(slide, title, Inches(1.3), sy + Inches(0.1),
                 Inches(4.5), Inches(0.45),
                 font_size=18, bold=True, color=WHITE)
    add_text_box(slide, body, Inches(1.3), sy + Inches(0.55),
                 Inches(9.5), Inches(0.45),
                 font_size=14, color=LIGHT_BLUE)

# Contact
add_text_box(slide,
             "Enterprise Architecture  ·  Multi-Signal Device Platform",
             Inches(1.0), Inches(6.7), Inches(11.0), Inches(0.5),
             font_size=14, bold=False, color=TEAL, align=PP_ALIGN.LEFT)

# ─────────────────────────────────────────────
# Save
# ─────────────────────────────────────────────
output_path = "/Users/GUNDLLX/learn-claude/projects/Multi-Signal Device/Multi-Signal-Device-Business-Deck.pptx"
prs.save(output_path)
print(f"Saved: {output_path}")
