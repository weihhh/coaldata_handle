import os,pandas,matplotlib
import matplotlib.pyplot as plt
import numpy

def get_full_path(test_name='test',test_number='1'):    
    curdir=os.path.dirname(os.path.realpath(__file__))
    current_file=test_name+test_number+'.csv'
    full_current_file=os.path.join(curdir,current_file)
    return full_current_file
    #print(full_current_f ile)

data=pandas.read_csv(get_full_path(),index_col=0,header=None)#关键词变量：sep(str or default ','),index_col代表第几列作为行名，设置列名就同时设置header=None

#print(data)#shape（记录（行），字段（列））

def get_row(times,updown):
    if updown=='u':
        times=2*times-2
    else:
        times=2*times-1
    row=data.iloc[times].values
    #print(row)
    datalen=len(row)
    #print(datalen)
    row=data.iloc[times,:datalen-1].values#iloc根据位置选取，【行，列】
    #print(type(row))
    #print(row)
    return row

#rows=numpy.concatenate((rows,data.iloc[0:2,:datalen].values[1]))

#row=pandas.Series(data.iloc[times,:datalen].values)#:datalen消去最后的不是数字部分
def pre_proceed(data):
    pjz=numpy.mean(data)
    bzc=numpy.std(data)
    data1=numpy.where(data<pjz+3*bzc,data,pjz)
    data2=numpy.where(data1>pjz-3*bzc,data1,pjz)
    
    return data2

u_data=get_row(1,'u')
d_data=get_row(1,'d')


u_data1=pre_proceed(u_data)
d_data1=pre_proceed(d_data)
row2=pandas.Series(u_data1)
row3=pandas.Series(d_data1)
plt.subplot(311)
row2.plot()
row3.plot()
print(u_data,d_data)
u_data=u_data-numpy.mean(u_data1)
d_data=d_data-numpy.mean(d_data1)
print(u_data,d_data)

c=numpy.correlate(u_data,d_data,'same')#算出的值为总长除以二加上延迟
max_index = numpy.argmax(c)
print(max_index)
print(c)
#first_row=numpy.concatenate((get_row(1,'u'),get_row(2,'u')))
first_row=pandas.Series(c)
plt.subplot(313)
first_row.plot()
plt.show()




