import image_slicer
import glob
import os
import sys

input_path = sys.argv[1]
num_slices = float(sys.argv[2])
target = sys.argv[3]
filetype = sys.argv[4]

counter=-1
for file in glob.glob(os.path.join(input_path,'*.'+filetype)):
    counter +=1
    print counter
    try:
        tiles = image_slicer.slice(file,num_slices,save=False)
        image_slicer.save_tiles(tiles,
                            directory=target,
                            prefix=str(counter))
    except:
        print 'err'
