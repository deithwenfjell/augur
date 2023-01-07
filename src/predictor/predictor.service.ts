import { Injectable } from '@nestjs/common';
import { IndicatorsDto } from './dto/indicators.dto';
import { ResultDto } from './dto/result.dto';
import * as tf from '@tensorflow/tfjs-node';
import { Rank, Tensor, Tensor1D } from '@tensorflow/tfjs';

class IndicatorsTensorInputArray{
  public tensorArray: Float32Array[][] = [[]];
  constructor(indicators: IndicatorsDto) {
    for (const key in indicators) {
      this.tensorArray[0].push(indicators[key])
    }
  }

}

@Injectable()
export class PredictorService {
  public async predict(indicators: IndicatorsDto): Promise<ResultDto> {
    const indicatorsTensorInputArray = new IndicatorsTensorInputArray(indicators)
    const indicatorsTensor = tf.tensor(indicatorsTensorInputArray.tensorArray);
    // indicatorsTensor.reshape([null,21])
    const model = await tf.loadLayersModel('file://data-frame/trained_model/model.json');
    const prediction: Tensor1D = <Tensor<Rank.R1>>model.predict(indicatorsTensor);
    const predictionData = prediction.dataSync();
    const res = new ResultDto();
    res.result = predictionData[0]
    return res;
  }
}
