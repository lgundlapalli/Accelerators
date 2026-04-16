# Ordering Context — Diagrams

## Aggregate Boundaries

```mermaid
classDiagram
    class Cart {
        <<Aggregate Root>>
        +String id
        +String customerId
        +CartItem[] items
        +addItem()
        +removeItem()
        +updateItemQuantity()
        +startCheckout()
    }
    class CartItem {
        <<Entity>>
        +String id
        +ProductReference product
        +number quantity
        +EligibilityCheck eligibility
        +lineTotal() Money
    }
    class ProductReference {
        <<Value Object>>
        +String productId
        +String name
        +Money price
    }
    class EligibilityCheck {
        <<Value Object>>
        +boolean passed
        +String reason
        +Date checkedAt
    }

    Cart *-- CartItem : contains
    CartItem *-- ProductReference : references
    CartItem *-- EligibilityCheck : has

    class Order {
        <<Aggregate Root>>
        +String id
        +CheckoutProfile checkoutProfile
        +OrderStatus status
        +PriceBreakdown priceBreakdown
        +place()
        +cancel()
        +sendConfirmation()
    }
    class OrderLineItem {
        <<Entity>>
        +String id
        +ProductReference product
        +number quantity
        +Money unitPrice
        +lineTotal() Money
    }
    class CheckoutProfile {
        <<Value Object>>
        +String customerId
        +String name
        +String email
        +ShippingAddress shippingAddress
    }
    class ShippingAddress {
        <<Value Object>>
        +String street
        +String city
        +String state
        +String zipCode
        +String country
        +boolean validated
    }
    class PriceBreakdown {
        <<Value Object>>
        +Money subtotal
        +Money tax
        +Money shippingCost
        +Discount discount
        +Money total
    }
    class Money {
        <<Value Object>>
        +number amount
        +String currency
        +add()
        +subtract()
        +multiply()
    }
    class Discount {
        <<Value Object>>
        +DiscountType type
        +Money amount
        +String reason
    }

    Order *-- OrderLineItem : contains
    Order *-- CheckoutProfile : has
    Order *-- PriceBreakdown : has
    OrderLineItem *-- ProductReference : references
    OrderLineItem *-- Money : unitPrice
    CheckoutProfile *-- ShippingAddress : has
    PriceBreakdown *-- Money : subtotal/tax/shipping/total
    PriceBreakdown *-- Discount : may have
```

## Event Flow — Happy Path (Browse to Confirmation)

```mermaid
sequenceDiagram
    participant C as Customer
    participant Cart as Cart Aggregate
    participant ES as EligibilityService
    participant PS as PricingService
    participant Ord as Order Aggregate
    participant Pay as Payment Context
    participant Inv as Inventory & Fulfillment
    participant Rec as Recommendations

    C->>Cart: AddItem(product, qty)
    Cart->>ES: checkItemEligibility()
    ES-->>Cart: EligibilityCheck(passed)
    Cart-->>Rec: ItemAddedToCart

    C->>Cart: StartCheckout()
    Cart-->>Inv: CheckoutStarted

    C->>PS: calculateBreakdown(items, address, discount)
    PS-->>Ord: PriceBreakdown

    C->>Pay: SubmitPayment(amount)
    Pay-->>Ord: PaymentConfirmed

    Ord->>Ord: place()
    Ord-->>Inv: OrderPlaced
    Ord-->>Rec: OrderPlaced
    Ord->>Ord: sendConfirmation()
    Ord-->>C: OrderConfirmationSent
```

## Event Flow — Cancellation

```mermaid
sequenceDiagram
    participant Actor as Customer / CS Rep
    participant Ord as Order Aggregate
    participant Inv as Inventory & Fulfillment
    participant Pay as Payment Context
    participant Ret as Returns & Refunds

    Actor->>Ord: cancel(reason)
    Ord-->>Inv: OrderCancelled
    Ord-->>Pay: OrderCancelled
    Ord-->>Ret: OrderCancelled

    Inv->>Inv: ReleaseInventoryReservation
    Pay->>Ret: IssueRefund
```

## Event Flow — Backorder & Auto-Cancel

```mermaid
sequenceDiagram
    participant Ord as Order Aggregate
    participant Inv as Inventory & Fulfillment
    participant Sched as Scheduler
    participant C as Customer

    Ord-->>Inv: OrderPlaced
    Inv->>Inv: CheckOnHandInventory
    Note over Inv: Inventory unavailable
    Inv->>Inv: MarkAsBackorder
    Inv-->>C: NotifyCustomerBackorder (OrderBackordered)

    Note over Sched: 2 weeks pass...
    Sched->>Inv: CheckBackorderAge
    Inv-->>Ord: BackorderAutoCancelled
    Ord->>Ord: cancel("Backorder exceeded 2 weeks")
```

## Context Map — Full System

```mermaid
graph LR
    subgraph "Core"
        ORD[Ordering<br/>Cart + Checkout + Order]
    end
    subgraph "Supporting"
        CAT[Product Catalog<br/>Add/Update/Manage]
        REC[Recommendations<br/>YMAL + Most Popular]
        INV[Inventory & Fulfillment<br/>On-hand + Direct Fulfillment Pool]
        RET[Returns & Refunds<br/>Cancel + Return + Refund]
    end
    subgraph "Generic"
        IDN[Identity & Profile<br/>Registration + Addresses]
        PAY[Payment<br/>Processing + Confirmation]
    end

    ORD -->|"Customer-Supplier"| CAT
    ORD -->|"Conformist"| IDN
    ORD -->|"ACL"| PAY
    ORD -->|"Customer-Supplier"| INV
    RET -->|"Customer-Supplier"| ORD
    RET -->|"ACL"| PAY
    REC -->|"Consumes events"| ORD
    REC -->|"Customer-Supplier"| CAT
    INV -->|"Published Language"| ORD
```
