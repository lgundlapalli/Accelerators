import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

def draw_capability_box(ax, x, y, w, h, label, bg_color, text_color="#1a1a1a", fontsize=8.5):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                         facecolor=bg_color, edgecolor="#aaaaaa", linewidth=0.8)
    ax.add_patch(box)
    ax.text(x + w/2, y + h/2, label, ha='center', va='center',
            fontsize=fontsize, color=text_color, fontweight='normal',
            wrap=True, multialignment='center',
            linespacing=1.3)

def draw_layer_label(ax, x, y, w, h, label, bg_color, text_color):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                         facecolor=bg_color, edgecolor=text_color, linewidth=1.5)
    ax.add_patch(box)
    ax.text(x + w/2, y + h/2, label, ha='center', va='center',
            fontsize=10, color=text_color, fontweight='bold')

# ─── DIAGRAM A: LAYERED ARCHITECTURE ──────────────────────────────────────────
fig, ax = plt.subplots(figsize=(22, 14))
ax.set_xlim(0, 22)
ax.set_ylim(0, 14)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(11, 13.6, "Project MARS — Abbott Pedialyte DTC\nBusiness Capability Map (Architecture Layers)",
        ha='center', va='center', fontsize=14, fontweight='bold', color='#1a1a1a')

layers = [
    {
        "label": "🖥️  EXPERIENCE LAYER",
        "y": 11.2, "height": 1.8,
        "bg": "#dbe8ff", "border": "#003087", "text": "#003087",
        "caps": [
            "Product Catalog\nBrowsing", "Shopping Cart\nManagement", "3-Step\nCheckout Flow",
            "Account\nDashboard", "Mobile\nResponsive UI", "Subscription\nManagement UI",
            "Loyalty Balance\nDisplay", "Order\nHistory UI", "Customer\nProfile Mgmt",
            "Product Search\n& Filtering"
        ]
    },
    {
        "label": "⚙️  APPLICATION SERVICES LAYER",
        "y": 8.8, "height": 1.8,
        "bg": "#e8f4e8", "border": "#1a7a1a", "text": "#1a5c1a",
        "caps": [
            "Order\nManagement", "Subscription\nEngine", "Loyalty\nEngine",
            "Pricing &\nPromotion Engine", "Customer\nRegistration", "Recurring Order\nScheduler",
            "Discount Rules\nService", "Points Ledger\nService", "Pricing\nService"
        ]
    },
    {
        "label": "🗄️  DATA LAYER",
        "y": 6.4, "height": 1.8,
        "bg": "#fff3e0", "border": "#b35a00", "text": "#7a3e00",
        "caps": [
            "Customer\nProfile Store", "Order\nStore", "Product\nCatalog DB",
            "Loyalty\nLedger Store", "Subscription\nStore", "Cart\nState DB",
            "Reporting\nDashboard"
        ]
    },
    {
        "label": "🔗  INTEGRATION LAYER",
        "y": 4.0, "height": 1.8,
        "bg": "#f3e5f5", "border": "#7b1fa2", "text": "#5c0e7a",
        "caps": [
            "Payment\nGateway", "Fulfillment\nConnector", "Notification\nService",
            "Analytics\nPipeline", "Tax Calculation\nAdapter", "Shipping Rate\nAdapter",
            "Inventory\nAvailability", "Order Status\nUpdater"
        ]
    },
    {
        "label": "🏗️  INFRASTRUCTURE & SECURITY",
        "y": 1.2, "height": 2.2,
        "bg": "#e3f2fd", "border": "#0277bd", "text": "#01579b",
        "caps": [
            "API Gateway\n(Azure APIM)", "CDN\n(Azure Front Door)", "Compute\n(AKS)",
            "CI/CD\n(Azure DevOps)", "Auth Service\n(Azure AD B2C)", "Key Vault\n(Secrets)",
            "Azure WAF\n(Edge Security)", "Azure Monitor\n(Audit Logging)",
            "Encryption\n(TLS + DB)", "SOC2 / PII\nControls"
        ]
    },
]

MARGIN_LEFT = 0.3
TOTAL_WIDTH = 21.4
LABEL_W = 1.8
CAP_AREA = TOTAL_WIDTH - LABEL_W - 0.2
GAP = 0.12
BOX_H = 0.0

for layer in layers:
    y = layer["y"]
    h = layer["height"]
    caps = layer["caps"]
    n = len(caps)
    cap_w = (CAP_AREA - (n - 1) * GAP) / n
    cap_h = h - 0.3

    # Layer background
    bg = FancyBboxPatch((MARGIN_LEFT, y), TOTAL_WIDTH, h,
                        boxstyle="round,pad=0.05",
                        facecolor=layer["bg"], edgecolor=layer["border"], linewidth=1.5)
    ax.add_patch(bg)

    # Layer label on left
    ax.text(MARGIN_LEFT + 0.1, y + h/2, layer["label"],
            ha='left', va='center', fontsize=9.5, fontweight='bold',
            color=layer["text"], rotation=0)

    # Capability boxes
    x_start = MARGIN_LEFT + LABEL_W
    for i, cap in enumerate(caps):
        bx = x_start + i * (cap_w + GAP)
        by = y + 0.15
        draw_capability_box(ax, bx, by, cap_w, cap_h, cap,
                            bg_color="white", text_color="#1a1a1a", fontsize=8)

plt.tight_layout(pad=0.5)
plt.savefig("capability-layered.png", dpi=180, bbox_inches='tight',
            facecolor='#f8f9fa', edgecolor='none')
plt.savefig("capability-layered.svg", bbox_inches='tight',
            facecolor='#f8f9fa', edgecolor='none')
plt.close()
print("Layered diagram saved.")


# ─── DIAGRAM C: DOMAIN VIEW ────────────────────────────────────────────────────
domains = [
    {
        "label": "🛒 COMMERCE", "bg": "#dbe8ff", "border": "#003087", "text": "#003087",
        "caps": ["Product Catalog & Search", "Shopping Cart", "3-Step Checkout",
                 "Payment Processing", "Tax Calculation", "Shipping Estimation",
                 "Pricing & Promotions", "Inventory Check"]
    },
    {
        "label": "📦 ORDER & FULFILLMENT", "bg": "#e8f4e8", "border": "#1a7a1a", "text": "#1a5c1a",
        "caps": ["Order Creation & Confirmation", "Order Routing to Fulfillment",
                 "Fulfillment Status Sync", "Recurring Order Scheduling",
                 "Transactional Notifications", "Order History UI"]
    },
    {
        "label": "🔄 SUBSCRIPTIONS & LOYALTY", "bg": "#fff3e0", "border": "#b35a00", "text": "#7a3e00",
        "caps": ["Subscribe & Save Enrollment", "Subscription Management",
                 "Discount Application (25%)", "Loyalty Points Accrual",
                 "Loyalty Points Redemption", "Loyalty Balance Display"]
    },
    {
        "label": "👤 IDENTITY & ACCOUNT", "bg": "#f3e5f5", "border": "#7b1fa2", "text": "#5c0e7a",
        "caps": ["Customer Registration", "Authentication (OAuth2/OIDC)",
                 "Session Management", "Password Reset & MFA",
                 "Customer Profile Mgmt", "Account Dashboard"]
    },
    {
        "label": "🗄️ DATA & ANALYTICS", "bg": "#fce4ec", "border": "#c62828", "text": "#8e0000",
        "caps": ["Customer PII Store", "Order Data Store", "Product Catalog DB",
                 "Loyalty Ledger Store", "Subscription Store",
                 "Revenue & KPI Reporting", "Analytics Event Pipeline"]
    },
    {
        "label": "🏗️ PLATFORM & SECURITY", "bg": "#e3f2fd", "border": "#0277bd", "text": "#01579b",
        "caps": ["API Gateway (Azure APIM)", "CDN (Azure Front Door)", "Compute (AKS)",
                 "CI/CD (Azure DevOps)", "Azure WAF & Rate Limiting",
                 "Encryption (TLS + DB)", "SOC2 / PII Compliance",
                 "Audit Logging (Azure Monitor)", "Key Vault (Secrets)"]
    },
]

COLS = 3
ROWS = 2
FIG_W, FIG_H = 24, 14
CELL_W = FIG_W / COLS
CELL_H = (FIG_H - 1.2) / ROWS
PAD = 0.25
BOX_W = 0.0
BOX_H2 = 0.0
GAP2 = 0.1
CAPS_PER_ROW = 4

fig2, ax2 = plt.subplots(figsize=(FIG_W, FIG_H))
ax2.set_xlim(0, FIG_W)
ax2.set_ylim(0, FIG_H)
ax2.axis('off')
ax2.set_facecolor('#f8f9fa')
fig2.patch.set_facecolor('#f8f9fa')

ax2.text(FIG_W/2, FIG_H - 0.45,
         "Project MARS — Abbott Pedialyte DTC\nBusiness Capability Map (Domain View)",
         ha='center', va='center', fontsize=14, fontweight='bold', color='#1a1a1a')

for idx, domain in enumerate(domains):
    col = idx % COLS
    row = ROWS - 1 - (idx // COLS)
    cx = col * CELL_W + PAD
    cy = row * CELL_H + PAD
    cw = CELL_W - 2 * PAD
    ch = CELL_H - 2 * PAD

    # Domain background
    bg2 = FancyBboxPatch((cx, cy), cw, ch, boxstyle="round,pad=0.08",
                         facecolor=domain["bg"], edgecolor=domain["border"], linewidth=2)
    ax2.add_patch(bg2)

    # Domain label
    ax2.text(cx + cw/2, cy + ch - 0.28, domain["label"],
             ha='center', va='center', fontsize=11, fontweight='bold', color=domain["text"])

    # Capability boxes in grid
    caps = domain["caps"]
    n = len(caps)
    cols_c = min(4, n)
    rows_c = int(np.ceil(n / cols_c))
    cap_area_w = cw - 0.2
    cap_area_h = ch - 0.65
    cap_w = (cap_area_w - (cols_c - 1) * GAP2) / cols_c
    cap_h = (cap_area_h - (rows_c - 1) * GAP2) / rows_c

    for i, cap in enumerate(caps):
        cr = i // cols_c
        cc = i % cols_c
        bx = cx + 0.1 + cc * (cap_w + GAP2)
        by = cy + 0.1 + (rows_c - 1 - cr) * (cap_h + GAP2)
        draw_capability_box(ax2, bx, by, cap_w, cap_h, cap,
                            bg_color="white", text_color="#1a1a1a", fontsize=8.5)

plt.tight_layout(pad=0.5)
plt.savefig("capability-domain.png", dpi=180, bbox_inches='tight',
            facecolor='#f8f9fa', edgecolor='none')
plt.savefig("capability-domain.svg", bbox_inches='tight',
            facecolor='#f8f9fa', edgecolor='none')
plt.close()
print("Domain diagram saved.")
