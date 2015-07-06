#!/bin/bash

#IMAGE=/Users/damoncrockett/Desktop/SD/SD_R6C2.tif
#CHUNKS=256
#TARGET=/Users/damoncrockett/Desktop/slices
#slice-image "$IMAGE" "$CHUNKS" -d 

PATH=/Users/damoncrockett/Desktop/SD_slices_2/*.*
TARGET=/Users/damoncrockett/Desktop/SD_slices_2_2/
CHUNKS=4096
for f in $PATH
do
	/usr/local/bin/slice-image "$f" "$CHUNKS" -d "$TARGET"
done