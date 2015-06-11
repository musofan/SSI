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

counter=-1
chunk_list = []
for chunklet in coll.find(query,projection).limit(55000000):
    counter+=1
    print counter
    chunk_list.append(chunklet)

import pandas as pd
df = pd.DataFrame(chunk_list)
df.to_csv('/data/damoncrockett/2013_id_actor_PART.csv',index=False)

counter=-1
chunk_list = []
for chunklet in coll.find(query,projection).skip(55000001):
    counter+=1
    print counter
    chunk_list.append(chunklet)

df = df.append(pd.DataFrame(chunk_list),ignore_index=True)
df.to_csv('/data/damoncrockett/2013_id_actor_WHOLE.csv',index=False)
