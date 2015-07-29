import image_slicer
import pandas as pd
import os
import sys

infile = sys.argv[1]
num_slices = int(sys.argv[2])
target = sys.argv[3]

df = pd.read_csv(infile)

# option to sample
df = df.sample(n=360)
df.reset_index(drop=True,inplace=True)

n = len(df.index)
for i in range(n):
    try:
        file = df.filename.loc[i]
        tiles = image_slicer.slice(file,num_slices,save=False)
        image_slicer.save_tiles(tiles,directory=target,prefix=os.path.basename(file))
        print i
    except:
        print 'err'