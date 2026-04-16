import { DomainEvent } from './domain-event';

export class FulfillmentPoolAssigned implements DomainEvent {
  readonly eventName = 'FulfillmentPoolAssigned';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly orderId: string,
    public readonly fulfillmentPoolId: string,
    public readonly locationName: string,
  ) {}
}

export class DirectFulfillmentRouted implements DomainEvent {
  readonly eventName = 'DirectFulfillmentRouted';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly orderId: string,
    public readonly fulfillmentPoolId: string,
    public readonly items: ReadonlyArray<{ sku: string; quantity: number }>,
  ) {}
}
