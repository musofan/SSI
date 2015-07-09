import image_slicer
import sys
import pandas as pd

infile = "/data/damoncrockett/downtown_SD_Flickr/data/all_image_exists.csv"
num_slices = 2048

df = pd.read_csv(infile)
df = df.sample(n=16384)

# Okay this is hacky...I don't care. Science awaits.
BASE_DIR = "/data/damoncrockett/downtown_SD_Flickr/images_sliced_"

counter=-1
for file in df.local_folder:
    counter +=1
    print counter
    try:
        tiles = image_slicer.slice(file,num_slices,save=False)
        if counter > 12000:
            ext = "4/"
        elif counter > 8000:
            ext = "3/"
        elif counter > 4000:
            ext = "2/"
        else:
            ext = "1/" 
            
        image_slicer.save_tiles(tiles,
                                directory=BASE_DIR+ext,
                                prefix=str(counter))
    except:
        print 'err'
