import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter.filedialog

filename=None

def get_file():
    global filename
    filename=askopenfilename(defaultextension=".csv",
        filetypes = [("csv文件",".csv")])


df=pd.read_csv('testdata1.csv',error_bad_lines=False,index_col=[0,1],header=None,skiprows=[0])
del_long=lambda x: x%10000#若碰到四位四位相连的数据，保留后四位
df_fill=df.fillna(method='ffill',axis=1).ix[:,0:5].applymap(del_long)#这里因为将1，2作为index，所以默认就是显示的，ix[:,y:4]中的y不管取0，1都是一样的，共0-5，0-1索引，2-5数据
print(df,'\n',df_fill)
df_fill.ix[3,:4].ix['d']#选取第3组数据的d路

