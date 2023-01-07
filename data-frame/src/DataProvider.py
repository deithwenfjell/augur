import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from pandas import DataFrame


class DataProvider:
    __filePath = 'data/diabetes_binary_health_indicators_BRFSS2015.csv'
    __resolvedPath = Path(__filePath).resolve()
    __data: DataFrame = {}

    def show_figures(self):
        print('Figures: ')
        # self.__data.plot()
        # self.__data.hist()
        X = self.__data.drop('Diabetes_binary', axis=1)
        y = self.__data.Diabetes_binary
        print(X.size)
        print(y.size)
        # X.corrwith(y).plot(kind='bar', grid=True, figsize=(15, 6), title="Korelácia s  Diabetes_binary");
        # self.__data['Diabetes_binary'].value_counts(Niermalize=True).plot(kind='bar', title='Zastúpenie hodnôt v Diabetes_binary')
        self.indicators_histograms(plt=plt)
        plt.show()

    def indicators_histograms(self, plt):
        data_visualisation = self.__data
        data_visualisation.Diabetes_binary[data_visualisation['Diabetes_binary'] == 0] = 'Bez diabetu'
        data_visualisation.Diabetes_binary[data_visualisation['Diabetes_binary'] == 1] = 'Diabetes'
        data_visualisation.HighBP[data_visualisation['HighBP'] == 0] = 'Krvný tlak v Nierme'
        data_visualisation.HighBP[data_visualisation['HighBP'] == 1] = 'Vysoký krvný tlak'
        plt.figure(1).suptitle('HighBP')
        plt.hist(data_visualisation.HighBP)

        data_visualisation.HighChol[data_visualisation['HighChol'] == 0] = 'Cholesterol v norme'
        data_visualisation.HighChol[data_visualisation['HighChol'] == 1] = 'Vysoký cholesterol'
        plt.figure(2).suptitle('HighChol')
        plt.hist(data_visualisation.HighChol)

        data_visualisation.CholCheck[data_visualisation['CholCheck'] == 0] = 'Žiadna kontrola cholesterolu za 5 rokov'
        data_visualisation.CholCheck[data_visualisation['CholCheck'] == 1] = 'Kontrola cholesterolu za 5 rokov'
        plt.figure(3).suptitle('CholCheck')
        plt.hist(data_visualisation.CholCheck)

        data_visualisation.Smoker[data_visualisation['Smoker'] == 0] = 'Nie'
        data_visualisation.Smoker[data_visualisation['Smoker'] == 1] = 'ÁNie'
        plt.figure(4).suptitle('Smoker')
        plt.hist(data_visualisation.Smoker)

        data_visualisation.Stroke[data_visualisation['Stroke'] == 0] = 'Nie'
        data_visualisation.Stroke[data_visualisation['Stroke'] == 1] = 'Áno'
        plt.figure(5).suptitle('Stroke')
        plt.hist(data_visualisation.Stroke)

        data_visualisation.HeartDiseaseorAttack[data_visualisation['HeartDiseaseorAttack'] == 0] = 'Nie'
        data_visualisation.HeartDiseaseorAttack[data_visualisation['HeartDiseaseorAttack'] == 1] = 'Áno'
        plt.figure(6).suptitle('HeartDiseaseorAttack')
        plt.hist(data_visualisation.HeartDiseaseorAttack)

        data_visualisation.PhysActivity[data_visualisation['PhysActivity'] == 0] = 'Nie'
        data_visualisation.PhysActivity[data_visualisation['PhysActivity'] == 1] = 'Áno'
        plt.figure(7).suptitle('PhysActivity')
        plt.hist(data_visualisation.PhysActivity)

        data_visualisation.Fruits[data_visualisation['Fruits'] == 0] = 'Nie'
        data_visualisation.Fruits[data_visualisation['Fruits'] == 1] = 'Áno'
        plt.figure(8).suptitle('Fruits')
        plt.hist(data_visualisation.Fruits)

        data_visualisation.Veggies[data_visualisation['Veggies'] == 0] = 'Nie'
        data_visualisation.Veggies[data_visualisation['Veggies'] == 1] = 'Áno'
        plt.figure(9).suptitle('Veggies')
        plt.hist(data_visualisation.Veggies)

        data_visualisation.HvyAlcoholConsump[data_visualisation['HvyAlcoholConsump'] == 0] = 'Nie'
        data_visualisation.HvyAlcoholConsump[data_visualisation['HvyAlcoholConsump'] == 1] = 'Áno'
        plt.figure(10).suptitle('HvyAlcoholConsump')
        plt.hist(data_visualisation.HvyAlcoholConsump)

        data_visualisation.AnyHealthcare[data_visualisation['AnyHealthcare'] == 0] = 'Nie'
        data_visualisation.AnyHealthcare[data_visualisation['AnyHealthcare'] == 1] = 'Áno'
        plt.figure(11).suptitle('AnyHealthcare')
        plt.hist(data_visualisation.AnyHealthcare)

        data_visualisation.NoDocbcCost[data_visualisation['NoDocbcCost'] == 0] = 'Nie'
        data_visualisation.NoDocbcCost[data_visualisation['NoDocbcCost'] == 1] = 'Áno'
        plt.figure(12).suptitle('NoDocbcCost')
        plt.hist(data_visualisation.NoDocbcCost)

        data_visualisation.GenHlth[data_visualisation['GenHlth'] == 1] = 'Výborné'
        data_visualisation.GenHlth[data_visualisation['GenHlth'] == 2] = 'Veľmi dobré'
        data_visualisation.GenHlth[data_visualisation['GenHlth'] == 3] = 'Dobré'
        data_visualisation.GenHlth[data_visualisation['GenHlth'] == 4] = 'Dostačujúce'
        data_visualisation.GenHlth[data_visualisation['GenHlth'] == 5] = 'Chatrné'
        plt.figure(13).suptitle('GenHlth')
        plt.hist(data_visualisation.GenHlth)

        data_visualisation.DiffWalk[data_visualisation['DiffWalk'] == 0] = 'Nie'
        data_visualisation.DiffWalk[data_visualisation['DiffWalk'] == 1] = 'Áno'
        plt.figure(14).suptitle('DiffWalk')
        plt.hist(data_visualisation.DiffWalk)

        data_visualisation.Sex[data_visualisation['Sex'] == 0] = 'Žena'
        data_visualisation.Sex[data_visualisation['Sex'] == 1] = 'Muž'
        plt.figure(15).suptitle('Sex')
        plt.hist(data_visualisation.Sex)

        data_visualisation.Education[data_visualisation['Education'] == 1] = 'Žiadne'
        data_visualisation.Education[data_visualisation['Education'] == 2] = 'Základné'
        data_visualisation.Education[data_visualisation['Education'] == 3] = 'Stredoškolské bez maturity'
        data_visualisation.Education[data_visualisation['Education'] == 4] = 'Stredoškolské s maturitou'
        data_visualisation.Education[data_visualisation['Education'] == 5] = 'VŠ štúdium'
        data_visualisation.Education[data_visualisation['Education'] == 6] = 'VŠ štúdium dokončené'
        plt.figure(16).suptitle('Education')
        plt.hist(data_visualisation.Education)

        data_visualisation.Income[data_visualisation['Income'] == 1] = 'Menej ako $10,000'
        data_visualisation.Income[data_visualisation['Income'] == 2] = 'Menej ako $10,000'
        data_visualisation.Income[data_visualisation['Income'] == 3] = 'Menej ako $10,000'
        data_visualisation.Income[data_visualisation['Income'] == 4] = 'Menej ako $10,000'
        data_visualisation.Income[data_visualisation['Income'] == 5] = 'Menej ako $35,000'
        data_visualisation.Income[data_visualisation['Income'] == 6] = 'Menej ako $35,000'
        data_visualisation.Income[data_visualisation['Income'] == 7] = 'Menej ako $35,000'
        data_visualisation.Income[data_visualisation['Income'] == 8] = '$75,000 alebo viac'
        plt.figure(17).suptitle('Income')
        plt.hist(data_visualisation.Income)

        # 1 = 18-24      9 = 60-64      13 = 80 or older
        data_visualisation.Age[data_visualisation['Age'] == 1] = '18 - 24'
        data_visualisation.Age[data_visualisation['Age'] == 2] = '25 - 29'
        data_visualisation.Age[data_visualisation['Age'] == 3] = '30 - 34'
        data_visualisation.Age[data_visualisation['Age'] == 4] = '35 - 39'
        data_visualisation.Age[data_visualisation['Age'] == 5] = '40 - 44'
        data_visualisation.Age[data_visualisation['Age'] == 6] = '45 - 49'
        data_visualisation.Age[data_visualisation['Age'] == 7] = '50 - 54'
        data_visualisation.Age[data_visualisation['Age'] == 8] = '55 - 59'
        data_visualisation.Age[data_visualisation['Age'] == 9] = '60 - 64'
        data_visualisation.Age[data_visualisation['Age'] == 10] = '65 - 69'
        data_visualisation.Age[data_visualisation['Age'] == 11] = '70 - 74'
        data_visualisation.Age[data_visualisation['Age'] == 12] = '75 - 80'
        data_visualisation.Age[data_visualisation['Age'] == 13] = '80 a viac'
        plt.figure(18).suptitle('Age')
        plt.hist(data_visualisation.Age)

        plt.figure(19).suptitle('BMI')
        plt.hist(data_visualisation.BMI)

        plt.figure(20).suptitle('PhysHlth')
        plt.hist(data_visualisation.PhysHlth)

        plt.figure(21).suptitle('MentHlth')
        plt.hist(data_visualisation.MentHlth)


    def __clean_data(self):
        self.__data = self.__data.drop_duplicates()
        data_count = self.__data.count()
        cleared_data_count = self.__data.dropna().count()
        if cleared_data_count.Diabetes_binary < data_count.Diabetes_binary:
            self.__data = self.__data.dropna()
            print('Warning: Data cleared!')
            return
        print('Info: Data does Niet need clearing, Nie NaN values detected.')

    def __shuffle_data(self):
        self.__data = self.__data.sample(frac=1)

    def __print_stats(self):
        print('Data types: ')
        print(self.__data.dtypes)
        print('Data sample: ')
        print(self.__data)
        print('Data stats: ')
        print(self.__data.describe())
        print('Data info: ')
        print(self.__data.info())
        print('Diabetes value counts: ')
        print(self.__data.Diabetes_binary.value_counts())

    def __read_from_csv(self):
        data = pd.read_csv(self.__resolvedPath)
        self.__data = data

    def provide_data(self):
        self.__read_from_csv()
        self.__clean_data()
        self.__shuffle_data()
        # self.__print_stats()
        self.show_figures()
        return self.__data
