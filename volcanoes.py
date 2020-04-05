# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 12:13:48 2020

@author: Santosh
"""

import folium
import pandas as pd

df = pd.read_csv('Volcanoes.txt')

lat_mean = df['LAT'].mean()
lon_mean = df['LON'].mean()


#creating map object
map1 = folium.Map(location = [lat_mean, lon_mean], zoom_start=6)

#Function to change elevation color 
def color1(elev):
    if elev in range(0,1000):
        col = 'green'
    elif elev in range(1001,1999):
        col = 'blue'
    elif elev in range(2000,2999):
        col = 'orange'
    else:
        col = 'red'
    return col

for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    folium.Marker(location=[lat, lon], popup = name, icon = folium.Icon(color=color1(elev), 
                  icon_color = 'yellow', icon  = 'cloud')).add_to(map1)
    

map1.save('volcano.html')