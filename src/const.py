#  Copyright (c)
#  Author: Szymon Leszkiewicz
#  Date: 2023 - 2
#  License: BSD 3-Clause
#  Description: This file is part of the project: "House prices prediction in Poland based on the
#               migration data and the real estate market data".
import pandas as pd

help_description = '''House price prediction in Poland based on migration data and real estate market data.'''
mode_help_description = '''Mode of the program. Possible values:     
i: best city to invest
m: best city to monetize investment
e: evaluatin of the market in a given city'''
epilog_text = '''Copyrigth (c) 2021 Szymon Leszkiewicz'''
df = pd.read_csv('../data/cleaned_data.csv')['miasto'].unique()
cities = ', '.join(df)
city_help_description = f'''City name. Possible values: '''+cities
categorical_features = ['miasto']
y_name = 'cena'

