#!/bin/bash

FILES=/Users/damoncrockett/Dropbox/cogs220/proposal/lit/one/*.pdf
EXT=".txt"

for f in $FILES
do
	pith=${f%%.*}
	pdf2txt.py -o "$pith$EXT" "$f"
done