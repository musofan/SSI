import image_slicer
import pandas as pd
import os


input_path = "/Users/damoncrockett/Desktop/lapland/"
df = pd.read_csv(input_path+"data/all_fixed_lapland_filename.csv")
num_slices = 1024
target = "/Users/damoncrockett/Desktop/lapland/slices/"                         

n = len(df.index)
for i in range(n):
    try:
        file = df.filename.loc[i]
        tiles = image_slicer.slice(file,num_slices,save=False)
        image_slicer.save_tiles(tiles,directory=target,prefix=os.path.basename(file))
        print i
    except:
        print 'err'