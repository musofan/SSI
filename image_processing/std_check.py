import pandas as pd
import sys
import numpy as np

infile = sys.argv[1]

df = pd.read_csv(infile)
print np.mean(df.hue_std), np.median(df.hue_std), df.hue_std.max()
