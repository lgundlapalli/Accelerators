# Inventory & Fulfillment Context — Diagrams

## Aggregate Boundaries

```mermaid
classDiagram
    class InventoryItem {
        <<Aggregate Root>>
        +String id
        +SKU sku
        +Quantity onHand
        +Quantity available
        +checkAvailability()
        +reserve()
        +releaseReservation()
        +restock()
    }
    class Reservation {
        <<Entity>>
        +String id
        +String orderId
        +Quantity quantity
        +ReservationStatus status
        +fulfill()
        +release()
    }
    class SKU {
        <<Value Object>>
        +String value
    }
    class Quantity {
        <<Value Object>>
        +number value
        +add()
        +subtract()
    }

    InventoryItem *-- Reservation : contains
    InventoryItem *-- SKU : identified by
    InventoryItem *-- Quantity : onHand
    Reservation *-- Quantity : reserved amount

    class FulfillmentOrder {
        <<Aggregate Root>>
        +String id
        +String orderId
        +FulfillmentOrderStatus status
        +FulfillmentPool pool
        +assignPool()
        +routeForDirectFulfillment()
        +markShipped()
    }
    class FulfillmentPool {
        <<Value Object>>
        +String poolId
        +FulfillmentLocation location
        +String poolType
    }
    class FulfillmentLocation {
        <<Value Object>>
        +String warehouseId
        +String name
        +String address
    }

    FulfillmentOrder *-- FulfillmentPool : assigned to
    FulfillmentPool *-- FulfillmentLocation : located at

    class Backorder {
        <<Aggregate Root>>
        +String id
        +String orderId
        +SKU sku
        +Quantity quantity
        +BackorderDeadline deadline
        +BackorderStatus status
        +checkDeadline()
        +fulfill()
    }
    class BackorderDeadline {
        <<Value Object>>
        +Date createdAt
        +Date expiresAt
        +isExpired()
        +daysRemaining()
    }

    Backorder *-- SKU : for product
    Backorder *-- Quantity : needed
    Backorder *-- BackorderDeadline : expires by
```

## Event Flow — Happy Path (Order Placed → Fulfilled)

```mermaid
sequenceDiagram
    participant Ord as Ordering Context
    participant Inv as InventoryItem
    participant Route as FulfillmentRoutingService
    participant FO as FulfillmentOrder

    Ord-->>Inv: OrderPlaced(orderId, items)
    Inv->>Inv: checkAvailability()
    Note over Inv: Stock available
    Inv->>Inv: reserve(orderId, qty)
    Inv-->>Ord: InventoryReserved

    Inv-->>Route: Request best pool
    Route-->>FO: Create FulfillmentOrder
    FO->>FO: assignPool(pool)
    FO-->>FO: FulfillmentPoolAssigned
    FO->>FO: routeForDirectFulfillment()
    FO-->>FO: DirectFulfillmentRouted
```

## Event Flow — Backorder Path

```mermaid
sequenceDiagram
    participant Ord as Ordering Context
    participant Inv as InventoryItem
    participant BO as Backorder
    participant Sched as Scheduler
    participant Mon as BackorderMonitorService

    Ord-->>Inv: OrderPlaced(orderId, items)
    Inv->>Inv: checkAvailability()
    Note over Inv: Stock unavailable
    Inv->>Inv: reserve() fails
    Inv-->>Ord: InventoryUnavailable

    Note over BO: Backorder created
    BO-->>Ord: OrderBackordered(deadline: +2 weeks)

    loop Daily check
        Sched->>Mon: checkAndCancelExpiredBackorders()
        Mon->>BO: checkDeadline()
    end

    Note over BO: 2 weeks pass...
    BO->>BO: checkDeadline() → expired
    BO-->>Ord: BackorderAutoCancelled
    Ord->>Ord: cancel("Backorder exceeded 2 weeks")
```

## Event Flow — Cancellation Releases Inventory

```mermaid
sequenceDiagram
    participant Ord as Ordering Context
    participant Inv as InventoryItem

    Ord-->>Inv: OrderCancelled(orderId)
    Inv->>Inv: releaseReservation(orderId)
    Inv-->>Ord: ReservationReleased
    Note over Inv: Available quantity increases
```

## Event Flow — Return Restocks Inventory

```mermaid
sequenceDiagram
    participant Ret as Returns & Refunds
    participant Inv as InventoryItem

    Ret-->>Inv: ItemReturned(sku, qty)
    Inv->>Inv: restock(qty, "customer return")
    Note over Inv: On-hand quantity increases
    Inv-->>Inv: InventoryRestocked
```
