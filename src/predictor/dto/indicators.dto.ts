import { ApiProperty } from "@nestjs/swagger";

export class IndicatorsDto {
@ApiProperty({ description: '0 = no diabetes 1 = prediabetes 2 = diabetes'})
public Diabetes_012?: number;

@ApiProperty({ description: '0 = no high BP 1 = high BP'})
public HighBP: number;

@ApiProperty({ description: '0 = no high cholesterol 1 = high cholesterol'})
public HighChol: number;

@ApiProperty({ description: '0 = no cholesterol check in 5 years 1 = yes cholesterol check in 5 years'})
public CholCheck: number;

@ApiProperty({ description: 'Body Mass Index'})
public BMI: number;

@ApiProperty({ description: 'Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes] 0 = no 1 = yes'})
public Smoker: number;

@ApiProperty({ description: '(Ever told) you had a stroke. 0 = no 1 = yes'})
public Stroke: number;

@ApiProperty({ description: 'coronary heart disease (CHD) or myocardial infarction (MI) 0 = no 1 = yes'})
public HeartDiseaseorAttack: number;

@ApiProperty({ description: 'physical activity in past 30 days - not including job 0 = no 1 = yes'})
public PhysActivity: number;

@ApiProperty({ description: 'Consume Fruit 1 or more times per day 0 = no 1 = yes'})
public Fruits: number;

@ApiProperty({ description: 'Consume Vegetables 1 or more times per day 0 = no 1 = yes'})
public Veggies: number;

@ApiProperty({ description: 'Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week) 0 = no 1 = yes'})
public HvyAlcoholConsump: number;

@ApiProperty({ description: 'Have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc. 0 = no 1 = yes'})
public AnyHealthcare: number;

@ApiProperty({ description: 'Was there a time in the past 12 months when you needed to see a doctor but could not because of cost? 0 = no 1 = yes'})
public NoDocbcCost: number;

@ApiProperty({ description: 'Would you say that in general your health is: scale 1-5 1 = excellent 2 = very good 3 = good 4 = fair 5 = poor'})
public GenHlth: number;

@ApiProperty({ description: 'Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good? scale 1-30 days'})
public MentHlth: number;

@ApiProperty({ description: 'Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? scale 1-30 days'})
public PhysHlth: number;

@ApiProperty({ description: 'Do you have serious difficulty walking or climbing stairs? 0 = no 1 = yes'})
public DiffWalk: number;

@ApiProperty({ description: '0 = female 1 = male'})
public Sex: number;

@ApiProperty({ description: '13-level age category (_AGEG5YR see codebook) 1 = 18-24 9 = 60-64 13 = 80 or older'})
public Age: number;

@ApiProperty({ description: 'Education level (EDUCA see codebook) scale 1-6 1 = Never attended school or only kindergarten 2 = Grades 1 through 8 (Elementary) 3 = Grades 9 through 11 (Some high school) 4 = Grade 12 or GED (High school graduate) 5 = College 1 year to 3 years (Some college or technical school) 6 = College 4 years or more (College graduate)'})
public Education: number;

@ApiProperty({ description: 'Income scale (INCOME2 see codebook) scale 1-8 1 = less than $10,000 5 = less than $35,000 8 = $75,000 or more'})
public Income: number;
}
