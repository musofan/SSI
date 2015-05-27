import glob
import os
import sys
from skimage.io import imread
from skimage import color
import numpy as np

input_path = sys.argv[1]
descriptor = sys.argv[2]

filename = []
hue = []
sat = []
val = []
counter = -1

for file in glob.glob(os.path.join(input_path,'*.jpg')):
    counter +=1
    
    try:
        img = color.rgb2hsv(imread(file))
        
        m_hue = np.mean(img[:,:,0])
        hue.append(m_hue)
    
        m_sat = np.mean(img[:,:,1])
        sat.append(m_sat)
    
        m_val = np.mean(img[:,:,2])
        val.append(m_val)
    
        filename.append(file)
        
        print counter, file
    
    except:
        print counter,file,'error'
        
import pandas as pd
pd.DataFrame({'filename':filename,
              'hue':hue,
              'sat':sat,
              'val':val}).to_csv(input_path+descriptor+'_metadata.csv',
              index=False)