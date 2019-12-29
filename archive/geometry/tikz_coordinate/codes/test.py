import numpy as np
import matplotlib.pyplot as plt


def line_seg(x1, y1, x2, y2):
	a = y1-y2
	b = x2-x1
	c = x1*y2-x2*y1
	return a, b, c 


x1 = -1
y1 = 0
x2 = 1
y2 = 2.5
x3 = 4
y3 = 1


a1, b1, c1 = line_seg(x1, y1, x2, y2) #AB
a2, b2, c2 = line_seg(x2, y2, x3, y3) #BC
a3, b3, c3 = line_seg(x3, y3, x1, y1) #CA

ABx = np.linspace(x1,x2,50)
ABy = -a1/b1*ABx-c1/b1
BCx = np.linspace(x2,x3,50)
BCy = -a2/b2*BCx-c2/b2
CAx = np.linspace(x3,x1,50)
CAy = -a3/b3*CAx-c3/b3

plt.plot(ABx,ABy)
plt.plot(BCx,BCy)
plt.plot(CAx,CAy)

plt.plot(x1,y1,'o')#A
plt.text(x1-0.2,y1+0.1,'A')#A
plt.plot(x2,y2,'o')#B
plt.text(x2-0.2,y2+0.1,'B')#B
plt.plot(x3,y3,'o')#C
plt.text(x3-0.2,y3+0.1,'C')#C


##ellipse
#t = np.linspace(-np.pi,np.pi,100)
#p = 2*np.sqrt(3)
#q = 4
#x = p*np.cos(t)
#y = q*np.sin(t)
#e = np.sqrt(1 - (p/q)**2)

#plt.plot(x,y)
#plt.grid()
#plt.axis('equal')
#plt.plot(0,q*e,'o')
#plt.plot(0,-q*e,'o')
#plt.text(0,(q*e)-0.6,'F1')
#plt.text(0,(-q*e)+0.2,'F2')

##hyperbola
#b = 2
#a = np.sqrt(5)

#x = np.linspace(-4,4,100)
#y1 = b*np.sqrt((x/a)**2 + 1)
#y2 = -b*np.sqrt((x/a)**2 + 1)

#plt.plot(x,y1)
#plt.plot(x,y2)
#plt.plot(np.sqrt(5),2*np.sqrt(2),'o')
#plt.plot(np.sqrt(10),2*np.sqrt(3),'o')
#plt.plot(5,2*np.sqrt(3),'o')
#plt.text(np.sqrt(5),2*np.sqrt(2)-0.55,'A')
#plt.text(np.sqrt(10)+0.2,2*np.sqrt(3)-0.2,'B')
#plt.text(5+0.2,2*np.sqrt(3)-0.2,'C')
#plt.savefig('problem 24.eps',format = 'eps')
plt.show()
