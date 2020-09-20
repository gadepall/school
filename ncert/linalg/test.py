import numpy as np

a = 12
b = 7
c = -10
d = 13
e = 45
f = -35
#a = 6
#b = 17
#c = 12
#d = 22
#e = 31
#f = 20

V = np.array(([a, b/2],[b/2,c]))
u = 0.5*np.array(([d, e]))
ucol = u[:, np.newaxis]
X = np.block([[V,ucol],[u,f]])

mat = f*V - np.outer(u,u)


print(u@np.linalg.inv(V)@u-f)
print(np.linalg.det(X))
print(np.linalg.det(mat))
#print(np.linalg.det(np.eye(2)))
