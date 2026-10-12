"""Add appendix slides to Multi-Signal-Device-Technical-Deck.pptx"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
import os

PPTX_PATH = "/Users/GUNDLLX/learn-claude/projects/Multi-Signal Device/Multi-Signal-Device-Technical-Deck.pptx"
DIAGRAMS = "/Users/GUNDLLX/learn-claude/projects/Multi-Signal Device/diagrams"
DOMAIN = "/Users/GUNDLLX/learn-claude/projects/Multi-Signal Device/domain-model"

NAVY = RGBColor(0x1F, 0x35, 0x64)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GREY = RGBColor(0x59, 0x59, 0x59)
LIGHT_GREY = RGBColor(0xCC, 0xCC, 0xCC)

SLIDE_W = Inches(13.33)
SLIDE_H = Inches(7.5)

prs = Presentation(PPTX_PATH)

# Use blank layout (index 6 is typically blank)
blank_layout = None
for layout in prs.slide_layouts:
    if layout.name in ("Blank", "blank"):
        blank_layout = layout
        break
if blank_layout is None:
    blank_layout = prs.slide_layouts[6]


def add_divider_slide(prs, title_text, subtitle_text):
    slide = prs.slides.add_slide(blank_layout)
    # Full navy background
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = NAVY

    # Centered title
    txBox = slide.shapes.add_textbox(Inches(1), Inches(2.8), Inches(11.33), Inches(1.2))
    tf = txBox.text_frame
    tf.word_wrap = False
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = title_text
    run.font.bold = True
    run.font.size = Pt(40)
    run.font.color.rgb = WHITE
    run.font.name = "Calibri"

    # Subtitle
    txBox2 = slide.shapes.add_textbox(Inches(1), Inches(4.1), Inches(11.33), Inches(0.8))
    tf2 = txBox2.text_frame
    p2 = tf2.paragraphs[0]
    p2.alignment = PP_ALIGN.CENTER
    run2 = p2.add_run()
    run2.text = subtitle_text
    run2.font.size = Pt(18)
    run2.font.color.rgb = WHITE
    run2.font.name = "Calibri"

    return slide


def add_appendix_slide(prs, title_text, image_path, explanation_text):
    slide = prs.slides.add_slide(blank_layout)

    # White background (default) — ensure no fill issues
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = WHITE

    # Top navy bar (full width, 0.15" height)
    bar = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        Inches(0), Inches(0), SLIDE_W, Inches(0.15)
    )
    bar.fill.solid()
    bar.fill.fore_color.rgb = NAVY
    bar.line.fill.background()

    # "APPENDIX" label top-right
    lbl = slide.shapes.add_textbox(Inches(11.0), Inches(0.17), Inches(2.2), Inches(0.25))
    tf = lbl.text_frame
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.RIGHT
    run = p.add_run()
    run.text = "APPENDIX"
    run.font.size = Pt(9)
    run.font.color.rgb = GREY
    run.font.name = "Calibri"

    # Slide title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(12.0), Inches(0.55))
    tf2 = title_box.text_frame
    p2 = tf2.paragraphs[0]
    run2 = p2.add_run()
    run2.text = title_text
    run2.font.bold = True
    run2.font.size = Pt(22)
    run2.font.color.rgb = NAVY
    run2.font.name = "Calibri"

    # Thin separator line below title
    line = slide.shapes.add_shape(1, Inches(0.5), Inches(0.8), Inches(12.33), Inches(0.02))
    line.fill.solid()
    line.fill.fore_color.rgb = NAVY
    line.line.fill.background()

    # Image — centered, max 11" wide, max 4.5" tall
    from PIL import Image as PILImage
    img = PILImage.open(image_path)
    img_w, img_h = img.size
    aspect = img_w / img_h

    max_w = Inches(11.0)
    max_h = Inches(4.3)

    if (max_w / aspect) <= max_h:
        pic_w = max_w
        pic_h = Emu(int(max_w / aspect))
    else:
        pic_h = max_h
        pic_w = Emu(int(max_h * aspect))

    pic_left = Emu(int((SLIDE_W - pic_w) / 2))
    pic_top = Inches(0.95)

    slide.shapes.add_picture(image_path, pic_left, pic_top, pic_w, pic_h)

    # Explanation text below image
    exp_top = Emu(int(pic_top + pic_h + Inches(0.1)))
    exp_box = slide.shapes.add_textbox(Inches(1.0), exp_top, Inches(11.0), Inches(1.2))
    tf3 = exp_box.text_frame
    tf3.word_wrap = True
    p3 = tf3.paragraphs[0]
    run3 = p3.add_run()
    run3.text = explanation_text
    run3.font.size = Pt(11)
    run3.font.color.rgb = GREY
    run3.font.italic = True
    run3.font.name = "Calibri"

    return slide


# ---- Slide A: Divider ----
add_divider_slide(prs, "APPENDIX", "Architecture Diagrams & Reference Models")

# ---- Slide B: Reference Architecture ----
add_appendix_slide(
    prs,
    "Appendix A: Reference Architecture",
    os.path.join(DIAGRAMS, "reference-architecture.png"),
    "The reference architecture organizes the platform into five horizontal layers: Device & Edge (IoT capture and transmission), Connectivity & Identity (packet ingestion and device-patient token binding), Processing & Intelligence (6-signal fusion and AI risk scoring), Domain Services (care coordination, research, observability, audit), and Integration & Access (EMR gateway, web app, mobile app). Data flows top-to-bottom; all inter-layer communication is event-driven via Apache Kafka."
)

# ---- Slide C: Capability Model ----
add_appendix_slide(
    prs,
    "Appendix B: Persona Capability Model",
    os.path.join(DIAGRAMS, "capability-model.png"),
    "The capability model maps platform capabilities across six persona swimlanes (Patient, Clinician, Care Team, Researcher, Hospital Administrator, Corporate Administrator) and three capability rows (View, Act, Manage). Each cell represents a specific capability delivered to that persona. The shared data platform footer underpins all personas with signal time-series, risk scores, and audit data."
)

# ---- Slide D: Generational Roadmap ----
add_appendix_slide(
    prs,
    "Appendix C: Generational Capability Roadmap",
    os.path.join(DIAGRAMS, "device-generations.png"),
    "The generational roadmap defines three capability releases tied to signal activation. Gen 1 activates Bio-impedance and Temperature with threshold alerting. Gen 2 adds pH and SpO₂, enabling AI risk scoring, LLM summaries, and EMR embedding. Gen 3 activates Hydrogen Peroxide, completing the full 6-signal composite risk model and enabling population-scale analytics. This phased approach reduces clinical validation scope per release."
)

# ---- Slide E: DDD Domain Map ----
add_appendix_slide(
    prs,
    "Appendix D: Domain Map — Bounded Contexts",
    os.path.join(DOMAIN, "ddd-domain-map.png"),
    "The domain map shows all eleven bounded contexts classified as Core (Signal Processing, Clinical Decision Support), Supporting (Patient Engagement, Care Coordination, Research Analytics, Population Health, Platform Observability), and Generic (Device Connectivity, Device Identity & Binding, Audit & Compliance, EMR Integration Gateway). Arrows show domain event flow and relationship patterns (Customer-Supplier, Published Language, ACL, Open Host Service)."
)

# ---- Slide F: DDD Aggregate Design ----
add_appendix_slide(
    prs,
    "Appendix E: Aggregate Design",
    os.path.join(DOMAIN, "ddd-aggregates.png"),
    "The aggregate diagram shows the internal structure of the three primary aggregates: SignalObservation (raw signals + derived metrics + quality score), RiskAssessment (risk score + factors + LLM clinical summary), and DevicePatientBinding (serial number → HMAC token + EMR vendor + status). Each aggregate enforces its own invariants and is the single unit of consistency within its bounded context."
)

# ---- Slide G: Domain Events Sequence ----
add_appendix_slide(
    prs,
    "Appendix F: Domain Events Sequence",
    os.path.join(DOMAIN, "ddd-events-sequence.png"),
    "The sequence diagram traces the end-to-end event flow from device signal transmission through to EMR write-back. Key events include: SignalObservationRecorded (triggers CDS), RiskAssessmentCompleted (triggers escalation and patient alert), EscalationTriggered (notifies care team), and RiskScoreWrittenToEMR / SOAPDraftWrittenToEMR (FHIR write-back via EMR adapter). All events are simultaneously mirrored to the immutable Audit & Compliance event log."
)

# ---- Slide H: Solution Architecture ----
add_appendix_slide(
    prs,
    "Appendix G: Solution Architecture — Zone View",
    os.path.join(DIAGRAMS, "solution-architecture.png"),
    "The solution architecture presents the platform as five deployment zones with explicit data flow arrows: Device Zone (wearable + edge gateway), Platform Zone (Kafka, microservices, ML), Integration Zone (IEMRGateway port + vendor adapters), Access Zone (web app, mobile app, EMR embedded UI), and Compliance Zone (WORM audit log, OpenLineage, consent store). Zone boundaries enforce security perimeters and data classification policies."
)

prs.save(PPTX_PATH)
print(f"Saved: {PPTX_PATH}")
print(f"Total slides: {len(prs.slides)}")
