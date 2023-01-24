import { PredictorController } from './predictor.controller';
import { PredictorService } from './predictor.service';
import { Test, TestingModule } from '@nestjs/testing';

describe('PredictorModule', () => {
  let controller: PredictorController;
  let service: PredictorService;

  beforeAll(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [PredictorController],
      providers: [PredictorService]
    }).compile();

    controller = await module.resolve<PredictorController>(PredictorController);
    service = await module.resolve<PredictorService>(PredictorService);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
    expect(controller).toBeInstanceOf(PredictorController);
    expect(service).toBeDefined();
    expect(service).toBeInstanceOf(PredictorService);
  });
});
