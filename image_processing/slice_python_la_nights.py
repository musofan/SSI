import image_slicer
import glob
import os

input_path = "/Users/damoncrockett/Desktop/lapland/images/"
num_slices = 1024
target = "/Users/damoncrockett/Desktop/lapland/slices/"                         

counter=-1
for file in glob.glob(os.path.join(input_path,"*.jpg")):
    counter+=1
    try:
        tiles = image_slicer.slice(file,num_slices,save=False)
        image_slicer.save_tiles(tiles,directory=target,prefix=os.path.basename(file))
        print counter
    except:
        print 'err'