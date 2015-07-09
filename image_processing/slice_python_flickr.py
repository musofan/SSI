import image_slicer
import sys
import pandas as pd

infile = sys.argv[1]
num_slices = float(sys.argv[2])

df = pd.read_csv(infile)
df = df.sample(n=16384)

base_dir = "/data/damoncrockett/downtown_SD_Flickr/images_sliced_"

counter=-1
for file in df.local_folder:
    counter +=1
    print counter
    if counter > 4000:
        try:
            tiles = image_slicer.slice(file,num_slices,save=False)
            image_slicer.save_tiles(tiles,
                                    directory=base_dir+"1/",
                                    prefix=str(counter))
        except:
            print 'err'
