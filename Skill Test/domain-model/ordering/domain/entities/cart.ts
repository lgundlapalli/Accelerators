import { CartItem } from './cart-item';
import { ProductReference } from '../value-objects/product-reference';
import { EligibilityCheck } from '../value-objects/eligibility-check';
import { DomainEvent } from '../events/domain-event';
import { ItemAddedToCart, ItemRemovedFromCart, CartUpdated, CheckoutStarted } from '../events/cart-events';

export class Cart {
  private _domainEvents: DomainEvent[] = [];

  constructor(
    public readonly id: string,
    public readonly customerId: string,
    private _items: CartItem[],
    public readonly createdAt: Date = new Date(),
  ) {}

  get items(): ReadonlyArray<CartItem> {
    return [...this._items];
  }

  get isEmpty(): boolean {
    return this._items.length === 0;
  }

  addItem(itemId: string, product: ProductReference, quantity: number, eligibility: EligibilityCheck): void {
    if (!eligibility.passed) {
      throw new Error(`Item not eligible: ${eligibility.reason}`);
    }

    const existing = this._items.find((i) => i.product.productId === product.productId);
    if (existing) {
      const updated = existing.updateQuantity(existing.quantity + quantity);
      this._items = this._items.map((i) => (i.id === existing.id ? updated : i));
    } else {
      this._items.push(new CartItem(itemId, product, quantity, eligibility));
    }

    this._domainEvents.push(new ItemAddedToCart(this.id, product.productId, quantity, product.price));
  }

  removeItem(productId: string): void {
    const item = this._items.find((i) => i.product.productId === productId);
    if (!item) throw new Error(`Product ${productId} not in cart`);

    this._items = this._items.filter((i) => i.product.productId !== productId);
    this._domainEvents.push(new ItemRemovedFromCart(this.id, productId));
  }

  updateItemQuantity(productId: string, newQuantity: number): void {
    const item = this._items.find((i) => i.product.productId === productId);
    if (!item) throw new Error(`Product ${productId} not in cart`);

    const updated = item.updateQuantity(newQuantity);
    this._items = this._items.map((i) => (i.id === item.id ? updated : i));
    this._domainEvents.push(new CartUpdated(this.id, this._items.length));
  }

  startCheckout(): void {
    if (this.isEmpty) {
      throw new Error('Cannot checkout with an empty cart');
    }

    const ineligible = this._items.find((i) => !i.eligibility.passed);
    if (ineligible) {
      throw new Error(`Item ${ineligible.product.name} is not eligible for purchase`);
    }

    this._domainEvents.push(
      new CheckoutStarted(
        this.id,
        this.customerId,
        this._items.map((i) => ({ productId: i.product.productId, quantity: i.quantity })),
      ),
    );
  }

  pullDomainEvents(): DomainEvent[] {
    const events = [...this._domainEvents];
    this._domainEvents = [];
    return events;
  }
}
