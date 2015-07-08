import pandas as pd

infile = "/data/damoncrockett/downtown_SD_Flickr/data/downtown_SD_all.csv"
BASE_PATH = "/data/damoncrockett/downtown_SD_Flickr/images/"

df = pd.read_csv(infile)

import requests
import shutil

n = len(df.index)

for i in range(n):
    path = BASE_PATH + df.dl_url.loc[i].split('/',5)[4]
    print i,path

    try:
        r = requests.get(df.dl_url.loc[i],stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
    except:
        print 'err'
