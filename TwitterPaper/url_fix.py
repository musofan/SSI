import pandas as pd
import sys

infile = sys.argv[1]
outfile = sys.argv[2]

df = pd.read_csv(infile)
df.media_url = df.media_url.str.split('/',3).str[3]
df.media_url = 'http://pbs.twimg.com/media/'+df.media_url 

del df['display_url']
del df['size_h']
del df['size_w']
del df['profile_url']
del df['post_url']
del df['img_url']

df.to_pickle(outfile)
                         

