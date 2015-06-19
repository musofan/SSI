import shapefile
import shapely

polygons_sf = shapefile.Reader("/data/damoncrockett/cb_2013_us_ua10_500k.shp")
polygon_shapes = polygons_sf.shapes()
polygon_points = [q.points for q in polygon_shapes]
from shapely.geometry import Polygon, Point
polygons = [Polygon(q) for q in polygon_points]

print 'd1'

records = polygons_sf.records()

m = len(records)
urban_areas = []
for i in range(m):
    urban_areas.append(records[i][3])

print 'd2'
    
import pandas as pd
d = pd.read_csv('/data/myazdani/US_HSV_modes_top60_cities.csv')

print 'd3'

n = len(d.index)
points = []
for i in range(n):
    point = Point(d.lon.loc[i],d.lat.loc[i])
    points.append(point)
    
print 'd4'
    
from rtree import index
idx = index.Index()
count = -1
for q in polygon_shapes:
    count +=1
    idx.insert(count, q.bbox)

print 'd5'
    
matches = []
for i in range(n):
    print i
    tmp= 'nan'
    for j in idx.intersection((d.lon[i],d.lat[i])):
        if points[i].within(polygons[j]):
            tmp=urban_areas[j]
            break
    matches.append(tmp)
    
print 'd6'    
    
d['urban_areas']=matches
d.to_csv('/data/damoncrockett/US_HSV_modes_top60_cities_urban-areas.csv')