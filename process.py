import serial
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation
import numpy as np
from pymouse import PyMouse

# Open up the serial port
ser = serial.Serial('/dev/tty.usbserial-A602TS3Y', 9600, timeout=1)

m = PyMouse()

while(ser.read() != '\n'):
    pass
        
print "reading data"
#fig, ax = plt.subplots()
#line, = ax.plot((0.5,1,1.5),np.random.rand(3),color='green', linestyle=' ', marker='o',
#     markerfacecolor='blue', markersize=12)
#ax.set_ylim(-15,15)

#plt.ion()
#plt.show(block=False)

def update_line(hl, new_data, count):
    hl.set_xdata(count)
    hl.set_ydata(x)
    plt.draw()
    
def update(data):
    line.set_ydata(data)
    return line,
    
def integerate(a,b,c):
    return b+( (c-b)/2)
    
def find_average(ser):
    avg_ax = 0
    avg_ay = 0
    avg_az = 0
    count = 0
    while count < 100:
        data =  ser.readline()
        #print data
        data.strip('\n')
        data.strip('\r')
        #time.sleep(0.001)
        values = data.split(',')
        values[2].strip('\r\n')
        if len(values) != 8:
            continue
        avg_ax += float(values[0]) 
        avg_ay += float(values[1]) 
        avg_az += float(values[2])
        count += 2
        
    return (avg_ax/201, avg_ay/201,avg_az/201)
    
posx = 500
posy = 600    
    
def move_gyro_mouse(a,b): 
    global posx
    global posy
    posx += a
    posy += b   
    m.move(posx, posy)
    
def move_mouse(prev_px,prev_py,px,py,button):
    global posx
    global posy
    if(prev_px < px):
        posx -= 80*(px - prev_px)
    else:
        posx += 80*abs(px - prev_px)
    if(prev_py < py):
        posy += 80*(py - prev_py)
    else:
        posy -= 80*abs(py - prev_py)
        
    #print button
    if button == 1:
        #m.press(posy,posx)
        pass
    else:
        #m.release(posy,posx)  
        pass 
    #else:
    
    m.move(posy,posx)
    
    
def data_gen():
    prevx = 0
    prevy = 0
    prevz = 0
    
    max_px = 0
    max_py = 0
    
    min_px = 0
    min_py = 0
    
    avg_ax,avg_ay,avg_az = find_average(ser)
    #print avg_ax,avg_ay,avg_az
    
    
    data =  ser.readline()
    data.strip('\n')
    data.strip('\r')
    #time.sleep(0.001)
    values = data.split(',')
    prev_ax = float(values[0]) - avg_ax
    prev_ay = float(values[1]) - avg_ay
    prev_az = float(values[2]) - avg_az
    
    prev_gx = float(values[3])
    prev_gy = float(values[4])
    prev_gz = float(values[5])
    
    
    prev_vx = 0
    prev_vy = 0
    
    prev_px = 0
    prev_py = 0
    
    #f = open('data.txt','a')
    while True:
        data =  ser.readline()
        #print data
        data.strip('\n')
        data.strip('\r')
        #time.sleep(0.001)
        values = data.split(',')
        values[2].strip('\r\n')
        if len(values) != 8:
            continue
        ax = float(values[0]) #- avg_ax
        ay = float(values[1]) #- avg_ay
        az = float(values[2]) #- avg_az
        
        #print 'acc values are ax = %s, ay = %s, az = %s' %(ax,ay,az)
        #move_gyro_mouse(ay,az)
        
        #continue
        gx = float(values[3])
        gy = float(values[4])
        gz = float(values[5])
        
        button = int(values[7])
        
        #count = count+ 1
        #update_line(hl,x, count)
        
        #print 'acc values are ax = %s, ay = %s, az = %s' %(ax,ay,az)
        #print 'gyro values are gx = %s, gy = %s, gz = %s' %(gx,gy,gz)
        
        #diffx = prev_gx - gx
        #diffy = prev_gy - gy
        #diffz = prev_gz - gz
        #
        #print str(diffx)+'  '+str(diffy)+'  '+str(diffz)
        #if abs(diffx > 100):
        #    if gx > 0:
        #        move_gyro_mouse(5,0)
        #    else:
        #        move_gyro_mouse(-5,0)
        #
        #if abs(diffy > 100):
        #    if gy > 0:
        #        move_gyro_mouse(0,5)
        #    else:
        #        move_gyro_mouse(0,-5)   
                
        #f.write(ax+','+ay+','+az+','+gx+','+gy+','+gz)
        
        vx = integerate(prev_vx, prev_ax, ax)
        px = integerate(prev_px, prev_vx, vx)
        
        vy = integerate(prev_vy, prev_ay, ay)
        py = integerate(prev_py, prev_vy, vy)
        
        if px > max_px:
            max_px = px
        if py > max_py:
            max_py = py
        if px < min_px:
            min_px = px
        if py < min_py:
            min_py = py
        
        #print str(ax)+','+str(ay)+'   '+str(vx)+','+str(vy)+'   '+
        #print str(px)+','+str(py)#+'   '+str(max_px)+','+str(max_py)+'   '+str(min_px)+','+str(min_py)
        
        move_mouse(prev_px,prev_py,px,py,button)
        
        prev_ax = ax
        prev_ay = ay
        
        prev_vx = vx
        prev_vy = vy
        
        prev_px = px
        prev_py = py
        #if count == 200:
        #    break
        #diffx = x - prevx
        #diffy = y - prevy
        #diffz = z - prevz
        #xxxx
        #if diffz > 0:
        #    v = 1
        #else:
        #    v = -1
        #prevx = x
        #prevy = y
        #prevz = z
        #z = z/10.6 * v
        #if abs(diffx) > 0.7 and abs(diffy) < 1 and abs(diffz) < 1 :
        #    yield(5*x,0,0)
        #elif abs(diffy) > 0.7 and abs(diffx) < 1 and abs(diffz) < 1:
        #    yield(0,5*y,0)
        #elif abs(diffz) > 0.7 and abs(diffy) < 1 and abs(diffx) < 1:
        #    yield(0,0,5*z)
        #else:
        #    yield(0,0,0)
        #yield (x,y,z)


data_gen()
#ani = animation.FuncAnimation(fig, update, data_gen, interval=100)
#plt.show()