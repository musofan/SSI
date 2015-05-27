# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:03:38 2015

@author: damoncrockett

USAGE NOTE: This script is meant to run on csv files whose rows are
images and whose columns are a specific set of image features used 
by the Software Studies Initiative. In particular, the first 180 columns
encode hue; the next 256 encode saturation; and the final 256 encode 
value. I've cut out the first column, which gives an image path. 

To run the script from the terminal, type:

$ python one_norm.py <input file> <output file> <hue, saturation, or value>
"""
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]
feature_axis = sys.argv[3]

# create dataframe
df = pd.read_csv(input_file)

# create feature matrix
if feature_axis == 'hue':
    feature_matrix = df.iloc[:,1:181]
elif feature_axis == 'saturation':
    feature_matrix = df.iloc[:,181:437]
elif feature_axis == 'value':
    feature_matrix = df.iloc[:,437:]
    
# define normalizing function    
def inf_norm(x):
    return x/x.max()

# apply function
normed_feature_matrix = feature_matrix.apply(inf_norm,axis=1)

# add back image paths
normed_feature_matrix['filename.path'] = df['filename.path']

# send to csv
normed_feature_matrix.to_csv(output_file)

    
    

    
    
