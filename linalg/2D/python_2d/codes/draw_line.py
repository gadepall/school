#Code by GVV Sharma
#January 28, 2019
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex
#end if

#Generate line points
def line_dir(m,c):
  len =10
  A = np.array([c,0]) 
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(-5,5,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB


m1 = np.array([-1,1]) 
m2 = np.array([1,3]) 

c1 = 8
c2 = 4

#Generating all lines
line1 = line_dir(m1,c1)
line2 = line_dir(m2,c2)

#fig, ax = plt.subplots()
#Plotting all lines
plt.plot(line1[0,:],line1[1,:],label='$AB$')
plt.plot(line2[0,:],line2[1,:],label='$BC$')

#plt.plot(A[0], A[1], 'o')
#plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
#plt.plot(B[0], B[1], 'o')
#plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
#plt.plot(C[0], C[1], 'o')
#plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
#Customize the major grid
#ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
#plt.grid(which='minor', linestyle='-', linewidth='0.5', color='black')
plt.grid(True, which='both')
plt.minorticks_on
#plt.grid(which='both') # minor

#if using termux
plt.savefig('../figs/draw_line.pdf')
plt.savefig('../figs/draw_line.eps')
subprocess.run(shlex.split("termux-open ../figs/draw_line.pdf"))
#else
#plt.show()







