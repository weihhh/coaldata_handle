#串口助手会省略\00
import serial,time,random

ser=serial.Serial('COM2',115200)
for i in range(1000):
    time.sleep(2)
    data=random.randint(1,100)
    print(data)
    ser.write((str(data)+',').encode('utf-8'))#b'\xe4\xb8'这样是直接发送的十六进制数据,b'hao'这样是发送unicode字节形式编码字节形式
     
ser.close()