import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

NAVY       = "#000050"
WHITE      = "#FFFFFF"
NEAR_BLACK = "#1A1A1A"
LIGHT_GRAY = "#AAAAAA"

LAYERS = [
    {
        "label": "LAYER 1 — USER EXPERIENCE & TOUCHPOINTS",
        "sublabel": "How users interact with GenAI across Abbott",
        "bg": "#E8F4E8", "border": "#1A7A1A", "text": "#1A5C1A",
        "components": [
            ("Microsoft\nM365 Copilot", "Enterprise\nProductivity"),
            ("Adobe\nGenStudio", "Creative\nWorkflows"),
            ("Veeva CRM\nAI Agents", "Field &\nSales"),
            ("Custom Web\n& Mobile Apps", "Division-built\nExperiences"),
            ("API / SDK\nIntegrations", "Developer\nAccess"),
            ("Chatbots &\nVirtual Assistants", "Five9, Zendesk\nPhenom AI"),
        ]
    },
    {
        "label": "LAYER 2 — AI ORCHESTRATION & AGENT LAYER",
        "sublabel": "Workflow orchestration, prompt engineering, agent frameworks",
        "bg": "#F3E5F5", "border": "#7B1FA2", "text": "#5C0E7A",
        "components": [
            ("Azure AI\nFoundry", "Agent Platform\n& Orchestration"),
            ("LangChain /\nLangfuse", "LLM Chaining\n& Observability"),
            ("Langsmith", "Prompt\nManagement"),
            ("GenAI CoE\nPrompt Library", "Abbott-approved\nPrompt Templates"),
            ("RAG\nPipelines", "Retrieval-Augmented\nGeneration"),
            ("Multi-Agent\nFrameworks", "C3.ai /\nAutoGen"),
        ]
    },
    {
        "label": "LAYER 3 — AI MODEL LAYER",
        "sublabel": "Foundation models, fine-tuned models, specialist models",
        "bg": "#D6E8FF", "border": "#003087", "text": "#003087",
        "components": [
            ("Anthropic\nClaude", "Enterprise LLM\nSonnet / Opus"),
            ("Microsoft\nAzure OpenAI", "GPT-4o /\nAzure-hosted"),
            ("AWS\nBedrock", "Multi-model\nGateway"),
            ("Adobe\nFirefly AI", "Creative &\nImage Models"),
            ("Salesforce\nEinstein AI", "CRM-native\nPredictive AI"),
            ("Specialist\nModels", "Neuron7, IQVIA\nDatabricks ML"),
        ]
    },
    {
        "label": "LAYER 4 — DATA & KNOWLEDGE LAYER",
        "sublabel": "Enterprise data, knowledge bases, vector stores, RAG sources",
        "bg": "#FFF3E0", "border": "#B35A00", "text": "#7A3E00",
        "components": [
            ("Salesforce\nData Cloud", "Unified Customer\n& HCP Data"),
            ("Databricks\nLakehouse", "Enterprise\nData Platform"),
            ("SharePoint /\nOneDrive", "Document &\nContent Store"),
            ("Veeva Vault", "Regulatory &\nClinical Content"),
            ("Vector\nDatabases", "Embeddings &\nSemantic Search"),
            ("SAP /\nERP Data", "Manufacturing\n& Finance Data"),
        ]
    },
    {
        "label": "LAYER 5 — INTEGRATION & API LAYER",
        "sublabel": "Connectivity, APIs, event streaming, middleware",
        "bg": "#FFE8D6", "border": "#C05000", "text": "#7A3000",
        "components": [
            ("Azure\nAPI Management", "API Gateway\n& Rate Limiting"),
            ("MuleSoft", "Enterprise\niPaaS"),
            ("Azure\nService Bus", "Event\nStreaming"),
            ("REST /\nGraphQL APIs", "Service\nContracts"),
            ("Webhook\nFramework", "Real-time\nTriggers"),
            ("ETL /\nData Pipelines", "Azure Data\nFactory"),
        ]
    },
    {
        "label": "LAYER 6 — SECURITY, GOVERNANCE & COMPLIANCE",
        "sublabel": "CoE governance, access control, audit, responsible AI",
        "bg": "#FCE4EC", "border": "#C62828", "text": "#8E0000",
        "components": [
            ("Abbott IAM\n& SSO", "Identity &\nAccess Control"),
            ("GenAI CoE\nGovernance", "ESC Approval\n& Policy"),
            ("Prompt\nFirewall", "Input / Output\nFiltering"),
            ("Audit &\nLogging", "Azure Monitor\n& Logging"),
            ("Data Privacy\n& DLP", "PII Masking\n& Classification"),
            ("Responsible\nAI Framework", "Bias, Safety\n& Compliance"),
        ]
    },
    {
        "label": "LAYER 7 — INFRASTRUCTURE & COMPUTE",
        "sublabel": "Cloud platforms, compute, networking, DevOps",
        "bg": "#E3F2FD", "border": "#0277BD", "text": "#01579B",
        "components": [
            ("Microsoft\nAzure (Primary)", "Abbott Cloud\nPlatform"),
            ("AWS\n(Secondary)", "Multi-cloud\nWorkloads"),
            ("AKS /\nKubernetes", "Container\nOrchestration"),
            ("Azure DevOps\n/ GitHub", "CI/CD\nPipelines"),
            ("CDN &\nNetworking", "Azure Front\nDoor / WAF"),
            ("Key Vault &\nSecrets Mgmt", "Credentials\n& Config"),
        ]
    },
]

# ── Figure setup ──────────────────────────────────────────
fig, ax = plt.subplots(figsize=(26, 22))
ax.set_xlim(0, 26)
ax.set_ylim(0, 22)
ax.axis('off')
fig.patch.set_facecolor('#F8F9FA')

# Title
ax.text(13, 21.6, "Abbott GenAI Technical Architecture",
        ha='center', fontsize=16, fontweight='bold', color=NAVY)
ax.text(13, 21.15, "Multi-Layer Reference Architecture supporting 220 Use Cases across 15 Divisions",
        ha='center', fontsize=10, color=LIGHT_GRAY)

# Layout constants
LAYER_X    = 0.25
TOTAL_W    = 25.5
LABEL_W    = 2.3
CAP_X      = LAYER_X + LABEL_W + 0.1
CAP_AREA_W = TOTAL_W - LABEL_W - 0.3
GAP        = 0.1
N_LAYERS   = len(LAYERS)
LAYER_H    = 2.3
LAYER_GAP  = 0.18

# Draw layers bottom-up (layer 7 at bottom, layer 1 at top)
for idx, layer in enumerate(LAYERS):
    y = 0.3 + (N_LAYERS - 1 - idx) * (LAYER_H + LAYER_GAP)
    h = LAYER_H
    caps = layer["components"]
    n = len(caps)
    cap_w = (CAP_AREA_W - (n - 1) * GAP) / n

    # Layer background
    bg = FancyBboxPatch((LAYER_X, y), TOTAL_W, h,
                        boxstyle="round,pad=0.04",
                        facecolor=layer["bg"], edgecolor=layer["border"], linewidth=1.8)
    ax.add_patch(bg)

    # Layer label (left side)
    ax.text(LAYER_X + 0.12, y + h - 0.28, layer["label"],
            ha='left', va='center', fontsize=9, fontweight='bold',
            color=layer["text"])
    ax.text(LAYER_X + 0.12, y + h - 0.58, layer["sublabel"],
            ha='left', va='center', fontsize=7.5, color=layer["text"],
            style='italic')

    # Component boxes
    for i, (name, subtitle) in enumerate(caps):
        bx = CAP_X + i * (cap_w + GAP)
        by = y + 0.18
        bh = h - 0.35

        comp_box = FancyBboxPatch((bx, by), cap_w, bh,
                                  boxstyle="round,pad=0.02",
                                  facecolor=WHITE, edgecolor=layer["border"],
                                  linewidth=0.9)
        ax.add_patch(comp_box)

        # Component name (bold, top)
        ax.text(bx + cap_w/2, by + bh/2 + 0.2, name,
                ha='center', va='center', fontsize=8.5, fontweight='bold',
                color=NEAR_BLACK, multialignment='center', linespacing=1.3)

        # Subtitle (smaller, bottom)
        ax.text(bx + cap_w/2, by + 0.3, subtitle,
                ha='center', va='center', fontsize=7.5, color="#555555",
                style='italic', multialignment='center', linespacing=1.2)

    # Arrow down to next layer (except last)
    if idx < N_LAYERS - 1:
        next_y = 0.3 + (N_LAYERS - 2 - idx) * (LAYER_H + LAYER_GAP) + LAYER_H
        ax.annotate("", xy=(13, next_y + LAYER_GAP - 0.04),
                    xytext=(13, y),
                    arrowprops=dict(arrowstyle="-|>", color="#AAAAAA",
                                   lw=1.5))

# Use case count badges (right side)
badge_data = [
    ("107 use cases\nEnterprise-wide", 0),
    ("WIP / Scaling\n43 active", 1),
    ("40 in production\nacross divisions", 2),
    ("133 Buy / 86 Build", 3),
    ("15 divisions\nintegrated", 4),
    ("ESC governed\nCoE approved", 5),
    ("Azure primary\nAWS secondary", 6),
]

for idx, (badge, layer_idx) in enumerate(badge_data):
    y = 0.3 + (N_LAYERS - 1 - layer_idx) * (LAYER_H + LAYER_GAP)
    by = y + LAYER_H/2 - 0.3
    bx = LAYER_X + TOTAL_W + 0.08
    badge_box = FancyBboxPatch((bx, by), 1.8, 0.65,
                               boxstyle="round,pad=0.04",
                               facecolor=LAYERS[layer_idx]["border"],
                               edgecolor=LAYERS[layer_idx]["border"],
                               linewidth=0)
    ax.add_patch(badge_box)
    ax.text(bx + 0.9, by + 0.32, badge,
            ha='center', va='center', fontsize=7, color=WHITE,
            fontweight='bold', multialignment='center', linespacing=1.2)

# Legend
legend_items = [
    ("Layer 1–2: Experience & Orchestration", "#1A7A1A"),
    ("Layer 3: AI Models", "#003087"),
    ("Layer 4–5: Data & Integration", "#B35A00"),
    ("Layer 6–7: Security & Infrastructure", "#C62828"),
]
lx = 0.4
for i, (lbl, col) in enumerate(legend_items):
    rect = FancyBboxPatch((lx + i*6.3, 0.05), 6.0, 0.28,
                          boxstyle="round,pad=0.02",
                          facecolor=WHITE, edgecolor=col, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(lx + i*6.3 + 3.0, 0.19, lbl,
            ha='center', va='center', fontsize=8, color=col, fontweight='bold')

ax.set_xlim(0, 28)
plt.tight_layout(pad=0.2)
plt.savefig("technical-architecture.png", dpi=180,
            bbox_inches='tight', facecolor='#F8F9FA')
plt.savefig("technical-architecture.svg",
            bbox_inches='tight', facecolor='#F8F9FA')
plt.close()
print("Technical architecture saved.")

# ── draw.io version ────────────────────────────────────────
import xml.etree.ElementTree as ET

def make_diagram(name):
    mxfile = ET.Element("mxfile", host="app.diagrams.net")
    diagram = ET.SubElement(mxfile, "diagram", name=name)
    mxgraph = ET.SubElement(diagram, "mxGraphModel",
                             dx="1422", dy="762", grid="0", gridSize="10",
                             guides="1", tooltips="1", connect="1",
                             arrows="1", fold="1", page="0",
                             pageScale="1", pageWidth="1654", pageHeight="1169",
                             math="0", shadow="0")
    root = ET.SubElement(mxgraph, "root")
    ET.SubElement(root, "mxCell", id="0")
    ET.SubElement(root, "mxCell", id="1", parent="0")
    return mxfile, root

def add_cell(root, cell_id, value, style, x, y, w, h):
    cell = ET.SubElement(root, "mxCell", id=str(cell_id), value=value,
                         style=style, vertex="1", parent="1")
    ET.SubElement(cell, "mxGeometry",
                  x=str(x), y=str(y), width=str(w), height=str(h),
                  **{"as": "geometry"})
    return cell

mxfile, root = make_diagram("Technical Architecture")
idc = 10

# Title
add_cell(root, idc, "Abbott GenAI Technical Architecture",
         "text;html=1;strokeColor=none;fillColor=none;align=center;"
         "verticalAlign=middle;fontColor=#000050;fontSize=18;fontStyle=1;",
         20, 10, 1600, 45)
idc += 1
add_cell(root, idc,
         "Multi-Layer Reference Architecture supporting 220 Use Cases across 15 Divisions",
         "text;html=1;strokeColor=none;fillColor=none;align=center;"
         "verticalAlign=middle;fontColor=#888888;fontSize=11;fontStyle=2;",
         20, 55, 1600, 30)
idc += 1

LAYER_X_DIO  = 20
LAYER_W_DIO  = 1400
LABEL_W_DIO  = 200
CAP_X_DIO    = LAYER_X_DIO + LABEL_W_DIO + 8
CAP_AREA_DIO = LAYER_W_DIO - LABEL_W_DIO - 20
LAYER_H_DIO  = 130
LAYER_GAP_DIO = 12
GAP_DIO = 8

for idx, layer in enumerate(LAYERS):
    y = 95 + idx * (LAYER_H_DIO + LAYER_GAP_DIO)
    c = layer

    # Layer background
    add_cell(root, idc, "",
             f"rounded=1;whiteSpace=wrap;html=1;fillColor={c['bg']};"
             f"strokeColor={c['border']};strokeWidth=2;",
             LAYER_X_DIO, y, LAYER_W_DIO, LAYER_H_DIO)
    idc += 1

    # Layer label
    add_cell(root, idc,
             f"<b>{layer['label']}</b><br/><i style='font-size:10px;'>{layer['sublabel']}</i>",
             f"text;html=1;strokeColor=none;fillColor=none;align=left;"
             f"verticalAlign=middle;fontColor={c['text']};fontSize=11;",
             LAYER_X_DIO + 6, y + 8, LABEL_W_DIO - 10, LAYER_H_DIO - 16)
    idc += 1

    # Component boxes
    caps = layer["components"]
    n = len(caps)
    cap_w = (CAP_AREA_DIO - (n-1)*GAP_DIO) / n
    cap_h = LAYER_H_DIO - 20

    for i, (name, subtitle) in enumerate(caps):
        bx = CAP_X_DIO + i*(cap_w + GAP_DIO)
        by = y + 10
        label = (f"<b>{name}</b><br/>"
                 f"<font style='font-size:9px;color:#555555;'><i>{subtitle}</i></font>")
        add_cell(root, idc, label,
                 f"rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;"
                 f"strokeColor={c['border']};strokeWidth=1;"
                 f"fontColor=#1A1A1A;fontSize=10;verticalAlign=middle;",
                 bx, by, cap_w, cap_h)
        idc += 1

    # Arrow between layers
    if idx < len(LAYERS) - 1:
        arrow_cell = ET.SubElement(root, "mxCell",
                                   id=str(idc), value="",
                                   style="edgeStyle=orthogonalEdgeStyle;"
                                         "strokeColor=#AAAAAA;strokeWidth=1.5;"
                                         "exitX=0.5;exitY=1;exitDx=0;exitDy=0;"
                                         "entryX=0.5;entryY=0;entryDx=0;entryDy=0;",
                                   edge="1", parent="1",
                                   source=str(idc-n-2),
                                   target=str(idc+1))
        ET.SubElement(arrow_cell, "mxGeometry", relative="1", **{"as": "geometry"})
        idc += 1

tree = ET.ElementTree(mxfile)
ET.indent(tree, space="  ")
tree.write("technical-architecture.drawio", encoding="unicode", xml_declaration=False)
print("draw.io file saved.")
print("\nAll technical architecture files complete.")
