import pandas as pd

la = pd.read_csv('/Users/damoncrockett/tweets_la.csv')
l = pd.DataFrame(la.img_url.str.split('/',4).tolist(),
                columns = ['a','b','c','d','e'])
                
BASE_PATH = '/Users/damoncrockett/images_la/'

import requests
import shutil

n = len(la.index)

for i in range(n):
    path = BASE_PATH + l.e.loc[i]
    print i,path
    try:
        r = requests.get(la.img_url.loc[i], stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
    except:
        print "err"
    