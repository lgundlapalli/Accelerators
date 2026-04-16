import { ProductReference } from '../value-objects/product-reference';
import { Money } from '../value-objects/money';
import { EligibilityCheck } from '../value-objects/eligibility-check';

export class CartItem {
  constructor(
    public readonly id: string,
    public readonly product: ProductReference,
    private _quantity: number,
    public readonly eligibility: EligibilityCheck,
  ) {
    if (_quantity <= 0) throw new Error('Quantity must be positive');
  }

  get quantity(): number {
    return this._quantity;
  }

  get lineTotal(): Money {
    return this.product.price.multiply(this._quantity);
  }

  updateQuantity(newQuantity: number): CartItem {
    if (newQuantity <= 0) throw new Error('Quantity must be positive');
    return new CartItem(this.id, this.product, newQuantity, this.eligibility);
  }

  withEligibility(check: EligibilityCheck): CartItem {
    return new CartItem(this.id, this.product, this._quantity, check);
  }
}
