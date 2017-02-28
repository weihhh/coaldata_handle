import os,pandas,matplotlib
import matplotlib.pyplot as plt
import numpy

def get_full_path(test_name='testdata',test_number='1'):    
    curdir=os.path.dirname(os.path.realpath(__file__))
    current_file=test_name+test_number+'.csv'
    full_current_file=os.path.join(curdir,current_file)
    return full_current_file
    #print(full_current_f ile)

data=pandas.read_csv(full_current_file,index_col=0,header=None)#关键词变量：sep(str or default ','),index_col代表第几列作为行名，设置列名就同时设置header=None

print(data)#shape（记录（行），字段（列））

def get_row(times,updown):
    if updown=='u':
        times=2*times-2
    else:
        times=2*times-1
    row=data.iloc[times].values
    print(row)
    datalen=len(row)
    print(datalen)
    row=data.iloc[times,:datalen-1].values#iloc根据位置选取，【行，列】
    #print(type(row))
    #print(row)
    return row

#rows=numpy.concatenate((rows,data.iloc[0:2,:datalen].values[1]))

#row=pandas.Series(data.iloc[times,:datalen].values)#:datalen消去最后的不是数字部分
first_row=numpy.concatenate((get_row(1,'u'),get_row(2,'u')))
first_row=pandas.Series(first_row)
first_row.plot()
plt.show()




