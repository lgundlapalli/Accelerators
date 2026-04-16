import { CartItem } from '../entities/cart-item';
import { Money } from '../value-objects/money';
import { PriceBreakdown } from '../value-objects/price-breakdown';
import { Discount } from '../value-objects/discount';
import { ShippingAddress } from '../value-objects/shipping-address';

export interface PricingService {
  calculateBreakdown(
    items: ReadonlyArray<CartItem>,
    shippingAddress: ShippingAddress,
    discount: Discount | null,
  ): Promise<PriceBreakdown>;

  calculateTax(subtotal: Money, shippingAddress: ShippingAddress): Promise<Money>;

  calculateShippingCost(items: ReadonlyArray<CartItem>, shippingAddress: ShippingAddress): Promise<Money>;
}
