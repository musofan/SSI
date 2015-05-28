import pandas as pd
d = pd.read_csv('/Users/damoncrockett/Dropbox/TwitterPaper/data/twitter/US_HSV_modes_top60_cities.csv')
d.city = d.city.map(lambda x:x.lower())

dd = pd.read_table('/Users/damoncrockett/Dropbox/CALIT2DATA/weather/rawData/QCLCD201301/201301station.txt',sep='|')
dd.Name = dd.Name.map(lambda x:x.lower())
dd = dd[['WBAN','Name','Latitude','Longitude']]
dd.rename(columns={'Name':'city'},inplace=True)

# spelling issues...
dd.city[dd.city=='st louis'] = 'st. louis'
dd.city[dd.city=='raleigh/durham'] = 'raleigh'

#find closest station to Anaheim and VA Beach
subset = d[['city','lon','lat']]
subset = subset[(subset.city == 'anaheim') | (subset.city == 'virginia beach')]
import numpy as np
tmp = subset.groupby('city').agg(np.mean)
from shapely.geometry import Point
anaheim = Point(tmp.lon.loc['anaheim'],tmp.lat.loc['anaheim'])
va_beach = Point(tmp.lon.loc['virginia beach'],tmp.lat.loc['virginia beach'])
weather_station_points = []
n = len(dd.index)
for i in range(n):
    tmp = Point(dd.Longitude.loc[i],dd.Latitude.loc[i])
    weather_station_points.append(tmp)
weather_station_wbans = list(dd.WBAN)
anaheim_station_point = min(weather_station_points,key=lambda x:x.distance(anaheim))
anaheim_station_wban_index = weather_station_points.index(anaheim_station_point)
anaheim_station_wban = weather_station_wbans[anaheim_station_wban_index]
va_beach_station_point = min(weather_station_points,key=lambda x:x.distance(va_beach))
va_beach_station_wban_index = weather_station_points.index(va_beach_station_point)
va_beach_station_wban = weather_station_wbans[va_beach_station_wban_index]

# back to the join
wbans = []
n = len(d.index)
for i in range(n):
    print i
    city = d.city.loc[i]
    tweet = Point(d.lon.loc[i],d.lat.loc[i])
    if city=='anaheim':
        wbans.append(anaheim_station_wban)
    elif city=='virginia beach':
        wbans.append(va_beach_station_wban)
    else:
        stations = dd[dd.city==city]
        if len(stations.index)==0:
            wbans.append('nan')
        else:
            stations.reset_index(drop=True,inplace=True)
            station_wbans = list(stations.WBAN)
            station_points = []
            m = len(stations.index)
            for j in range(m):
                tmp = Point(stations.Longitude.loc[j],stations.Latitude.loc[j])
                station_points.append(tmp)
            tmp = min(station_points, key = lambda x: x.distance(tweet))
            tmp_idx = station_points.index(tmp)
            wban = station_wbans[tmp_idx]
            wbans.append(wban)
d['WBAN'] = wbans
d.to_csv('/Users/damoncrockett/Dropbox/TwitterPaper/data/twitter/US_HSV_modes_top60_cities_wban.csv',
        index=False)