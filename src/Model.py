#  Copyright (c)
#  Author: Szymon Leszkiewicz
#  Date: 2023 - 2
#  License: BSD 3-Clause
#  Description: This file is part of the project: "House prices prediction in Poland based on the
#               migration data and the real estate market data".
import pandas as pd

from const import Const
from sklearn.model_selection import train_test_split, cross_validate, KFold

c = Const()
class Model:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def dummy_features(X):
        '''
        Uses OneHotEncoder to create dummies for categorical features
        :param X: dataset
        :return: dateset with dummies
        '''
        for i in c.categorical_features:
            dummy = pd.get_dummies(X[i], prefix=i, prefix_sep='_')
            X.drop(i, axis=1, inplace=True)
            X.join(dummy)
        return X

    @staticmethod
    def cross_validation(X, y, model):
        '''
        Uses cross validation to evaluate the model
        :param X: dataset
        :param y: target
        :param model: model to evaluate
        :return: score
        '''
        scoring = ['neg_mean_absolute_error', 'neg_mean_squared_error', 'r2']
        kfold = KFold(n_splits=3, shuffle=True, random_state=123)
        cv_results = cross_validate(model, X, y, cv=kfold, scoring=scoring)
        return cv_results

