"""
mongod server process must be running:
./mongod --dbpath /data/damoncrockett/2013_tweets_db
"""

import pymongo
conn    = pymongo.MongoClient()
db      = conn.sample_tweets
coll    = db.sample_tweets_collection

query = {'_id':{"$exists":1},
         'actor.id':{"$exists":1}}

projection = {'_id':1,
              'actor.id':1}

iterator = coll.find(query,projection)

chunk_1 = iterator[:55000000]
chunk_2 - iterator[55000001:]

import pandas as pd
df = pd.DataFrame(chunk_1)
df.to_csv('/data/damoncrockett/2013_id_actor_PART.csv',index=False)
df = df.append(pd.DataFrame(chunk_2),ignore_index=True)
df.to_csv('/data/damoncrockett/2013_id_actor_WHOLE.csv',index=False)

