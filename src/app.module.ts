import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { PredictorModule } from './predictor/predictor.module';

@Module({
  imports: [PredictorModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
