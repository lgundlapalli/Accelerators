#!/usr/bin/env python3
"""Generate Multi-Signal Device Technical Architecture Deck"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import copy

# Color palette
NAVY = RGBColor(0x1F, 0x35, 0x64)
TEAL = RGBColor(0x00, 0x70, 0xC0)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_BLUE = RGBColor(0xD9, 0xE1, 0xF2)
DARK_GREY = RGBColor(0x59, 0x59, 0x59)
LIGHT_GREY = RGBColor(0xF2, 0xF2, 0xF2)
ALT_ROW = RGBColor(0xE9, 0xEF, 0xF8)

# Slide dimensions: 13.33" x 7.5"
SLIDE_W = Inches(13.33)
SLIDE_H = Inches(7.5)


def create_presentation():
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    return prs


def add_accent_bar(slide, color=NAVY):
    """Add top navy accent bar"""
    from pptx.util import Inches, Pt
    bar = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        Inches(0), Inches(0),
        SLIDE_W, Inches(0.12)
    )
    bar.fill.solid()
    bar.fill.fore_color.rgb = color
    bar.line.fill.background()


def add_bottom_bar(slide):
    """Add thin bottom accent bar"""
    bar = slide.shapes.add_shape(
        1, Inches(0), Inches(7.38), SLIDE_W, Inches(0.12)
    )
    bar.fill.solid()
    bar.fill.fore_color.rgb = TEAL
    bar.line.fill.background()


def set_slide_bg(slide):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = WHITE


def add_textbox(slide, text, left, top, width, height,
                font_name="Calibri", font_size=14, bold=False,
                color=DARK_GREY, align=PP_ALIGN.LEFT, italic=False):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
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


def add_heading(slide, text, top=Inches(0.18), font_size=26):
    add_textbox(slide, text,
                left=Inches(0.4), top=top,
                width=Inches(12.5), height=Inches(0.5),
                font_size=font_size, bold=True, color=NAVY)


def add_table(slide, headers, rows, left, top, width, height,
              col_widths=None):
    """Add a formatted table with navy header and alternating rows"""
    from pptx.util import Pt
    from pptx.oxml.ns import qn
    from lxml import etree

    n_cols = len(headers)
    n_rows = len(rows) + 1  # +1 for header

    tbl = slide.shapes.add_table(n_rows, n_cols, left, top, width, height)
    table = tbl.table

    # Set column widths if provided
    if col_widths:
        for i, w in enumerate(col_widths):
            table.columns[i].width = w

    # Header row
    for j, h in enumerate(headers):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY
        tf = cell.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run = p.add_run()
        run.text = h
        run.font.name = "Calibri"
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = WHITE

    # Data rows
    for i, row in enumerate(rows):
        bg = LIGHT_BLUE if i % 2 == 0 else WHITE
        for j, val in enumerate(row):
            cell = table.cell(i + 1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg
            tf = cell.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.LEFT
            run = p.add_run()
            run.text = val
            run.font.name = "Calibri"
            run.font.size = Pt(11)
            run.font.color.rgb = DARK_GREY

    return tbl


def add_callout_box(slide, text, left, top, width, height, bg=LIGHT_BLUE):
    box = slide.shapes.add_shape(1, left, top, width, height)
    box.fill.solid()
    box.fill.fore_color.rgb = bg
    box.line.color.rgb = TEAL
    box.line.width = Pt(1.5)
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.1)
    tf.margin_right = Inches(0.1)
    tf.margin_top = Inches(0.06)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    run = p.add_run()
    run.text = text
    run.font.name = "Calibri"
    run.font.size = Pt(12)
    run.font.bold = False
    run.font.color.rgb = NAVY


def add_code_block(slide, code_lines, left, top, width, height):
    box = slide.shapes.add_shape(1, left, top, width, height)
    box.fill.solid()
    box.fill.fore_color.rgb = LIGHT_GREY
    box.line.color.rgb = RGBColor(0xCC, 0xCC, 0xCC)
    box.line.width = Pt(1)
    tf = box.text_frame
    tf.word_wrap = False
    tf.margin_left = Inches(0.12)
    tf.margin_top = Inches(0.08)

    for idx, line in enumerate(code_lines):
        if idx == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        run = p.add_run()
        run.text = line
        run.font.name = "Courier New"
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0x1A, 0x1A, 0x2E)


def slide1_title(prs):
    slide_layout = prs.slide_layouts[6]  # blank
    slide = prs.slides.add_slide(slide_layout)
    set_slide_bg(slide)

    # Full-width navy header band
    hdr = slide.shapes.add_shape(1, Inches(0), Inches(0), SLIDE_W, Inches(2.8))
    hdr.fill.solid()
    hdr.fill.fore_color.rgb = NAVY
    hdr.line.fill.background()

    # Title
    add_textbox(slide, "Multi-Signal Wearable Device Platform",
                Inches(0.6), Inches(0.55), Inches(12), Inches(1.1),
                font_size=36, bold=True, color=WHITE)

    # Subtitle
    add_textbox(slide, "Architecture Overview — Technical Deep Dive",
                Inches(0.6), Inches(1.55), Inches(11), Inches(0.6),
                font_size=20, bold=False, color=LIGHT_BLUE)

    # Teal divider
    div = slide.shapes.add_shape(1, Inches(0.6), Inches(2.85), Inches(5), Inches(0.05))
    div.fill.solid()
    div.fill.fore_color.rgb = TEAL
    div.line.fill.background()

    # Version line
    add_textbox(slide, "v1.0  ·  October 2026  ·  Confidential",
                Inches(0.6), Inches(3.05), Inches(8), Inches(0.4),
                font_size=13, color=DARK_GREY)

    # Bottom decorative band
    add_bottom_bar(slide)

    return slide


def slide2_principles(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)
    add_accent_bar(slide)
    add_heading(slide, "Five Design Principles", top=Inches(0.18))

    principles = [
        ("1  No Patient Profile on Platform",
         "PatientReference is session-only FHIR Patient ID. DevicePatientToken is one-way HMAC-SHA256 hash. Zero PII/PHI written to database."),
        ("2  Port & Adapter EMR Integration",
         "IEMRGateway abstract interface. New EMR vendor = new adapter only. No platform core changes required."),
        ("3  Event-Driven Bounded Contexts",
         "Apache Kafka for all inter-context communication. No synchronous cross-boundary calls."),
        ("4  AI-Augmented, Not AI-Dependent",
         "LLM outputs are clinician-reviewed suggestions. No autonomous EMR writes."),
        ("5  Hyperscaler-Agnostic",
         "AWS and Azure equivalents for every component. No proprietary lock-in."),
    ]

    top_start = Inches(0.78)
    box_h = Inches(1.16)
    gap = Inches(0.08)

    for i, (title, body) in enumerate(principles):
        top = top_start + i * (box_h + gap)
        # Left badge
        badge = slide.shapes.add_shape(1, Inches(0.3), top, Inches(0.22), box_h)
        badge.fill.solid()
        badge.fill.fore_color.rgb = TEAL if i % 2 == 0 else NAVY
        badge.line.fill.background()

        # Card bg
        card = slide.shapes.add_shape(1, Inches(0.55), top, Inches(12.55), box_h)
        card.fill.solid()
        card.fill.fore_color.rgb = LIGHT_BLUE if i % 2 == 0 else RGBColor(0xF5, 0xF7, 0xFB)
        card.line.color.rgb = RGBColor(0xBD, 0xCB, 0xE8)
        card.line.width = Pt(0.75)

        # Title
        add_textbox(slide, title, Inches(0.72), top + Inches(0.08),
                    Inches(12.2), Inches(0.36),
                    font_size=13, bold=True, color=NAVY)
        # Body
        add_textbox(slide, body, Inches(0.72), top + Inches(0.42),
                    Inches(12.2), Inches(0.62),
                    font_size=12, color=DARK_GREY)

    add_bottom_bar(slide)
    return slide


def slide3_arch_layers(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)
    add_accent_bar(slide)
    add_heading(slide, "5-Layer Reference Architecture")

    headers = ["Layer", "Name", "Components"]
    rows = [
        ("Layer 1", "Device & Edge",
         "Wearable Device → BLE/LTE → IoT Greengrass / IoT Edge → packet validation"),
        ("Layer 2", "Connectivity & Identity",
         "Device Connectivity · Device Identity & Binding (serial# → HMAC token → PatientReference)"),
        ("Layer 3", "Processing & Intelligence",
         "Signal Processing (6-signal fusion, derived metrics, baseline) · CDS (risk scoring, anomaly detection, Claude API LLM)"),
        ("Layer 4", "Domain Services",
         "Care Coordination · Patient Engagement · Research Analytics · Population Health · Platform Observability · Audit & Compliance"),
        ("Layer 5", "Integration & Access",
         "IEMRGateway (EpicAdapter · CernerAdapter · GenericFHIRAdapter) · Platform Web App · Patient Mobile App"),
    ]

    col_widths = [Inches(1.1), Inches(2.2), Inches(9.7)]
    add_table(slide, headers, rows,
              left=Inches(0.3), top=Inches(0.78),
              width=Inches(12.73), height=Inches(6.35),
              col_widths=col_widths)

    add_bottom_bar(slide)
    return slide


def slide4_device_identity(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)
    add_accent_bar(slide)
    add_heading(slide, "Device-to-Patient Identity: No PII Storage Problem Solved")

    steps = [
        "1.  Clinician launches platform via SMART on FHIR → receives FHIR PatientReference.",
        "2.  Platform creates DevicePatientBinding: SerialNumber → HMAC-SHA256(TenantID + FHIR PatientID).",
        "3.  Token stored in PostgreSQL (binding store) + Redis (active lookup cache).",
        "4.  Device transmits signal packet with SerialNumber only — no patient data on device.",
        "5.  Device Connectivity looks up token → IEMRGateway.resolve_patient_from_token() → adapter fetches Patient/{id}.",
        "6.  PatientReference used for signal pipeline — never written to database.",
    ]

    top = Inches(0.78)
    for i, step in enumerate(steps):
        add_textbox(slide, step,
                    Inches(0.4), top + i * Inches(0.82),
                    Inches(12.5), Inches(0.72),
                    font_size=13, color=DARK_GREY)

    # Callout box
    callout_text = (
        "⬛  One active binding per SerialNumber.  "
        "Token is write-once.  "
        "Rebinding requires explicit revocation."
    )
    add_callout_box(slide, callout_text,
                    Inches(0.4), Inches(6.3),
                    Inches(12.5), Inches(0.88))

    add_bottom_bar(slide)
    return slide


def slide5_emr_integration(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)
    add_accent_bar(slide)
    add_heading(slide, "IEMRGateway — Vendor-Agnostic FHIR Integration")

    # Code block
    code = [
        "class IEMRGateway:",
        "    def get_patient_reference(self, launch_token) -> PatientReference",
        "    def resolve_patient_from_token(self, token, tenant_id) -> PatientReference",
        "    def write_observation(self, ref, obs) -> str",
        "    def write_risk_score(self, ref, assessment) -> str",
        "    def write_soap_draft(self, ref, assessment) -> str",
        "    def write_escalation_alert(self, ref, escalation) -> str",
    ]
    add_code_block(slide, code,
                   Inches(0.35), Inches(0.78),
                   Inches(12.63), Inches(2.0))

    # Adapter table
    headers = ["Adapter", "Marketplace", "Auth Method", "Write Targets"]
    rows = [
        ("EpicAdapter", "Epic App Orchard", "SMART on FHIR", "Epic FHIR R4 + In-Basket"),
        ("CernerAdapter", "Cerner App Gallery", "SMART on FHIR", "Cerner FHIR R4 + Message Center"),
        ("GenericFHIRAdapter", "Per-vendor config", "OAuth 2.0 / SMART", "Standard FHIR R4"),
    ]
    col_widths = [Inches(2.4), Inches(2.8), Inches(2.8), Inches(4.5)]
    add_table(slide, headers, rows,
              left=Inches(0.35), top=Inches(2.92),
              width=Inches(12.63), height=Inches(2.2),
              col_widths=col_widths)

    # Note
    add_textbox(slide,
                "New EMR integration = implement IEMRGateway interface only. Zero changes to platform core services.",
                Inches(0.35), Inches(5.25), Inches(12.6), Inches(0.5),
                font_size=12, italic=True, color=TEAL)

    add_bottom_bar(slide)
    return slide


def slide6_domain_events(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)
    add_accent_bar(slide)
    add_heading(slide, "Event-Driven Architecture — Key Domain Events")

    headers = ["Event", "Raised By", "Consumed By"]
    rows = [
        ("SignalObservationRecorded", "Signal Processing", "CDS, Patient Engagement, Research Analytics"),
        ("HypoxiaFlagRaised", "Signal Processing", "CDS, Care Coordination"),
        ("RiskAssessmentCompleted", "CDS", "Care Coordination, Patient Engagement, Population Health"),
        ("EscalationTriggered", "Care Coordination", "Patient Engagement"),
        ("PatientSessionEstablished", "EMR Gateway", "Signal Processing, CDS"),
        ("DevicePatientBindingCreated", "Device Identity & Binding", "EMR Gateway, Audit"),
        ("DevicePatientBindingRevoked", "Device Identity & Binding", "EMR Gateway, Audit"),
        ("RiskScoreWrittenToEMR", "EMR Gateway", "Audit & Compliance"),
        ("DeviceOfflineDetected", "Device Connectivity", "Platform Observability"),
        ("SLABreachTriggered", "Platform Observability", "Corporate Administrator"),
    ]
    col_widths = [Inches(4.2), Inches(3.2), Inches(5.33)]
    add_table(slide, headers, rows,
              left=Inches(0.3), top=Inches(0.78),
              width=Inches(12.73), height=Inches(6.42),
              col_widths=col_widths)

    add_bottom_bar(slide)
    return slide


def slide7_tech_stack(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)
    add_accent_bar(slide)
    add_heading(slide, "Core Technology Decisions")

    headers = ["Component", "Recommended", "AWS Alternative", "Azure Alternative"]
    rows = [
        ("Event Bus", "Apache Kafka (MSK)", "Kinesis Data Streams", "Azure Event Hubs"),
        ("Time-Series DB", "InfluxDB", "AWS Timestream", "Azure Data Explorer"),
        ("ML Platform", "MLflow + SageMaker", "SageMaker Autopilot", "Azure Machine Learning"),
        ("LLM", "Claude API (Haiku / Sonnet)", "Bedrock (Claude)", "Azure AI (Claude)"),
        ("Identity Store", "PostgreSQL + Redis", "RDS + ElastiCache", "Azure DB + Azure Cache"),
        ("Secrets Mgmt", "AWS Secrets Manager", "—", "Azure Key Vault"),
        ("Audit Log", "Kafka + S3 WORM", "S3 Object Lock", "ADLS Gen2 WORM"),
        ("Data Lineage", "OpenLineage + Marquez", "—", "Microsoft Purview"),
        ("EMR Auth", "smart-on-fhir (Python)", "—", "HAPI FHIR (Java)"),
    ]
    col_widths = [Inches(2.2), Inches(3.2), Inches(3.2), Inches(3.8)]
    add_table(slide, headers, rows,
              left=Inches(0.3), top=Inches(0.78),
              width=Inches(12.4), height=Inches(6.3),
              col_widths=col_widths)

    add_bottom_bar(slide)
    return slide


def slide8_phases(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)
    add_accent_bar(slide)
    add_heading(slide, "6-Phase Delivery Plan")

    headers = ["Phase", "Duration", "Signals", "Key Deliverables"]
    rows = [
        ("Phase 0 — Foundation", "8 wks", "None",
         "Infra, Kafka, IEMRGateway scaffold, Device Identity & Binding service, HIPAA BAA"),
        ("Phase 1 — Gen 1 MVP", "12 wks", "Bio-impedance + Temp",
         "Device Connectivity, Signal Processing, threshold alerting, Patient Mobile App"),
        ("Phase 2 — Gen 1 Complete", "8 wks", "Bio-impedance + Temp",
         "Baseline engine, SLA alerting, Platform Observability, Audit & Compliance, pen test"),
        ("Phase 3 — Gen 2 Alpha", "12 wks", "+ pH + SpO₂",
         "CDS risk scoring, Claude API LLM, EpicAdapter, SMART on FHIR, Escalation queue"),
        ("Phase 4 — Gen 2 Complete", "10 wks", "+ pH + SpO₂",
         "SOAP draft write-back, CernerAdapter, Research Analytics, clinical pilot"),
        ("Phase 5 — Gen 3", "14 wks", "+ H₂O₂",
         "Full 6-signal composite risk, oxidative stress, population ML, FDA SaMD determination"),
    ]
    col_widths = [Inches(2.5), Inches(1.2), Inches(2.1), Inches(6.9)]
    add_table(slide, headers, rows,
              left=Inches(0.3), top=Inches(0.78),
              width=Inches(12.7), height=Inches(6.35),
              col_widths=col_widths)

    add_bottom_bar(slide)
    return slide


def slide9_risks(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)
    add_accent_bar(slide)
    add_heading(slide, "Top Risks & Decisions to Resolve")

    # Left: Risks
    add_textbox(slide, "RISKS", Inches(0.4), Inches(0.82),
                Inches(5.8), Inches(0.38),
                font_size=13, bold=True, color=NAVY)

    risks = [
        "Epic App Orchard review: 8–12 weeks — submit in Phase 0 to avoid Gen 2 delay.",
        "SMART on FHIR token expiry during long sessions — implement refresh logic in all adapters.",
        "Device serial number uniqueness — enforce at manufacturing + database constraint.",
        "FDA SaMD classification: engage regulatory counsel in Phase 3 planning.",
    ]
    for i, r in enumerate(risks):
        add_textbox(slide, f"▸  {r}",
                    Inches(0.4), Inches(1.28) + i * Inches(1.3),
                    Inches(6.0), Inches(1.15),
                    font_size=12, color=DARK_GREY)

    # Vertical divider
    div = slide.shapes.add_shape(1, Inches(6.7), Inches(0.82), Inches(0.04), Inches(6.2))
    div.fill.solid()
    div.fill.fore_color.rgb = TEAL
    div.line.fill.background()

    # Right: Open Decisions
    add_textbox(slide, "OPEN DECISIONS", Inches(6.9), Inches(0.82),
                Inches(6.0), Inches(0.38),
                font_size=13, bold=True, color=NAVY)

    decisions = [
        ("Hyperscaler", "AWS vs Azure — pending IT infrastructure decision."),
        ("LLM Selection", "Haiku (latency-optimized) vs Sonnet (quality-optimized) — define quality threshold with CDS team."),
        ("Mobile Framework", "React Native vs Flutter for Patient Mobile App."),
        ("Service Mesh", "Istio vs Linkerd for inter-service mTLS."),
        ("Binding Expiry", "Discharge event vs session end vs fixed time window."),
    ]
    for i, (title, body) in enumerate(decisions):
        top = Inches(1.28) + i * Inches(1.1)
        add_textbox(slide, title, Inches(6.9), top,
                    Inches(6.0), Inches(0.32),
                    font_size=12, bold=True, color=TEAL)
        add_textbox(slide, body, Inches(6.9), top + Inches(0.3),
                    Inches(6.0), Inches(0.68),
                    font_size=11, color=DARK_GREY)

    add_bottom_bar(slide)
    return slide


def slide10_next_steps(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)
    add_accent_bar(slide)
    add_heading(slide, "Next Steps")

    items = [
        ("Phase 0 Kickoff",
         "Cloud provisioning, HIPAA BAA execution, Kafka cluster setup, IEMRGateway scaffold."),
        ("Epic App Orchard Application",
         "Submit in Phase 0 to avoid blocking Gen 2 delivery. 8–12 week review lead time."),
        ("Device Identity & Binding",
         "Finalize binding expiry policy and token revocation SLA with clinical and security teams."),
        ("LLM Quality Threshold",
         "Define Haiku vs Sonnet selection criteria with CDS team — latency budget vs clinical accuracy."),
        ("FDA Regulatory Consultation",
         "Initiate SaMD determination discussion in Phase 3 planning with regulatory counsel."),
    ]

    top_start = Inches(0.85)
    for i, (title, body) in enumerate(items):
        top = top_start + i * Inches(1.22)

        # Number circle (via shape)
        circle = slide.shapes.add_shape(9, Inches(0.3), top + Inches(0.05),
                                        Inches(0.45), Inches(0.45))
        circle.fill.solid()
        circle.fill.fore_color.rgb = TEAL
        circle.line.fill.background()
        tf = circle.text_frame
        tf.margin_top = Inches(0.04)
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run = p.add_run()
        run.text = str(i + 1)
        run.font.name = "Calibri"
        run.font.size = Pt(13)
        run.font.bold = True
        run.font.color.rgb = WHITE

        # Title
        add_textbox(slide, title, Inches(0.88), top,
                    Inches(12.1), Inches(0.38),
                    font_size=14, bold=True, color=NAVY)
        # Body
        add_textbox(slide, body, Inches(0.88), top + Inches(0.38),
                    Inches(12.1), Inches(0.72),
                    font_size=12, color=DARK_GREY)

    add_bottom_bar(slide)
    return slide


def main():
    prs = create_presentation()

    slide1_title(prs)
    slide2_principles(prs)
    slide3_arch_layers(prs)
    slide4_device_identity(prs)
    slide5_emr_integration(prs)
    slide6_domain_events(prs)
    slide7_tech_stack(prs)
    slide8_phases(prs)
    slide9_risks(prs)
    slide10_next_steps(prs)

    out = "/Users/GUNDLLX/learn-claude/projects/Multi-Signal Device/Multi-Signal-Device-Technical-Deck.pptx"
    prs.save(out)
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()
