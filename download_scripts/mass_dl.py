import pandas as pd
import sys
import os

infile = sys.argv[1]
BASE_PATH = sys.argv[2]

df = pd.read_csv(infile)

import requests
import shutil

n = len(df.index)

for i in range(n):
    path = BASE_PATH + os.path.basename(df.media_url.loc[i])
    print i,path

    try:
        r = requests.get(df.media_url.loc[i],stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
    except:
        print 'err'
