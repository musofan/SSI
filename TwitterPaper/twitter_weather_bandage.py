import pandas as pd
weather = pd.read_csv('/Users/damoncrockett/Dropbox/TwitterPaper/data/twitter/weather_2013.csv')
tweets = pd.read_csv('/Users/damoncrockett/Dropbox/TwitterPaper/data/twitter/US_HSV_modes_top60_cities_wban.csv')
tweet_wbans = list(set(list(tweets.WBAN)))
weather_subset = weather[weather.WBAN.isin(tweet_wbans)]
weather_subset_wbans = list(set(list(weather_subset.WBAN)))
missing_wbans = list(set(tweet_wbans) - set(weather_subset_wbans))
tweets_without_weather = tweets[['city','lat','lon','filename']][tweets.WBAN.isin(missing_wbans)]
wban_table = pd.read_table('/Users/damoncrockett/Dropbox/CALIT2DATA/weather/rawData/QCLCD201301/201301station.txt',
                          sep='|')
                          
print 'data loaded'

houston = wban_table[wban_table.Name.str.contains('HOUSTON')]
baltimore = wban_table[wban_table.Name.str.contains('BALTIMORE')]
sacramento = wban_table[wban_table.Name.str.contains('SACRAMENTO')]
kansas_city = wban_table[wban_table.Name.str.contains('KANSAS CITY')]
dallas = wban_table[wban_table.Name.str.contains('DALLAS')]
corpus_christi = wban_table[wban_table.Name.str.contains('CORPUS CHRISTI')]
jacksonville = wban_table[wban_table.Name.str.contains('JACKSONVILLE')]

weather_wbans = list(set(list(weather.WBAN)))

houston = houston[houston.WBAN.isin(weather_wbans)]
baltimore = baltimore[baltimore.WBAN.isin(weather_wbans)]
sacramento = sacramento[sacramento.WBAN.isin(weather_wbans)]
kansas_city = kansas_city[kansas_city.WBAN.isin(weather_wbans)]
dallas = dallas[dallas.WBAN.isin(weather_wbans)]
corpus_christi = corpus_christi[corpus_christi.WBAN.isin(weather_wbans)]
jacksonville = jacksonville[jacksonville.WBAN.isin(weather_wbans)]

houston = houston[['WBAN','Latitude','Longitude']]
baltimore = baltimore[['WBAN','Latitude','Longitude']]
sacramento = sacramento[['WBAN','Latitude','Longitude']]
kansas_city = kansas_city[['WBAN','Latitude','Longitude']]
dallas = dallas[['WBAN','Latitude','Longitude']]
corpus_christi = corpus_christi[['WBAN','Latitude','Longitude']]
jacksonville = jacksonville[['WBAN','Latitude','Longitude']]

frames = [houston,baltimore,sacramento,kansas_city,dallas,corpus_christi,jacksonville]
alternate_weather_stations = pd.concat(frames)

from shapely.geometry import Point
import shapely

alternate_weather_station_wbans = list(alternate_weather_stations.WBAN)
alternate_weather_station_points = []
m = len(alternate_weather_stations.index)
alternate_weather_stations.reset_index(drop=True,inplace=True)
for j in range(m):
    station_point = Point(alternate_weather_stations.Longitude.loc[j],
                          alternate_weather_stations.Latitude.loc[j])
    alternate_weather_station_points.append(station_point)

print 'short loop...'

alt_wban = []
n = len(tweets_without_weather.index)
tweets_without_weather.reset_index(drop=True,inplace=True)
for i in range(n):
    tweet_point = Point(tweets_without_weather.lon.loc[i],tweets_without_weather.lat.loc[i])
    closest_station_point = min(alternate_weather_station_points,key=lambda x:x.distance(tweet_point))
    closest_station_point_idx = alternate_weather_station_points.index(closest_station_point)
    closest_station_wban = alternate_weather_station_wbans[closest_station_point_idx]
    alt_wban.append(closest_station_wban)
tweets_without_weather['alt_wban'] = alt_wban
tweets_without_weather = tweets_without_weather[['filename','alt_wban']]
tweets_without_weather.set_index('filename',inplace=True)

print 'big join...'

tweets = tweets.join(tweets_without_weather,on='filename')

print 'writing csv...'

tweets.to_csv('/Users/damoncrockett/Desktop/tweets.csv',index=False)

