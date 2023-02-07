import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("data/combined_edit.csv", sep=";")
# drop nan values and print number of dropped rows
print("Usunięto", data.isna().sum().sum(), "wierszy")
data = data.dropna()
# convert miasto to string
data['miasto'] = data['miasto'].astype('string')


corr = data['wsp_mig'].corr(data['cena'])
print("Współczynnik korelacji:", corr, end='\n\n\n\n\n')

miasta_corr = dict.fromkeys(data['miasto'].unique(), 0)
for city in data['miasto'].unique():
    city_data = data[data['miasto'] == city]
    corr = city_data['wsp_mig'].corr(city_data['cena'])
    miasta_corr[city] = corr
    print(city, ":", corr)

#plot correlation for each city
plt.bar(miasta_corr.keys(), miasta_corr.values())
plt.xticks(rotation=90)
# wrote title with mean correlation
plt.title('Korelacja dla miast (średnia: {:.2f})'.format(np.mean(list(miasta_corr.values()))))
plt.xlabel('Miasto')
plt.ylabel('Korelacja')
# annotate average correlation
plt.axhline(np.mean(list(miasta_corr.values())), color='red')
plt.tight_layout()
plt.show()


# # drop data
# for city in miasta_corr:
#     if miasta_corr[city] < 0.5:
#         data = data[data['miasto'] != city]
#         print("Usunięto miasto", city)

corr = data.corr()

sns.heatmap(corr, annot=True)
plt.title('Macierz korelacji')
plt.show()


corr = data['wsp_mig'].corr(data['cena'])
print("Współczynnik korelacji:", corr)

sns.regplot(x='wsp_mig', y='cena', data=data)
plt.xlabel('Współczynnik migracji')
plt.ylabel('Cena')
plt.title('Zależność ceny od współczynnika migracji')
plt.show()


# plot data for wrocław
wroclaw_data = data[data['miasto'] == 'Wrocław']
sns.regplot(x='wsp_mig', y='cena', data=wroclaw_data)
plt.xlabel('Współczynnik migracji')
plt.ylabel('Cena')
plt.title('Zależność ceny od współczynnika migracji dla Wrocławia')
plt.show()
