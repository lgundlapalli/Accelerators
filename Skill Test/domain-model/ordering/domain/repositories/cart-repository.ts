import { Cart } from '../entities/cart';

export interface CartRepository {
  findById(cartId: string): Promise<Cart | null>;
  findByCustomerId(customerId: string): Promise<Cart | null>;
  save(cart: Cart): Promise<void>;
}
