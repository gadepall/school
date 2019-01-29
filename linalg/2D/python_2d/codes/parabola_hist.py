import numpy as np
import matplotlib.pyplot as plt
 
#x = np.linspace(0,1,20)
#y = np.sqrt(x)
#plt.plot(x,y,'r')
#plt.stem(x,y)
#plt.savefig('../figs/parabola_area.eps')
n = 20
x = np.linspace(0,1,n)
y = x**2
plt.plot(x,y,'r')
plt.stem(x,y)
#plt.savefig('../figs/parabola_inverted_area.eps')
plt.show()
