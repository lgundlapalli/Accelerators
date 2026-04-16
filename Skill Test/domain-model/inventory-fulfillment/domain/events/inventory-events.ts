import { DomainEvent } from './domain-event';

export class OnHandInventoryChecked implements DomainEvent {
  readonly eventName = 'OnHandInventoryChecked';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly sku: string,
    public readonly availableQuantity: number,
  ) {}
}

export class InventoryReserved implements DomainEvent {
  readonly eventName = 'InventoryReserved';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly orderId: string,
    public readonly sku: string,
    public readonly quantity: number,
    public readonly reservationId: string,
  ) {}
}

export class InventoryUnavailable implements DomainEvent {
  readonly eventName = 'InventoryUnavailable';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly orderId: string,
    public readonly sku: string,
    public readonly requestedQuantity: number,
  ) {}
}

export class InventoryRestocked implements DomainEvent {
  readonly eventName = 'InventoryRestocked';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly sku: string,
    public readonly quantity: number,
    public readonly reason: string,
  ) {}
}

export class ReservationReleased implements DomainEvent {
  readonly eventName = 'ReservationReleased';
  readonly occurredOn = new Date();

  constructor(
    public readonly aggregateId: string,
    public readonly orderId: string,
    public readonly sku: string,
    public readonly quantity: number,
  ) {}
}
