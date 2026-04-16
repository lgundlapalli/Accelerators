import { Order, OrderStatus } from '../entities/order';

export interface OrderRepository {
  findById(orderId: string): Promise<Order | null>;
  findByCustomerId(customerId: string): Promise<Order[]>;
  findByStatus(status: OrderStatus): Promise<Order[]>;
  save(order: Order): Promise<void>;
  nextId(): string;
}
