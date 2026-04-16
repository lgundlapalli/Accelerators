import { Money } from './money';

export type DiscountType = 'PERCENTAGE' | 'FIXED_AMOUNT' | 'FREE_SHIPPING';

export class Discount {
  constructor(
    public readonly type: DiscountType,
    public readonly amount: Money,
    public readonly reason: string,
  ) {
    if (amount.amount < 0) throw new Error('Discount amount cannot be negative');
    if (!reason) throw new Error('Discount reason is required');
  }

  equals(other: Discount): boolean {
    return this.type === other.type && this.amount.equals(other.amount) && this.reason === other.reason;
  }
}
