import { FulfillmentPool } from '../value-objects/fulfillment-pool';

interface FulfillmentRoutingRequest {
  orderId: string;
  items: ReadonlyArray<{ sku: string; quantity: number }>;
  shippingAddress: { city: string; state: string; country: string };
}

export interface FulfillmentRoutingService {
  selectBestPool(request: FulfillmentRoutingRequest): Promise<FulfillmentPool>;
}
