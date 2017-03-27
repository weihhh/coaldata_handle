#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#pyw为后缀名则运行不带控制台

__author__='weizhang'

import tkinter
import tkinter.filedialog#这里要小写，不能用FileDialog，这里主要是matlabplot库对这个有依赖
from tkinter import *
import tkinter.messagebox as messagebox
import os,pandas,matplotlib
import matplotlib.pyplot as plt
import numpy

def get_full_path(test_name='testdata',test_number='1'):    
    curdir=os.path.dirname(os.path.realpath(__file__))
    current_file=test_name+test_number+'.csv'
    full_current_file=os.path.join(curdir,current_file)
    return full_current_file


def get_row(times,updown):
    if updown=='u':
        times=2*times-2
    else:
        times=2*times-1
    row=self.data.iloc[times].values
    #print(row)
    datalen=len(row)
    #print(datalen)
    row=self.data.iloc[times,:datalen-1].values#iloc根据位置选取，【行，列】
    #print(type(row))
    #print(row)
    return row    
    
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.testname='testdata'
        self.testnumber='1'
        self.filename=StringVar()
        self.up_value=IntVar()
        self.down_value=IntVar()
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
        
        self.backButton = Button(self, text='back', command=self.setvar)
        self.backButton.grid(row=6,column=0)#确认输入按钮
        self.nextButton = Button(self, text='next', command=self.setvar)
        self.nextButton.grid(row=6,column=1)#确认输入按钮
        
        
    def set_filename(self):
        self.testname = self.testnameInput.get() or self.testname
        self.testnumber = self.testnumberInput.get() or self.testnumber
        full_current_file=get_full_path(self.testname,self.testnumber)
        self.filename.set(full_current_file)
        self.data=pandas.read_csv(full_current_file,index_col=0,header=None)#关键词变量：sep(str or default ','),index_col代表第几列作为行名，设置列名就同时设置header=None
        
    def make_pic(self):
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
            
            
            
        
        plot_data=pandas.Series(plot_data_array)
        plot_data.plot()
        plt.show()
    
    def get_row(self,times,updown):
        if updown=='u':
            times=2*times-2
        else:
            times=2*times-1
        row=self.data.iloc[times].values.copy()
        #print(row)
        datalen=len(row)
        #print(datalen)
        row=self.data.iloc[times,:datalen-1].values.copy()#iloc根据位置选取，【行，列】
        #print(type(row))
        #print(row)
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