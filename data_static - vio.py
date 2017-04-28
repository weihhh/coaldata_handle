import os,re,csv
import numpy as np

def get_full_path(test_name='port',test_number='1'):    
    curdir=os.path.dirname(os.path.realpath(__file__))
    current_file=test_name+test_number+'.csv'
    full_current_file=os.path.join(curdir,current_file)
    return full_current_file
    


findpath=r'C:\Users\weihao\Desktop\第三次煤粉数据处理\旧管测试\0.5无屏蔽\python_data'
newpath=os.path.join(findpath,'python_data_statics')
if not os.path.exists(newpath):
    os.mkdir(newpath)
filenames=os.listdir(findpath)
for filename in filenames:
    pjz_of_row_u=[]
    pjz_of_row_d=[]
    if os.path.splitext(filename)[1]=='.csv':
        with open(os.path.join(findpath,filename),'r') as f:
            csv_file=csv.reader(f)
            data_rowlist=[data for data in csv_file]
            for i,datas in enumerate(data_rowlist):
                nparray=np.array(datas[1:1025]).astype(np.float)
                pjz=np.mean(nparray)
                bzc=np.std(nparray)
                purelist=[i for i in datas[1:1025] if (pjz-2*bzc)<int(i)<(pjz+2*bzc)]
                nparray=np.array(purelist).astype(np.float)                
                if i%2==0:
                    pjz_of_row_u.append(str(np.mean(nparray)))
                if i%2!=0:
                    pjz_of_row_d.append(str(np.mean(nparray)))
                
                
        with open(os.path.join(newpath,'statics.txt'),'a') as f1:        
            nparray=np.array(pjz_of_row_u).astype(np.float)
            pjz=np.mean(nparray)
            f1.write(filename+'\n'+' u: '+','.join(pjz_of_row_u)+'\n')
            f1.write('total:'+str(pjz)+'\n'+'\n')            
            nparray=np.array(pjz_of_row_d).astype(np.float)
            pjz=np.mean(nparray)
            f1.write(' d: '+','.join(pjz_of_row_d)+'\n')
            f1.write('total:'+str(pjz)+'\n'+'\n')
    