import { ProductReference } from '../value-objects/product-reference';
import { Money } from '../value-objects/money';

export class OrderLineItem {
  constructor(
    public readonly id: string,
    public readonly product: ProductReference,
    public readonly quantity: number,
    public readonly unitPrice: Money,
  ) {
    if (quantity <= 0) throw new Error('Quantity must be positive');
  }

  get lineTotal(): Money {
    return this.unitPrice.multiply(this.quantity);
  }
}
