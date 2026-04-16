const TWO_WEEKS_MS = 14 * 24 * 60 * 60 * 1000;

export class BackorderDeadline {
  public readonly expiresAt: Date;

  constructor(public readonly createdAt: Date) {
    this.expiresAt = new Date(createdAt.getTime() + TWO_WEEKS_MS);
  }

  isExpired(asOf: Date = new Date()): boolean {
    return asOf >= this.expiresAt;
  }

  daysRemaining(asOf: Date = new Date()): number {
    const remaining = this.expiresAt.getTime() - asOf.getTime();
    return Math.max(0, Math.ceil(remaining / (24 * 60 * 60 * 1000)));
  }
}
