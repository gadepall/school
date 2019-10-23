#This program calculates the inradius

import numpy as np
import matplotlib.pyplot as plt

def line_coeff(A,B):
	p = np.zeros((2,1))
	p[0] = (A[1]-B[1])/(A[0]-B[0])
	p[1] = (A[0]*B[1]-A[1]*B[0])/(A[0]-B[0])
	return p

def line_dist(I,p):
	return np.abs((I[0]*p[0]-I[1]+p[1])/(np.sqrt(p[0]**2+1)))

I = np. matrix('1.15;0.14')
A = np. matrix('-2;-2')
B = np. matrix('1;3')
C = np. matrix('4;-1')

AB = line_coeff(A,B)
BC = line_coeff(B,C)
CA = line_coeff(C,A)


print(line_dist(I,AB))
print(line_dist(I,BC))
print(line_dist(I,CA))



