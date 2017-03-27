#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#存在最后一行不正确的问题，因为有的空了
import os 

def get_full_path(test_name='port',test_number='1'):    
    curdir=os.path.dirname(os.path.realpath(__file__))
    current_file=test_name+test_number+'.csv'
    full_current_file=os.path.join(curdir,current_file)
    return full_current_file
    
def new_sytax(lines):  
    with open(get_full_path(),encoding='utf-8') as f1:
        with open(get_full_path('port','2'),'rt',encoding='utf-8') as f2:
            with open(get_full_path('port','3'),'wt',encoding='utf-8') as f3:    
                for i in range(lines):
                    
                    f3.write(str(i+1)+'u,')
                    f3.write(f1.readline())
                    f3.write(str(i+1)+'d,')
                    f3.write(f2.readline())
                    
new_sytax(1000)                   
                    
    
