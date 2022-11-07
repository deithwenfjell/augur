import { Controller, Get } from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger';
import { PredictorService } from './predictor.service';

@ApiTags('Predictor')
@Controller('predictor')
export class PredictorController {
    constructor(public readonly predictorService: PredictorService) {}

    @Get()
    public predict() {
        return 12345;
    }
}
