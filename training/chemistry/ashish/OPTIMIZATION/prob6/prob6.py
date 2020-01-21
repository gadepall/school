#QCQP example
import cvxpy as cvx
from numpy import matrix, round, eye

#Create Variable
vect = cvx.Variable((2))

#Create constant vectors/matrices
P = matrix([[1,-1],[-1,1]])
Q = matrix([[0,0],[0,1]])
q = matrix([[1,0]])
c = 2;

#Define the problem
f =  0.5*cvx.quad_form(vect, P)
obj = cvx.Minimize(f)
constraints = [cvx.quad_form(vect, Q) - q*vect + c <= 0]
# #solution
cvx.Problem(obj, constraints).solve()
print ("Minimum of f(x) is ",round((f.value)**(0.5),2),"at X=", vect.value )

