import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model
import sklearn.neighbors

def prepare_country_stats(oecd_bli, gdp_per_capita):
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index("Country", inplace=True)
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                  left_index=True, right_index=True)
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
    return full_country_stats[["GDP per capita", 'Life satisfaction']].iloc[keep_indices]

# load the data
oecd_bli = pd.read_csv("bli_2020.csv",thousands=',')
gdp_per_capita = pd.read_csv("gdp.csv",thousands=',',
                             encoding='latin1',na_values='n/a')

# Prepare the data
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
x = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats['Life satisfaction']]

# visualize the data
country_stats.plot(kind='scatter',x="GDP per capita", y='Life satisfaction')
plt.show()

# select a linear model
lin_reg_model = sklearn.linear_model.LinearRegression()
clf = sklearn.neighbors.KNeighborsRegressor(n_neighbors=3)

# Train the model
lin_reg_model.fit(x,y)
print(lin_reg_model.fit(x,y))

clf.fit(x,y)
print(clf.fit(x,y))

# make prediction
X_new = [[23354.312]] #Cyprus' GDP per Capita
print(lin_reg_model.predict(X_new))
print(clf.predict(X_new))
