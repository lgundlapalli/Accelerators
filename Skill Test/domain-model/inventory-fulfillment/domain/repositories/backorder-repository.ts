import { Backorder } from '../entities/backorder';

export interface BackorderRepository {
  findById(id: string): Promise<Backorder | null>;
  findByOrderId(orderId: string): Promise<Backorder | null>;
  findExpired(asOfDate: Date): Promise<Backorder[]>;
  save(backorder: Backorder): Promise<void>;
}
