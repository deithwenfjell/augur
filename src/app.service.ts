import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHealthCheck(): string {
    const date: string = new Date().toISOString();
    return date;
  }
}
