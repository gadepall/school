import numpy as np

a = 6
b = 17
c = 12
d = 22
e = 31
f = 20

V = np.array(([a, b/2],[b/2,c]))
u = 0.5*np.array(([d, e]))
ucol = u[:, np.newaxis]
X = np.block([[V,ucol],[u,f]])

mat = f*V - np.outer(u,u)
#print(np.linalg.det(X))
#print(np.linalg.det(mat))
#print(np.linalg.det(np.eye(2)))
