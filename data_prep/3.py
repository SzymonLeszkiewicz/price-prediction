import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression



'''
combine migration and price data
'''

migration_data = pd.read_csv("data/migration2.csv", sep=";")
# set first column as index
migration_data.set_index('rok', inplace=True)
price_data = pd.read_csv("data/srednie2.csv")
# set first column as index
price_data.set_index('rok', inplace=True)
# replace NaN with 0
price_data.fillna(0, inplace=True)





lata = [x for x in range(2006, 2022)]
# iterate over all cities

df_data = pd.DataFrame(columns=['rok', 'wsp_mig', 'miasto'])

for city in migration_data.columns:
    # prepare data
    X = migration_data[city].values
    #combine lata and X
    X = np.array(list(zip(lata, X)))
    # convert X[0][0] to int
    X = np.array([[int(x[0]), x[1]] for x in X])

    #  add city to every element in X
    X = np.array([[x[0], x[1], city] for x in X])
    # cinvert X to dataframe
    X = pd.DataFrame(X, columns=['rok', 'wsp_mig', 'miasto'])

    # change rok data type to int
    X['rok'] = X['rok'].astype(float)
    X['rok'] = X['rok'].astype(int)
    # set rok as index

    # add X to df_data
    df_data = pd.concat([df_data, X], ignore_index=True)


df_ceny = pd.DataFrame(columns=['rok', 'cena', 'miasto'])

# iterate over price_data
for city in price_data.columns:
    # print values
    # prepare data
    X = price_data[city].values
    #combine lata and X
    X = np.array(list(zip(lata, X)))
    # convert X[0][0] to int
    X = np.array([[int(x[0]), x[1]] for x in X])
    # change lata to int
    X = np.array([[int(x[0]), x[1]] for x in X])
    #  add city to every element in X
    X = np.array([[x[0], x[1], city] for x in X])
    # cinvert X to dataframe
    X = pd.DataFrame(X, columns=['rok', 'cena', 'miasto'])
    # change rok data type to int
    X['rok'] = X['rok'].astype(float)
    X['rok'] = X['rok'].astype(int)
    # add X to df_ceny
    df_ceny = pd.concat([df_ceny, X], ignore_index=True)

print(df_ceny)
# combine df_data and df_ceny
df = pd.merge(df_data, df_ceny, on=['rok', 'miasto'], how='outer')

# sacve to csv
df.to_csv('data/combined.csv', index=False)

