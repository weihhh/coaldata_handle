import matplotlib.pyplot as plt
plt.ion()    # 打开交互模式
# 同时打开两个窗口显示图片
plt.figure()
plt.imshow(i1)
plt.figure()
plt.imshow(i2)
# 显示前关掉交互模式
plt.ioff()
plt.show()