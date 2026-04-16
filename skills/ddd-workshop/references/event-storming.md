# Event Storming Facilitation Guide

Event Storming is a collaborative discovery technique invented by Alberto Brandolini. In a virtual session with Claude, it follows the same principles: start with what happens in the domain (events), then work backwards and forwards to understand the full picture.

## The Session Flow

### Step 1: Domain Events (Orange Sticky Notes)

Ask the user to brainstorm domain events — things that happen in the system, phrased in past tense.

Prompt: "Let's start by listing everything that happens in your domain. Think of past-tense facts: OrderPlaced, PaymentReceived, ItemShipped. Don't worry about order or completeness yet — just dump them all out."

Capture every event. Don't filter or organize yet. Encourage quantity.

If the user struggles, help with probing questions:
- "What triggers work in your system?"
- "What do people check on or wait for?"
- "What can go wrong?"
- "What notifications or alerts exist?"

### Step 2: Timeline Ordering

Arrange events into a rough chronological flow. Group related events together.

Present back to the user: "Here's a rough timeline of events. Does this flow make sense? What's missing between [EventA] and [EventB]?"

### Step 3: Commands (Blue Sticky Notes)

For each event, identify what caused it — the command or action that triggered it.

"What action causes [EventName] to happen? Who or what initiates it?"

Commands are imperative: PlaceOrder, ProcessPayment, ShipItem.

### Step 4: Actors (Yellow Sticky Notes)

Identify who or what issues each command:
- Human actors (Customer, Admin, Warehouse Worker)
- External systems (Payment Gateway, Shipping API)
- Time-based triggers (Daily batch, Cron job)

### Step 5: Policies (Lilac Sticky Notes)

Policies are reactive rules: "When [Event] happens, then [Command] should be issued."

These are business rules that connect events to commands automatically:
- "When PaymentReceived, then FulfillOrder"
- "When InventoryBelowThreshold, then ReorderStock"

Ask: "Are there any automatic reactions? When X happens, does something always follow?"

### Step 6: Read Models (Green Sticky Notes)

What information does an actor need to make a decision or issue a command?

"Before [Actor] can [Command], what information do they need to see?"

These become your query/read models and help identify what data needs to be available where.

### Step 7: Hotspots and Questions (Red/Pink)

Mark areas of confusion, disagreement, or complexity:
- Where the user says "it depends" or "it's complicated"
- Where the process branches significantly
- Where there are known pain points

These are the areas that need the most design attention.

## Deriving the Model from Event Storming

### Finding Aggregate Boundaries

Look for clusters of events and commands that:
- Share the same data/state
- Must be consistent with each other
- Are triggered by the same actor in the same workflow

Each cluster likely represents an aggregate. The entity that "owns" the state being modified is the aggregate root.

### Finding Bounded Context Boundaries

Look for:
- **Language shifts** — Where the same word means different things (e.g., "Account" in billing vs. authentication)
- **Actor boundaries** — Different groups of people work with different clusters
- **Temporal boundaries** — Events that happen in different phases (ordering vs. fulfillment vs. returns)
- **Large gaps** in the timeline between event clusters

### Finding Domain Services

Policies that coordinate across multiple aggregates often become domain services.

## Presenting Results

After the event storming session, summarize:

1. **Event timeline** — The ordered list of events with commands and actors
2. **Policies** — The reactive business rules discovered
3. **Proposed aggregates** — Clusters of events/commands and their aggregate roots
4. **Proposed bounded contexts** — Higher-level groupings with language boundaries
5. **Hotspots** — Areas needing further exploration

Confirm with the user before transitioning to Strategic or Tactical Design.
