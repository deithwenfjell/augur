import { Body, Controller, Post } from '@nestjs/common';
import { ApiOkResponse, ApiTags } from '@nestjs/swagger';
import { PredictorService } from './predictor.service';
import { IndicatorsDto } from './dto/indicators.dto';
import { ResultDto } from './dto/result.dto';

@ApiTags('Predictor')
@Controller('predictor')
@ApiOkResponse({type: ResultDto })
export class PredictorController {
    constructor(public readonly predictorService: PredictorService) {}

    @Post()
    public predict(@Body() indicators: IndicatorsDto): ResultDto {
        return this.predictorService.predict(indicators);
    }
}
