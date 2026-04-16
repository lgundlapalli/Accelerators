export class EligibilityCheck {
  constructor(
    public readonly passed: boolean,
    public readonly reason: string,
    public readonly checkedAt: Date,
  ) {}

  static pass(): EligibilityCheck {
    return new EligibilityCheck(true, 'Eligible', new Date());
  }

  static fail(reason: string): EligibilityCheck {
    return new EligibilityCheck(false, reason, new Date());
  }
}
