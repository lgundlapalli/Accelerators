import { FulfillmentPool } from '../value-objects/fulfillment-pool';
import { Quantity } from '../value-objects/quantity';
import { DomainEvent } from '../events/domain-event';
import { FulfillmentPoolAssigned, DirectFulfillmentRouted } from '../events/fulfillment-events';

export type FulfillmentOrderStatus = 'PENDING' | 'ASSIGNED' | 'ROUTED' | 'SHIPPED';

interface FulfillmentLineItem {
  sku: string;
  quantity: Quantity;
}

export class FulfillmentOrder {
  private _domainEvents: DomainEvent[] = [];

  constructor(
    public readonly id: string,
    public readonly orderId: string,
    private _items: FulfillmentLineItem[],
    private _pool: FulfillmentPool | null,
    private _status: FulfillmentOrderStatus = 'PENDING',
    public readonly createdAt: Date = new Date(),
  ) {}

  get status(): FulfillmentOrderStatus {
    return this._status;
  }

  get pool(): FulfillmentPool | null {
    return this._pool;
  }

  get items(): ReadonlyArray<FulfillmentLineItem> {
    return [...this._items];
  }

  assignPool(pool: FulfillmentPool): void {
    if (this._status !== 'PENDING') {
      throw new Error(`Cannot assign pool when status is ${this._status}`);
    }

    this._pool = pool;
    this._status = 'ASSIGNED';

    this._domainEvents.push(
      new FulfillmentPoolAssigned(this.id, this.orderId, pool.poolId, pool.location.name),
    );
  }

  routeForDirectFulfillment(): void {
    if (!this._pool) {
      throw new Error('Must be assigned to a pool before routing');
    }
    if (this._status !== 'ASSIGNED') {
      throw new Error(`Cannot route when status is ${this._status}`);
    }

    this._status = 'ROUTED';

    this._domainEvents.push(
      new DirectFulfillmentRouted(
        this.id,
        this.orderId,
        this._pool.poolId,
        this._items.map((i) => ({ sku: i.sku, quantity: i.quantity.value })),
      ),
    );
  }

  markShipped(): void {
    if (this._status !== 'ROUTED') {
      throw new Error(`Cannot mark shipped when status is ${this._status}`);
    }
    this._status = 'SHIPPED';
  }

  pullDomainEvents(): DomainEvent[] {
    const events = [...this._domainEvents];
    this._domainEvents = [];
    return events;
  }
}
