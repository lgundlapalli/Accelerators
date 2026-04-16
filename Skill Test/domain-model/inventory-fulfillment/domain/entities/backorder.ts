import { SKU } from '../value-objects/sku';
import { Quantity } from '../value-objects/quantity';
import { BackorderDeadline } from '../value-objects/backorder-deadline';
import { DomainEvent } from '../events/domain-event';
import { OrderBackordered, BackorderAutoCancelled } from '../events/backorder-events';

export type BackorderStatus = 'WAITING' | 'FULFILLED' | 'AUTO_CANCELLED';

export class Backorder {
  private _domainEvents: DomainEvent[] = [];

  constructor(
    public readonly id: string,
    public readonly orderId: string,
    public readonly sku: SKU,
    public readonly quantity: Quantity,
    public readonly deadline: BackorderDeadline,
    private _status: BackorderStatus = 'WAITING',
  ) {
    this._domainEvents.push(
      new OrderBackordered(this.id, orderId, sku.value, deadline.expiresAt),
    );
  }

  get status(): BackorderStatus {
    return this._status;
  }

  get isExpired(): boolean {
    return this.deadline.isExpired();
  }

  checkDeadline(asOf: Date = new Date()): boolean {
    if (this._status !== 'WAITING') return false;

    if (this.deadline.isExpired(asOf)) {
      this._status = 'AUTO_CANCELLED';
      this._domainEvents.push(
        new BackorderAutoCancelled(this.id, this.orderId, this.sku.value),
      );
      return true;
    }
    return false;
  }

  fulfill(): void {
    if (this._status !== 'WAITING') {
      throw new Error(`Cannot fulfill backorder in status ${this._status}`);
    }
    this._status = 'FULFILLED';
  }

  pullDomainEvents(): DomainEvent[] {
    const events = [...this._domainEvents];
    this._domainEvents = [];
    return events;
  }
}
