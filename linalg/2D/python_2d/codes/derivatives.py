import numpy as np

def slope_coeff(A,B):
	p = np.zeros((2,1))
	p[0] = (A[1]-B[1])/(A[0]-B[0])
	p[1] = (A[0]*B[1]-A[1]*B[0])/(A[0]-B[0])
	return p

A = np.matrix('-2;-2')
B = np.matrix('1;3')
p = slope_coeff(A,B)
print(p[0])
X=np.matrix('-0.22;0.96')
I=np.matrix('1.15;0.14')
print(-(X[0]-I[0])/(X[1]-I[1]))




#C=np.matrix('2.43;1.09')
