import { Test, TestingModule } from '@nestjs/testing';
import { PredictorController } from './predictor.controller';
import { IndicatorsDto } from './dto/indicators.dto';
import { ResultDto } from './dto/result.dto';
import { PredictorService } from './predictor.service';

describe('PredictorController', () => {
  let controller: PredictorController;
  let service: PredictorService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [PredictorController],
      providers: [PredictorService]
    }).compile();

    controller = module.get<PredictorController>(PredictorController);
    service = module.get<PredictorService>(PredictorService);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });

  it('should return result', async () => {
    jest.spyOn(service, 'predict').mockImplementationOnce(async (): Promise<ResultDto>  => {
      const res = new ResultDto();
      res.result = 0;
      return res;
    })
    const data = new IndicatorsDto();

    const result = await controller.predict(data);
    expect(result).toBeInstanceOf(ResultDto);
    expect(result.result).toBeLessThan(1);
  })
});
