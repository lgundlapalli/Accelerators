# Tactical Design Patterns Reference

Tactical design is about the building blocks inside a bounded context: how to structure entities, value objects, aggregates, events, services, and repositories to faithfully represent the domain.

## Entities

Objects with a distinct identity that persists over time. Two entities are equal if they have the same ID, even if all other attributes differ.

**How to identify entities:**
- Does this thing have a lifecycle? (created, modified, archived, deleted)
- Do you need to track "which one" specifically? (which order, which customer)
- Would two instances with identical attributes still be different things?

**Design guidance:**
- Give entities a unique identifier (ID). Prefer domain-meaningful IDs when they exist (ISBN, SSN) over synthetic UUIDs, but UUIDs are fine as a default.
- Keep entities focused — if an entity has 30+ attributes, it's probably serving multiple contexts.
- Entities contain behavior (methods), not just data. An Order knows how to add a line item, not just store data.

## Value Objects

Immutable objects defined by their attributes, not by an identity. Two value objects with the same attributes are interchangeable.

**How to identify value objects:**
- Is it defined entirely by its attributes? (An Address is an Address if street, city, zip match)
- Is it immutable? (You don't change a price; you replace it with a new price)
- Can it be shared freely between entities without problems?

**Common value objects:** Money, Address, DateRange, EmailAddress, PhoneNumber, Coordinates, Color, Percentage, Quantity.

**Design guidance:**
- Make them immutable. "Changing" a VO means creating a new instance.
- Put validation in the constructor. A Money object with a negative amount should never exist (unless your domain allows it).
- Value objects are excellent places for domain logic. Money can handle currency conversion, DateRange can check for overlaps.

## Aggregates

A cluster of entities and value objects with a consistency boundary. An aggregate is a transactional unit — everything inside it must be consistent after every operation.

**The aggregate root** is the single entity through which all external access to the aggregate happens. No outside code should hold a reference to an internal entity.

**How to design aggregates:**
1. Start with a single entity as a candidate aggregate
2. Ask: "What else MUST be consistent with this entity in the same transaction?"
3. Whatever must be consistent goes inside the aggregate
4. Everything else stays outside and communicates via domain events

**Key rules:**
- **Reference other aggregates by ID only.** Don't hold object references across aggregate boundaries.
- **One aggregate per transaction.** If you need to update two aggregates, use domain events and eventual consistency.
- **Keep aggregates small.** A large aggregate means large transactions, lock contention, and merge conflicts. If an aggregate grows large, look for ways to split it.

**Example:**
```
Order (Aggregate Root)
├── OrderLine (Entity — identity within the Order)
├── ShippingAddress (Value Object)
└── OrderTotal (Value Object)

// NOT inside the Order aggregate:
// - Customer (separate aggregate, referenced by customerId)
// - Product (separate aggregate, referenced by productId)
// - Payment (separate aggregate, linked via domain events)
```

## Domain Events

Something that happened in the domain that other parts of the system care about. Phrased in past tense: OrderPlaced, PaymentReceived, ItemShipped.

**How to identify domain events:**
- What state changes are other aggregates or contexts interested in?
- What triggers policies or workflows?
- What would a domain expert say "happened"?

**Design guidance:**
- Name events in the ubiquitous language of the context that produces them
- Events are immutable facts — they describe what happened, not what should happen
- Include enough data for consumers to act without calling back to the producer
- Include a timestamp and the aggregate ID that produced the event

**Event structure:**
| Field | Description |
|-------|-------------|
| Event name | Past tense, domain language (OrderPlaced) |
| Aggregate ID | Which aggregate produced this event |
| Timestamp | When it happened |
| Payload | Data consumers need (order details, amounts, etc.) |
| Metadata | Correlation ID, causation ID, user who triggered it |

## Domain Services

Operations that don't naturally belong to any single entity or value object. They represent domain concepts that are verbs, not nouns.

**When to use a domain service:**
- The operation involves multiple aggregates
- The operation doesn't conceptually belong to any entity
- The operation represents a domain concept in its own right

**Examples:**
- PricingService — Calculates prices based on customer tier, promotions, and product rules (spans Customer, Product, Promotion aggregates)
- TransferService — Moves money between accounts (involves two Account aggregates)
- RoutingService — Determines the best shipping route (involves Order, Warehouse, Carrier)

**When NOT to use a domain service:**
- If the behavior clearly belongs to an entity, put it there. Don't create an OrderService to do things that Order should do itself.
- Don't use services as a dumping ground for logic you're not sure where to put. Think harder about which entity or VO owns the behavior.

## Repositories

Provide the illusion of an in-memory collection of aggregates. Repositories handle persistence so the domain model doesn't have to know about databases.

**Design guidance:**
- One repository per aggregate root (not per entity)
- The interface is defined in the domain layer; the implementation lives in infrastructure
- Methods should use domain language: `findByCustomerId()`, not `getByForeignKey()`
- Return full aggregates, not partial data

**Typical repository interface:**
```
interface OrderRepository {
    findById(orderId: OrderId): Order | null
    findByCustomerId(customerId: CustomerId): Order[]
    save(order: Order): void
    delete(orderId: OrderId): void
    nextId(): OrderId
}
```

## Application Services

Thin orchestration layer that coordinates domain objects to fulfill a use case. Application services don't contain domain logic — they delegate to the domain model.

**Pattern:**
1. Load aggregate(s) from repository
2. Call domain method(s) on the aggregate
3. Save the aggregate back
4. Publish any domain events

Application services are where transactions, authorization checks, and input validation live — not domain logic.

## Invariant Documentation

For each aggregate, document the business rules that must always hold:

| Invariant | Aggregate | Condition | On Violation |
|-----------|-----------|-----------|-------------|
| Order must have at least one line item | Order | lineItems.length > 0 | Reject command, raise error |
| Order total cannot be negative | Order | total >= 0 | Recalculate, reject if impossible |
| Account balance cannot go below overdraft limit | Account | balance >= -overdraftLimit | Reject withdrawal |
