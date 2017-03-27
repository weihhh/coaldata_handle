import os,re

def get_full_path(test_name='port',test_number='1'):    
    curdir=os.path.dirname(os.path.realpath(__file__))
    current_file=test_name+test_number+'.csv'
    full_current_file=os.path.join(curdir,current_file)
    return full_current_file
    
def file_to_iter(filename):
    with open(filename,'r')as f:        
        data_pat=re.compile(r'\[(.*?)\]')
        data_iter=data_pat.finditer(f.read())
        return data_iter

findpath=r'C:\Users\weihao\Desktop\第三次煤粉数据处理\旧管测试\0.5无屏蔽'
newpath=os.path.join(findpath,'python_data')
if not os.path.exists(newpath):
    os.mkdir(newpath)
filenames=os.listdir(findpath)
for filename in filenames:
    if os.path.splitext(filename)[1]=='.txt':
        data_iter=file_to_iter(os.path.join(findpath,filename))        
        csv_filename=os.path.join(newpath,os.path.splitext(filename)[0]+'.csv')
        with open(csv_filename,'w') as f1:
            for index,data in enumerate(data_iter,1):
                if index%2==0:
                    f1.write(str(index//2)+'d,')
                else:
                    f1.write(str((index+1)//2)+'u,')
                data_str_list=data.group(1).split(',')#注意split会将最后逗号后面再分出一个‘’空字符！！！！！！！['1', '2', '3', '']
                # print(data_str_list)
                # print(len(data_str_list))#第一行和第二行为1025，其余1026
                x=(n  for n in data_str_list if n!='')
                if not index==1 and not index==2:#因为原数据格式的第一行和第二行【】中没有d1和d2，所以要设置为1024，其余要设置为1025排除其中的d1和d2
                    rangenumber=1025
                else:
                    rangenumber=1024
                last_data=0
                
                for i in range(rangenumber):
                    try:                                
                        
                        xdata=next(x)
                        if xdata=='d1' or xdata=='d2':
                            continue
                        if not xdata.isdigit():
                            f1.write(last_data+',')
                        else:
                            f1.write(xdata+',')
                            last_data=xdata
                        
                    except:
                        f1.write('0,')
                    if (i==1023 and rangenumber==1024) or (i==1024 and rangenumber==1025):
                        f1.write('\n')