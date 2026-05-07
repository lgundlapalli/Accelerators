import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import xml.etree.ElementTree as ET

NAVY       = "#000050"
WHITE      = "#FFFFFF"
NEAR_BLACK = "#1A1A1A"
LIGHT_GRAY = "#AAAAAA"

# ── 8 Layers — index 0 = BOTTOM (Infrastructure), index 7 = TOP (UX) ─────
LAYERS = [
    {
        "label": "LAYER 1 — CLOUD INFRASTRUCTURE & PLATFORM SERVICES",
        "sublabel": "Azure primary · AWS secondary · GCP · compute, networking, containers, DevOps, observability",
        "bg": "#E3F2FD", "border": "#0277BD", "text": "#01579B",
        "tall": True,
        "groups": [
            {
                "label": "MICROSOFT AZURE — AI Services & Infrastructure",
                "color": "#0277BD",
                "components": [
                    ("Azure AI\nFoundry",               "Agent & Model\nOrchestration"),
                    ("Azure OpenAI\nService",           "GPT-4o · o1\nDALL-E · Whisper"),
                    ("Azure Machine\nLearning",         "MLOps &\nModel Registry"),
                    ("Azure AI\nSearch",                "Vector Store\n& RAG Index"),
                    ("Azure Cognitive\nServices",       "Vision · Speech\nLanguage · Form"),
                    ("AKS /\nKubernetes",               "Container\nOrchestration"),
                    ("Azure DevOps\n/ GitHub Actions",  "CI/CD\nPipelines"),
                    ("Azure Key Vault\n/ App Config",   "Secrets &\nConfig Mgmt"),
                    ("Azure Front Door\n/ WAF / CDN",   "Networking &\nEdge Security"),
                    ("Azure Monitor\n/ Log Analytics",  "Platform\nObservability"),
                ]
            },
            {
                "label": "AWS — AI Services & Infrastructure",
                "color": "#FF9900",
                "components": [
                    ("AWS\nBedrock",                    "Multi-model\nGateway"),
                    ("AWS\nSageMaker",                  "Model Training\n& Fine-tuning"),
                    ("AWS\nComprehend",                 "NLP &\nEntity Extraction"),
                    ("Amazon\nRekognition",             "Image & Video\nAI Analysis"),
                    ("Amazon\nLex / Polly",             "Conversational\nAI & TTS"),
                    ("Amazon EKS /\nFargate",           "Container\nOrchestration"),
                    ("AWS CodePipeline\n/ CodeBuild",   "CI/CD\nPipelines"),
                    ("AWS Secrets\nManager / KMS",      "Secrets &\nKey Mgmt"),
                    ("AWS CloudFront\n/ WAF / Shield",  "Networking &\nEdge Security"),
                    ("Amazon CloudWatch\n/ X-Ray",      "Platform\nObservability"),
                ]
            },
            {
                "label": "GOOGLE CLOUD — AI Services & Infrastructure",
                "color": "#34A853",
                "components": [
                    ("Google Vertex\nAI",               "Gemini · PaLM\nModel Garden"),
                    ("Google Cloud\nNatural Language",  "NLP · Sentiment\nEntity Analysis"),
                    ("Google Cloud\nVision / Video AI", "Image & Video\nAI Analysis"),
                    ("Google Cloud\nSpeech & TTS",      "Speech-to-Text\nText-to-Speech"),
                    ("Google\nDuet AI",                 "Workspace AI\n& Code Assist"),
                    ("Google\nKubernetes Engine",       "Container\nOrchestration"),
                    ("Cloud Build\n/ Cloud Deploy",     "CI/CD\nPipelines"),
                    ("Secret Manager\n/ Cloud KMS",     "Secrets &\nKey Mgmt"),
                    ("Cloud CDN\n/ Cloud Armor",        "Networking &\nEdge Security"),
                    ("Cloud Monitoring\n/ Cloud Trace", "Platform\nObservability"),
                ]
            },
        ]
    },
    {
        "label": "LAYER 2 — SECURITY & GOVERNANCE",
        "sublabel": "Identity, access, compliance, responsible AI, CoE oversight",
        "bg": "#FFEBEE", "border": "#C62828", "text": "#8E0000",
        "components": [
            ("Abbott IAM\n& SSO",              "Identity &\nAccess Control"),
            ("GenAI CoE\nGovernance",          "ESC Approval\n& Policy"),
            ("Prompt Firewall",                "Input / Output\nFiltering"),
            ("DLP & PII\nMasking",             "Data Privacy\n& Classification"),
            ("Audit &\nLogging",               "Azure Monitor\n& SIEM"),
            ("Responsible AI\nFramework",      "Bias, Safety\n& Compliance"),
            ("Snyk / Checkov\n/ SonarQube",    "DevSecOps\nCode Scanning"),
            ("Veeva Vault\nCompliance",        "Regulated\nContent Control"),
        ]
    },
    {
        "label": "LAYER 3 — DATA & KNOWLEDGE",
        "sublabel": "Enterprise data, vector stores, embeddings, RAG sources",
        "bg": "#FFF3E0", "border": "#E65100", "text": "#BF360C",
        "components": [
            ("Salesforce\nData Cloud",         "Unified Customer\n& HCP Data"),
            ("Databricks\nLakehouse",          "Enterprise\nData Platform"),
            ("SharePoint /\nOneDrive",         "Document &\nContent Store"),
            ("Veeva Vault",                    "Regulatory &\nClinical Content"),
            ("Azure AI Search\n/ Pinecone",    "Vector DB &\nSemantic Search"),
            ("SAP / ERP\nData",                "Manufacturing\n& Finance Data"),
            ("Azure Data\nFactory",            "ETL & Data\nIngestion"),
            ("Apache Kafka\n/ Service Bus",    "Real-time\nData Streaming"),
        ]
    },
    {
        "label": "LAYER 4 — AI MODEL LAYER",
        "sublabel": "Foundation models · fine-tuned models · specialist domain models · model routing",
        "bg": "#EDE7F6", "border": "#5E35B1", "text": "#311B92",
        "tall_model": True,
        "groups": [
            {
                "label": "FRONTIER / FOUNDATION LLMs",
                "color": "#5E35B1",
                "components": [
                    ("Anthropic\nClaude 3.5 / 4",    "Sonnet · Opus\nEnterprise Reasoning"),
                    ("OpenAI\nGPT-4o / o1",          "Azure-hosted\nCoding & Analysis"),
                    ("Google\nGemini 1.5 Pro",        "Vertex AI\nLong-context · Multi-modal"),
                    ("Meta\nLlama 3.1 / 3.2",        "AWS Bedrock\nOpen-weight Fine-tune"),
                    ("Mistral\nLarge / Mixtral",      "Bedrock · Azure\nEfficiency Models"),
                ]
            },
            {
                "label": "SPECIALIST & DOMAIN MODELS",
                "color": "#AD1457",
                "components": [
                    ("Adobe\nFirefly",                "Creative &\nImage Generation"),
                    ("Salesforce\nEinstein AI",       "CRM-native\nPredictive AI"),
                    ("Databricks\nMLflow Models",     "Custom ML &\nAbbott Fine-tunes"),
                    ("Neuron7\nField AI",             "Field Service\nDomain Model"),
                    ("IQVIA\nAI Models",              "Pharma &\nMarket Intelligence", "future"),
                ]
            },
            {
                "label": "CONTENT & LANGUAGE MODELS",
                "color": "#00695C",
                "components": [
                    ("Writer /\nWriter.com",          "Enterprise\nContent Gen"),
                    ("Persado\nAI",                   "Marketing\nLanguage Optimization", "future"),
                    ("OpenAI\nDALL-E 3",              "Image\nGeneration"),
                    ("ElevenLabs\n/ Azure TTS",       "Voice &\nAudio Generation"),
                    ("Cohere\nEmbed / Rerank",        "Embeddings &\nSemantic Search", "future"),
                ]
            },
            {
                "label": "TRANSLATION MODELS",
                "color": "#00838F",
                "components": [
                    ("Collate\nAI",                   "Content Synthesis\n& Translation"),
                    ("Accolad\nTranslation",          "Human-AI Hybrid\nLocalization"),
                    ("SmartCat\nPlatform",            "AI-powered\nTranslation TMS"),
                    ("Azure\nTranslator",             "Neural Machine\nTranslation (Azure)"),
                    ("Google Cloud\nTranslation",     "Neural Machine\nTranslation (GCP)", "future"),
                ]
            },
        ]
    },
    {
        "label": "LAYER 5 \u2014 DEVELOPER EXPERIENCE",
        "sublabel": "Enterprise-approved toolchain  |  Green border = Approved  \u00b7  Amber = In Evaluation  \u00b7  Gray = Archived",
        "bg": "#E8F5E9", "border": "#2E7D32", "text": "#1B5E20",
        "tall_model": True,
        "groups": [
            {
                "label": "CODE & BUILD",
                "color": "#2E7D32",
                "components": [
                    ("GitHub\nSCM",              "Source Control\n& Collaboration",    "approved"),
                    ("GitHub\nActions",          "CI/CD Automation\n& Pipelines",      "approved"),
                    ("GitHub\nCopilot",          "AI Pair Programmer\n1,275 seats",    "approved"),
                    ("jFrog\nArtifactory",       "Package &\nArtifact Registry",       "approved"),
                    ("Claude\nCode",             "Agentic AI\nCoding Assistant",       "trial"),
                    ("ChatGPT\nEnterprise",      "AI Coding &\nDocumentation",         "trial"),
                    ("CodeRabbit",               "AI Code\nReview",                    "assess"),
                    ("Rematiq",                  "AI Workflow\nAutomation",            "assess"),
                    ("Jenkins",                  "Legacy CI/CD\n(deprecated)",         "archived"),
                    ("Bitbucket",                "Legacy Source\nControl",             "archived"),
                ]
            },
            {
                "label": "PLANNING & COLLABORATION",
                "color": "#2E7D32",
                "components": [
                    ("Jira",                     "Work Tracking\n& Planning",          "approved"),
                    ("Confluence",               "Docs & Knowledge\nMgmt",             "approved"),
                    ("ALM",                      "Lifecycle &\nRegulated Delivery",    "approved"),
                    ("MS Teams\n/ Slack",       "Collaboration\n& Communication",     "approved"),
                    ("Atlassian\nRovo",         "AI-native\nProject Assistant",       "trial"),
                    ("ChatGPT\nEnterprise",     "Requirements &\nDocumentation",      "trial"),
                    ("Claude\nEnterprise",      "Analysis &\nRequirements AI",        "assess"),
                    ("Notion AI",               "AI Knowledge\nManagement",           "assess"),
                ]
            },
            {
                "label": "TEST & QUALITY",
                "color": "#2E7D32",
                "components": [
                    ("BrowserStack",             "Cross-browser &\nDevice Testing",    "approved"),
                    ("Tosca",                    "Functional &\nRegression Testing",   "approved"),
                    ("Selenium",                 "Test Automation\nFramework",         "approved"),
                ]
            },
            {
                "label": "SECURITY & COMPLIANCE",
                "color": "#2E7D32",
                "components": [
                    ("GitHub Adv.\nSecurity",   "Code Scanning\n& Secret Detection",  "approved"),
                    ("ALM",                      "Traceability &\nAudit Governance",   "approved"),
                    ("Ketryx",                   "Regulated SW\nCompliance AI",        "assess"),
                    ("Collate",                  "AI Compliance\n& Lifecycle",         "assess"),
                    ("Aikido",                   "AI Security\nScanning",              "assess"),
                    ("Regology",                "Regulatory\nIntelligence AI",        "assess"),
                    ("Veracode",                "SAST/DAST\nScanning",               "archived"),
                    ("SonarQube",               "Code Quality\nAnalysis",            "archived"),
                ]
            },
            {
                "label": "OBSERVABILITY & MONITORING",
                "color": "#2E7D32",
                "components": [
                    ("New Relic",               "Platform\nObservability",            "approved"),
                    ("Sentry",                  "Error Tracking\n& Alerting",         "approved"),
                    ("OpenTelemetry",           "Distributed\nTracing",               "approved"),
                    ("LangSmith /\nLangFuse",  "LLM Prompt &\nTrace Mgmt",           "trial"),
                    ("Azure AI Foundry\nTrace","LLM Eval &\nObservability",          "trial"),
                    ("Arize Phoenix",           "AI Model\nMonitoring",               "assess"),
                    ("Ragas",                   "RAG Evaluation\nFramework",          "assess"),
                    ("Whylabs",                 "Data & Model\nQuality Monitor",      "assess"),
                ]
            },
            {
                "label": "DESIGN & UX",
                "color": "#2E7D32",
                "components": [
                    ("Figma",                   "UI/UX Design\n& Prototyping",        "approved"),
                    ("Miro",                    "Ideation &\nCollaboration",          "approved"),
                    ("Adobe Express\n/ Firefly","Creative &\nMarketing Assets",      "approved"),
                    ("Miro AI",                 "AI Diagrams\n& Design",              "trial"),
                    ("Figma AI",                "AI UX\nAssistant",                   "trial"),
                    ("Adobe Foundry",           "AI Creative\nPlatform",              "assess"),
                ]
            },
        ]
    },
    {
        "label": "LAYER 6 — INTEGRATION & ORCHESTRATION",
        "sublabel": "API management, agent frameworks, RAG pipelines, event streaming, middleware",
        "bg": "#F3E5F5", "border": "#7B1FA2", "text": "#5C0E7A",
        "components": [
            ("Azure API\nManagement",          "API Gateway\n& Rate Limiting"),
            ("Azure AI Foundry\nAgents SDK",   "Agent Platform\n& Orchestration"),
            ("LangChain /\nLangGraph",         "LLM Chaining\n& Workflow"),
            ("AutoGen /\nSemantic Kernel",     "Multi-Agent\nFrameworks"),
            ("RAG\nPipelines",                 "Retrieval-Augmented\nGeneration"),
            ("Azure Service\nBus / Kafka",     "Event\nStreaming"),
            ("REST / GraphQL\n/ Webhooks",     "Service\nContracts"),
        ]
    },
    {
        "label": "LAYER 7 — AI APPLICATIONS",
        "sublabel": "Division solutions, GenAI apps, productivity tools, custom builds",
        "bg": "#D6E8FF", "border": "#003087", "text": "#003087",
        "components": [
            ("Microsoft M365\nCopilot",        "Enterprise\nProductivity"),
            ("Adobe\nGenStudio",               "Creative &\nContent Workflows"),
            ("SmartRep\nCall Planning",        "Field Sales\nAI (EPD)"),
            ("Veeva CRM\nAI Agents",           "HCP Engagement\n& Sales"),
            ("Custom Web\n& Mobile Apps",      "Division-built\nExperiences"),
            ("GenAI CoE\nPrompt Library",      "Abbott-approved\nTemplates"),
            ("Five9 /\nZendesk AI",            "Customer Service\nAssistants"),
            ("Databricks\nInsights Apps",      "Analytics &\nReporting AI"),
        ]
    },
    {
        "label": "LAYER 8 — USER EXPERIENCE & TOUCHPOINTS",
        "sublabel": "Enterprise touchpoints + custom UI build technologies — employees, field reps, customers, developers",
        "bg": "#FCE4EC", "border": "#AD1457", "text": "#880E4F",
        "tall_model": True,
        "groups": [
            {
                "label": "ENTERPRISE TOUCHPOINTS",
                "color": "#AD1457",
                "components": [
                    ("M365 Copilot\n/ Teams",      "Enterprise AI\nProductivity"),
                    ("Veeva CRM\n/ Salesforce",    "Field &\nSales Tools"),
                    ("Five9 /\nZendesk AI",        "Customer Service\n& IVR"),
                    ("Adobe",                      "Creative &\nContent Workflows"),
                    ("MIA",                        "Enterprise AI\nAssistant (Abbott)"),
                ]
            },
            {
                "label": "CUSTOM UI — WEB & MOBILE",
                "color": "#6A1B9A",
                "components": [
                    ("React.js /\nNext.js",         "Web SPA &\nFull-stack"),
                    ("Spring Boot\n/ Node.js",      "Backend API\n& Microservices"),
                    ("React Native\n/ Flutter",     "Cross-platform\nMobile Apps"),
                    ("MS Teams\nApp SDK",           "Embedded Teams\nTab / Bot"),
                ]
            },
            {
                "label": "DIVISIONAL FUNCTIONAL APPS",
                "color": "#E65100",
                "components": [
                    ("SmartRep\nCall Planning",    "Field Sales AI\nEPD Production"),
                    ("Synthesia",                  "AI Video &\nAvatar Generation"),
                    ("Pharmacovigilance\n/ Safety","Adverse Event\n& Regulatory AI"),
                    ("Custom Division\nApps",      "220+ Abbott-built\nGenAI Solutions"),
                ]
            },
        ]
    },
]

# ── Heights per layer type ─────────────────────────────────
BASE_H       = 2.55
TALL_H       = 4.5      # infra layer (3 groups × 10 cols)
TALL_MODEL_H = 3.8      # model layer (4 groups × 5 cols)
TALL_DEVEX_H = 5.0      # devex layer (8 lifecycle phases)
LAYER_GAP    = 0.18
N_LAYERS     = len(LAYERS)

def layer_h(layer):
    if layer.get("tall"):        return TALL_H
    if layer.get("tall_model"):  return TALL_MODEL_H
    if layer.get("tall_devex"):  return TALL_DEVEX_H
    return BASE_H

total_h = sum(layer_h(l) for l in LAYERS) + (N_LAYERS - 1) * LAYER_GAP + 1.6

fig, ax = plt.subplots(figsize=(30, total_h))
ax.set_xlim(0, 30)
ax.set_ylim(0, total_h)
ax.axis('off')
fig.patch.set_facecolor('#F0F2F5')

ax.text(15, total_h - 0.42,
        "Abbott GenAI — Platform & Tools Reference Architecture",
        ha='center', fontsize=16, fontweight='bold', color=NAVY)
ax.text(15, total_h - 0.87,
        "8-Layer Architecture  |  UX on top · Cloud Infrastructure at base  |  Azure Primary · AWS Secondary · GCP  |  Separate AI Model Layer",
        ha='center', fontsize=9.5, color="#555555")

LAYER_X  = 0.25
TOTAL_W  = 28.8
LABEL_W  = 2.45
CAP_X    = LAYER_X + LABEL_W + 0.1
CAP_AREA = TOTAL_W - LABEL_W - 0.3
GAP      = 0.1

# Build y-positions bottom-up
y_positions = []
y_cur = 0.35
for layer in LAYERS:
    y_positions.append(y_cur)
    y_cur += layer_h(layer) + LAYER_GAP

# Status styles — border/bg/text per status flag
STATUS = {
    "approved": {"bg": WHITE,     "ec": None,      "tc": NEAR_BLACK, "lw": 1.0, "ls": "-",       "badge": ""},
    "trial":    {"bg": "#E3F2FD", "ec": "#1565C0", "tc": "#0D47A1",  "lw": 1.5, "ls": "-",       "badge": " [T]"},
    "assess":   {"bg": "#FFFDE7", "ec": "#F9A825", "tc": "#E65100",  "lw": 1.5, "ls": (0,(4,2)), "badge": " [~]"},
    "archived": {"bg": "#F5F5F5", "ec": "#9E9E9E", "tc": "#9E9E9E",  "lw": 1.0, "ls": (0,(3,3)), "badge": " [x]"},
    "future":   {"bg": "#FFFDE7", "ec": "#F9A825", "tc": "#E65100",  "lw": 1.5, "ls": (0,(4,2)), "badge": " [!]"},
}

def draw_group_layer(ax, layer, y, lh):
    """Render a grouped layer (infra or model)."""
    groups   = layer["groups"]
    ng       = len(groups)
    gap_g    = 0.12 if ng <= 4 else 0.08
    gw       = (CAP_AREA - (ng - 1) * gap_g) / ng

    for gi, grp in enumerate(groups):
        gx    = CAP_X + gi * (gw + gap_g)
        gcol  = grp["color"]
        gcaps = grp["components"]
        nc    = len(gcaps)

        # Group header bar
        hdr = FancyBboxPatch((gx, y + lh - 0.72), gw, 0.42,
                             boxstyle="round,pad=0.02",
                             facecolor=gcol, edgecolor="none")
        ax.add_patch(hdr)
        ax.text(gx + gw/2, y + lh - 0.51, grp["label"],
                ha='center', va='center', fontsize=6.8, fontweight='bold', color=WHITE)

        cap_w = (gw - (nc - 1) * GAP) / nc
        bh    = lh - 1.0
        by    = y + 0.18

        for ci, cap in enumerate(gcaps):
            name, subtitle = cap[0], cap[1]
            st    = cap[2] if len(cap) > 2 else "approved"
            s     = STATUS.get(st, STATUS["approved"])
            ec    = s["ec"] if s["ec"] else gcol
            bx    = gx + ci * (cap_w + GAP)
            comp  = FancyBboxPatch((bx, by), cap_w, bh,
                                   boxstyle="round,pad=0.02",
                                   facecolor=s["bg"], edgecolor=ec,
                                   linewidth=s["lw"], linestyle=s["ls"])
            ax.add_patch(comp)
            ax.text(bx + cap_w/2, by + bh/2 + 0.17,
                    name + s["badge"],
                    ha='center', va='center', fontsize=7.0, fontweight='bold',
                    color=s["tc"], multialignment='center', linespacing=1.25)
            ax.text(bx + cap_w/2, by + 0.25, subtitle,
                    ha='center', va='center', fontsize=6.3,
                    color=s["tc"] if st != "approved" else "#555555",
                    style='italic', multialignment='center', linespacing=1.2)


# Draw all layers
for idx, layer in enumerate(LAYERS):
    y  = y_positions[idx]
    lh = layer_h(layer)
    c  = layer

    bg = FancyBboxPatch((LAYER_X, y), TOTAL_W, lh,
                        boxstyle="round,pad=0.04",
                        facecolor=c["bg"], edgecolor=c["border"], linewidth=2)
    ax.add_patch(bg)

    ax.text(LAYER_X + 0.13, y + lh - 0.27, c["label"],
            ha='left', va='center', fontsize=8.5, fontweight='bold', color=c["text"])
    ax.text(LAYER_X + 0.13, y + lh - 0.54, c["sublabel"],
            ha='left', va='center', fontsize=6.8, color=c["text"], style='italic')

    if layer.get("tall") or layer.get("tall_model"):
        draw_group_layer(ax, layer, y, lh)
    elif layer.get("tall_devex"):
        phases = layer["phases"]
        np_    = len(phases)
        pw     = (CAP_AREA - (np_ - 1) * GAP) / np_
        ph     = lh - 0.9
        py     = y + 0.2
        # Column headers
        for hi, hlbl in enumerate(["LIFECYCLE PHASE", "EXISTING TOOLS", "NEW / PIPELINE", "VALUE METRIC"]):
            hx = CAP_X + (pw * hi / 4) if hi > 0 else CAP_X
        # Phase boxes
        for i, (phase, existing, pipeline, value) in enumerate(phases):
            bx = CAP_X + i * (pw + GAP)
            # phase box
            pb = FancyBboxPatch((bx, py), pw, ph,
                                boxstyle="round,pad=0.02",
                                facecolor=WHITE, edgecolor=c["border"], linewidth=1.0)
            ax.add_patch(pb)
            # Phase name header
            phdr = FancyBboxPatch((bx, py + ph - 0.52), pw, 0.42,
                                  boxstyle="round,pad=0.02",
                                  facecolor=c["border"], edgecolor="none")
            ax.add_patch(phdr)
            ax.text(bx + pw/2, py + ph - 0.31, phase,
                    ha='center', va='center', fontsize=7.0, fontweight='bold',
                    color=WHITE, multialignment='center', linespacing=1.2)
            # Existing
            ax.text(bx + pw/2, py + ph - 0.78, "Existing",
                    ha='center', fontsize=6.2, color="#888888", style='italic')
            ax.text(bx + pw/2, py + ph - 1.22, existing,
                    ha='center', va='center', fontsize=6.8, color=NEAR_BLACK,
                    multialignment='center', linespacing=1.2)
            ax.plot([bx+0.06, bx+pw-0.06], [py+ph-1.48, py+ph-1.48],
                    color=c["border"], lw=0.4, alpha=0.4)
            # New/pipeline
            pip_col = "#E65100" if pipeline.strip() != "—" else "#AAAAAA"
            ax.text(bx + pw/2, py + ph - 1.65, "New / Pipeline",
                    ha='center', fontsize=6.2, color="#888888", style='italic')
            ax.text(bx + pw/2, py + ph - 2.05, pipeline,
                    ha='center', va='center', fontsize=6.8, color=pip_col,
                    fontweight='bold', multialignment='center', linespacing=1.2)
            ax.plot([bx+0.06, bx+pw-0.06], [py+ph-2.3, py+ph-2.3],
                    color=c["border"], lw=0.4, alpha=0.4)
            # Value
            ax.text(bx + pw/2, py + ph - 2.48, "Value",
                    ha='center', fontsize=6.2, color="#888888", style='italic')
            ax.text(bx + pw/2, py + 0.22, value,
                    ha='center', va='bottom', fontsize=6.5, color="#1B5E20",
                    multialignment='center', linespacing=1.2)
    else:
        caps  = layer["components"]
        n     = len(caps)
        cap_w = (CAP_AREA - (n - 1) * GAP) / n
        for i, (name, subtitle) in enumerate(caps):
            bx = CAP_X + i * (cap_w + GAP)
            by = y + 0.2
            bh = lh - 0.38
            comp = FancyBboxPatch((bx, by), cap_w, bh,
                                  boxstyle="round,pad=0.02",
                                  facecolor=WHITE, edgecolor=c["border"], linewidth=0.9)
            ax.add_patch(comp)
            ax.text(bx + cap_w/2, by + bh/2 + 0.18, name,
                    ha='center', va='center', fontsize=7.8, fontweight='bold',
                    color=NEAR_BLACK, multialignment='center', linespacing=1.3)
            ax.text(bx + cap_w/2, by + 0.28, subtitle,
                    ha='center', va='center', fontsize=7.0, color="#555555",
                    style='italic', multialignment='center', linespacing=1.2)

    # Arrow upward
    if idx < N_LAYERS - 1:
        next_y = y_positions[idx + 1]
        mx     = LAYER_X + TOTAL_W / 2
        ax.annotate("", xy=(mx, next_y - 0.02), xytext=(mx, y + lh + 0.02),
                    arrowprops=dict(arrowstyle="-|>", color="#AAAAAA", lw=1.5))

# ── Right-rail cross-cutting callouts ─────────────────────
rail_sections = [
    ("HYPERSCALER\nPLATFORM\nSERVICES",  0, 0, "#0277BD"),
    ("GOVERNANCE\n&\nCOMPLIANCE",        1, 1, "#C62828"),
    ("AI MODEL\nSELECTION\nLAYER",       3, 3, "#5E35B1"),
    ("GENAI\nSOLUTION\nPATTERN",         2, 6, "#003087"),
    ("BUILD\nTOOLCHAIN",                 4, 4, "#2E7D32"),
]
for (lbl, i_bot, i_top, col) in rail_sections:
    y_bot  = y_positions[i_bot]
    y_top  = y_positions[i_top]
    lh_top = layer_h(LAYERS[i_top])
    rh     = (y_top + lh_top) - y_bot
    rb     = FancyBboxPatch((LAYER_X + TOTAL_W + 0.12, y_bot), 1.4, rh,
                            boxstyle="round,pad=0.04",
                            facecolor=WHITE, edgecolor=col, linewidth=1.5)
    ax.add_patch(rb)
    ax.text(LAYER_X + TOTAL_W + 0.82, y_bot + rh/2, lbl,
            ha='center', va='center', fontsize=6.5, fontweight='bold',
            color=col, multialignment='center', linespacing=1.3)

# ── Legend ─────────────────────────────────────────────────
legend = [
    ("Infrastructure",        "#0277BD"),
    ("Security & Governance", "#C62828"),
    ("Data & Knowledge",      "#E65100"),
    ("AI Model Layer",        "#5E35B1"),
    ("Developer Experience",  "#2E7D32"),
    ("Integration & Orch",    "#7B1FA2"),
    ("AI Applications",       "#003087"),
    ("User Experience",       "#AD1457"),
]
for i, (lbl, col) in enumerate(legend):
    lx = 0.3 + i * 3.68
    lb = FancyBboxPatch((lx, 0.04), 3.5, 0.26,
                        boxstyle="round,pad=0.02",
                        facecolor=WHITE, edgecolor=col, linewidth=1.4)
    ax.add_patch(lb)
    ax.text(lx + 1.75, 0.17, lbl,
            ha='center', va='center', fontsize=7.5, color=col, fontweight='bold')

ax.set_xlim(0, 30.5)
plt.tight_layout(pad=0.15)
plt.savefig("build-reference-architecture.png", dpi=180,
            bbox_inches='tight', facecolor='#F0F2F5')
plt.savefig("build-reference-architecture.svg",
            bbox_inches='tight', facecolor='#F0F2F5')
plt.close()
print("Build reference architecture PNG/SVG saved.")


# ── draw.io version ────────────────────────────────────────
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

mxfile, root = make_diagram("Build Reference Architecture")
idc = 10

add_cell(root, idc,
         "Abbott GenAI — Platform &amp; Tools Reference Architecture",
         "text;html=1;strokeColor=none;fillColor=none;align=center;"
         "verticalAlign=middle;fontColor=#000050;fontSize=20;fontStyle=1;",
         20, 10, 1720, 48); idc += 1
add_cell(root, idc,
         "8-Layer Architecture  |  UX on top · Cloud Infrastructure at base  |  Azure Primary · AWS Secondary · GCP  |  Separate AI Model Layer",
         "text;html=1;strokeColor=none;fillColor=none;align=center;"
         "verticalAlign=middle;fontColor=#555555;fontSize=11;fontStyle=2;",
         20, 56, 1720, 26); idc += 1

LAYER_X_DIO   = 20
LAYER_W_DIO   = 1520
LABEL_W_DIO   = 220
CAP_X_DIO     = LAYER_X_DIO + LABEL_W_DIO + 8
CAP_AREA_DIO  = LAYER_W_DIO - LABEL_W_DIO - 18
STD_H_DIO     = 148
TALL_H_DIO    = 260
MODEL_H_DIO   = 230
DEVEX_H_DIO   = 250
LAYER_GAP_DIO = 12
GAP_DIO       = 8

def dio_layer_h(layer):
    if layer.get("tall"):        return TALL_H_DIO
    if layer.get("tall_model"):  return MODEL_H_DIO
    if layer.get("tall_devex"):  return DEVEX_H_DIO
    return STD_H_DIO

# draw.io: top = UX (reversed), bottom = Infra
dio_y = 90
for idx, layer in enumerate(reversed(LAYERS)):
    lh_dio = dio_layer_h(layer)
    c = layer

    add_cell(root, idc, "",
             f"rounded=1;whiteSpace=wrap;html=1;fillColor={c['bg']};"
             f"strokeColor={c['border']};strokeWidth=2;",
             LAYER_X_DIO, dio_y, LAYER_W_DIO, lh_dio); idc += 1

    add_cell(root, idc,
             f"<b>{layer['label']}</b><br/><i style='font-size:9px;'>{layer['sublabel']}</i>",
             f"text;html=1;strokeColor=none;fillColor=none;align=left;"
             f"verticalAlign=middle;fontColor={c['text']};fontSize=11;",
             LAYER_X_DIO + 6, dio_y + 8, LABEL_W_DIO - 10, lh_dio - 16); idc += 1

    if layer.get("tall") or layer.get("tall_model"):
        groups = layer["groups"]
        ng     = len(groups)
        gw     = (CAP_AREA_DIO - (ng-1)*10) // ng
        cap_h  = lh_dio - 68

        for gi, grp in enumerate(groups):
            gx   = CAP_X_DIO + gi*(gw+10)
            gy   = dio_y + 8
            gcol = grp["color"]
            add_cell(root, idc, f"<b>{grp['label']}</b>",
                     f"rounded=1;whiteSpace=wrap;html=1;fillColor={gcol};"
                     f"strokeColor=none;fontColor=#FFFFFF;fontSize=10;fontStyle=1;",
                     gx, gy, gw, 28); idc += 1

            gcaps = grp["components"]
            nc    = len(gcaps)
            gcw   = (gw - (nc-1)*GAP_DIO) // nc
            DIO_STATUS = {
                "approved": {"bg": "#FFFFFF", "ec": None,      "tc": "#1A1A1A", "badge": ""},
                "trial":    {"bg": "#E3F2FD", "ec": "#1565C0", "tc": "#0D47A1", "badge": " [T]"},
                "assess":   {"bg": "#FFFDE7", "ec": "#F9A825", "tc": "#E65100", "badge": " [~]"},
                "archived": {"bg": "#F5F5F5", "ec": "#9E9E9E", "tc": "#9E9E9E", "badge": " [x]"},
                "future":   {"bg": "#FFFDE7", "ec": "#F9A825", "tc": "#E65100", "badge": " [!]"},
            }
            for ci, cap in enumerate(gcaps):
                name, subtitle = cap[0], cap[1]
                st    = cap[2] if len(cap) > 2 else "approved"
                ds    = DIO_STATUS.get(st, DIO_STATUS["approved"])
                ec    = ds["ec"] if ds["ec"] else gcol
                cx    = gx + ci*(gcw+GAP_DIO)
                cy    = gy + 34
                label = (f"<b>{name}{ds['badge']}</b><br/>"
                         f"<font style='font-size:9px;color:{ds['tc']};'><i>{subtitle}</i></font>")
                add_cell(root, idc, label,
                         f"rounded=1;whiteSpace=wrap;html=1;fillColor={ds['bg']};"
                         f"strokeColor={ec};strokeWidth=1;"
                         f"fontColor={ds['tc']};fontSize=10;verticalAlign=middle;",
                         cx, cy, gcw, cap_h); idc += 1
    elif layer.get("tall_devex"):
        phases = layer["phases"]
        np_    = len(phases)
        pw     = (CAP_AREA_DIO - (np_-1)*GAP_DIO) / np_
        ph     = lh_dio - 20
        for i, (phase, existing, pipeline, value) in enumerate(phases):
            bx     = CAP_X_DIO + i*(pw+GAP_DIO)
            by     = dio_y + 10
            pc     = c["border"]
            pip_c  = "#E65100" if pipeline.strip() != "—" else "#AAAAAA"
            label  = (
                f"<b style='background-color:{pc};color:#ffffff;'>&nbsp;{phase.replace(chr(10),' ')}&nbsp;</b><br/><br/>"
                f"<font style='font-size:9px;color:#888888;font-style:italic;'>Existing</font><br/>"
                f"<font style='font-size:9px;'>{existing.replace(chr(10),'<br/>')}</font><br/><br/>"
                f"<font style='font-size:9px;color:#888888;font-style:italic;'>New / Pipeline</font><br/>"
                f"<b style='font-size:9px;color:{pip_c};'>{pipeline.replace(chr(10),'<br/>')}</b><br/><br/>"
                f"<font style='font-size:9px;color:#888888;font-style:italic;'>Value</font><br/>"
                f"<font style='font-size:9px;color:#1B5E20;'>{value.replace(chr(10),'<br/>')}</font>"
            )
            add_cell(root, idc, label,
                     f"rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;"
                     f"strokeColor={pc};strokeWidth=1;"
                     f"fontColor=#1A1A1A;fontSize=10;verticalAlign=top;spacingTop=6;",
                     bx, by, pw, ph); idc += 1
    else:
        caps  = layer["components"]
        n     = len(caps)
        cap_w = (CAP_AREA_DIO - (n-1)*GAP_DIO) / n
        cap_h = lh_dio - 20
        for i, (name, subtitle) in enumerate(caps):
            bx    = CAP_X_DIO + i*(cap_w+GAP_DIO)
            by    = dio_y + 10
            label = (f"<b>{name}</b><br/>"
                     f"<font style='font-size:9px;color:#555555;'><i>{subtitle}</i></font>")
            add_cell(root, idc, label,
                     f"rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;"
                     f"strokeColor={c['border']};strokeWidth=1;"
                     f"fontColor=#1A1A1A;fontSize=10;verticalAlign=middle;",
                     bx, by, cap_w, cap_h); idc += 1

    if idx < N_LAYERS - 1:
        arr = ET.SubElement(root, "mxCell", id=str(idc), value="",
                            style="edgeStyle=orthogonalEdgeStyle;"
                                  "strokeColor=#AAAAAA;strokeWidth=1.5;",
                            edge="1", parent="1")
        ET.SubElement(arr, "mxGeometry", relative="1", **{"as": "geometry"})
        idc += 1

    dio_y += lh_dio + LAYER_GAP_DIO

tree = ET.ElementTree(mxfile)
ET.indent(tree, space="  ")
tree.write("build-reference-architecture.drawio", encoding="unicode", xml_declaration=False)
print("draw.io file saved.")
print("\nAll build reference architecture files complete.")
