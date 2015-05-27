import os
import pandas as pd

d = pd.read_csv('tweets_la.csv')

for file in d['image.path']:
    os.system("scp damoncrockett@137.110.118.15:file ~/images_la/")
