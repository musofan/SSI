import pandas as pd
d = pd.read_csv('/data/damoncrockett/LA_oscars.csv')
file_paths = list(set(list(d.file_path)))

import shutil
n = len(d.index)
for i in range(n):
    shutil.copy2(file_paths[i], /data/damoncrockett/)
    