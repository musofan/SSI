import glob
import os
import sys
from skimage.io import imread
from skimage import color
import numpy as np
import pandas as pd

data = pd.read_csv("/Users/damoncrockett/Desktop/lapland/data/all_fixed_lapland_filename.csv")

hue = []
sat = []
val = []
hsd = []

n = len(data.index)
for i in range(n):
    try:
        img = color.rgb2hsv(imread(data.filename.loc[i]))

        m_hue = np.mean(img[:,:,0])
        hue.append(m_hue)

        m_sat = np.mean(img[:,:,1])
        sat.append(m_sat)

        m_val = np.mean(img[:,:,2])
        val.append(m_val)
         
        m_hsd = np.std(img[:,:,0])
        hsd.append(m_hsd)

        print i

    except:
        print i,'error'
        hue.append("missing")
        sat.append("missing")
        val.append("missing")
        hsd.append("missing")

data['hue'] = hue
data['sat'] = sat
data['val'] = val
data['hsd'] = hsd

data.to_csv("/Users/damoncrockett/Desktop/lapland/data/all_fixed_lapland_filename_hsv.csv",
          index=False)