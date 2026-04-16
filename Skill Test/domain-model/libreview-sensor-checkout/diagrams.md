# LibreView Sensor Self-Service Checkout — Diagrams

## Entity Relationship Diagram

```mermaid
classDiagram
    class Patient {
        +String patientId
    }

    class LibreViewAccount {
        +String accountId
        +String email
        +String[] linkedDevices
        +boolean dataSharingConsent
        +Date createdAt
    }

    class PatientProfile {
        +String profileId
        +String firstName
        +String lastName
        +Date dateOfBirth
        +String phone
        +Address[] shippingAddresses
    }

    class Prescription {
        +String rxId
        +String sensorType
        +number quantity
        +number refillsRemaining
        +Date issuedDate
        +Date expiryDate
        +RxStatus status
    }

    class HealthcareProvider {
        +String providerId
        +String npi
        +String name
        +String practice
        +String phone
        +String fax
    }

    class InsurancePlan {
        +String planId
        +String payerName
        +String payerId
        +String memberId
        +String groupNumber
        +CoverageTier coverageTier
        +Date effectiveDate
        +Date terminationDate
        +PlanStatus status
    }

    class EligibilityCheck {
        +String checkId
        +String sensorType
        +EligibilityResult result
        +Money copayAmount
        +number coveragePercentage
        +String denialReason
        +Date checkedAt
        +Date expiresAt
    }

    class PriorAuthorization {
        +String authId
        +PAStatus status
        +Date requestedAt
        +Date decidedAt
        +Date expiryDate
        +String authorizationNumber
    }

    class SensorProduct {
        +String productId
        +String name
        +SensorType sensorType
        +number wearDurationDays
        +Money price
        +boolean requiresPrescription
        +boolean requiresPriorAuth
    }

    class CheckoutSession {
        +String sessionId
        +Address shippingAddress
        +Money copayAmount
        +Money totalAmount
        +CheckoutStatus status
        +Date startedAt
    }

    class Order {
        +String orderId
        +number quantity
        +Money totalAmount
        +Address shippingAddress
        +OrderStatus status
        +Date orderedAt
    }

    class Payment {
        +String paymentId
        +PaymentMethod method
        +Money amount
        +Money insurancePortion
        +Money patientPortion
        +PaymentStatus status
        +Date processedAt
    }

    class Shipment {
        +String shipmentId
        +String carrier
        +String trackingNumber
        +Date shippedAt
        +Date estimatedDelivery
        +Date deliveredAt
        +ShipmentStatus status
    }

    Patient "1" -- "1" LibreViewAccount : has
    Patient "1" -- "1" PatientProfile : has
    Patient "1" -- "N" Prescription : has
    Patient "1" -- "N" InsurancePlan : has
    Patient "1" -- "N" Order : places

    Prescription "N" -- "1" HealthcareProvider : prescribed by
    Prescription "N" -- "1" SensorProduct : authorizes

    InsurancePlan "1" -- "N" EligibilityCheck : verified by
    EligibilityCheck "1" -- "0..1" PriorAuthorization : may require
    Prescription "1" -- "0..1" PriorAuthorization : linked to

    CheckoutSession "N" -- "1" Prescription : uses
    CheckoutSession "1" -- "1" EligibilityCheck : uses
    CheckoutSession "N" -- "1" SensorProduct : for
    CheckoutSession "1" -- "1" Order : creates

    Order "1" -- "1" Payment : has
    Order "1" -- "1" Shipment : has
```

## Self-Service Checkout Flow

```mermaid
sequenceDiagram
    participant P as Patient
    participant LV as LibreView Account
    participant PP as Patient Profile
    participant Rx as Prescription
    participant Ins as Insurance Plan
    participant Elig as Eligibility Check
    participant PA as Prior Authorization
    participant CS as Checkout Session
    participant Pay as Payment
    participant Ord as Order
    participant Ship as Shipment

    P->>LV: Log in
    LV-->>P: Authenticated

    P->>PP: Verify/update profile
    PP-->>P: Profile confirmed

    P->>Rx: Select active prescription
    Rx-->>CS: Rx validated (active, not expired, refills > 0)

    P->>CS: Select sensor product
    Note over CS: Product must match Rx sensorType

    CS->>Elig: Run eligibility check
    Elig->>Ins: Verify coverage
    Ins-->>Elig: Coverage response

    alt Eligibility Approved
        Elig-->>CS: Approved (copay: $X)
    else Eligibility Denied
        Elig-->>P: Denied (reason)
        Note over P: Checkout blocked
    end

    alt Prior Auth Required
        CS->>PA: Check PA status
        alt PA Approved
            PA-->>CS: Approved (authNumber)
        else PA Not Approved
            PA-->>P: PA required — contact provider
            Note over P: Checkout blocked
        end
    end

    P->>CS: Select shipping address
    P->>CS: Review & confirm order

    CS->>Pay: Charge patient portion (copay)
    alt Payment Success
        Pay-->>CS: Authorized
        CS->>Ord: Create order
        Ord->>Rx: Decrement refillsRemaining
        Ord-->>Ship: Initiate shipment
        Ship-->>P: Tracking info sent
    else Payment Failed
        Pay-->>P: Payment failed — retry or update method
    end
```

## Healthcare Gate Diagram

```mermaid
flowchart TD
    START([Patient starts checkout]) --> LOGIN[Log in to LibreView]
    LOGIN --> PROFILE{Profile complete?}
    PROFILE -->|No| UPDATE_PROFILE[Update profile / address]
    UPDATE_PROFILE --> PROFILE
    PROFILE -->|Yes| SELECT_RX[Select prescription]

    SELECT_RX --> RX_VALID{Rx valid?}
    RX_VALID -->|Expired / No refills| RX_BLOCKED[❌ Contact provider for new Rx]
    RX_VALID -->|Active + refills remaining| SELECT_PRODUCT[Select sensor product]

    SELECT_PRODUCT --> ELIG[Run eligibility check]
    ELIG --> ELIG_RESULT{Eligible?}
    ELIG_RESULT -->|Denied| ELIG_BLOCKED[❌ Coverage denied — show reason]
    ELIG_RESULT -->|Approved| PA_CHECK{Prior auth required?}

    PA_CHECK -->|No| CHECKOUT[Proceed to checkout]
    PA_CHECK -->|Yes| PA_STATUS{PA approved?}
    PA_STATUS -->|No / Pending| PA_BLOCKED[❌ PA required — contact provider]
    PA_STATUS -->|Yes| CHECKOUT

    CHECKOUT --> SELECT_ADDRESS[Select shipping address]
    SELECT_ADDRESS --> REVIEW[Review order + copay]
    REVIEW --> PAYMENT[Submit payment]

    PAYMENT --> PAY_RESULT{Payment success?}
    PAY_RESULT -->|Failed| PAY_RETRY[Retry or update payment method]
    PAY_RETRY --> PAYMENT
    PAY_RESULT -->|Success| ORDER[✅ Order created]

    ORDER --> FULFILL[Shipment initiated]
    FULFILL --> TRACKING[Tracking info sent to patient]
```

## Entity Lifecycle — Checkout Session States

```mermaid
stateDiagram-v2
    [*] --> IN_PROGRESS: Patient starts checkout
    IN_PROGRESS --> IN_PROGRESS: Updating selections
    IN_PROGRESS --> BLOCKED: Rx invalid / Eligibility denied / PA missing
    BLOCKED --> IN_PROGRESS: Issue resolved
    IN_PROGRESS --> COMPLETED: Payment authorized → Order created
    IN_PROGRESS --> ABANDONED: Patient leaves / Session timeout
    COMPLETED --> [*]
    ABANDONED --> [*]
    BLOCKED --> ABANDONED: Patient gives up
```

## Entity Lifecycle — Order States

```mermaid
stateDiagram-v2
    [*] --> CONFIRMED: Checkout completed
    CONFIRMED --> PROCESSING: Sent to fulfillment
    PROCESSING --> SHIPPED: Carrier picked up
    SHIPPED --> DELIVERED: Delivery confirmed
    CONFIRMED --> CANCELLED: Patient or system cancels
    PROCESSING --> CANCELLED: Cancelled before shipment
    DELIVERED --> [*]
    CANCELLED --> [*]
```
