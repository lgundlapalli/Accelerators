import { InventoryItem } from '../entities/inventory-item';
import { SKU } from '../value-objects/sku';

export interface InventoryItemRepository {
  findBySku(sku: SKU): Promise<InventoryItem | null>;
  findBySkuWithAvailability(sku: SKU): Promise<InventoryItem | null>;
  save(item: InventoryItem): Promise<void>;
}
