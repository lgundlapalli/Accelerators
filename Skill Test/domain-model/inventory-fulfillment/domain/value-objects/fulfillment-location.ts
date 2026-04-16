export class FulfillmentLocation {
  constructor(
    public readonly warehouseId: string,
    public readonly name: string,
    public readonly address: string,
    public readonly city: string,
    public readonly state: string,
    public readonly country: string,
  ) {
    if (!warehouseId) throw new Error('Warehouse ID is required');
    if (!name) throw new Error('Location name is required');
  }

  equals(other: FulfillmentLocation): boolean {
    return this.warehouseId === other.warehouseId;
  }
}
