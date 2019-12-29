import numpy as np
import matplotlib.pyplot as plt

def slope_coeff(A,B):
	p = np.zeros((2,1))
	p[0] = (A[1]-B[1])/(A[0]-B[0])
	p[1] = (A[0]*B[1]-A[1]*B[0])/(A[0]-B[0])
	return p

A = np. matrix('-2;-2')
B = np. matrix('1;3')
C = np. matrix('4;-1')

print (slope_coeff(A,B))
print (slope_coeff(B,C))
print (slope_coeff(C,A))


