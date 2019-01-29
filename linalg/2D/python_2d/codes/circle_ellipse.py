#This program draws the triangle ABC
import numpy as np
import matplotlib.pyplot as plt


r = 1
theta = np.linspace(-np.pi,np.pi,50)
x = r*np.cos(theta)
y = r*np.sin(theta)
X = np.row_stack((x,y))
M = np.matrix('3,0;0,2')
Y = M*X
x1 = np.array(Y)[0]
y1 = np.array(Y)[1]

plt.plot(x1,y1)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axis('equal')
#plt.savefig('../figs/ellipse_transform.eps')
plt.show()


