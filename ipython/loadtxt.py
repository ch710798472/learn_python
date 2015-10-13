# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

from pandas import DataFrame,Series
import pandas as pd
import numpy as np
tx = pd.read_csv('/home/ch/Downloads/dim_fashion_matchsets-txt.txt')
records = [tx['123'] for rows in tx['Column']]
frame = DataFrame(records)
frame

# <codecell>

import csv
with open('/home/ch/Downloads/dim_fashion_matchsets-txt.csv') as f:
    data = csv.reader(f)
    for line in data:
        print line

# <codecell>


