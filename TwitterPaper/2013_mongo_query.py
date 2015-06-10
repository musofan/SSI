"""
mongod server process must be running:
./mongod --dbpath /data/damoncrockett/2013_tweets_db
"""

import pymongo
conn    = pymongo.MongoClient()
db      = conn.sample_tweets
coll    = db.sample_tweets_collection

query = {'_id':{"$exists":1},
         'body':{"$exists":1},
         'actor.id':{"$exists":1}}

projection = {'_id':1,
              'body':1,
              'actor.id':1}

iterator = coll.find(query,projection)

nrec = iterator.count()
chunk_size = 10000000
chunk_points = arange(0,nrec,chunk_size)
chunk_points.append(nrec-1)

import pandas as pd

for i in range(len(chunk_points)):
    chunk = iterator[i:i+1]
    print i
    if i == 0:
        df = pd.DataFrame(list(chunk))
    else:
        df = df.append(pd.DataFrame(list(chunk)),ignore_index=True)

df.to_pickle('/data/damoncrockett/2013_tweets_actor_body.pickle')








       

