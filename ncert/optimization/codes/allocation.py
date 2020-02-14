#Solution to the allocation problem
import pulp as p
from cvxpy import *
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

#Line parameters
A = np.array(( [3.0, 4.0], [1.0, 0.0 ], [0.0, 1.0 ])).T
print(A)
b = np.array([ 800.0, 0.0, 0.0 ]).reshape((3,-1))

n =  np.array([1,1]).reshape(2,-1)
#P = np.array([20,10]).reshape(2,-1)
a=np.array([10500,9000]).reshape(2,-1)
x = Variable((2,1))
#Cost function
f =  a.T@x
obj = Maximize(f)
#Constraints

constraints = [A.T@x <=b,n.T@x==10]

#solution
Problem(obj, constraints).solve()

print(f.value,x.value)


#profit = p.LpProblem("profit_maximising_problem", p.LpMaximize)
#
#x = p.LpVariable("x", lowBound=0)
#y = p.LpVariable("y", lowBound=0)
#
#profit += 10500 * x + 9000 * y
#profit += x + y == 50
#profit += 20 * x + 10 * y <= 800
#
#print(profit)
#status = profit.solve()
#print(p.LpStatus[status])
#print("Number of hectares in which x is grown:",p.value(x))
#print("Number of hectares in which y is grown:",p.value(y))
#print("Maximum Profit:",p.value(profit.objective))

