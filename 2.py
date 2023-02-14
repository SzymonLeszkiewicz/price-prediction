#  Copyright (c)
#  Author: Szymon Leszkiewicz
#  Date: 2023 - 2
#  License: BSD 3-Clause
#  Description: This file is part of the project: "House prices prediction in Poland based on the
#               migration data and the real estate market data".
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.linear_model import LinearRegression
''''
preliminary data analysis
correlation graphs by city
'''

migration_data = pd.read_csv("arch/data_prep/data/migration2.csv", sep=";")
migration_data.set_index('rok', inplace=True)
price_data = pd.read_csv("arch/data_prep/data/srednie2.csv")
price_data.set_index('rok', inplace=True)


X = migration_data.values.T
y = price_data.values.T
X = np.nan_to_num(X)
y = np.nan_to_num(y)




corr_dict = dict.fromkeys(migration_data.columns, 0)
for i in range(0, len(X)):
    # plt.scatter(X[i], y[i], color='red')
    # plt.title('Migration vs Price - {}'.format(migration_data.columns[i]))
    # plt.xlabel('Migration')
    # plt.ylabel('Price')
    corr = np.corrcoef(X[i], y[i])[0, 1]
    corr_dict[migration_data.columns[i]] = corr
    print("Correlation for city {}: {:.2f}".format(migration_data.columns[i], corr))
    # sns.regplot(x=X[i], y=y[i], color='blue')
    # plt.pause(0.01)
    # plt.close()


# plot correlation for all cities
plt.bar(corr_dict.keys(), corr_dict.values())
plt.title('Correlation for cities (mean: {:.2f})'.format(np.mean(list(corr_dict.values()))))
plt.xlabel('City')
plt.ylabel('Correlation')
plt.xticks(rotation=90)
plt.axhline(np.mean(list(corr_dict.values())), color='red')
sns.set_style("whitegrid")
sns.set_context("paper", font_scale=1.5)
plt.tight_layout()
plt.bar(corr_dict.keys(), corr_dict.values(), color=['red' if x < 0.5 else 'blue' for x in corr_dict.values()])

plt.savefig('data/figures/corr-for-city.png', dpi=300)
plt.show()

# drop data
for city in corr_dict:
    if corr_dict[city] < 0.5:
        migration_data.drop(city, axis=1, inplace=True)
        price_data.drop(city, axis=1, inplace=True)
corr_dict2 = {k: v for k, v in corr_dict.items() if v >= 0.5}

# clean plot
plt.bar(corr_dict2.keys(), corr_dict2.values())
plt.xlabel('City')
plt.ylabel('Correlation')
plt.xticks(rotation=90)
plt.axhline(np.mean(list(corr_dict2.values())), color='red')
plt.title('Correlation for cities with correlation > 0.5 (mean: {:.2f})'.format(np.mean(list(corr_dict2.values()))))
sns.set_style("whitegrid")
sns.set_context("paper", font_scale=1.5)
plt.tight_layout()
plt.bar(corr_dict2.keys(), corr_dict2.values(), color=['red' if x < 0.5 else 'blue' for x in corr_dict2.values()])
plt.show()


