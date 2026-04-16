export interface BackorderMonitorService {
  checkAndCancelExpiredBackorders(asOf?: Date): Promise<string[]>;
}
