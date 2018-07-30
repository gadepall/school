#This program calculates the equations of
#all the sides of the triangle
import numpy as np
import matplotlib.pyplot as plt

def line_coeff(A,B):
	p = np.zeros((3,1))
	p[0] = A[1]-B[1]
	p[1] = B[0]-A[0]
	p[2] = A[0]*B[1]- A[1]*B[0]
	return p

A = np. matrix('-2;-2')
B = np. matrix('1;3')
C = np. matrix('4;-1')

print (line_coeff(A,B))
print (line_coeff(B,C))
print (line_coeff(C,A))


