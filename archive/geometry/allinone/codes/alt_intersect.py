#This program calculates the orthocentre
import numpy as np
import matplotlib.pyplot as plt


def line_intersect(p,q):
	P = np.column_stack((p[0:2],q[0:2])).transpose()	
	c = -np.row_stack((p[2],q[2]))
	return np.matmul(np.linalg.inv(P),c)


def line_coeff(A,B):
	p = np.zeros((2,1))
	p[0] = (A[1]-B[1])/(A[0]-B[0])
	p[1] = (A[0]*B[1]-A[1]*B[0])/(A[0]-B[0])
	return p

def alt_coeff(p,A):
	q = np.zeros((2,1))
	q[0] = -1/p[0]
	q[1] = A[1] - q[0]*A[0]
	return q

def slope_intersect(a,p):
	a_eq = np.row_stack((a[0], -1,a[1]))
	p_eq = np.row_stack((p[0], -1,p[1]))
	return line_intersect(a_eq,p_eq)

A = np. matrix('-2;-2')
B = np. matrix('1;3')
C = np. matrix('4;-1')

a = line_coeff(B,C)
b = line_coeff(C,A)
c = line_coeff(A,B)
p = alt_coeff(a,A)
q = alt_coeff(b,B)
r = alt_coeff(c,C)


print (slope_intersect(p,q))
print (slope_intersect(q,r))
print (slope_intersect(r,p))

