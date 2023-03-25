#  Copyright (c)
#  Author: Szymon Leszkiewicz
#  Date: 2023 - 2
#  License: BSD 3-Clause
#  Description: This file is part of the project: "House prices prediction in Poland based on the
#               migration data and the real estate market data".
import os
import pickle as pkl

import pandas as pd


def get_data():
    df = pd.read_csv(os.path.join('..', 'data', 'cleaned_data.csv'))
    return df


def load_model():
    with open(os.path.join('..', 'results', 'LR model.pkl'), 'rb') as f:
        try:
            model = pkl.load(f)
            print('model', model)
        except Exception as e:
            print("loading model error", e)
    return model['model']


def save_model(model, model_name):
    with open(os.path.join('..', 'results', f'{model_name} model.pkl'), 'wb') as f:
        # assert isinstance(model, Model)
        data = {'model': model, 'model_name': model_name}
        print(data)
        pkl.dump(data, f)


