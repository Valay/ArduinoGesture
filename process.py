import serial
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation
import numpy as np

# Open up the serial port
ser = serial.Serial('/dev/tty.usbserial-A602TRLO', 9600, timeout=1)

while(ser.read() != '\n'):
    pass
    
    
fig, ax = plt.subplots()
line, = ax.plot((0.5,1,1.5),np.random.rand(3),color='green', linestyle=' ', marker='o',
     markerfacecolor='blue', markersize=12)
ax.set_ylim(-15,15)

#plt.ion()
#plt.show(block=False)

def update_line(hl, new_data, count):
    hl.set_xdata(count)
    hl.set_ydata(x)
    plt.draw()
    
def update(data):
    line.set_ydata(data)
    return line,

def data_gen():
    prevx = 0
    prevy = 0
    prevz = 0
    while True:
        data =  ser.readline()
        #time.sleep(0.001)
        values = data.split(',')
        values[2].strip('\r\n')
        if len(values) != 3:
            continue
        x = float(values[0])
        y = float(values[1])
        z = float(values[2])
        #count = count+ 1
        #update_line(hl,x, count)
        print 'acc values are x = %s, y = %s, z = %s' %(x,y,z)
        #if count == 200:
        #    break
        diffx = x - prevx
        diffy = y - prevy
        diffz = z - prevz
        
        if diffz > 0:
            v = 1
        else:
            v = -1
        prevx = x
        prevy = y
        prevz = z
        z = z/10.6 * v
        if abs(diffx) > 0.7 and abs(diffy) < 1 and abs(diffz) < 1 :
            yield(5*x,0,0)
        elif abs(diffy) > 0.7 and abs(diffx) < 1 and abs(diffz) < 1:
            yield(0,5*y,0)
        elif abs(diffz) > 0.7 and abs(diffy) < 1 and abs(diffx) < 1:
            yield(0,0,5*z)
        else:
            yield(0,0,0)
        #yield (x,y,z)


ani = animation.FuncAnimation(fig, update, data_gen, interval=100)
plt.show()