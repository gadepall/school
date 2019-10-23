#This program calculates point
#where the angle bisector meets the
#opposite side

import numpy as np
import matplotlib.pyplot as plt

def line_intersect(p,q):
	P = np.column_stack((p[0:2],q[0:2])).transpose()	
	c = -np.row_stack((p[2],q[2]))
	return np.matmul(np.linalg.inv(P),c)

def line_coeff(A,B):
	p = np.zeros((3,1))
	p[0] = A[1]-B[1]
	p[1] = B[0]-A[0]
	p[2] = A[0]*B[1]- A[1]*B[0]
	return p

def side_length(A,B):
	return np.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)

def angle_bisect_coord(b,c,B,C):
	return np.multiply((np.multiply(b,B)+np.multiply(c,C)),1/(b+c))

A = np. matrix('-2;-2')
B = np. matrix('1;3')
C = np. matrix('4;-1')

a = side_length(B,C)
b = side_length(C,A)
c = side_length(A,B)

U = angle_bisect_coord(b,c,B,C)
V = angle_bisect_coord(c,a,C,A)
W = angle_bisect_coord(a,b,A,B)

#AB = line_coeff(A,B)
#BC = line_coeff(B,C)
#CA = line_coeff(C,A)
AU = line_coeff(A,U)
BV = line_coeff(B,V)
CW = line_coeff(C,W)

print(line_intersect(AU,BV))
print(line_intersect(BV,CW))
print(line_intersect(CW,AU))


#print (U)
#print (V)
#print (W)

