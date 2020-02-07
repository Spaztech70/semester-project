#%%
# Import needed packages

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from time import perf_counter
import gzip
#%%

# read in the .gzip file
def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

df = getDF('reviews_Tools_and_Home_Improvement_5.json.gz')

print(df.head())

# this breaks the "helpful" column into two columns
pd.DataFrame(df['helpful'].values.tolist())

#%%