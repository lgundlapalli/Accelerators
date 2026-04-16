import { FulfillmentOrder } from '../entities/fulfillment-order';

export interface FulfillmentOrderRepository {
  findById(id: string): Promise<FulfillmentOrder | null>;
  findByOrderId(orderId: string): Promise<FulfillmentOrder[]>;
  save(fulfillmentOrder: FulfillmentOrder): Promise<void>;
}
