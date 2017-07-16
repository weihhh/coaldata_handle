import time,sys#注意这里的程序，如果print函数是不已\n结尾的画则终端不能正确显示打印结果,原因在于缓存刷新机制
 
while(1):
    print('sdf',end='',flush=True)
    #sys.stdout.flush()
    time.sleep(2)
    