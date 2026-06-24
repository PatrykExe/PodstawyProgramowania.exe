import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#csv - dane podzielone przecinkami

data = pd.read_csv('data.csv')
print(data.head().to_string()) #head() pobiera pierwsze 5 wierszy, to_string() pobiera wszystkie kolumny

print(data.isnull().sum())

corr = data.loc[:, data.columns != 'diagnosis'].corr()

#sns.heatmap(corr, cmap = 'coolwarm')


data.drop('diagnosis', axis = 1).hist(bins = 30, figsize = (15, 20))
plt.tight_layout()
plt.show()

data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})

data = data.drop(['id', 'Unnamed: 32'], axis=1, errors='ignore')

print(data.to_string())