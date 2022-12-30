import { ApiProperty } from '@nestjs/swagger';

export class ResultDto {
  @ApiProperty({ description: '0 = no diabetes 1 = prediabetes 2 = diabetes'})
  public result: number;
}
