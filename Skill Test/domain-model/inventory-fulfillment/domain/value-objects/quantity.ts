export class Quantity {
  constructor(public readonly value: number) {
    if (value < 0) throw new Error('Quantity cannot be negative');
    if (!Number.isInteger(value)) throw new Error('Quantity must be a whole number');
  }

  add(other: Quantity): Quantity {
    return new Quantity(this.value + other.value);
  }

  subtract(other: Quantity): Quantity {
    return new Quantity(this.value - other.value);
  }

  isZero(): boolean {
    return this.value === 0;
  }

  isGreaterThan(other: Quantity): boolean {
    return this.value > other.value;
  }

  equals(other: Quantity): boolean {
    return this.value === other.value;
  }
}
