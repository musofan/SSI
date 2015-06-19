import pandas as pd
import sys

infile = sys.argv[1]
BASE_PATH = sys.argv[2]

df = pd.read_csv(infile)
l = pd.DataFrame(df.media_url.str.split('/',4).tolist(),
                columns = ['a','b','c','d','e'])

import requests
import shutil

n = len(df.index)

for i in range(n):
    path = BASE_PATH + l.e.loc[i]
    print i,path
    try:
        r = requests.get(df.media_url.loc[i]+":thumb",stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
    except:
        print 'err'
