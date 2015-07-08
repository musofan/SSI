#!/bin/bash

#IMAGE=/Users/damoncrockett/Desktop/SD/SD_R6C2.tif
#CHUNKS=256
#TARGET=/Users/damoncrockett/Desktop/slices
#slice-image "$IMAGE" "$CHUNKS" -d

PATH=/data/damoncrockett/streetview_sample/*.jpg
TARGET=/data/damoncrockett/streetview_sample_sliced/
CHUNKS=100

for f in $PATH
do
	/usr/local/bin/slice-image "$f" "$CHUNKS" --dir "$TARGET"
done
