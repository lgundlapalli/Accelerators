import { DomainEvent } from './domain-event';
import { Money } from '../value-objects/money';

export class ItemAddedToCart implements DomainEvent {
  readonly eventName = 'ItemAddedToCart';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly productId: string,
    public readonly quantity: number,
    public readonly price: Money,
  ) {}
}

export class ItemRemovedFromCart implements DomainEvent {
  readonly eventName = 'ItemRemovedFromCart';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly productId: string,
  ) {}
}

export class CartUpdated implements DomainEvent {
  readonly eventName = 'CartUpdated';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly itemCount: number,
  ) {}
}

export class EligibilityChecked implements DomainEvent {
  readonly eventName = 'EligibilityChecked';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly customerId: string,
    public readonly passed: boolean,
    public readonly reason: string,
  ) {}
}

export class CheckoutStarted implements DomainEvent {
  readonly eventName = 'CheckoutStarted';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly customerId: string,
    public readonly items: ReadonlyArray<{ productId: string; quantity: number }>,
  ) {}
}
