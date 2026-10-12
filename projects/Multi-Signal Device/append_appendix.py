"""
Append Appendix sections with embedded diagrams to existing Word document.
Run: python3 append_appendix.py
"""

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

DOC_PATH = "/Users/GUNDLLX/learn-claude/projects/Multi-Signal Device/Multi-Signal-Device-Architecture-Design.docx"

NAVY = RGBColor(31, 53, 100)
GREY = RGBColor(89, 89, 89)

def add_page_break(doc):
    p = doc.add_paragraph()
    run = p.add_run()
    run.add_break(docx_break_type())
    return p

def docx_break_type():
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    br = OxmlElement('w:br')
    br.set(qn('w:type'), 'page')
    return br

def add_page_break_v2(doc):
    """Add a page break by inserting a paragraph with a page break run."""
    para = doc.add_paragraph()
    run = para.add_run()
    br = OxmlElement('w:br')
    br.set(qn('w:type'), 'page')
    run._r.append(br)
    return para

def add_h2(doc, text):
    """Add a Heading 2 style paragraph in navy bold."""
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.bold = True
    run.font.color.rgb = NAVY
    run.font.size = Pt(14)
    para.style = doc.styles['Heading 2'] if 'Heading 2' in [s.name for s in doc.styles] else doc.styles['Normal']
    # Re-apply color after style (styles can override)
    run.font.color.rgb = NAVY
    return para

def add_explanation(doc, text):
    """Add an explanation paragraph at 10pt with 6pt space after."""
    para = doc.add_paragraph(text)
    para.style = doc.styles['Normal']
    for run in para.runs:
        run.font.size = Pt(10)
    para.paragraph_format.space_after = Pt(6)
    # Apply size to all runs
    for run in para.runs:
        run.font.size = Pt(10)
    return para

def add_image(doc, img_path, width_inches):
    """Add an image paragraph."""
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = para.add_run()
    run.add_picture(img_path, width=Inches(width_inches))
    return para

def add_caption(doc, text):
    """Add italic grey caption at 9pt."""
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.italic = True
    run.font.size = Pt(9)
    run.font.color.rgb = GREY
    para.paragraph_format.space_after = Pt(6)
    return para

BASE = "/Users/GUNDLLX/learn-claude/projects/Multi-Signal Device"

appendices = [
    {
        "heading": "Appendix A: Reference Architecture",
        "explanation": (
            "The reference architecture organizes the platform into five horizontal layers. "
            "Data flows top-to-bottom from the physical device through edge processing, signal intelligence, "
            "domain services, and EMR integration to access endpoints. All inter-layer communication is "
            "event-driven via Apache Kafka. The five layers are: (1) Device & Edge — IoT capture and transmission; "
            "(2) Connectivity & Identity — packet ingestion and device-patient token binding; "
            "(3) Processing & Intelligence — 6-signal fusion and AI risk scoring via Claude API; "
            "(4) Domain Services — care coordination, research analytics, observability, and audit; "
            "(5) Integration & Access — EMR gateway with Port & Adapter pattern, platform web app, and patient mobile app."
        ),
        "image": os.path.join(BASE, "diagrams/reference-architecture.png"),
        "width": 6,
        "caption": "Figure A: Reference Architecture — 5-Layer Platform Model",
    },
    {
        "heading": "Appendix B: Persona Capability Model",
        "explanation": (
            "The capability model maps platform capabilities across six persona swimlanes (Patient, Clinician, "
            "Care Team, Researcher, Hospital Administrator, Corporate Administrator) and three capability rows "
            "(View, Act, Manage). Each cell represents a specific capability delivered to that persona across "
            "the three device generations. The shared data platform footer (Signal Time-Series, Risk Scores, "
            "Audit Log) underpins all personas. This model is the primary tool for scoping per-generation "
            "feature sets and prioritizing delivery."
        ),
        "image": os.path.join(BASE, "diagrams/capability-model.png"),
        "width": 6,
        "caption": "Figure B: Persona Capability Model — 6 Personas × 3 Capability Rows",
    },
    {
        "heading": "Appendix C: Generational Capability Roadmap",
        "explanation": (
            "The generational roadmap defines three sequential capability releases, each tied to the activation "
            "of additional sensor signals. Gen 1 (Bio-impedance + Temperature) delivers the foundational monitoring "
            "and alerting platform. Gen 2 (+ pH + SpO₂) unlocks AI-driven clinical decision support, SMART on FHIR "
            "EMR embedding, and LLM-generated SOAP drafts. Gen 3 (+ Hydrogen Peroxide) completes the full six-signal "
            "composite risk model, adds oxidative stress detection, and enables population-scale ML. This phased "
            "structure reduces clinical validation scope per release and allows the platform to generate value early "
            "while building toward full capability."
        ),
        "image": os.path.join(BASE, "diagrams/device-generations.png"),
        "width": 6,
        "caption": "Figure C: Generational Capability Roadmap — 3 Signal Generations",
    },
    {
        "heading": "Appendix D: Domain Map — Bounded Contexts",
        "explanation": (
            "The domain map visualizes all eleven bounded contexts and their inter-relationships using Domain-Driven "
            "Design (DDD) patterns. Core contexts (Signal Processing, Clinical Decision Support) are shown in red — "
            "these represent the competitive differentiator. Supporting contexts (Patient Engagement, Care Coordination, "
            "Research Analytics, Population Health, Platform Observability) are shown in yellow. Generic contexts "
            "(Device Connectivity, Device Identity & Binding, Audit & Compliance, EMR Integration Gateway) are shown "
            "in green. Arrows are labeled with relationship patterns: Customer-Supplier, Published Language, Open Host "
            "Service, Conformist, and ACL (Anti-Corruption Layer)."
        ),
        "image": os.path.join(BASE, "domain-model/ddd-domain-map.png"),
        "width": 6,
        "caption": "Figure D: DDD Domain Map — 11 Bounded Contexts",
    },
    {
        "heading": "Appendix E: Aggregate Class Diagram",
        "explanation": (
            "The aggregate class diagram shows the internal structure and relationships of the three primary domain "
            "aggregates. SignalObservation (Signal Processing context) contains RawSignals (all six sensor values) "
            "and DerivedMetrics (computed clinical indicators), gated by a QualityScore threshold of 0.6. "
            "RiskAssessment (CDS context) contains a RiskScore with tier classification, a list of contributing "
            "RiskFactors with signal evidence, and an LLM-generated ClinicalSummary. DevicePatientBinding "
            "(Device Identity & Binding context) maps a SerialNumber to a write-once DevicePatientToken with "
            "EMR vendor, binding clinician, and lifecycle status. Each aggregate is the unit of consistency "
            "within its bounded context."
        ),
        "image": os.path.join(BASE, "domain-model/ddd-aggregates.png"),
        "width": 3.5,
        "caption": "Figure E: Aggregate Class Diagram — 3 Core Aggregates",
    },
    {
        "heading": "Appendix F: Domain Events Sequence Diagram",
        "explanation": (
            "The sequence diagram traces the end-to-end event flow from device signal transmission through to "
            "EMR write-back and audit logging. The critical path is: device transmits → Device Connectivity "
            "validates and publishes → Signal Processing derives metrics and raises SignalObservationRecorded → "
            "CDS evaluates and raises RiskAssessmentCompleted → Care Coordination creates escalation → "
            "EMR Integration Gateway writes risk score and SOAP draft back to the clinician’s EMR. All domain "
            "events are simultaneously mirrored to the immutable Audit & Compliance log for compliance and lineage tracking."
        ),
        "image": os.path.join(BASE, "domain-model/ddd-events-sequence.png"),
        "width": 6,
        "caption": "Figure F: Domain Events Sequence — Device to EMR Write-Back",
    },
    {
        "heading": "Appendix G: Solution Architecture — Zone View",
        "explanation": (
            "The solution architecture presents the platform as five deployment zones with explicit data flow "
            "arrows and security boundaries. The Device Zone covers the wearable hardware and edge gateway. "
            "The Platform Zone hosts the Kafka event bus and all microservices. The Integration Zone contains "
            "the IEMRGateway port and its vendor-specific adapters (Epic, Cerner, Generic FHIR). The Access "
            "Zone serves the platform web app, patient mobile app, and EMR-embedded clinician UI. The Compliance "
            "Zone holds the WORM audit log, OpenLineage lineage store, and consent registry. Zone boundaries "
            "enforce security perimeters and data classification policies consistent with HIPAA requirements."
        ),
        "image": os.path.join(BASE, "diagrams/solution-architecture.png"),
        "width": 6,
        "caption": "Figure G: Solution Architecture — 5 Deployment Zones",
    },
]

def main():
    print(f"Opening: {DOC_PATH}")
    doc = Document(DOC_PATH)

    # Page break before appendix section
    add_page_break_v2(doc)

    # Main appendix heading (Heading 1 equivalent)
    h1 = doc.add_heading("Appendix: Architecture Diagrams", level=1)
    for run in h1.runs:
        run.font.color.rgb = NAVY
        run.bold = True

    # Intro paragraph
    intro = doc.add_paragraph(
        "The following diagrams provide visual representations of the platform architecture, capability model, "
        "domain design, and data flow. Each diagram is accompanied by a brief explanation of what it shows "
        "and how to read it."
    )
    for run in intro.runs:
        run.font.size = Pt(10)
    intro.paragraph_format.space_after = Pt(6)

    # Each appendix section
    for i, app in enumerate(appendices):
        # Page break before each appendix section
        add_page_break_v2(doc)

        # Heading
        h2 = doc.add_heading(app["heading"], level=2)
        for run in h2.runs:
            run.font.color.rgb = NAVY
            run.bold = True

        # Explanation
        add_explanation(doc, app["explanation"])

        # Image
        if os.path.exists(app["image"]):
            add_image(doc, app["image"], app["width"])
            print(f"  Inserted image: {app['image']}")
        else:
            doc.add_paragraph(f"[Image not found: {app['image']}]")
            print(f"  WARNING: Image not found: {app['image']}")

        # Caption
        add_caption(doc, app["caption"])

    doc.save(DOC_PATH)
    print(f"\nSaved: {DOC_PATH}")

if __name__ == "__main__":
    main()
