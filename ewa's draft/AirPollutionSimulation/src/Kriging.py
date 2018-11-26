#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 21:43:49 2018

@author: hushmans
"""
from pylab import *
import numpy as np
from pandas import DataFrame, Series
from scipy.spatial.distance import pdist, squareform
 

z = [(1500,2000),(2000,1000, )]
z = np.array( z, dtype=np.float )
z = DataFrame( z, columns=['x','y','thk','por','perm','lperm','lpermp','lpermr'] )

fig, ax = subplots()
ax.scatter( z.x, z.y, c=z.por, cmap='gray' )
ax.set_aspect(1)
xlim(-1500,22000)
ylim(-1500,17500)
xlabel('Easting [m]')
ylabel('Northing [m]')
title('Porosity %')