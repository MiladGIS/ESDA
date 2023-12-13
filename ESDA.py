# All used librairies
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt

'''
This doucumnet need to be run part by part
in other words, each part may have conflict with other parts
'''
# Chapter Two - part one - Histogram -----------------------------------------

df = pd.read_csv(r"countries of the world1.csv")

df["Infant mortality (per 1000 births)"] = df["Infant mortality (per 1000 births)"].str.replace(",",".").astype(float)

df.hist(column='Infant mortality (per 1000 births)', grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)


# Chapter Two - part two - Boxplot -------------------------------------------

shpData = gpd.read_file("Environment_Canada_Weather_Conditions.shp")

shpData.boxplot(column = "Humidity_P",  fontsize = 20.0 , figsize=(12,8), color='red')


# Chapter Two - part three - Scatterplot -------------------------------------

df = pd.read_csv(r"countries of the world1.csv")

for i in df.columns:
    try:
        df[i] = df[i].str.replace(",",".").astype(float)
    except:
        continue

df.plot.scatter(x = 'Net migration',  y = 'GDP ($ per capita)', xlabel = "pko", ylabel = "ok",
                c = 'Infant mortality (per 1000 births)', s = 'Birthrate',
                colormap='viridis')


# Chapter Two - part four - Trend analysis -----------------------------------

shpData = gpd.read_file("Environment_Canada_Weather_Conditions.shp")

x, y = [], []
for i in shpData['geometry']:
  x.append(i.x)
  y.append(i.y)

z = np.abs(shpData["Temperatur"].fillna(0))

ax = plt.figure(figsize = (12,8)).gca(projection='3d')

for xx, yy, zz in zip(x, y, z):
  ax.plot([xx, xx], [yy, yy], [0, zz], '-', color='b', alpha = 0.5)

ax.plot(x, y, z, 'o', markersize=4, markerfacecolor='r', color='b')

xzM = np.poly1d(np.polyfit(x, z, 5))
xzL = np.linspace(min(x), max(x), len(z))
ax.plot(xzL, np.zeros_like(x), xzM(xzL))

yzM = np.poly1d(np.polyfit(y, z, 4))
yzL = np.linspace(min(y), max(y), len(z))
ax.plot(yzL, np.zeros_like(y), yzM(yzL))

ax.view_init(azim = 120)
plt.show()


# Chapter Two - part six - Normal QQ plot ------------------------------------

import statsmodels.api as sm

shpData = gpd.read_file("Environment_Canada_Weather_Conditions.shp")

data_points = shpData['Temperatur'].fillna(0)

sm.qqplot(data_points, line="r")

# Chapter Two - part seven - Voronoi map -------------------------------------

import geoplot as gplt

shpData = gpd.read_file("Environment_Canada_Weather_Conditions.shp")

ax = gplt.Voronoi(shpData, figsize = (14, 8))

gplt.pointplot(shpData, color = 'red', ax = ax, extent = shpData.total_bounds)

plt.title("Canada countries Metrological stations Voronoi map", fontsize = 15);

