import { ApiProperty } from '@nestjs/swagger';

export class ResultDto {
  @ApiProperty({ description: '0 = no diabetes 1 = diabetes'})
  public result: number;
}
