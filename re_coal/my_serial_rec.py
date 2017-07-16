#串口接收,一个bug：如果while循环处开头不打印一个换行，下面的print都不会显示,在有进程挂起的地方都需要强制刷新缓存区
import serial,time
import matplotlib.pyplot as plt
import numpy as np

t=[]
v=[]
i=0
plt.ion()
fig = plt.figure()
ax1 = fig.add_subplot(111)
line, = ax1.plot(t, v, linestyle="-", color="r")
#ys = np.random.normal(100, 10, 1000)

with open('result.csv','at') as f1:    
    with serial.Serial('COM1',115200,timeout=8) as ser:
        while(1):
            #print('scanning',end='')
            s=ser.read(12)
            if s:
                print(s.decode('utf-8'),end='',flush=True)
                f1.write(s.decode('utf-8'))
                f1.flush()
                a=s.decode('utf-8').split(',')
                for x in a:
                    if x:
                        v.append(int(x))
                        t.append(i)
                        i=i+1
                        ax1.set_xlim(min(t), max(t) + 10)
                        ax1.set_ylim(min(v), max(v) + 1)
                        line.set_data(t, v)
                        plt.pause(0.01)
                        ax1.figure.canvas.draw()
                #print(a)
plt.ioff()
plt.show()                