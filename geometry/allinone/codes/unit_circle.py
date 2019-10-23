#This program draws the unit circle
import numpy as np
import matplotlib.pyplot as plt


r = 1
theta = np.linspace(-np.pi,np.pi,50)
x = r*np.cos(theta)
y = r*np.sin(theta)

plt.plot(x,y)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axis('equal')
plt.show()


