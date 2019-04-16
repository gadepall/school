import numpy as np
import math
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex
#end if


#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

#defining centre and radius of Circle C1
c=np.array([1,0])
r=2**0.5

#Generating points on the circle
len = 100
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + c).T

#plotting circle C1
plt.plot(x_circ[0,:],x_circ[1,:],label='$C_1$')

ax.plot()
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
#if using termux
plt.savefig('../figs/circle.pdf')
plt.savefig('../figs/circle.eps')
subprocess.run(shlex.split("termux-open ../figs/circle.pdf"))
#else
#plt.show()
