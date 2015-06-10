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
chunk_2 = iterator[55000001:]

counter=-1
chunk_1_list = []
for chunk in chunk_1:
    counter+=1
    print counter
    chunk_1_list.append(chunk)

import pandas as pd
df = pd.DataFrame(chunk_1_list)
df.to_csv('/data/damoncrockett/2013_id_actor_PART.csv',index=False)

counter=-1
chunk_2_list = []
for chunk in chunk_2:
    counter+=1
    print counter
    chunk_2_list.append(chunk)  

df = df.append(pd.DataFrame(chunk_2_list),ignore_index=True)
df.to_csv('/data/damoncrockett/2013_id_actor_WHOLE.csv',index=False)

