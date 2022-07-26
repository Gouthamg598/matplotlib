# To install matplotlb pakages run the command in terminal windoww
# pip install matplotlib


''' matplotlib used for data visualiztiion it is low level data visualization'''

import matplotlib.pyplot as plt
a=[80,60,90,70,56,32]
b=[20,60,86,69,75,63]
plt.bar(a,b,color='maroon')
plt.title('abcd')
plt.show()

import numpy as np
print(np.__version__)#1.22.2
import matplotlib as mp
print(mp.__version__)#3.5.2

import numpy as np
a=np.array(55)
print(a.ndim)# dimensions 0
b=np.array([55])
print(b.ndim)#1
c=np.array([55,6,3,6,6,7,8,77])
print(c.ndim)#1

c=np.array([[55,6,8,77],[7,8,5,6]])
print(c.ndim)#2

c=np.array([[[55,6,8,77],[7,8,5,6]],[[78,4,9,88],[9,8,7,65]]])
print(c.ndim)#3

import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,10])
y=np.array([11,20])
plt.plot(x,y)
plt.show()
x=np.array([1,9])
y=np.array([5,9])
plt.plot(x,y,'o') #point with round shape
plt.plot(x,y,'s')#square shape points
plt.plot(x,y,'p')#pentgon shape
plt.plot(x,y,'h')#hexagon shape
plt.plot(x,y)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,5,10,23,25])
y=np.array([10,18,11,19,22])
# plt.plot(x,y,'p')
plt.plot(x,y,marker='p')
plt.plot(x,y,'s:k')# (s)-square points,(:)-dotted lines,(k)-black color
plt.plot(x,y,'s:c')#dotted lines with light blue color
plt.plot(x,y,'s:y')#dotted lines with yellow color
plt.plot(x,y,'s:w')#white color graph
plt.plot(x,y,'s--b')# small lines  blue color d
plt.plot(x,y,'s--r')# red color small lines
plt.plot(x,y,'s--g')#green color small lines
plt.plot(x,y,'s--m')#violet color small lines
plt.plot(x,y,'s-.m')#violet color small lines with dots
plt.plot(x,y,'s-.g',ms=10,mec='r',mfc='y')#ms=marker size,mec=marker edge (border) color red ,mfc=marker font color yellow
plt.plot(x,y,ls='dotted') #dotted
plt.plot(x,y,ls='dashed') #dashed
plt.plot(x,y,ls='none') 
plt.plot(x,y,ls='solid',lw='5') #ls--line style,lw-line width
plt.plot(x,y,ls='solid',lw='2') 
plt.show()



import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,5,10,23,25])
y=np.array([10,18,11,19,22])
font1={'family':'TimesNewRoman','color':'blue','size':'20'}
font2={'family':'Arial','color':'darkred','size':'15'}
plt.title('course',fontdict=font2)
plt.xlabel('python',fontdict=font1)
plt.ylabel('java',fontdict=font1)
plt.plot(x,y)
plt.show()
print(dir(plt))

import matplotlib
print(dir(matplotlib))
