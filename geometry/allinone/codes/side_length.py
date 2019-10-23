#This program calculates the distance between
#two points
import numpy as np
import matplotlib.pyplot as plt


def side_length(A,B):
	return np.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)

A = np. matrix('-2;-2')
B = np. matrix('1;3')
C = np. matrix('4;-1')

print (side_length(A,B))
print (side_length(B,C))
print (side_length(C,A))

