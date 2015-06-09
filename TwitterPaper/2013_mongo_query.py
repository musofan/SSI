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

query_iterator = coll.find(query,projection)

import pandas as pd
tmp_list = []
counter = -1
for item in query_iterator:
    counter+=1
    print counter
    tmp_list.append(item)    
df = pd.DataFrame(tmp_list)
df.to_pickle('/data/damoncrockett/2013_tweets_actor_body.pickle')








       

