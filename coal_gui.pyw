#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#pyw为后缀名则运行不带控制台

__author__='weizhang'

from tkinter import *
import tkinter.messagebox as messagebox
import os,pandas,matplotlib
import matplotlib.pyplot as plt
import numpy

def get_full_path(test_name='port',test_number='1'):    
    curdir=os.path.dirname(os.path.realpath(__file__))
    current_file=test_name+test_number+'.csv'
    full_current_file=os.path.join(curdir,current_file)
    return full_current_file


  

def pre_proceed(data):
    pjz=numpy.mean(data)
    bzc=numpy.std(data)
    data1=numpy.where(data<pjz+2*bzc,data,pjz)
    data2=numpy.where(data1>pjz-2*bzc,data1,pjz)#两倍方差效果很好，三倍会有数据出错    
    return data2

    
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.testname='port'
        self.testnumber='3'
        self.filename=StringVar()
        self.up_value=IntVar()
        self.down_value=IntVar()
        self.corr_multi=IntVar()
        self.createWidgets()
        
    def createWidgets(self):        
        
        
        self.noteLabel1 = Label(self, text='1.input your testname here !')
        self.noteLabel1.grid(row=0,sticky=W)#提示测试名称标签
        self.testnameInput = Entry(self)
        self.testnameInput.grid(row=0,column=1)#测试名称输入框
        
        self.noteLabel2 = Label(self, text='2.input your testnumber here !')
        self.noteLabel2.grid(row=1,sticky=W)#提示测试编号标签
        self.testnumberInput = Entry(self)
        self.testnumberInput.grid(row=1,column=1)#测试编号输入框
        
        self.confirmButton1 = Button(self, text='ok', command=self.set_filename)
        self.confirmButton1.grid(row=1,column=2)#确认测试文件名按钮
        
        
        self.noteLabel3=Label(self)
        self.noteLabel3['textvariable']=self.filename        
        self.noteLabel3.grid(row=2,sticky=W)#显示当前读取文件名
        
        self.noteLabel4=Label(self,text='3.choose up or down datapath,only one')
        self.noteLabel4.grid(row=3,sticky=W)
        self.up_choose=Checkbutton(self,text='choose up ',variable=self.up_value)
        self.down_choose=Checkbutton(self,text='choose down ',variable=self.down_value)
        self.up_choose.grid(row=3,column=1)
        self.down_choose.grid(row=3,column=2)
        
        self.noteLabel5 = Label(self, text='4.input the row you want !')
        self.noteLabel5.grid(row=4,sticky=W)#提示标签
        self.start_rowInput = Entry(self)
        self.start_rowInput.grid(row=5)#输入框
        self.end_rowInput = Entry(self)
        self.end_rowInput.grid(row=5,column=1)#输入框
        self.confirmButton2 = Button(self, text='ok', command=self.make_pic)
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
        
        
        
        
        
        self.noteLabel7 = Label(self, text='welcome!')
        self.noteLabel7.grid(row=8,sticky=W)#提示标签
        
        # self.backButton = Button(self, text='back', command=self.setvar)
        # self.backButton.grid(row=6,column=0)#确认输入按钮
        # self.nextButton = Button(self, text='next', command=self.setvar)
        # self.nextButton.grid(row=6,column=1)#确认输入按钮
        
        
    def set_filename(self):
        self.testname = self.testnameInput.get() or self.testname
        self.testnumber = self.testnumberInput.get() or self.testnumber
        full_current_file=get_full_path(self.testname,self.testnumber)
        self.filename.set(full_current_file)
        self.data=pandas.read_csv(full_current_file,index_col=0,header=None)#关键词变量：sep(str or default ','),index_col代表第几列作为行名，设置列名就同时设置header=None
        
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
                    
                    u_data_corr=u_data_origin-numpy.mean(u_data_pre)
                    d_data_corr=d_data_origin-numpy.mean(d_data_pre)
                    
                    c=numpy.correlate(u_data_corr,d_data_corr,'same')#算出的值为总长除以二加上延迟
                    max_index = numpy.argmax(c)
                    print(i,':',max_index-512)
                    f.write(str(max_index-512)+',')
                    if i==end_times:
                        f.write('\n')
                
        else:            
            u_data_origin=self.get_row(start_times,'u')
            d_data_origin=self.get_row(start_times,'d')

            u_data_pre=pre_proceed(u_data_origin)
            d_data_pre=pre_proceed(d_data_origin)
            
            u_data_origin_s=pandas.Series(u_data_origin)
            d_data_origin_s=pandas.Series(d_data_origin)            
            u_data_pre_s=pandas.Series(u_data_pre)#series才有plot函数，将get_row取得的array转换为series
            d_data_pre_s=pandas.Series(d_data_pre)
            
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
            u_data_corr=u_data_origin-numpy.mean(u_data_pre)
            d_data_corr=d_data_origin-numpy.mean(d_data_pre)
            # print(u_data,d_data)

            c=numpy.correlate(u_data_corr,d_data_corr,'same')#算出的值为总长除以二加上延迟
            max_index = numpy.argmax(c)
            print('corr:',max_index-512)
            corr_s=pandas.Series(c)
            plt.figure(2)
            plt.subplot(211)
            u_data_origin_s.plot()
            plt.hold
            d_data_origin_s.plot()
            plt.subplot(212)
            corr_s.plot()            
            plt.show()

        
    
    
    def make_pic(self):
        #从这开始做根据设置的范围取出数据
        start_times=int(self.start_rowInput.get() or '1')
        if self.up_value.get()==1 and self.down_value.get()!=1 :
            
            self.current_up_row=self.get_row(start_times,'u')
        if self.down_value.get()==1:
            self.current_up_row=self.get_row(start_times,'d')
        #self.previous_row=self.current_row.copy()
        plot_data_array=self.current_up_row#self.current_row=pandas.Series(self.current_row)这样子的程序没有用，无法改变类型
        #self.current_up_row=b
        #print(type(self.current_row))
        if self.end_rowInput.get():
            end_times=int(self.end_rowInput.get())
            if self.up_value.get()==1 and self.down_value.get()!=1:            
                for i in range(start_times+1,end_times+1):
                    self.current_down_row=self.get_row(i,'u')
                    plot_data_array=numpy.concatenate((plot_data_array,self.current_down_row))#注意这里需要结合的两个array需要在一个括号里面
            if self.down_value.get()==1:
                for i in range(start_times+1,end_times+1):
                    self.current_down_row=self.get_row(i,'d')
                    plot_data_array=numpy.concatenate((plot_data_array,self.current_down_row))#注意这里需要结合的两个array需要在一个括号里面
        #完成取出数据plot_data_array    
                               
        plot_data=pandas.Series(plot_data_array)
        plot_data.plot()
        plt.show()
    
    def get_row(self,times,updown):
        if updown=='u':
            times=2*times-2
        else:
            times=2*times-1
        row=self.data.iloc[times].values
        #print(row)
        datalen=len(row)
        print(datalen)
        row=self.data.iloc[times,0:datalen-1].values.copy()#iloc根据位置选取，【行，列从0开始，不取到：后那个数字】
        #print(type(row))
        print(row)
        return row    
    
    def setvar(self):
        
        self.testname = self.testnameInput.get()
        self.testnumber = self.testnumberInput.get() or self.testnumber
        print(self.up_value.get())#checkbutton的值为0或1，通过绑定一个intvar到本身变量
        self.filename.set(self.testname+self.testnumber)
        

app = Application()
# 设置窗口标题:
app.master.title('coal_data_handle')
# 主消息循环:
app.mainloop()