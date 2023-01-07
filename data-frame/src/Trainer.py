import sys
import pandas as pd
import sklearn as sk
import scipy as sp
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import platform
import tensorflowjs as tfjs

from pandas import DataFrame
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn import metrics


class Trainer:
    __data_frame: DataFrame = {}
    __data = {}
    __X_train = {}
    __y_train = {}
    __X_validation = {}
    __y_validation = {}
    __X_test = {}
    __y_test = {}

    def train(self, data_frame: DataFrame):
        self.__data_frame = data_frame
        numpy_data = self.__data_frame.to_numpy()
        self.__data = tf.constant(numpy_data)

        X = self.__data_frame.drop('Diabetes_binary', axis=1).to_numpy()
        y = (self.__data_frame.Diabetes_binary).to_numpy()
        print(X.shape, y.shape)
        eighty_percent_X = int(len(X) * 0.8)
        print(eighty_percent_X)
        self.__X_train, self.__y_train = X[:eighty_percent_X], y[:eighty_percent_X]
        self.__X_test, self.__y_test = X[eighty_percent_X:], y[eighty_percent_X:]
        print('Train shapes:', self.__X_train.shape, self.__y_train.shape)

        # self.train_alternate()

        # 1. Vytvorenie modelu
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(100, activation=tf.keras.activations.relu),
            tf.keras.layers.Dense(100, activation=tf.keras.activations.relu),
            tf.keras.layers.Dense(100, activation=tf.keras.activations.relu),
            tf.keras.layers.Dense(1, activation=tf.keras.activations.sigmoid)
        ])

        # 2. Kompilácia modelu
        model.compile(loss="binary_crossentropy",
                      optimizer=tf.keras.optimizers.Adam(lr=0.001),
                      metrics=["accuracy"])
        lr_scheduler = tf.keras.callbacks.LearningRateScheduler(lambda epoch: 1e-4 * 10 ** (epoch / 20))

        # 3. Nattrénovanie modelu
        history = model.fit(self.__X_train, self.__y_train, epochs=20)

        tfjs.converters.save_keras_model(model, 'trained_model')

        print('Eval:')
        results = model.evaluate(self.__X_test, self.__y_test)
        print("test loss, test acc:", results)
        print("Generate predictions for 3 samples")
        predictions = model.predict(self.__X_test[:3])
        print("predictions shape:", predictions.shape)
        print("predictions:", predictions)
        print("truth:", self.__y_train[:3])

        # self.plot_decision_boundary(model, self.__X_train, self.__y_train)
        pd.DataFrame(history.history).plot()
        plt.show()

    def train_alternate(self):
        dt = DecisionTreeClassifier(max_features=12, max_depth=15)
        dt.fit(self.__X_train, self.__y_train)
        print('decision tree:')
        print(dt.score(self.__X_train, self.__y_train))
        print(dt.score(self.__X_test, self.__y_test))
        ada = AdaBoostClassifier()
        ada.fit(self.__X_train, self.__y_train)
        yhat = ada.predict(self.__X_test)
        print('Train set Accuracy :', metrics.accuracy_score(self.__y_train, ada.predict(self.__X_train)) * 100)
        print('Test set Accuracy :', metrics.accuracy_score(self.__y_test, yhat) * 100)

    def tensor_test(self):
        print(f"Python Platform: {platform.platform()}")
        print(f"Tensor Flow Version: {tf.__version__}")
        print(f"Keras Version: {tf.keras.__version__}")
        print()
        print(f"Python {sys.version}")
        print(f"Pandas {pd.__version__}")
        print(f"Scikit-Learn {sk.__version__}")
        print(f"SciPy {sp.__version__}")
        gpu = len(tf.config.list_physical_devices('GPU')) > 0
        print("GPU is", "available" if gpu else "NOT AVAILABLE")

    def plot_decision_boundary(self, model, X, y):
        """
        Plots the decision boundary created by a model predicting on X.
        This function was inspired by two resources:
         1. https://cs231n.github.io/neural-networks-case-study/
         2. https://github.com/madewithml/basics/blob/master/notebooks/09_Multilayer_Perceptrons/09_TF_Multilayer_Perceptrons.ipynb
        """
        # Define the axis boundaries of the plot and create a meshgrid
        x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
        y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                             np.linspace(y_min, y_max, 100))

        # Create X value (we're going to make predictions on these)
        x_in = np.c_[xx.ravel(), yy.ravel()]  # stack 2D arrays together

        # Make predictions
        y_pred = model.predict(x_in)

        # Check for multi-class
        if len(y_pred[0]) > 1:
            print("doing multiclass classification")
            # We have to reshape our prediction to get them ready for plotting
            y_pred = np.argmax(y_pred, axis=1).reshape(xx.shape)
        else:
            print("doing binary classification")
            y_pred = np.round(y_pred).reshape(xx.shape)

        # Plot the decision boundary
        plt.contourf(xx, yy, y_pred, cmap=plt.cm.RdYlBu, alpha=0.7)
        plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.RdYlBu)
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
