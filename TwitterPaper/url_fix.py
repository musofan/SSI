import pandas as pd
df = pd.read_csv('/data/damoncrockett/2011/output_2011.csv')
l = pd.DataFrame(df.media_url.str.split('/',3).tolist(),
    columns=['a','b','c','d'])
l.c = 'pbs.twimg.com'
n = len(df.index)
for i in range(n):
    print i
    df.media_url.loc[i] = (l.a.loc[i]+
                         '/'+l.b.loc[i]+
                         '/'+l.c.loc[i]+
                         '/media'+
                         '/'+l.d.loc[i])

del df['display_url']
del df['size_h']
del df['size_w']
del df['profile_url']
del df['post_url']
del df['img_url']

df.to_pickle('/data/damoncrockett/2011/output_2011_fixed.pickle')
                         

