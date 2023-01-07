from src.DataProvider import DataProvider
from src.Trainer import Trainer


def greet():
    print('Augur ANN training sequence.')


if __name__ == '__main__':
    greet()
    data = DataProvider().provide_data()
    # Trainer().train(data)
