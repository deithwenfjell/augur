import { Injectable } from '@nestjs/common';
import { IndicatorsDto } from './dto/indicators.dto';
import { ResultDto } from './dto/result.dto';

@Injectable()
export class PredictorService {
  public predict(indicators: IndicatorsDto): ResultDto {
    const res =  new ResultDto();
    res.result = 12345 + indicators.Age;
    return res;
  }
}
