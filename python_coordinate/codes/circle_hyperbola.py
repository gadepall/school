#This program draws a hyperbola
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,50)
y1 = np.sqrt(1+x**2)
y2 = -np.sqrt(1+x**2)

plt.plot(x,y1,x,y2)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axis('equal')
plt.savefig('../figs/circle_hyperbola.eps')
plt.show()


