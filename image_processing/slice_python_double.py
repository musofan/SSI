import image_slicer
import glob
import os
import sys

input_path = "/Users/damoncrockett/Desktop/scaled_slices/"
num_slices = float(sys.argv[1])
target = "/Users/damoncrockett/Desktop/scaled_slices_slices/"

# this part a hack for satellite tiles
infile = "/Users/damoncrockett/Desktop/SD_R6C2_scaled.tif"
tiles = image_slicer.slice(infile,num_slices,save=False)
image_slicer.save_tiles(tiles,directory=input_path)
                            
counter=-1
for file in glob.glob(os.path.join(input_path,'*.png')):
    counter +=1
    print counter
    try:
        tiles = image_slicer.slice(file,num_slices,save=False)
        image_slicer.save_tiles(tiles,
                            directory=target,
                            prefix=str(counter))
    except:
        print 'err'
