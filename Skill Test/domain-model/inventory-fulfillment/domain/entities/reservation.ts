import { Quantity } from '../value-objects/quantity';

export type ReservationStatus = 'ACTIVE' | 'FULFILLED' | 'RELEASED';

export class Reservation {
  constructor(
    public readonly id: string,
    public readonly orderId: string,
    public readonly quantity: Quantity,
    private _status: ReservationStatus = 'ACTIVE',
    public readonly createdAt: Date = new Date(),
  ) {
    if (!orderId) throw new Error('Order ID is required for reservation');
  }

  get status(): ReservationStatus {
    return this._status;
  }

  get isActive(): boolean {
    return this._status === 'ACTIVE';
  }

  fulfill(): void {
    if (this._status !== 'ACTIVE') {
      throw new Error(`Cannot fulfill reservation in status ${this._status}`);
    }
    this._status = 'FULFILLED';
  }

  release(): void {
    if (this._status !== 'ACTIVE') {
      throw new Error(`Cannot release reservation in status ${this._status}`);
    }
    this._status = 'RELEASED';
  }
}
