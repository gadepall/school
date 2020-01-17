import numpy as np
from cvxpy import *

x = Variable((2,1),nonneg=True)

P = np.array([[0],[5]])
V = np.array([[1,0],[0,0]])
U = np.array([[0],[-2]])
I = np.array([[1,0],[0,1]])

f = quad_form(x,I) - 2* P.T@x + P.T@P
constraint = [quad_form(x,V) + U.T@x <= 0]

obj = Minimize(f)

Problem(obj, constraint).solve()

print(f.value,x.value)
