import { FulfillmentLocation } from './fulfillment-location';

export class FulfillmentPool {
  constructor(
    public readonly poolId: string,
    public readonly location: FulfillmentLocation,
    public readonly poolType: 'DIRECT' | 'REGIONAL' | 'OVERFLOW',
  ) {
    if (!poolId) throw new Error('Pool ID is required');
  }

  equals(other: FulfillmentPool): boolean {
    return this.poolId === other.poolId;
  }
}
