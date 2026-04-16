import { Money } from './money';

export class ProductReference {
  constructor(
    public readonly productId: string,
    public readonly name: string,
    public readonly price: Money,
  ) {
    if (!productId) throw new Error('Product ID is required');
    if (!name) throw new Error('Product name is required');
  }

  equals(other: ProductReference): boolean {
    return this.productId === other.productId;
  }
}
