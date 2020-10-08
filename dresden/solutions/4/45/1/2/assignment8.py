#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:10:44 2020

@author: shantanu
"""

import numpy as np

A=np.array([[1,0], [0,1], [1/2,3/4]])
b=np.matrix([[3], [-2], [0]])

u,s,v=np.linalg.svd(A)
#print(u)
#print(s)
#print(v)
sinv=1./s
S=np.zeros(A.shape)
Sinv=S.T
Sinv[:2,:2]=np.diag(sinv)
Aplus=v.T.dot(Sinv).dot(u.T)
x=Aplus.dot(b)
print(x)
