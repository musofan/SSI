import pandas as pd
import sys

infile = sys.argv[1]
BASE_PATH = sys.argv[2]

urls = pd.read_csv(infile)
urls = list(urls.media_url)

import grequests
import shutil

def exception_handler(request,exception):
    print 'err'

quests = [grequests.get(url+":thumb",stream=True) for url in urls]
sponses = grequests.map(quests,
                        size=5,
                        exception_handler=exception_handler)

    path = BASE_PATH + url.split('/',4)[4]
        if r.status_code == 200:
            with open(path,'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw,f)
    except:
        pass
            
quests = asy            
async.map(quests)

