#Code by GVV Sharma
#Jan 12, 2019
#Released under GNU GPL
#Lagrange Multipliers
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex
from coeffs import *

#Line parameters
n =  np.array([3,-4]) 
c = 26
P = np.array([3,-5]) 

#A,B = line_icepts(n,c)
#m = omat@n
#Plotting the circle
x = P[0]*np.ones(8)
y = P[1]*np.ones(8)
rmin =0.6*10
r = np.arange(8)*rmin/6
#/np.sqrt(2)
phi = np.linspace(0.0,2*np.pi,100)
na=np.newaxis
# the first axis of these arrays varies the angle, 
# the second varies the circles
x_line = x[na,:]+r[na,:]*np.sin(phi[:,na])
y_line = y[na,:]+r[na,:]*np.cos(phi[:,na])
ax=plt.plot(x_line,y_line,'-')

#Plotting the line
k = np.array([5,30])
print(k)
x_AB=line_norm_eq(n,c,k)
#x1 = np.linspace(0,10,100)
#x2 = (c*np.ones(100) - n[1]*x1)/n[0]
#bx=plt.plot(x1,x2,label="$x_1+x_2-9=0$")
bx=plt.plot(x_AB[:,0],x_AB[:,1],label="$x_1+x_2-9=0$")
plt.axis('equal')
plt.grid()
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.legend([ax[5], bx[0]],['$(x_1-8)^2+(x_2- 6)^2=\\frac{25}{2}$','$x_1+x_2-9=0$'], loc='best')

#if using termux
plt.savefig('./figs/concirc.pdf')
plt.savefig('./figs/concirc.eps')
subprocess.run(shlex.split("termux-open ./figs/concirc.pdf"))
#else
#plt.show()









