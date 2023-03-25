#  Copyright (c)
#  Author: Szymon Leszkiewicz
#  Date: 2023 - 3
#  License: BSD 3-Clause
#  Description: This file is part of the project: "House prices prediction in Poland based on the
#               migration data and the real estate market data".
import os

from LR_model import LrModel
from const import Const
from utils import get_data, save_model, load_model

c = Const()


class Predict:
    def __init__(self):
        '''
        This class is responsible for the prediction of the house prices in Poland.
        '''
        self.model = None
        self.data = None
        if os.path.exists(os.path.join('..', c.files_dir, 'LR model.pkl')):
            self.model = load_model()
        else:
            self.model_train()
            save_model(self.model, 'LR')
        self.prediction = None
        self.predict()

    def model_train(self):
        self.data = get_data()
        self.model = LrModel(self.data)
        self.model.train_model()

    def predict(self, year=2021):
        self.prediction = self.model.model_predict(year)
        print(self.prediction)
        return self.prediction


if __name__ == '__main__':
    p = Predict()
