import { DomainEvent } from './domain-event';

export class OrderBackordered implements DomainEvent {
  readonly eventName = 'OrderBackordered';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly orderId: string,
    public readonly sku: string,
    public readonly backorderDeadline: Date,
  ) {}
}

export class BackorderAutoCancelled implements DomainEvent {
  readonly eventName = 'BackorderAutoCancelled';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly orderId: string,
    public readonly sku: string,
  ) {}
}
