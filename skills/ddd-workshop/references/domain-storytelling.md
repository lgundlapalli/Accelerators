# Domain Storytelling Facilitation Guide

Domain Storytelling is a collaborative modeling technique developed by Stefan Hofer and Henning Schwentner. The user tells stories about how work gets done in their domain, and you extract the model from the narrative.

## The Session Flow

### Step 1: Set the Scene

Ask the user to pick a concrete scenario — not an abstract process, but a specific story with a specific actor doing a specific thing.

Prompt: "Tell me a story about how something gets done in your domain. Pick a specific scenario — for example, 'A customer places an order' or 'A manager approves a leave request.' Walk me through it step by step, as if you're explaining it to a new team member."

### Step 2: Listen and Extract

As the user narrates, extract three elements:

**Actors** — Who is doing something? (People, roles, or systems)
**Work Objects** — What are they working with? (Documents, records, physical items, digital artifacts)
**Activities** — What are they doing? (Verbs: creates, sends, approves, checks)

Number each activity in sequence to capture the flow.

Example extraction:
> "The customer fills out an order form and submits it. The sales team reviews the order and checks inventory. If everything is in stock, they confirm the order and send a confirmation email to the customer."

| # | Actor | Activity | Work Object |
|---|-------|----------|-------------|
| 1 | Customer | fills out | Order Form |
| 2 | Customer | submits | Order Form |
| 3 | Sales Team | reviews | Order |
| 4 | Sales Team | checks | Inventory |
| 5 | Sales Team | confirms | Order |
| 6 | Sales Team | sends | Confirmation Email |

### Step 3: Play Back and Refine

Read the extracted story back to the user in structured form: "So let me make sure I've got this right: First, the Customer fills out an Order Form..."

Ask:
- "Did I capture this correctly?"
- "What happens if inventory is NOT in stock?" (explore alternate paths)
- "Are there any steps I missed?"

### Step 4: Tell More Stories

One story reveals one path. Ask for more stories to build coverage:

- "What's the happy path we just covered? Now what's the most common exception?"
- "What happens after this process completes? What's the next story?"
- "Is there a different actor who interacts with these same work objects?"

Aim for 3-5 stories to get a good picture of a bounded context.

### Step 5: Identify Boundaries

After collecting multiple stories, look for:

**Scope boundaries** — Where does one group of stories end and another begin? Stories about "placing orders" are different from stories about "shipping orders" — these might be different bounded contexts.

**Language boundaries** — Does "order" mean the same thing in the sales story as in the warehouse story? If not, you've found a context boundary.

**Actor boundaries** — Different actors working with different work objects often indicates different contexts.

## Deriving the Model from Stories

### Work Objects → Entities and Value Objects

- Work objects that have identity and lifecycle (Order, Customer, Invoice) → **Entities**
- Work objects that are descriptive and interchangeable (Address, Price, Date Range) → **Value Objects**

### Activities → Commands and Domain Events

- Activities that change state → **Commands** (PlaceOrder, ApproveRequest)
- The results of activities → **Domain Events** (OrderPlaced, RequestApproved)

### Actors → User Roles and External Systems

- Human actors → User roles and permissions
- System actors → Integration points and anti-corruption layers

### Story Sequences → Process Flows

- Numbered sequences → The happy-path workflow
- Alternate paths → Business rules and policies
- "If/then" branches → Domain logic and invariants

## Presenting Results

After collecting stories, present:

1. **Story summary** — Each story in structured table format
2. **Extracted actors** — All roles and systems identified
3. **Extracted work objects** — Classified as potential entities or value objects
4. **Extracted activities** — Mapped to potential commands and events
5. **Proposed boundaries** — Where the stories suggest bounded contexts
6. **Questions and gaps** — What stories are we missing?

Confirm with the user before transitioning to Strategic or Tactical Design.
