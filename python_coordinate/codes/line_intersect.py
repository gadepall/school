#This program calculates the
#intersection of AD and CF
import numpy as np
import matplotlib.pyplot as plt

def mid_pt(B,C):
		D = (B+C)/2
		return D


def line_intersect(p,q):
	P = np.matrix([[p[0][0],-1],[q[0][0],-1]])
	c = -np.matrix([[p[1][0]],[q[1][0]]])
	return np.linalg.inv(P)*c	



def line_coeff(A,B):
	p = np.zeros((2,1))
	p[0] = (A[1]-B[1])/(A[0]-B[0])
	p[1] = (A[0]*B[1]-A[1]*B[0])/(A[0]-B[0])
	return p

A = np.matrix('-2;-2')
B = np.matrix('1;3')
C = np.matrix('4;-1')

D = mid_pt(B,C)
F = mid_pt(A,B)

p = line_coeff(A,D)
q = line_coeff(C,F)

print(line_intersect(p,q))

