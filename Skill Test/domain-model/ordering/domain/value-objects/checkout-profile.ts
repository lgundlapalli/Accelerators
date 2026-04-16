import { ShippingAddress } from './shipping-address';

export class CheckoutProfile {
  constructor(
    public readonly customerId: string,
    public readonly name: string,
    public readonly email: string,
    public readonly shippingAddress: ShippingAddress,
  ) {
    if (!customerId) throw new Error('Customer ID is required');
    if (!name) throw new Error('Name is required');
    if (!email) throw new Error('Email is required');
  }

  withShippingAddress(address: ShippingAddress): CheckoutProfile {
    return new CheckoutProfile(this.customerId, this.name, this.email, address);
  }

  equals(other: CheckoutProfile): boolean {
    return this.customerId === other.customerId && this.shippingAddress.equals(other.shippingAddress);
  }
}
