#This program draws the triangle ABC
import numpy as np
import matplotlib.pyplot as plt


def slope_coeff(A,B):
	p = np.zeros((2,1))
	p[0] = (A[1]-B[1])/(A[0]-B[0])
	p[1] = (A[0]*B[1]-A[1]*B[0])/(A[0]-B[0])
	return p

A = np.matrix('-2;-2')
B = np.matrix('1;3')
C = np.matrix('4;-1')

x = np.linspace(np.asscalar(A[0]), np.asscalar(B[0]),50)
p = slope_coeff(A,B)
y = p[0]*x + p[1]
plt.plot(x,y,label='$5x-3y+4=0$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
    
x = np.linspace(np.asscalar(B[0]), np.asscalar(C[0]),50)
p = slope_coeff(B,C)
y = p[0]*x + p[1]
plt.plot(x,y,label='$4x+3y-13=0$')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')

x = np.linspace(np.asscalar(C[0]), np.asscalar(A[0]),50)
p = slope_coeff(C,A)
y = p[0]*x + p[1]
plt.plot(x,y,label='$x-6y-10=0$')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')




plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
#plt.savefig('../figs/triangle.eps')
plt.show()
