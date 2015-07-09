#!/bin/bash

IMAGE=/Users/damoncrockett/Desktop/SD_R6C2_scaled.tif
CHUNKS=1024
TARGET=/Users/damoncrockett/Desktop/scaled_slices
#slice-image "$IMAGE" "$CHUNKS" -d

PATH=/data/damoncrockett/streetview_sample/*.jpg
TARGET=/data/damoncrockett/streetview_sample_sliced/
CHUNKS=100

for f in $PATH
do
	/usr/local/bin/slice-image "$f" "$CHUNKS" --dir "$TARGET"
done
