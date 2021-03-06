#import numpy as np
#import matplotlib.pyplot as plt
#
##data
#x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#y = [3, 2, 5, 7, 4, 2, 4, 6, 7, 8]
#ysize = [10, 20, 4, 15, 9, 9, 14, 8, 4, 9]
#    
#
#for i in range (0, len(x)):
#    plt.plot(x[i], y[i], linestyle="None", marker="o", markersize=ysize[i], color="red")
#    
#plt.plot(x, y, linestyle="dotted", color="red")
#
#
#plt.xlim(np.min(x)-1.3, np.max(x)+1.3) #optional 
#plt.ylim(np.min(y)-1.3, np.max(y)+1.3) #optional 
#
#plt.xlabel("random y")
#plt.ylabel("random x")
#
#plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
line, = ax.plot(np.random.rand(10))
ax.set_ylim(0, 1)

def update(data):
    line.set_ydata(data)
    return line,

def data_gen():
    while True: yield np.random.rand(10)

ani = animation.FuncAnimation(fig, update, data_gen, interval=10)
plt.show()