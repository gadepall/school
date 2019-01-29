#This program computes the equations of 
#all the medians
import numpy as np
import matplotlib.pyplot as plt

def line_coeff(A,B):
	p = np.zeros((3,1))
	p[0] = A[1]-B[1]
	p[1] = B[0]-A[0]
	p[2] = A[0]*B[1]- A[1]*B[0]
	return p
	
def mid_pt(B,C):
		D = (B+C)/2
		return D
	

A = np. matrix('-2;-2')
B = np. matrix('1;3')
C = np. matrix('4;-1')
D = mid_pt(B,C)
E = mid_pt(C,A)
F = mid_pt(A,B)

#print (D,E,F)

print (line_coeff(A,D))
print (line_coeff(B,E))
print (line_coeff(C,F))




