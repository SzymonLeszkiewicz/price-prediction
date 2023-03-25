#  Copyright (c)
#  Author: Szymon Leszkiewicz
#  Date: 2023 - 2
#  License: BSD 3-Clause
#  Description: This file is part of the project: "House prices prediction in Poland based on the
#               migration data and the real estate market data".
import pandas as pd

from os import path


class Const:
    def __init__(self):
        self.__help_description = '''House price prediction in Poland based on migration data and real estate market data.'''
        self.__mode_help_description = '''Mode of the program. Possible values:     
        i: best city to invest
        m: best city to monetize investment
        e: evaluatin of the market in a given city'''
        self.__epilog_text = '''Copyrigth (c) 2021 Szymon Leszkiewicz'''
        df = pd.read_csv(path.join('..', 'data', 'cleaned_data.csv'))['miasto'].unique()
        self.__cities = ', '.join(df)
        self.__city_help_description = f'''City name. Possible values: ''' + self.cities
        self.__categorical_features = ['miasto']
        self.__y_name = 'cena'
        self.__files_dir = 'results'

    @property
    def help_description(self):
        return self.__help_description

    @property
    def mode_help_description(self):
        return self.__mode_help_description

    @property
    def epilog_text(self):
        return self.__epilog_text

    @property
    def cities(self):
        return self.__cities

    @property
    def city_help_description(self):
        return self.__city_help_description

    @property
    def categorical_features(self):
        return self.__categorical_features

    @property
    def y_name(self):
        return self.__y_name

    @property
    def files_dir(self):
        return self.__files_dir


if __name__ == '__main__':
    c = Const()
    c.__help_description = 'test'
    print(c.__help_description)
