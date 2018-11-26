#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 15:18:36 2018

@author: hushmans
"""

import numpy as np
from matplotlib import pyplot as plt


class Model(object):
    def __init__(self, sill=None, range=None, nugget=None):
        self.sill = float(sill)
        self.range = float(range)
        self.nugget = float(nugget)
        if self.nugget < 0:
            self.nugget = 0
        self.func = np.vectorize(self.f)
        self.variance = 0

    def f(self, h):
        return 0

    def __cmp__(self, other):
        return cmp(self.variance, other.variance)

    def residual(self, params, dist, svar):
        self.dist = dist
        self.svar = svar
        self.sill, self.range, self.nugget = params
        if self.nugget < 0:
            self.nugget = 0
        if self.nugget > self.sill:
            self.nugget = self.sill
        err = self.svar - self.func(self.dist) #Reals variances less computed variances
        return err

    def plot(self):
        h = np.arange(0, np.max(self.dist), 0.1)
        v = self.func(h)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(h, v, 'r-')
        ax.plot(self.dist, self.svar, 'bo')
        plt.legend(['Fit', 'True'])
        plt.xlabel("distance")
        plt.ylabel("semivariance")
        plt.title("SemiVariogram\n %.1f*%s(%.1f)+%.1f"%(self.sill,
        self.range, self.nugget))

    def getCorrectedSill(self):
        return self.nugget + self.sill

    corrected_sill = property(getCorrectedSill)


class Spherical(Model):
    def __init__(self, sill=None, range=None, nugget=None):
        super(Spherical, self).__init__(sill, range, nugget)

    def f(self, h):
        if self.range <= h:
            return self.nugget + self.sill
        else:
            range = float(h)/self.range
            return (self.nugget + self.sill*( (1.5*range) - (0.5*(range**3))))