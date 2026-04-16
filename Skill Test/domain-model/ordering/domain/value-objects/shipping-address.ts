export class ShippingAddress {
  constructor(
    public readonly street: string,
    public readonly city: string,
    public readonly state: string,
    public readonly zipCode: string,
    public readonly country: string,
    public readonly validated: boolean = false,
  ) {
    if (!street || !city || !zipCode || !country) {
      throw new Error('Street, city, zip code, and country are required');
    }
  }

  markValidated(): ShippingAddress {
    return new ShippingAddress(this.street, this.city, this.state, this.zipCode, this.country, true);
  }

  equals(other: ShippingAddress): boolean {
    return (
      this.street === other.street &&
      this.city === other.city &&
      this.state === other.state &&
      this.zipCode === other.zipCode &&
      this.country === other.country
    );
  }
}
