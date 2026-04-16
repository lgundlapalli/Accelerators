import { EligibilityCheck } from '../value-objects/eligibility-check';
import { ShippingAddress } from '../value-objects/shipping-address';

export interface EligibilityService {
  checkItemEligibility(customerId: string, productId: string, shippingAddress: ShippingAddress): Promise<EligibilityCheck>;

  checkCheckoutEligibility(customerId: string, shippingAddress: ShippingAddress): Promise<EligibilityCheck>;
}
