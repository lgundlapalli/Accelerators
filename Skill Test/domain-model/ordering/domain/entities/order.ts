import { OrderLineItem } from './order-line-item';
import { CheckoutProfile } from '../value-objects/checkout-profile';
import { PriceBreakdown } from '../value-objects/price-breakdown';
import { ShippingAddress } from '../value-objects/shipping-address';
import { DomainEvent } from '../events/domain-event';
import { OrderPlaced, OrderCancelled, OrderConfirmationSent } from '../events/order-events';

export type OrderStatus = 'PENDING' | 'PLACED' | 'CANCELLED';

export class Order {
  private _domainEvents: DomainEvent[] = [];

  constructor(
    public readonly id: string,
    public readonly checkoutProfile: CheckoutProfile,
    private _lineItems: OrderLineItem[],
    private _priceBreakdown: PriceBreakdown,
    private _status: OrderStatus,
    public readonly createdAt: Date = new Date(),
  ) {
    if (_lineItems.length === 0) {
      throw new Error('Order must have at least one line item');
    }
    if (!checkoutProfile.shippingAddress.validated) {
      throw new Error('Shipping address must be validated before order creation');
    }
  }

  get status(): OrderStatus {
    return this._status;
  }

  get lineItems(): ReadonlyArray<OrderLineItem> {
    return [...this._lineItems];
  }

  get priceBreakdown(): PriceBreakdown {
    return this._priceBreakdown;
  }

  place(): void {
    if (this._status !== 'PENDING') {
      throw new Error(`Cannot place order in status ${this._status}`);
    }
    this._status = 'PLACED';

    this._domainEvents.push(
      new OrderPlaced(
        this.id,
        this.checkoutProfile.customerId,
        this._lineItems.map((li) => ({
          productId: li.product.productId,
          quantity: li.quantity,
          price: li.unitPrice,
        })),
        {
          street: this.checkoutProfile.shippingAddress.street,
          city: this.checkoutProfile.shippingAddress.city,
          state: this.checkoutProfile.shippingAddress.state,
          zipCode: this.checkoutProfile.shippingAddress.zipCode,
          country: this.checkoutProfile.shippingAddress.country,
        },
        this._priceBreakdown.total,
      ),
    );
  }

  sendConfirmation(): void {
    if (this._status !== 'PLACED') {
      throw new Error('Can only send confirmation for placed orders');
    }
    this._domainEvents.push(
      new OrderConfirmationSent(this.id, this.checkoutProfile.customerId, this.checkoutProfile.email),
    );
  }

  cancel(cancelledBy: 'CUSTOMER' | 'CS_REP', reason: string, repId?: string): void {
    if (this._status === 'CANCELLED') {
      throw new Error('Order is already cancelled');
    }
    this._status = 'CANCELLED';
    this._domainEvents.push(new OrderCancelled(this.id, cancelledBy, reason, repId));
  }

  pullDomainEvents(): DomainEvent[] {
    const events = [...this._domainEvents];
    this._domainEvents = [];
    return events;
  }
}
