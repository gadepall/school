#Gradient Descent
#Least Squares
import numpy as np 

c = 2
cur_w = np.array([[1.0],[1.0]]) # The algorithm starts at x=1
gamma = 0.01 # step size multiplier
precision = 1e-6
previous_step_size = 1 
max_iters = 10000 # maximum number of iterations
iters = 0 #iteration counter

X = np.array([[1.0,0.0],[1.0,1.0],[1.0,2.0]])
y = np.array([[6.0],[0.0],[0.0]])

df = lambda x, y, w: (-2.0*np.matmul(x.T,(y-np.matmul(x,w))))

while (previous_step_size > precision) & (iters < max_iters):
    prev_w = cur_w
    cur_w -= gamma * df(X,y,prev_w)
    previous_step_size = np.linalg.norm(cur_w - prev_w)
    iters+=1

# equation for least squares
least_squares = np.matmul(np.linalg.inv(np.matmul(X.T,X)),(np.matmul(X.T,y)))

print("The local minimum occurs at(gradient Descent)\n", cur_w)
print("Least squares method\n", least_squares )