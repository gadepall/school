import numpy as np


def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B))

A = np.array([-2,-2]) 
B = np.array([1,3]) 
dvec = np.array([-1,1]) 
omat = np.array([[0,1],[-1,0]]) 
#AB =np.vstack((A,B)).T

#print (dir_vec(A,B))
#print (norm_vec(A,B))



