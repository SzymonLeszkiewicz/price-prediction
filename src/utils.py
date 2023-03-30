#  Copyright (c)
#  Author: Szymon Leszkiewicz
#  Date: 2023 - 2
#  License: BSD 3-Clause
#  Description: This file is part of the project: "House prices prediction in Poland based on the
#               migration data and the real estate market data".
import os
import pickle as pkl
import datetime

import pandas as pd


def get_data():
    df = pd.read_csv(os.path.join('..', 'data', 'cleaned_data.csv'))
    return df


def load_model():
    with open(os.path.join('..', 'results', 'LR model.pkl'), 'rb') as f:
        try:
            data = pkl.load(f)
        except Exception as e:
            print("loading model error", e)
    return data['model']


def save_model(model, model_name):
    with open(os.path.join('..', 'results', f'{model_name} model.pkl'), 'wb') as f:
        data = {'model': model, 'model_name': model_name}
        pkl.dump(data, f)


def get_last_year():
    year = datetime.date.today().year
    return year
