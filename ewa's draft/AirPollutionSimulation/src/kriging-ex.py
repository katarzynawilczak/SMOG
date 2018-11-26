#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:11:25 2018

@author: hushmans
"""

from __future__ import division 
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as LA

def SK(x,y,v,variogram,grid):
    cov_ang = np.zeros((x.shape[0],x.shape[0]))
    cov_dist = np.zeros((x.shape[0],x.shape[0]))
    K = np.zeros((x.shape[0],x.shape[0]))
    for i in xrange(x.shape[0]-1):
        cov_ang[i,i:]=np.arctan2((y[i:]-y[i]),(x[i:]-x[i]))
        cov_dist[i,i:]=np.sqrt((x[i:]-x[i])**2+(y[i:]-y[i])**2)
    for i in xrange(x.shape[0]):
        for j in xrange(x.shape[0]):
            if cov_dist[i,j]!=0:
                amp=np.sqrt((variogram[1]*np.cos(cov_ang[i,j]))**2+(variogram[0]*np.sin(cov_ang[i,j]))**2)
                K[i,j]=v[:].var()*(1-np.e**(-3*cov_dist[i,j]/amp))
    K = K + K.T

    for i in xrange(grid.shape[0]):
        for j in xrange(grid.shape[1]):
             distancias = np.sqrt((i-x[:])**2+(j-y[:])**2)
             angulos = np.arctan2(i-y[:],j-x[:])
             amplitudes = np.sqrt((variogram[1]*np.cos(angulos[:]))**2+(variogram[0]*np.sin(angulos[:]))**2)
             M = v[:].var()*(1-np.e**(-3*distancias[:]/amplitudes[:]))
             W = LA.solve(K,M)
             grid[i,j] = np.sum(W*(v[:]-v[:].mean()))+v[:].mean()
    return grid

np.random.seed(123433789) # GIVING A SEED NUMBER FOR THE EXPERIENCE TO BE REPRODUCIBLE
grid = np.zeros((100,100),dtype='float32') # float32 gives us a lot precision
x,y = np.random.randint(0,100,10),np.random.randint(0,100,10) # CREATE POINT SET.
v = np.random.randint(0,10,10) # THIS IS MY VARIABLE

grid = SK(x,y,v,(50,30),grid)
plt.imshow(grid.T,origin='lower',interpolation='nearest',cmap='jet')
plt.scatter(x,y,c=v,cmap='jet',s=120)
plt.xlim(0,grid.shape[0])
plt.ylim(0,grid.shape[1])
plt.grid()
plt.show()