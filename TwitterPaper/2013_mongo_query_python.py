"""
mongod server process must be running:
./mongod --dbpath /data/damoncrockett/2013_tweets_db
"""

import pymongo
conn 	= pymongo.MongoClient()
coll 	= conn.sample_tweets.sample_tweets_collection

def gen(coll):
    counter = -1
    for item in coll.find():
        if ('_id' in item and item['_id'] and
        'body' in item and item['body'] and
        'actor' in item and item['actor']):
            a = item['actor']
            if 'id' in a and a['id']:
                counter +=1
                print counter
                yield item['_id'],item['body'],a['id']
                
import pandas as pd
df = pd.DataFrame(gen(coll))
df.to_pickle('/data/damoncrockett/2013_tweets_body_actor.pickle')
