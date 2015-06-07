import pandas as pd

d = pd.read_csv('/Users/damoncrockett/Desktop/img_urls.csv')
l = pd.DataFrame(d['0'].str.split('/',3).tolist(),
                columns = ['a','b','c','d'])

BASE_PATH = '/Users/damoncrockett/Desktop/test_imgs/'

import requests
import shutil

n = len(d.index)

import random
idx = random.sample(xrange(n),n)

for i in idx:
    print i
    path = BASE_PATH + l.d.loc[i]
    try:
        r = requests.get(d['0'].loc[i], stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
    except:
        print "err"