import image_slicer
import glob
import os
import sys

input_file = "/Users/damoncrockett/Desktop/encanto_4096.tif"
num_slices = float(sys.argv[1])
target = "/Users/damoncrockett/Desktop/enc/slices/"

# don't need informative filenames at this stage
tiles = image_slicer.slice(input_file,num_slices,save=False)
image_slicer.save_tiles(tiles,directory=target)

new_target = "/Users/damoncrockett/Desktop/enc/slices_of_slices/"
# can adjust num_slices if need be                      
counter=-1
for file in glob.glob(os.path.join(target,'*.png')):
    counter +=1
    print counter
    try:
        tiles = image_slicer.slice(file,num_slices,save=False)
        image_slicer.save_tiles(tiles,
                            directory=new_target,
                            prefix=str(counter))
    except:
        print 'err'
