import numpy as np
import matplotlib.pyplot as plt

#Point of intersection
A = np.array([[1,-1],[2,1]])
B = np.transpose(np.array([1,3]))
O = np.dot(np.linalg.inv(A),B)

#Finding radius
P = np.transpose(np.array([1,-1]))
r = np.linalg.norm(O-P)

#Intersection plot
x = np.linspace(-3,5,10000)
y = x - 1
z = 3 - 2*x
plt.axis('equal')
plt.plot(x,y,label = '$y - x + 1 = 0$')
plt.plot(x,z,label = '$y + 2x = 3$')
plt.grid()

theta = np.linspace(0,2*np.pi,100)
x = r*np.cos(theta) + 4.0/3
y = r*np.sin(theta) + 1.0/3

r = 3 - 4*x
s = -(3 + x)/4.0
t = 3*x - 4
u = (x - 4)/3.0

plt.plot(x,y)
plt.plot(x,r,label = '$y + 3x = 3$')
plt.plot(x,t,label = '$y - 3x + 4 = 0$')
plt.plot(x,u,label = '$3y - x + 4 = 0$')
plt.plot(x,s,label = '$4y + x + 3 = 0$')

plt.axis([-3,5,-3,3],'equal')
plt.legend()
plt.savefig('../figs/ee16b1022.eps')
plt.show()

