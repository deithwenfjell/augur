import { Test, TestingModule } from '@nestjs/testing';
import { PredictorService } from './predictor.service';
import { IndicatorsDto } from './dto/indicators.dto';
import { ResultDto } from './dto/result.dto';

describe('PredictorService', () => {
  let service: PredictorService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [PredictorService],
    }).compile();

    service = module.get<PredictorService>(PredictorService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });

  it('should return result', async () => {
    const data = new IndicatorsDto();
    data.HighBP = 0;
    data.HighChol = 0;
    data.CholCheck = 0;
    data.BMI = 0;
    data.Smoker = 0;
    data.Stroke = 0;
    data.HeartDiseaseorAttack = 0;
    data.PhysActivity = 0;
    data.Fruits = 0;
    data.Veggies = 0;
    data.HvyAlcoholConsump = 0;
    data.AnyHealthcare = 0;
    data.NoDocbcCost = 0;
    data.GenHlth = 0;
    data.MentHlth = 0;
    data.PhysHlth = 0;
    data.DiffWalk = 0;
    data.Sex = 0;
    data.Age = 0;
    data.Education = 0;
    data.Income = 0;
    const result = await service.predict(data);
    expect(result).toBeInstanceOf(ResultDto);
    expect(result.result).toBeLessThan(1);
  })
});
