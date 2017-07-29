#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#pyw为后缀名则运行不带控制台

__author__='weizhang'
'''
最终版
用类进行包装，方便多个文件多次试验数据的整合处理
可以直接根据文件名中的重量进行拟合
'''
import tkinter
import tkinter.filedialog
from tkinter import *
import tkinter.messagebox as messagebox
import os,pandas,matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

DATA_SIZE=1024


def calman_python(Z):#array
    N=len(Z)
    xkf=np.zeros(N)
    #Z=np.array([1338,1341,1338,1342,1338,1340,1343,1337,1341,1337,1342,1336,1345,1340,1338,1340,1343,1335,1340,1340,1340,1341,1340,1342,1338,1340,1340,1344,1336,1346,1337,1344,1341,1347,1338,1348,1336,1343,1336,2092,1579,1336,1345,1338,1342,1340,1340,1342,1337,1303,1338,1339,1343,1339,1340,1341,1339,1348,1337,1331,1317,1314,1335,1342,1341,1339,1342,1343,1342,1337,1281,1339,1349,1342,1345,1340,1345,1342,1342,1346,1340,1341,1344,1341,1345,1342,1342,1341,1345,1343,1346,1339,1345,1345,1345,1341,1346,1342,1341,1348,1331,1344,1340,1346,1342,1341,1346,1344,1340,1348,1333,1348,1342,1343,1343,1341,1347,1342,1346,1346,1341,1342,1340,1344,1341,1342,1342,1342,1343,1341,1343,1342,1335,1344,1342,1341,1338,1340,1342,1342,1341,1340,1339,1339,1341,1341,1344,1340,1342,1336,1348,1341,1339,1342,1339,1344,1342,1342,1339,1342,1337,1343,1340,1338,1341,1343,1335,1341,1340,1336,1335,1336,1341,1340,1338,1340,1336,1341,1341,1334,1344,1337,1339,1341,1340,1341,1344,1343,1338,1347,1338,1339,1343,1336,1340,1335,1344,1338,1339,1338,1343,1336,1344,1336,1339,1339,1332,1342,1340,1340,1339,1343,1338,1340,1339,1342,1333,1341,1338,1343,1338,1346,1338,1339,1341,1338,1349,1339,1341,1339,1339,1340,1337,1341,1341,1343,1341,1344,1338,1344,1343,1340,1338,1341,1340,1343,1338,1338,1341,1341,1335,1347,1341,1338,1340,1336,1336,1338,1339,1332,1344,1337,1342,1336,1339,1339,1336,1335,1344,1340,1337,1343,1341,1338,1341,1335,1349,1341,1342,1342,1341,1339,1340,1345,1338,1341,1348,1339,1343,1341,1343,1342,1338,1346,1338,1345,1335,1342,1340,1346,1338,1340,1340,1346,1338,1346,1332,1340,1345,1342,1346,1346,1341,1343,1342,1343,1344,1341,1347,1337,1346,1339,1342,1344,1341,1347,1352,1340,1341,1340,1344,1339,1345,1343,1342,1347,1345,1339,1344,1343,1349,1341,1348,1344,1341,1346,1339,1346,1340,1346,1343,1346,1343,1343,1342,1345,1335,1345,1338,1341,1343,1338,1349,1340,1344,1343,1344,1342,1341,1344,1342,1339,1345,1339,1345,1344,1347,1345,1336,1348,1335,1346,1342,1342,1342,1342,1342,1343,1340,1340,1344,1342,1342,1339,1343,1338,1334,1336,1338,1344,1336,1344,1338,1342,1342,1338,1334,1341,1337,1342,1338,1341,1337,1339,1337,1340,1345,1338,1338,1337,1338,1337,1340,1337,1338,1335,1355,1337,1340,1337,1341,1337,1338,1342,1340,1339,1335,1343,1336,1338,1335,1340,1339,1341,1338,1338,1329,1334,1347,1335,1347,1336,1340,1343,1339,1337,1342,1340,1338,1342,1338,1343,1332,1347,1336,1339,1353,1344,1335,1342,1339,1343,1338,1342,1339,1343,1342,1334,1344,1336,1343,1337,1337,1341,1340,1340,1317,1341,1337,1340,1340,1340,1337,1340,1342,1340,1336,1340,1342,1336,1345,1336,1343,1340,1340,1341,1358,1341,1340,1338,1345,1341,1341,1341,1340,1341,1345,1345,1338,1338,1339,1340,1342,1340,1343,1340,1327,1343,1343,1338,1348,1338,1344,1339,1344,1337,1330,1343,1339,1340,1344,1344,1340,1341,1344,1341,1348,1345,1339,1345,1341,1343,1342,1341,1345,1340,1359,1342,1345,1340,1345,1341,1341,1343,1346,1342,1343,1344,1342,1341,1341,1348,1340,1341,1343,1339,1331,1346,1341,1340,1342,1346,1341,1340,1343,1340,1335,1339,1343,1339,1345,1340,1342,1344,1344,1342,1355,1341,1343,1341,1340,1345,1340,1342,1341,1340,1347,1339,1345,1339,1343,1338,1340,1341,1340,1341,1330,1338,1345,1338,1338,1341,1338,1340,1339,1342,1324,1340,1338,1340,1338,1342,1336,1338,1339,1342,1343,1337,1339,1336,1341,1337,1341,1336,1340,1340,1343,1338,1340,1339,1342,1337,1339,1339,1340,1342,1336,1340,1338,1337,1337,1340,1340,1338,1339,1339,1335,1340,1342,1338,1337,1337,1344,1337,1340,1338,1335,1342,1337,1342,1337,1338,1338,1339,1341,1340,1340,1341,1340,1340,1339,1340,1342,1337,1342,1340,1340,1339,1342,1341,1339,1338,1340,1339,1340,1340,1339,1340,1338,1341,1338,1338,1341,1339,1341,1338,1341,1338,1338,1342,1339,1339,1340,1339,1341,1338,1341,1340,1338,1341,1339,1343,1337,1341,1340,1337,1343,1338,1341,1340,1340,1342,1337,1341,1340,1340,1339,1340,1341,1340,1340,1343,1338,1342,1340,1340,1340,1341,1343,1339,1339,1342,1340,1341,1341,1340,1343,1339,1343,1340,1341,1342,1341,1343,1340,1343,1341,1340,1344,1340,1343,1342,1342,1344,1341,1345,1342,1342,1342,1343,1343,1339,1341,1343,1341,1344,1343,1342,1342,1343,1345,1341,1342,1343,1341,1344,1341,1344,1341,1342,1344,1342,1342,1344,1342,1343,1343,1345,1342,1341,1344,1343,1343,1343,1343,1344,1341,1344,1342,1341,1345,1341,1345,1339,1344,1342,1340,1344,1341,1342,1341,1341,1344,1339,1342,1342,1341,1343,1341,1343,1340,1340,1342,1339,1342,1340,1341,1340,1340,1342,1340,1339,1341,1338,1341,1338,1341,1338,1338,1340,1339,1339,1340,1337,1341,1338,1341,1338,1337,1339,1339,1340,1338,1339,1340,1337,1340,1339,1338,1339,1338,1341,1336,1341,1337,1337,1341,1338,1337,1338,1338,1341,1336,1340,1339,1338,1339,1340,1339,1339,1337,1339,1337,1341,1339,1338,1340,1338,1341,1336,1338,1339,1339,1339,1339,1338,1340,1336,1342,1337,1339,1340,1339,1338,1339,1340,1339,1337,1343,1338,1341,1337,1340,1339,1339,1340,1340,1338,1341,1340,1341,1338,1340,1341,1337,1343,1338,1340,1339,1340,1342,1338,1339,1341,1337,1341,1339,1341,1339,1338,1342,1338,1342,1340,1340,1340,1341,1341,1339,1339,1341,1340,1341,1341,1340,1341,1338,1344,1339,1340,1341,1339,1342,1339,1343,1340,1339,1343,1340,1340,1341,1341,1342,1340,1343,1343,1339,1343,1341,1343,1342,1342,1343,1339,1345,1341,1341,1342,1342,1345,1338,1344,1342,1341])
    var_data=np.var(Z)
    P=np.zeros(N)
    P[0]=0.01
    xkf[0]=Z[0]
    Q=10
    R=50
    for k in range(1,N):
        x_pre=xkf[k-1]
        p_pre=P[k-1]+Q
        KG=p_pre/(p_pre+R)
        E=Z[k]-x_pre
        xkf[k]=x_pre+KG*E
        P[k]=(1-KG)*p_pre
        #print(k)   
    return xkf#array

class coal_file(object):
    """一个煤粉记录对应的相关数据整合"""
    def __init__(self, file_name,weight,data_size,data_mean,data_delay_list,flow_all):
        super(coal_file, self).__init__()
        self.file_name = file_name
        self.weight=weight
        self.data_size=data_size
        self.data_mean_list=data_mean
        self.data_delay_list=data_delay_list
        self.flow_all=flow_all

coal_file_dict={}

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.filename_lable=StringVar()
        self.calman_flag=IntVar()
        self.up_value=IntVar()
        self.down_value=IntVar()
        self.corr_multi=IntVar()
        self.createWidgets()

    def createWidgets(self):#界面布局        
        
        
        self.noteLabel1 = Label(self, text='1.点击打开选择数据文件!')
        self.noteLabel1.grid(row=0,sticky=W)#提示测试名称标签
        
        self.confirmButton1 = Button(self, text='打开', command=self.init_file_class)
        self.confirmButton1.grid(row=0,column=1)#确认测试文件名按钮

        self.confirmButtonx = Button(self, text='预处理', command=self.pre_file)
        self.confirmButtonx.grid(row=0,column=2)#删除数据中的问号,先点击打开文件，选择文件后，若第一次打开这个文件，则点击预处理
        
        self.calman_choose=Checkbutton(self,text='卡尔曼',variable=self.calman_flag)
        self.calman_choose.grid(row=0,column=3)

        self.noteLabelAD = Label(self, text='2.输入累计文件范围')
        self.noteLabelAD.grid(row=1,sticky=W)
        self.folw_start_input = Entry(self)#输入开始范围
        self.folw_start_input.grid(row=1,column=1)
        self.folw_end_input = Entry(self)#输入结束范围
        self.folw_end_input.grid(row=1,column=2)
        self.sumbutton = Button(self, text='统计流量', command=self.addflow)
        self.sumbutton.grid(row=1,column=3)

        
        self.noteLabel3=Label(self)
        self.noteLabel3['textvariable']=self.filename_lable        
        self.noteLabel3.grid(row=2,sticky=W)#显示当前读取文件名
        
        self.noteLabel4=Label(self,text='3.选择上下游通道')
        self.noteLabel4.grid(row=3,sticky=W)
        self.up_choose=Checkbutton(self,text='上路',variable=self.up_value)
        self.down_choose=Checkbutton(self,text='下路',variable=self.down_value)
        self.up_choose.grid(row=3,column=1)
        self.down_choose.grid(row=3,column=2)
        
        self.noteLabel5 = Label(self, text='4.选择需要显示的组数!')
        self.noteLabel5.grid(row=4,sticky=W)#提示标签
        self.start_rowInput = Entry(self)
        self.start_rowInput.grid(row=5)#输入框
        self.end_rowInput = Entry(self)
        self.end_rowInput.grid(row=5,column=1)#输入框
        self.confirmButton2 = Button(self, text='绘图', command=self.make_pic)
        self.confirmButton2.grid(row=5,column=2)#确认输入按钮
        
        self.noteLabel6 = Label(self, text='5.input the row you want to do corr!')
        self.noteLabel6.grid(row=6,sticky=W)#提示标签
        self.start_rowInput1 = Entry(self)
        self.start_rowInput1.grid(row=7)#输入框
        self.end_rowInput1 = Entry(self)
        self.end_rowInput1.grid(row=7,column=1)#输入框
        self.corr_multi_check=Checkbutton(self,text='multi ',variable=self.corr_multi)
        self.corr_multi_check.grid(row=7,column=2)
        self.confirmButton3 = Button(self, text='corr', command=self.my_corr)
        self.confirmButton3.grid(row=7,column=3)#确认输入按钮
        
        self.noteLabel7 = Label(self, text='fuck coal!')
        self.noteLabel7.grid(row=8,sticky=W)#提示标签

    
    def init_file_class(self):
        file_names=tkinter.filedialog.askopenfilenames(defaultextension=".csv",filetypes = [("csv文件",".csv")])
        self.filename_lable.set(str(self.calman_flag.get()))
        for file_name in file_names:
            ori_data=pd.read_csv(file_name,error_bad_lines=False,index_col=[0,1],header=None,skiprows=[0])
            # if re.match(r'.*testa.*',file_name):
            #     self.pro_data=ori_data.fillna(method='ffill',axis=1).ix[:,0:DATA_SIZE+1]*1.05
            # else:
            #     self.pro_data=ori_data.fillna(method='ffill',axis=1).ix[:,0:DATA_SIZE+1]
            #print(self.pro_data)
            self.pro_data=ori_data.fillna(method='ffill',axis=1).ix[:,0:DATA_SIZE+1]
            self.filename_lable.set(file_name+'--calmanflag--'+str(self.calman_flag.get()))
            if(re.match(r'.*_(.*)_.*',file_name)):
                weight=float(re.match(r'.*_(.*)_.*',file_name).group(1))#文件格式test3_7_kg.csv
            else:
                weight="wrong_sytax!"
            data_size=self.pro_data.shape[0]//2
            flow_all,data_mean_list,data_delay_list=self.my_corr_file(self.pro_data,1,data_size)
            now_class=coal_file(file_name,weight,data_size,data_mean_list,data_delay_list,flow_all)
            coal_file_dict[file_name]=now_class
        self.print_class_list()


    def pre_file(self):
        file=tkinter.filedialog.askopenfilename(defaultextension=".csv",filetypes = [("csv文件",".csv")])
        with open(file,'rt',errors='ignore') as f:
            data=f.read()
        with open(file,'wt') as f:
            pre_data=re.sub(r'[^,a-z0-9\n]','',data)#.replace方法不修改原字符串
            pre_data_list=pre_data.split('\n')
            length=len(pre_data_list)
            #如果数据奇数行则说明最后一组只收了上路，直接删除最后一组数据，偶数则判断最后一行是否个数符合要求
            #要额外考虑第一行的start
            if (length-1)%2:
                pre_data='\n'.join(pre_data_list[:length-1])
            else:
                if len(pre_data_list[length-1].split(','))!=1026:
                    pre_data='\n'.join(pre_data_list[:length-2])
            f.write(pre_data)
        print(pre_data)

    def make_pic(self):#对应绘图按钮
        #从这开始做根据设置的范围取出数据
        start_times=int(self.start_rowInput.get() or '1')
        end_times=int(self.end_rowInput.get()) if self.end_rowInput.get() else start_times
        if self.up_value.get()==1:        
            start_series_up=pd.Series()
            plot_data_series_up=start_series_up.append([self.get_row(i,'u') for i in range(start_times,end_times+1)],ignore_index=True)
            plot_data_series_up.plot()
            if self.calman_flag.get()==1 :
                for_mean_up=pd.Series(calman_python(np.array(plot_data_series_up)))
                for_mean_up.plot()
                print('up--calman--mean:',np.mean(for_mean_up))
            print('up--mean:',np.mean(plot_data_series_up))
        if self.down_value.get()==1 :
            start_series_down=pd.Series()
            plot_data_series_down=start_series_down.append([self.get_row(i,'d') for i in range(start_times,end_times+1)],ignore_index=True)
            plot_data_series_down.plot()
            if self.calman_flag.get()==1:
                for_mean_down=pd.Series(calman_python(np.array(plot_data_series_down)))
                for_mean_down.plot()
                print('down--calman--mean:',np.mean(for_mean_down))
            print('down:',np.mean(plot_data_series_down))
        
        plt.show()

    def get_row(self,times,updown):#获取某一行数据的接口函数
        row=self.pro_data.ix[times,:DATA_SIZE+1].ix[updown]#return series,非副本，只是视图,从times从1开始，因为pro_data中行0为列名
        #self.datalen=len(row)
        #print(row)
        return row   

    def print_class_list(self):
        for dataclass in coal_file_dict:
            print(coal_file_dict[dataclass].file_name,end=' , ')
            print(coal_file_dict[dataclass].weight,end=' kg , ')
            print(coal_file_dict[dataclass].data_size,end=' , ')
            print(coal_file_dict[dataclass].flow_all,end=' , ')
            print(coal_file_dict[dataclass].data_delay_list,end=' , ')
            # print(coal_file_dict[dataclass].data_mean_list,end=' , ')
            print('\n')
        print('数据文件总数：',len(coal_file_dict))


    def addflow(self):
        x=[coal_file_dict[data].flow_all for data in coal_file_dict] 
        y=[coal_file_dict[data].weight for data in coal_file_dict]
        z1=np.polyfit(x,y,1)#得到点列表，最后的数字代表多项式次数
        p1 = np.poly1d(z1)#得到公式
        #print(p1)
        #计算拟合相关度
        huigui=0
        allpinggang=0
        cancha=0
        for i,number in enumerate(y):
            allpinggang=allpinggang+number**2
            cancha=cancha+(number-p1(x[i]))**2#p1公式直接代入x，p1()
            print('真值：',number,' 拟合值：',p1(x[i]),' 差值：',number-p1(x[i]),' 比例：',(number-p1(x[i]))/number)
        rpingfang=(allpinggang-cancha)/allpinggang
        print('拟合相关度:',rpingfang)
        #产生画布
        fig=plt.figure(1)
        ax1=fig.add_subplot(111)
        #设置标题
        ax1.set_title('scatter plot')
        #设置x轴标签
        plt.xlabel('x')
        plt.ylabel('y')
        ax1.scatter(x,y,c='r',marker='o',label='o_data')
        #ax1.scatter(x,z,c='b',marker='o')
        #画出拟合曲线
        yvals=p1(x)
        plot2=plt.plot(x, yvals, 'r',label='polyfit values')
        plt.legend()
        #右上角线条说明
        plt.show()
        #print(filenumber_start)
    
    def my_corr(self):
        #pure corr and add
        sum_pipe=0
        last_time=200
        start_times=int(self.start_rowInput1.get() or '1')
        end_times=int(self.end_rowInput1.get() or '2')
        if self.corr_multi.get()==1 :
            for i in range(start_times,end_times+1):
                    u_data_origin=self.get_row(i,'u')
                    d_data_origin=self.get_row(i,'d')
                                      
                    u_data_calman=calman_python(np.array(u_data_origin))
                    d_data_calman=calman_python(np.array(d_data_origin))
                    u_data_corr=u_data_calman-np.mean(u_data_calman)
                    d_data_corr=d_data_calman-np.mean(d_data_calman)
                    
                    c=np.correlate(u_data_corr,d_data_corr,'same')#算出的值为总长除以二加上延迟
                    max_index = np.argmax(c)
                    time=np.fabs(max_index-DATA_SIZE//2)
                    dense=np.mean(u_data_calman)#这里用了卡尔曼滤波后的平均值
                    print(i,' time:',time,' dense:',dense,'\n')
                    if(time < 100 and time>3):
                        sum_pipe=sum_pipe+dense/(time*10)
                        last_time=time
                    if(time==0 and last_time <100 and last_time >3):
                        sum_pipe=sum_pipe+dense//(time*10)
                        continue
                    last_time=200
            print(sum_pipe)
            
        else:            
            u_data_origin=self.get_row(start_times,'u')
            d_data_origin=self.get_row(start_times,'d')
            
            u_data_calman=calman_python(np.array(u_data_origin))
            d_data_calman=calman_python(np.array(d_data_origin))
            u_data_corr=u_data_calman-np.mean(u_data_calman)
            d_data_corr=d_data_calman-np.mean(d_data_calman)
            plt.plot(range(1024),u_data_origin,'b',range(1024),u_data_calman,'k')
            plt.plot(range(1024),d_data_origin,'r',range(1024),d_data_calman,'y')
            c=np.correlate(u_data_corr,d_data_corr,'same')#算出的值为总长除以二加上延迟
            max_index = np.argmax(c)
            print('time:',max_index-DATA_SIZE//2,'\n')
            print('dense_calmanbefore:',np.mean(u_data_calman),'dense_after',np.mean(u_data_origin),'\n')
            plt.show()   

    def my_corr_file(self,data,start_times,end_times):
        sum_pipe=0
        last_time=200
        alist=[]#平均值
        blist=[]#delay
        for i in range(start_times,end_times+1):
            u_data_origin=data.ix[i,:DATA_SIZE+1].ix['u']
            d_data_origin=data.ix[i,:DATA_SIZE+1].ix['d']
                              
            if self.calman_flag.get()==1:

                u_data_calman=calman_python(np.array(u_data_origin))
                d_data_calman=calman_python(np.array(d_data_origin))
                dense=np.mean(u_data_calman)
                #下面用的是减去平均值的普通处理
                u_data_corr=u_data_calman-np.mean(u_data_calman)
                d_data_corr=d_data_calman-np.mean(d_data_calman)
                #下面用归一化数据处理
                # u_data_corr=(u_data_calman-np.min(u_data_calman))/(np.max(u_data_calman)-np.min(u_data_calman))
                # d_data_corr=(d_data_calman-np.min(d_data_calman))/(np.max(d_data_calman)-np.min(d_data_calman))
                # print(u_data_corr)
            else:
                dense=np.mean(u_data_origin)
                u_data_corr=u_data_origin-np.mean(u_data_origin)
                d_data_corr=d_data_origin-np.mean(d_data_origin)
            
            #算出的值为总长除以二加上延迟
            c=np.correlate(u_data_corr,d_data_corr,'same')
            max_index = np.argmax(c)
            time=np.fabs(max_index-DATA_SIZE//2)
            
            alist.append(dense)
            blist.append(time)
            #print(i,' time:',time,' dense:',dense,'\n')
            
            #下面是不考虑删除正常值
            # if time>0:
            #     sum_pipe=sum_pipe+(dense)/(time)


            #下面这一段是考虑删除不正常值的
            if(time < 25 and time>3):
                sum_pipe=sum_pipe+(dense)/(time)
                last_time=time
            if(time==0 and last_time <25 and last_time >3):
                sum_pipe=sum_pipe+(dense)//(time)
                continue
            last_time=200
        return sum_pipe,alist,blist

app = Application()
# 设置窗口标题:
app.master.title('coal_data_handle_calman')
# 主消息循环:
app.mainloop()