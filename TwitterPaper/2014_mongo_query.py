"""
mongod server process must be running:
./mongod --dbpath /data/damoncrockett/2014_tweets_db
"""

import pymongo
conn 	= pymongo.MongoClient()
db 	= conn.sample_tweets
coll 	= db.sample_tweets_collection

counter = -1

def gen(coll):
    for item in coll.find():
        if ('_id' in item and 
        item['_id'] and
        'postedTime' in item and
        item['postedTime'] and
        'body' in item and item['body'] and
        'twitter_entities' in item and
        item['twitter_entities'] and
        'media' in item['twitter_entities'] and 
        item['twitter_entities']['media'] and
        'location' in item and
        item['location'] and
        'geo' in item and
        item['geo']):
            m = item['twitter_entities']['media'][0] # only the first image listed
            if 'media_url' in m and m['media_url']:
                counter +=1
                print counter
                yield item['_id'],
                item['postedTime'],
                item['location'],
                item['geo'],
                m['media_url']
                
import pandas as pd
df = pd.DataFrame(gen(coll))
df.to_pickle('/data/damoncrockett/2014_tweets_query.pickle')
