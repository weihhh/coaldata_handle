import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('testdata.csv',index_col=0,header=None,skiprows=[0])
df[pd.isnull(df)]=0
print(df.ix[:,:4])