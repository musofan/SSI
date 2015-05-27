import pandas as pd

nyc = pd.read_csv('/Users/damoncrockett/tweets_nyc.csv')
l = pd.DataFrame(nyc.img_url.str.split('/',4).tolist(),
                columns = ['a','b','c','d','e'])
                
BASE_PATH = '/Users/damoncrockett/images_nyc/'

import requests
import shutil

n = len(nyc.index)

for i in range(n):
    path = BASE_PATH + l.e.loc[i]
    print i,path
    try:
        r = requests.get(nyc.img_url.loc[i], stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
    except:
        print 'err'                