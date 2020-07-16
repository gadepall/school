#Code by GVV Sharma
#December 7, 2019
#Revised July 15, 2020
#released under GNU GPL
#Functions related to conics

import numpy as np
from params import *
from line.funcs import *

def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

def parab_gen(x1,x2,N):
	x = np.zeros((2,N))
	x[0,:] = np.linspace(x1,x2,N)
	x[1,:] = x[0]**2
	return x

#Directrix of standard parabola
def directrix_gen(x1,x2):
	D = -parab_focus
	m = np.array([1,0])
	x_D = line_dir_pt(m,D,x1,x2)
	return x_D
