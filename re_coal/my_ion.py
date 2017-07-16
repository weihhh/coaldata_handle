import matplotlib.pyplot as plt
import numpy as np


t=[]
v=[]
plt.ion()
fig = plt.figure()
ax1 = fig.add_subplot(111)
line, = ax1.plot(t, v, linestyle="-", color="r")
ys = np.random.normal(100, 10, 1000)


def p(a, b):
    t.append(a)
    v.append(b)
    ax1.set_xlim(min(t), max(t) + 1)
    ax1.set_ylim(min(v), max(v) + 1)
    line.set_data(t, v)
    plt.pause(0.001)
    ax1.figure.canvas.draw()

for i in range(len(ys)):
    p(i, ys[i])
    
plt.ioff()
plt.show()