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

def pre_proceed(data):
    pjz=np.mean(data)
    bzc=np.std(data)
    #med_data=np.median(data)
    #print(med_data)
    # print(len(data))
    # for i,number in enumerate(data):
        # print(number)
        # if np.isnan(number):
            # print(i)
    data1=np.where(data<pjz+2*bzc,data,pjz)
    data2=np.where(data1>pjz-2*bzc,data1,pjz)#两倍方差效果很好，三倍会有数据出错,一倍两倍差别不大    
    return data2

    
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
        self.filename_lable.set(self.filename)
        self.ori_data=pd.read_csv(self.filename,error_bad_lines=False,index_col=[0,1],header=None,skiprows=[0])
        del_long=lambda x: x%10000#若碰到四位四位相连的数据，保留后四位
        self.pro_data=self.ori_data.fillna(method='ffill',axis=1).ix[:,0:1025].applymap(del_long)#这里因为将1，2作为index，所以默认就是显示的，ix[:,y:4]中的y不管取0，1都是一样的，共0-5，0-1索引，2-5数据
        print(self.pro_data)

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
        start_series=pd.Series()
        if self.up_value.get()==1 and self.down_value.get()!=1 :        
            plot_data_series=start_series.append([self.get_row(i,'u') for i in range(start_times,end_times+1)],ignore_index=True)
        if self.down_value.get()==1:
            plot_data_series=start_series.append([self.get_row(i,'d') for i in range(start_times,end_times+1)],ignore_index=True)

        plot_data_series.plot()
        plt.show()
    
    def get_row(self,times,updown):
        row=self.pro_data.ix[times,:1025].ix[updown]#return series,非副本，只是视图
        #self.datalen=len(row)
        return row   

                
    def my_corr(self):
        #做互相关，并显示原始数据，处理后数据，相关值获取
        
        start_times=int(self.start_rowInput1.get() or '1')
        end_times=int(self.end_rowInput1.get() or '2')
        if self.corr_multi.get()==1 :
            # print(self.corr_multi)
            with open(r'D:\project\pypro\coaldata_handle\corr_all.csv','a',encoding='utf-8') as f:
                f.write(self.filename.get()+',')
                for i in range(start_times,end_times+1):
                    u_data_origin=self.get_row(i,'u')
                    d_data_origin=self.get_row(i,'d')

                    u_data_pre=pre_proceed(u_data_origin)
                    d_data_pre=pre_proceed(d_data_origin)
                    
                    u_data_corr=u_data_origin-np.max(u_data_pre)
                    d_data_corr=d_data_origin-np.max(d_data_pre)
                    
                    c=np.correlate(u_data_corr,d_data_corr,'same')#算出的值为总长除以二加上延迟
                    max_index = np.argmax(c)
                    print(i,':',max_index-512)
                    f.write(str(max_index-512)+',')
                    if i==end_times:
                        f.write('\n')
                
        else:            
            u_data_origin=self.get_row(start_times,'u')
            d_data_origin=self.get_row(start_times,'d')

            u_data_pre=pre_proceed(u_data_origin)
            d_data_pre=pre_proceed(d_data_origin)
            
            u_data_origin_s=pd.Series(u_data_origin)
            d_data_origin_s=pd.Series(d_data_origin)            
            u_data_pre_s=pd.Series(u_data_pre)#series才有plot函数，将get_row取得的array转换为series
            d_data_pre_s=pd.Series(d_data_pre)
            
            plt.figure(1)
            plt.subplot(221)#行数，列数，当前第几幅图
            u_data_origin_s.plot()
            plt.subplot(223)
            d_data_origin_s.plot()
            plt.subplot(222)
            u_data_pre_s.plot()
            plt.subplot(224)
            d_data_pre_s.plot()
            
            
            
            # print(u_data,d_data)
            u_data_corr=u_data_origin-np.max(u_data_pre)
            d_data_corr=d_data_origin-np.max(d_data_pre)
            # print(u_data,d_data)

            c=np.correlate(u_data_corr,d_data_corr,'same')#算出的值为总长除以二加上延迟
            max_index = np.argmax(c)
            print('corr:',max_index-512)
            corr_s=pd.Series(c)
            plt.figure(2)
            plt.subplot(211)
            u_data_origin_s.plot()
            plt.hold
            d_data_origin_s.plot()
            plt.subplot(212)
            corr_s.plot()            
            plt.show()

        
 

app = Application()
# 设置窗口标题:
app.master.title('coal_data_handle')
# 主消息循环:
app.mainloop()