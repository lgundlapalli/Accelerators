import { DomainEvent } from './domain-event';
import { Money } from '../value-objects/money';

export class OrderPlaced implements DomainEvent {
  readonly eventName = 'OrderPlaced';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly customerId: string,
    public readonly lineItems: ReadonlyArray<{ productId: string; quantity: number; price: Money }>,
    public readonly shippingAddress: { street: string; city: string; state: string; zipCode: string; country: string },
    public readonly total: Money,
  ) {}
}

export class PriceCalculated implements DomainEvent {
  readonly eventName = 'PriceCalculated';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly subtotal: Money,
    public readonly tax: Money,
    public readonly shippingCost: Money,
    public readonly total: Money,
  ) {}
}

export class DiscountApplied implements DomainEvent {
  readonly eventName = 'DiscountApplied';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly discountType: string,
    public readonly discountAmount: Money,
    public readonly reason: string,
  ) {}
}

export class OrderConfirmationSent implements DomainEvent {
  readonly eventName = 'OrderConfirmationSent';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly customerId: string,
    public readonly email: string,
  ) {}
}

export class OrderCancelled implements DomainEvent {
  readonly eventName = 'OrderCancelled';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly cancelledBy: 'CUSTOMER' | 'CS_REP',
    public readonly reason: string,
    public readonly repId?: string,
  ) {}
}
