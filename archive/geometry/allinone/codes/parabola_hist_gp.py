import numpy as np
import matplotlib.pyplot as plt
 
n = 10
r = 0.8
temp = [ r ** (k - 1) for k in range(1, n + 1)]
x = np.array(temp)
y = x**2
plt.plot(x,y,'r')
plt.stem(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('../figs/parabola_area_gp.eps')
plt.show()
