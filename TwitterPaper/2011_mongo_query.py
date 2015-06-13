import pymongo
conn    = pymongo.MongoClient()
db      = conn.sample_tweets
coll    = db.sample_tweets_collection

query = {'geo' : {"$exists" : 1},
         'twitter_entities.media.media_url' : {"$exists" : 1}}
projection = {'twitter_entities.media.media_url': 1,
              'geo.coordinates': 1,
              'actor.favoritesCount': 1,
              'actor.followersCount' : 1,
              'actor.friendsCount': 1,
              'actor.statusesCount': 1,
              'postedTime': 1,
              'location.country_code': 1,
              'location.name': 1,
              '_id' : 1,
              'actor.id': 1}

counter = -1
record_list = []
for item in coll.find(query, projection):
    counter += 1
    print counter
    record_list.append(item)

import pandas as pd
df = pd.DataFrame(record_list)
df.to_csv('/data/damoncrockett/2011/output_2011.csv')
