#  Copyright (c)
#  Author: Szymon Leszkiewicz
#  Date: 2023 - 3
#  License: BSD 3-Clause
#  Description: This file is part of the project: "House prices prediction in Poland based on the
#               migration data and the real estate market data".
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from Model import Model
from const import Const
from utils import get_data, save_model
import pandas as pd

c = Const()


class LrModel(Model):
    def __init__(self, data):
        super().__init__(data)
        self.model = LinearRegression()
        self.score = None
        self.X, self.y = None, None  # X - features, y - target

    def make_new_features(self):
        def value_year_before(x, df, column):
            old = df.loc[(df['rok'] == x['rok'] - 1) & (df['miasto'] == x['miasto'])][column].values
            if len(old) == 0:
                return None
            return old[0]

        self.data.drop_duplicates(subset=['miasto', 'rok'], inplace=True)
        self.data['old_price'] = self.data.apply(lambda x: value_year_before(x, self.data, 'cena'), axis=1)
        self.data['old_im'] = self.data.apply(lambda x: value_year_before(x, self.data, 'im'), axis=1)
        self.data['old_em'] = self.data.apply(lambda x: value_year_before(x, self.data, 'em'), axis=1)
        self.data['old_wsp'] = self.data.apply(lambda x: value_year_before(x, self.data, 'wsp_mig'), axis=1)
        self.data.dropna(inplace=True)

    def prepare_date(self):
        X = self.dummy_features(self.data)
        y = X[c.y_name]
        X = X.drop(c.y_name, axis=1)
        return X, y

    def train_model(self):
        self.make_new_features()
        self.X, self.y = self.prepare_date()
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y)
        self.model.fit(X_train, y_train)
        self.score = self.cross_validation(X_train, y_train, self.model)
        return self.model

    def get_cities_from_dummies(self, d):
        col = [c for c in d.columns if c.startswith('miasto')]
        return d[col].idxmax(axis=1).str.replace('miasto_', '')
    def model_predict(self, year):
        new_data = self.X.loc[self.X['rok'] == year]
        cities = self.get_cities_from_dummies(new_data)
        pred = self.model.predict(new_data)
        new_data = pd.DataFrame({'miasto': cities, 'rok': year, 'cena': pred})
        return new_data


if __name__ == '__main__':
    from utils import get_data

    data = get_data()
    m = LrModel(data)
    m.train_model()
    print(m.model_predict(2021))
