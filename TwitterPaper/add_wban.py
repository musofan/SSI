import pandas as pd
d = pd.read_csv('/Users/damoncrockett/Dropbox/TwitterPaper/data/twitter/US_HSV_modes_top60_cities_urban-areas.csv')
del d['Unnamed: 0']
d.city = d.city.map(lambda x:x.lower())

dd = pd.read_table('/Users/damoncrockett/Dropbox/CALIT2DATA/weather/rawData/QCLCD201301/201301station.txt',sep='|')
dd.Name = dd.Name.map(lambda x:x.lower())
dd = dd[['WBAN','Name','Latitude','Longitude']]
dd.rename(columns={'Name':'city'},inplace=True)

from shapely.geometry import Point
station_points = []
l = len(dd.index)
for k in range(l):
    tmp = Point(dd.Longitude.loc[k],dd.Latitude.loc[k])
    station_points.append(tmp)
dd['weather_station_point'] = station_points    

weather_stations = []
n = len(d.index)
for i in range(n):
    print i
    city = d.city.loc[i]
    tweet = Point(d.lon.loc[i],d.lat.loc[i])
    stations = dd[dd.city == city]
    
    if len(stations.index) == 0:
        weather_stations.append('nan')
    else:
        stations.reset_index(drop=True,inplace=True)
        station_points = []
        m = len(stations.index)
        for j in range(m):
            tmp = Point(stations.Longitude.loc[j],stations.Latitude.loc[j])
            station_points.append(tmp)
        tmp = min(station_points, key = lambda x: x.distance(tweet))
        weather_stations.append(tmp)

d['weather_station_point'] = weather_stations

dd = dd[['WBAN','weather_station_point']]
dd.set_index('weather_station_point',inplace=True)
d = d.join(dd,on='weather_station_point')
d.to_csv('/Users/damoncrockett/Dropbox/TwitterPaper/data/twitter/US_HSV_modes_top60_cities_ua_wban.csv',
        index=False)