# LibreView Sensor Self-Service Checkout — Domain Model

## Overview
A self-service checkout system for FreeStyle Libre continuous glucose monitoring (CGM) sensors, integrated with a healthcare flow. Patients with a valid prescription and verified insurance eligibility can purchase sensors through a streamlined online checkout tied to their LibreView account.

## Actors

| Actor | Role |
|-------|------|
| **Patient** | Purchases sensors via self-service checkout |
| **Healthcare Provider / Prescriber** | Issues prescriptions authorizing sensor purchase |
| **Insurance / Payer** | Verifies coverage, approves prior authorizations, covers portion of cost |
| **Pharmacy / Fulfillment** | Ships sensors to the patient |

## Entities

### LibreView Account
The patient's account on the LibreView platform. Manages login credentials, linked CGM devices, and glucose data sharing preferences. Distinct from the patient's checkout profile.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| accountId | string | yes | Unique LibreView ID |
| email | string | yes | Login email |
| linkedDevices | string[] | no | CGM devices linked to account |
| dataSharingConsent | boolean | yes | Whether glucose data can be shared with provider |
| createdAt | Date | yes | Account creation date |

### Patient Profile
Demographics, shipping addresses, and contact info. Managed separately from the LibreView account to support profile updates without affecting account credentials.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| profileId | string | yes | Unique profile ID |
| accountId | string | yes | Link to LibreView Account |
| firstName | string | yes | Legal first name |
| lastName | string | yes | Legal last name |
| dateOfBirth | Date | yes | DOB — needed for insurance verification |
| phone | string | yes | Contact number |
| shippingAddresses | Address[] | yes | One or more delivery addresses |
| insurancePlanId | string | no | Link to active insurance plan |

### Prescription
A valid Rx from a healthcare provider authorizing sensor purchase. Tracks refill count, expiry, and the specific sensor type prescribed.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| rxId | string | yes | Prescription ID |
| patientId | string | yes | Link to patient |
| prescriberId | string | yes | Link to healthcare provider |
| sensorType | string | yes | Which sensor (Libre 2, Libre 3, etc.) |
| quantity | number | yes | Units per fill |
| refillsRemaining | number | yes | How many refills left |
| issuedDate | Date | yes | When Rx was written |
| expiryDate | Date | yes | When Rx expires |
| status | enum | yes | ACTIVE, EXPIRED, CANCELLED |

### Insurance Plan
The patient's insurance coverage details. A patient may have multiple plans (primary/secondary).

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| planId | string | yes | Unique plan ID |
| patientId | string | yes | Link to patient |
| payerName | string | yes | Insurance company name |
| payerId | string | yes | Payer system ID |
| memberId | string | yes | Patient's member ID on the plan |
| groupNumber | string | no | Group number |
| coverageTier | enum | yes | COMMERCIAL, MEDICARE, MEDICAID, CASH_PAY |
| effectiveDate | Date | yes | Coverage start date |
| terminationDate | Date | no | Coverage end date |
| status | enum | yes | ACTIVE, INACTIVE, PENDING |

### Eligibility Check
A verification request against the payer to confirm the patient's plan covers the specific sensor. Returns approval/denial, copay amount, and coverage tier.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| checkId | string | yes | Unique check ID |
| patientId | string | yes | Link to patient |
| planId | string | yes | Link to insurance plan |
| sensorType | string | yes | Product being checked |
| result | enum | yes | APPROVED, DENIED, PENDING |
| copayAmount | Money | no | Patient's copay if approved |
| coveragePercentage | number | no | What % insurance covers |
| denialReason | string | no | Why denied, if applicable |
| checkedAt | Date | yes | When verification ran |
| expiresAt | Date | yes | How long this check is valid |

### Prior Authorization
A separate pre-approval from the payer required for certain plans before purchase is allowed. Has its own status, expiry, and authorization reference number.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| authId | string | yes | Unique PA ID |
| patientId | string | yes | Link to patient |
| planId | string | yes | Link to insurance plan |
| rxId | string | yes | Link to prescription |
| status | enum | yes | REQUESTED, APPROVED, DENIED, EXPIRED |
| requestedAt | Date | yes | When PA was submitted |
| decidedAt | Date | no | When payer responded |
| expiryDate | Date | no | When approval expires |
| authorizationNumber | string | no | Payer's auth reference number |

### Sensor Product
The FreeStyle Libre sensor being purchased. Tracks type, wear duration, price, and whether Rx/PA is required.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| productId | string | yes | Unique product ID |
| name | string | yes | Display name (FreeStyle Libre 3) |
| sensorType | enum | yes | LIBRE_2, LIBRE_3, LIBRE_3_PLUS |
| wearDurationDays | number | yes | How long the sensor lasts (14 days, etc.) |
| price | Money | yes | Retail price |
| requiresPrescription | boolean | yes | Whether Rx is needed |
| requiresPriorAuth | boolean | yes | Whether PA is commonly required |

### Healthcare Provider
The prescribing physician or practice. Identified by NPI for Rx verification.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| providerId | string | yes | NPI or internal ID |
| npi | string | yes | National Provider Identifier |
| name | string | yes | Provider name |
| practice | string | no | Practice/clinic name |
| phone | string | no | Contact number |
| fax | string | no | For Rx verification |

### Checkout Session
The self-service checkout flow tying together patient, Rx, eligibility, product selection, and shipping. Gates on valid Rx + approved eligibility before allowing order placement.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| sessionId | string | yes | Unique session ID |
| patientId | string | yes | Link to patient |
| rxId | string | yes | Link to valid prescription |
| eligibilityCheckId | string | yes | Link to eligibility result |
| priorAuthId | string | no | Link to PA if required |
| productId | string | yes | Sensor being purchased |
| shippingAddress | Address | yes | Selected delivery address |
| copayAmount | Money | no | From eligibility check |
| totalAmount | Money | yes | What patient pays |
| status | enum | yes | IN_PROGRESS, COMPLETED, ABANDONED, BLOCKED |
| startedAt | Date | yes | When checkout began |

### Order
A confirmed purchase created from a successful checkout session.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| orderId | string | yes | Unique order ID |
| sessionId | string | yes | Link to checkout session |
| patientId | string | yes | Link to patient |
| productId | string | yes | Sensor ordered |
| quantity | number | yes | Units ordered |
| totalAmount | Money | yes | Amount charged |
| paymentId | string | yes | Link to payment |
| shippingAddress | Address | yes | Delivery address |
| status | enum | yes | CONFIRMED, PROCESSING, SHIPPED, DELIVERED, CANCELLED |
| orderedAt | Date | yes | When order was placed |

### Payment
Transaction record for the order. Splits between insurance portion and patient portion (copay).

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| paymentId | string | yes | Unique payment ID |
| orderId | string | yes | Link to order |
| method | enum | yes | CREDIT_CARD, HSA, FSA, INSURANCE_DIRECT |
| amount | Money | yes | Total amount |
| insurancePortion | Money | no | What insurance covers |
| patientPortion | Money | yes | What patient pays (copay) |
| status | enum | yes | PENDING, AUTHORIZED, CAPTURED, FAILED, REFUNDED |
| processedAt | Date | no | When payment completed |

### Shipment
Fulfillment record for delivering the sensor to the patient.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| shipmentId | string | yes | Unique shipment ID |
| orderId | string | yes | Link to order |
| carrier | string | yes | Shipping carrier |
| trackingNumber | string | no | Tracking ID |
| shippedAt | Date | no | When shipped |
| estimatedDelivery | Date | no | Expected delivery date |
| deliveredAt | Date | no | Actual delivery date |
| status | enum | yes | PENDING, SHIPPED, IN_TRANSIT, DELIVERED, FAILED |

## Relationships

| Entity A | Relationship | Entity B | Cardinality | Description |
|----------|-------------|----------|-------------|-------------|
| Patient | has one | LibreView Account | 1:1 | Every patient has one LibreView account |
| Patient | has one | Patient Profile | 1:1 | Demographics and addresses |
| Patient | has many | Prescription | 1:N | Multiple Rx over time |
| Patient | has many | Insurance Plan | 1:N | Can have multiple plans (primary/secondary) |
| Patient | has many | Order | 1:N | Order history |
| Prescription | prescribed by | Healthcare Provider | N:1 | One provider per Rx |
| Prescription | authorizes | Sensor Product | N:1 | Rx specifies which sensor type |
| Insurance Plan | verified by | Eligibility Check | 1:N | Multiple checks over time |
| Eligibility Check | may require | Prior Authorization | 1:0..1 | PA only if plan requires it |
| Prescription | linked to | Prior Authorization | 1:0..1 | PA ties to a specific Rx |
| Checkout Session | uses | Prescription | N:1 | Session validates against an Rx |
| Checkout Session | uses | Eligibility Check | 1:1 | Must have a valid eligibility result |
| Checkout Session | for | Sensor Product | N:1 | One product per checkout |
| Checkout Session | creates | Order | 1:1 | Successful checkout → one order |
| Order | has one | Payment | 1:1 | One payment per order |
| Order | has one | Shipment | 1:1 | One shipment per order |

## Self-Service Checkout Flow

The healthcare-gated checkout follows this sequence:

1. **Patient logs in** via LibreView Account
2. **Profile check** — verify demographics, shipping address on file
3. **Prescription validation** — confirm active, non-expired Rx with refills remaining
4. **Product selection** — choose sensor type matching the Rx
5. **Eligibility check** — verify insurance covers the sensor, get copay amount
6. **Prior authorization** — if required by plan, check PA status (must be approved)
7. **Checkout** — confirm shipping address, review copay/total
8. **Payment** — charge patient portion (copay via credit card, HSA, or FSA)
9. **Order created** — confirmed and sent to fulfillment
10. **Shipment** — sensor shipped, tracking provided

### Checkout Gates (must all pass before order placement)
- Rx is ACTIVE and not expired
- Rx has refillsRemaining > 0
- Eligibility check result is APPROVED and not expired
- Prior Authorization (if required) is APPROVED and not expired
- Shipping address is valid
- Payment is authorized
