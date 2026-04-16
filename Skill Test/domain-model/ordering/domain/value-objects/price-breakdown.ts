import { Money } from './money';
import { Discount } from './discount';

export class PriceBreakdown {
  public readonly total: Money;

  constructor(
    public readonly subtotal: Money,
    public readonly tax: Money,
    public readonly shippingCost: Money,
    public readonly discount: Discount | null,
  ) {
    const discountAmount = discount ? discount.amount : new Money(0, subtotal.currency);
    this.total = subtotal.add(tax).add(shippingCost).subtract(discountAmount);

    if (this.total.amount < 0) {
      throw new Error('Order total cannot be negative');
    }
  }

  equals(other: PriceBreakdown): boolean {
    return this.total.equals(other.total) && this.subtotal.equals(other.subtotal);
  }
}
