import { SKU } from '../value-objects/sku';
import { Quantity } from '../value-objects/quantity';
import { Reservation } from './reservation';
import { DomainEvent } from '../events/domain-event';
import {
  OnHandInventoryChecked,
  InventoryReserved,
  InventoryUnavailable,
  InventoryRestocked,
  ReservationReleased,
} from '../events/inventory-events';

export class InventoryItem {
  private _domainEvents: DomainEvent[] = [];

  constructor(
    public readonly id: string,
    public readonly sku: SKU,
    private _onHand: Quantity,
    private _reservations: Reservation[],
  ) {}

  get onHand(): Quantity {
    return this._onHand;
  }

  get totalReserved(): Quantity {
    return this._reservations
      .filter((r) => r.isActive)
      .reduce((sum, r) => sum.add(r.quantity), new Quantity(0));
  }

  get available(): Quantity {
    return this._onHand.subtract(this.totalReserved);
  }

  get reservations(): ReadonlyArray<Reservation> {
    return [...this._reservations];
  }

  checkAvailability(): Quantity {
    this._domainEvents.push(
      new OnHandInventoryChecked(this.id, this.sku.value, this.available.value),
    );
    return this.available;
  }

  reserve(reservationId: string, orderId: string, quantity: Quantity): boolean {
    if (this.available.isGreaterThan(quantity) || this.available.equals(quantity)) {
      const reservation = new Reservation(reservationId, orderId, quantity);
      this._reservations.push(reservation);

      this._domainEvents.push(
        new InventoryReserved(this.id, orderId, this.sku.value, quantity.value, reservationId),
      );
      return true;
    }

    this._domainEvents.push(
      new InventoryUnavailable(this.id, orderId, this.sku.value, quantity.value),
    );
    return false;
  }

  releaseReservation(orderId: string): void {
    const reservation = this._reservations.find((r) => r.orderId === orderId && r.isActive);
    if (!reservation) {
      throw new Error(`No active reservation found for order ${orderId}`);
    }

    reservation.release();
    this._domainEvents.push(
      new ReservationReleased(this.id, orderId, this.sku.value, reservation.quantity.value),
    );
  }

  restock(quantity: Quantity, reason: string): void {
    this._onHand = this._onHand.add(quantity);
    this._domainEvents.push(
      new InventoryRestocked(this.id, this.sku.value, quantity.value, reason),
    );
  }

  pullDomainEvents(): DomainEvent[] {
    const events = [...this._domainEvents];
    this._domainEvents = [];
    return events;
  }
}
