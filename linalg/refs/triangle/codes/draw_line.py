#Plotting AB
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

#Function for generating the line AB
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Enter the points A and B
A = np.array([-2,-2]) 
B = np.array([1,3]) 
#Generate the line AB
x_AB=line_gen(A,B)
#Plot the line AB
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')

#Figure details
plt.grid() # minor
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 - 0.1), A[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.xlabel('$x$')
plt.ylabel('$y$')

#if using termux
plt.savefig('../figs/draw_line.pdf')
plt.savefig('../figs/draw_line.eps')
subprocess.run(shlex.split("termux-open ../figs/draw_line.pdf"))
#else
#plt.show()



