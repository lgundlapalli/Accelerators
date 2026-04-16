# **AI-Powered Returns Resolution System**

**DRI:** Marcus Chen (PM) \| **Eng:** Rachel Zhang \| **DS:** David
Kumar **Last Updated:** August 16, 2025\
**Links:** [[Figma]{.underline}](https://claude.ai/chat/link) \| [[Model
Training]{.underline}](https://claude.ai/chat/link) \|
[[Dashboard]{.underline}](https://claude.ai/chat/link) \|
[[Runbook]{.underline}](https://claude.ai/chat/link)

## **1. Problem & Hypothesis**

**Problem:** Returns drive 18% margin compression on apparel orders. Top
3 reasons are fit issues (31%), color variance (24%), and shipping
damage (19%). Our current manual process results in 73% refund rate when
exchanges or size advice could retain 40-50% of that revenue.

**Hypothesis:** If we implement structured reason classification +
tailored resolution suggestions, we can reduce refund rate by 8-12% on
eligible orders because customers will receive better-matched solutions
(exchanges vs refunds) while maintaining CSAT ≥4.2/5.

**Strategy Fit:** Directly supports Q3 \"Margin Recovery\" OKR.
Foundation for personalized shopping experience roadmap by understanding
fit patterns.

## **2. Scope & Non-Goals**

**In Scope:**

- Apparel orders \<60 days from purchase

- English-language return requests

- Integration with existing Shopify returns portal

- 8 core return reason categories + resolution engine

**Non-Goals:**

- Electronics/accessories (different return patterns)

- International orders (regulatory complexity)

- Wholesale/B2B returns (separate business rules)

**Tradeoffs Accepted:**

- Initial focus on clear-cut cases vs edge cases (80/20 rule)

- +\$0.12 per order processing cost vs manual CS overhead

- Conservative classification (favor human handoff vs wrong automation)

## **3. AI Behavior Contract**

**Primary Tasks:**

1.  **Classify** return reason into 8 categories (fit, damage, quality,
    color, description, change-of-mind, defect, other)

2.  **Generate** appropriate resolution action (exchange, store credit,
    refund, size guide)

**Inputs Available:**

- Customer free-text description

- Order details (item, size, color, price)

- Purchase history and return patterns

- Product reviews mentioning fit/quality

- High-res return photos (when provided)

**Constraints:**

- Never suggest keeping item + receiving refund (policy violation)

- Size exchanges only for available inventory

- Store credit expires per company policy (90 days)

- Damage claims require photo evidence review

**Resolution Logic Examples:**

**Input:** \"Sweater too small, usually wear M but ordered S by mistake.
Worn once.\" **GOOD:** Offer size exchange to M + auto-generated return
label; classify as \"fit issue - size error\" **BAD:** \"Would you like
to return for refund?\" (misses exchange opportunity) **REJECT:**
Auto-approve refund without exploring exchange options

**Input:** \"Color looks different than website photo, darker than
expected.\" **GOOD:** Offer exchange to different color + note for
product team photo review; classify as \"color variance\" **BAD:**
Immediate refund without exploring color alternatives **REJECT:**
Suggesting customer is wrong about color perception

## **4. Evaluation Plan**

**Offline Metrics:**

- Golden set: 1,200 labeled historical returns

- Target: F1 ≥ 0.84 for reason classification

- Target: 4.3/5 human rating for resolution appropriateness

- Edge case coverage: 95% of returns mapped to defined categories

**Online Metrics:**

- **Primary:** Refund rate on eligible orders ↓ 8-12% vs baseline

- **Secondary:**

  - Exchange rate ↑ 15-20% vs baseline

  - Resolution time P50 ↓ 4 hours vs current 24hr

- **Guardrails:**

  - CSAT ≥ 4.2/5 (baseline 4.3/5)

  - Human escalation rate ≤ 25%

  - Policy violation rate ≤ 1%

**Graduate When:** Primary metric + all guardrails achieved for 21
consecutive days

**Fail → Action:** Rollback if CSAT drops below 4.0 or policy violations
\>2%

## **5. Rollout Plan**

**Exposure:** Store-cohort level randomization (avoid
cross-contamination)

- Week 1-3: 20 stores (highest volume apparel)

- Week 4-5: 100 stores (if metrics green)

- Week 6-8: 500 stores (if metrics green)

- Week 9+: All eligible stores

**Eligibility:**

- Apparel orders only

- \<60 days from purchase date

- Order value \$25-\$500 (exclude extreme cases)

- Domestic US orders

**Ramp Gates:**

- Finance approval required (revenue impact)

- No increase in customer complaints to executives

- System performance maintaining \<2s response time

## **6. Risks & Recovery**

**Top Risks:**

1.  **Fraud Exploitation:** Repeat customers gaming \"didn\'t arrive\"
    classifications

2.  **Inventory Issues:** Exchange offers for out-of-stock items

3.  **Policy Hallucination:** AI suggesting non-existent return policies

4.  **Revenue Impact:** Higher than expected exchange rates impacting
    margin

**Detection:**

- Customer return frequency monitoring (\>3 returns/90 days)

- Inventory sync validation before exchange offers

- Policy compliance automated checking

- Daily revenue impact reports with alerts

**Fallbacks:**

- **High-risk customers:** Route to human agent with context

- **Inventory issues:** Offer store credit + discount on future purchase

- **Policy violations:** Revert to standard return flow

- **System down:** Graceful degradation to manual processing

**Kill Switch:** Feature toggle accessible to operations team, automatic
trigger on revenue variance \>5%

## **7. Financial Impact Model**

**Current State:**

- 15,000 returns/month on eligible orders

- 73% refund rate = \$2.1M monthly refunds

- Manual processing cost: \$12/return

**Projected Impact:**

- 8-12% refund rate reduction = \$168K-252K monthly savings

- 40% automation rate = \$72K monthly CS cost savings

- Total monthly benefit: \$240K-324K

- Implementation cost: \$180K (6-month payback)

## **8. Owner & Next Steps**

**Team:**

- **PM:** Marcus Chen

- **Engineering:** Rachel Zhang (ML), Tommy Liu (Integration)

- **Data Science:** David Kumar, Sofia Petrov

- **Design:** Jennifer Park

- **Legal/Compliance:** Amanda Foster ✓ (review complete)

- **Finance:** Kevin Zhao (revenue impact approval pending)

- **CS Operations:** Maria Rodriguez

**Dependencies:**

- Shopify API rate limit increase (Rachel - 8/20)

- Return photo storage infrastructure (Tommy - 8/25)

- Model training data labeling complete (David - 8/22)

**Next Milestones:**

- 8/23: Technical architecture review

- 8/30: Alpha build ready for internal testing

- 9/6: Pilot store selection and setup

- 9/13: 20-store pilot launch

- 10/4: Full rollout decision point

## **9. Training Data & Examples**

**Classification Categories with Examples:**

**Fit Issue (31% of returns):**

- \"Too small/large\"

- \"Sleeves too long\"

- \"Runs small compared to size chart\"

**Color Variance (24%):**

- \"Darker than photo\"

- \"Different shade than expected\"

- \"Color not as vibrant\"

**Shipping Damage (19%):**

- \"Arrived torn\"

- \"Package was wet, item damaged\"

- \"Stains on arrival\"

**Quality Issues (12%):**

- \"Cheap material\"

- \"Stitching coming apart\"

- \"Fabric pilling immediately\"

**Description Mismatch (8%):**

- \"Material not as described\"

- \"Features missing from description\"

- \"Style different than shown\"

**Resolution Success Patterns:**

- Fit issues: 67% accept exchange when offered

- Color variance: 45% accept different color option

- Damage: 89% prefer replacement over refund

**Meeting Notes:**

- 8/16: Kickoff - alignment on conservative approach for launch

- Finance review scheduled 8/19 for revenue impact approval

- CS team requests 1-week training period before pilot launch
