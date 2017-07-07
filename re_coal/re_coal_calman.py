#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#pyw为后缀名则运行不带控制台

__author__='weizhang'

import tkinter
import tkinter.filedialog
from tkinter import *
import tkinter.messagebox as messagebox
import os,pandas,matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_number=1024
def calman_python(Z):#array
    N=1024
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
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.filename=None
        self.filename_lable=StringVar()
        self.up_value=IntVar()
        self.down_value=IntVar()
        self.corr_multi=IntVar()
        self.createWidgets()
    
        
    
    def createWidgets(self):#界面布局        
        
        
        self.noteLabel1 = Label(self, text='1.点击打开选择数据文件!')
        self.noteLabel1.grid(row=0,sticky=W)#提示测试名称标签
        
        self.confirmButton1 = Button(self, text='打开', command=self.get_file)
        self.confirmButton1.grid(row=0,column=1)#确认测试文件名按钮

        self.confirmButtonx = Button(self, text='预处理', command=self.pre_file)
        self.confirmButtonx.grid(row=0,column=2)#删除数据中的问号,先点击打开文件，选择文件后，若第一次打开这个文件，则点击预处理
        
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
        
        self.noteLabel4=Label(self,text='3.选择上下游通道，仅可选一路')
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
            
    def get_file(self):#打开文件获取初始数据
        self.filename=tkinter.filedialog.askopenfilename(defaultextension=".csv",filetypes = [("csv文件",".csv")])#filetypes将对文件进行筛选显示，askopenfilename返回的是字符串
        self.filename_lable.set(self.filename)#显示的标签需要set方法来设置
        self.ori_data=pd.read_csv(self.filename,error_bad_lines=False,index_col=[0,1],header=None,skiprows=[0])
        #del_long=lambda x: x%10000#若碰到四位四位相连的数据，保留后四位
        #self.pro_data=self.ori_data.fillna(method='ffill',axis=1).ix[:,0:data_number+1].applymap(del_long)#这里因为将1，2作为index，所以默认就是显示的，ix[:,y:4]中的y不管取0，1都是一样的，共0-5，0-1索引，2-5数据
        self.pro_data=self.ori_data.fillna(method='ffill',axis=1).ix[:,0:data_number+1]
        print(self.pro_data,'\n')

    def pre_file(self):
        file=tkinter.filedialog.askopenfilename(defaultextension=".csv",filetypes = [("csv文件",".csv")])
        with open(file,'rt',errors='ignore') as f:
            data=f.read()
        with open(file,'wt') as f:
            pre_data=re.sub(r'[^,a-z0-9\n]','',data)#.replace方法不修改原字符串
            f.write(pre_data)
            
    def make_pic(self):
        #从这开始做根据设置的范围取出数据
        start_times=int(self.start_rowInput.get() or '1')
        end_times=int(self.end_rowInput.get()) if self.end_rowInput.get() else start_times
        if self.up_value.get()==1:        
            start_series_up=pd.Series()
            plot_data_series_up=start_series_up.append([self.get_row(i,'u') for i in range(start_times,end_times+1)],ignore_index=True)
            plot_data_series_up.plot()
            print('up:',np.mean(calman_python(np.array(plot_data_series_up))))
        if self.down_value.get()==1 :
            start_series_down=pd.Series()
            plot_data_series_down=start_series_down.append([self.get_row(i,'d') for i in range(start_times,end_times+1)],ignore_index=True)
            plot_data_series_down.plot()
            print('down:',np.mean(calman_python(np.array(plot_data_series_down))))
        '''
        last_data=0
        self.empty_ad=int(self.empty_ad_imput.get() or '2000')
        for i,data_tmp in enumerate(plot_data_series):
            gap=np.abs(data_tmp-last_data)
            if i<10:
                last_data=data_tmp+last_data
            elif i==10:
                last_data=last_data//10
            elif gap>150:
                plot_data_series[i]=last_data
            else:
                last_data=data_tmp
            if data_tmp<self.empty_ad:
                plot_data_series[i]=self.empty_ad
        
        sum_plotz_data=plot_data_series.copy()
        self.data_for_ad=(sum_plotz_data-self.empty_ad)/1000
        print(sum(self.data_for_ad))
        print(np.var(plot_data_series))
        '''
        #plt.plot(plot_data_series,'ko')
        plt.show()
    def get_row(self,times,updown):
        row=self.pro_data.ix[times,:data_number+1].ix[updown]#return series,非副本，只是视图,从times从1开始，因为pro_data中行0为列名
        #self.datalen=len(row)
        #print(row)
        return row   

    def adsum(self):
        self.empty_ad=int(self.empty_ad_imput.get() or '2000')/1000
        self.data_for_ad=self.pro_data.copy()/1000
        self.data_for_ad[self.data_for_ad<self.empty_ad]=self.empty_ad
        #print(self.data_for_ad)
        self.data_for_ad=self.data_for_ad-self.empty_ad
        print(self.data_for_ad)
        ad_sum=0
        #print(type(self.data_for_ad.shape[0]))
        for i in range(1,self.data_for_ad.shape[0]//2+1):#//强制整形，/的话会转换位float
            ad_sum+=self.data_for_ad.ix[i,:data_number+1].ix['u'].sum()
            #ad_sum+=self.data_for_ad.ix[i,:1025].ix['d'].sum()
        print('空管值：',self.empty_ad,'ad总和',ad_sum)

    def addflow(self):#统计各个文件流量，写入数据，画出曲线，拟合
        curdir=os.path.dirname(self.filename or 'C:/Users/weihao/Desktop/6.16/test1.csv')
        filenumber_start=int(self.folw_start_input.get() or '12')
        filenumber_end=int(self.folw_end_input.get() or '23')
        x=[]
        for i in range(filenumber_start,filenumber_end+1):
            # self.filename=os.path.normpath(os.path.join(curdir,'test'+str(i)+'.csv'))#os.path.normcase(path)转换path的大小写和斜杠os.path.normpath(path)规范path字符串形式
            # self.filename_lable.set(self.filename)
            if i not in [16,18,21]:#去除坏点
                flow_filename=os.path.normpath(os.path.join(curdir,'test'+str(i)+'.csv'))
                flow_ori_data=pd.read_csv(flow_filename,error_bad_lines=False,index_col=[0,1],header=None,skiprows=[0])
                flow_pro_data=flow_ori_data.fillna(method='ffill',axis=1).ix[:,0:data_number+1]

                sum_flow=self.my_corr_file(flow_pro_data,1,flow_pro_data.shape[0]//2)
                x.append(sum_flow)
                print('test'+str(i),':',sum_flow)
        #y=[6.4,3.1,1.1,2.3,2.2,3,3.2,3.5,5,2.1,1.9]
        y=[6.4,3.1,1.1,2.3,3,3.5,5,2.2,1.9]
        z1=np.polyfit(x,y,1)#得到点列表，最后的数字代表多项式次数
        p1 = np.poly1d(z1)#得到公式
        print(p1)
        #计算拟合相关度
        huigui=0
        allpinggang=0
        cancha=0
        for i,number in enumerate(y):
            allpinggang=allpinggang+number**2
            cancha=cancha+(number-p1(x[i]))**2#p1公式直接代入x，p1()
            print('真值：',number,' 拟合值：',p1(x[i]),' 差值：',number-p1(x[i]),' 比例：',(number-p1(x[i]))/number)
        rpingfang=(allpinggang-cancha)/allpinggang
        print(rpingfang)
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
    def my_corr_file(self,data,start_times,end_times):
        sum_pipe=0
        last_time=200
        for i in range(start_times,end_times+1):
                u_data_origin=data.ix[i,:data_number+1].ix['u']
                d_data_origin=data.ix[i,:data_number+1].ix['d']
                                  
                u_data_calman=calman_python(np.array(u_data_origin))
                d_data_calman=calman_python(np.array(d_data_origin))
                #下面用的是减去平均值的普通处理
                u_data_corr=u_data_calman-np.mean(u_data_calman)
                d_data_corr=d_data_calman-np.mean(d_data_calman)
                #下面用归一化数据处理
                # u_data_corr=(u_data_calman-np.min(u_data_calman))/(np.max(u_data_calman)-np.min(u_data_calman))
                # d_data_corr=(d_data_calman-np.min(d_data_calman))/(np.max(d_data_calman)-np.min(d_data_calman))
                # print(u_data_corr)
                
                c=np.correlate(u_data_corr,d_data_corr,'same')#算出的值为总长除以二加上延迟
                max_index = np.argmax(c)
                time=np.fabs(max_index-data_number//2)
                dense=np.mean(u_data_calman)
                #print(i,' time:',time,' dense:',dense,'\n')
                if(time < 100 and time>3):
                    sum_pipe=sum_pipe+(dense)/(time)
                    last_time=time
                if(time==0 and last_time <100 and last_time >3):
                    sum_pipe=sum_pipe+(dense)//(time)
                    continue
                last_time=200
        return sum_pipe
    
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
                    time=np.fabs(max_index-data_number//2)
                    dense=np.mean(u_data_calman)
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
            print('time:',max_index-data_number//2,'\n')
            print('dense_calmanbefore:',np.mean(u_data_calman),'dense_after',np.mean(u_data_origin),'\n')
            plt.show()            


app = Application()
# 设置窗口标题:
app.master.title('coal_data_handle_calman')
# 主消息循环:
app.mainloop()