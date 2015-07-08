import pandas as pd

# taken from Damons-MacBook-Pro:~/Desktop/FISP_notebooks/downtown_tile_geo.ipynb
box = [-117.219018,-117.131525,32.686961,32.760859]

# we want 25,000 random latlons from this box

import numpy as np
lons = [item for item in np.random.uniform(box[0],box[1],25000)]
lats = [item for item in np.random.uniform(box[2],box[3],25000)]

l = pd.DataFrame(lons,columns=['lon'])
l['lat']=lats

import requests
import shutil

BASEPATH = "/data/damoncrockett/streetview/"
BASEURL = "https://maps.googleapis.com/maps/api/streetview?"
KEY="key=AIzaSyAcUHvpeU-08T469Ww0xXRVFUUiJ_sALRM&"
SIZE="size=640x640&"

n = len(l.index)
for i in range(n):
    loc_param = str(l.lat.loc[i])+","+str(l.lon.loc[i])
    # can't use comma in filename, so use underscore instead
    filestring = str(l.lat.loc[i])+"_"+str(l.lon.loc[i])
    # can't have dots or negative signs in filename; use str.translate()
    path = BASEPATH+filestring.translate(None,"-.")+".jpg"
    print i,path
    try:
        r = requests.get(BASEURL+KEY+SIZE+"location="+loc_param,stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
    except:
        print 'err'
