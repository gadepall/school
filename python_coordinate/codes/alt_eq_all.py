#This program finds the slope equations for
#all the altitudes

import numpy as np
import matplotlib.pyplot as plt

def slope_coeff(A,B):
	p = np.zeros((2,1))
	p[0] = (A[1]-B[1])/(A[0]-B[0])
	p[1] = (A[0]*B[1]-A[1]*B[0])/(A[0]-B[0])
	return p

def alt_coeff(p,A):
	q = np.zeros((2,1))
	q[0] = -1/p[0]
	q[1] = A[1] - q[0]*A[0]
	return q

A = np. matrix('-2;-2')
B = np. matrix('1;3')
C = np. matrix('4;-1')

a = slope_coeff(B,C)
b = slope_coeff(C,A)
c = slope_coeff(A,B)
p = alt_coeff(a,A)
q = alt_coeff(b,B)
r = alt_coeff(c,C)

print (p)
print (q)
print (r)




