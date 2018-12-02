from __future__ import division 
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as LA
from matplotlib.animation import FuncAnimation


def SimpleKriging(x,y,v,variogram,grid):    #SIMPLEKRIGING
    cov_angulos = np.zeros((x.shape[0],x.shape[0]))
    cov_distancias = np.zeros((x.shape[0],x.shape[0]))
    K = np.zeros((x.shape[0],x.shape[0]))
    for i in range(x.shape[0]-1):
        cov_angulos[i,i:]=np.arctan2((y[i:]-y[i]),(x[i:]-x[i]))
        cov_distancias[i,i:]=np.sqrt((x[i:]-x[i])**2+(y[i:]-y[i])**2)
    for i in range(x.shape[0]):
        for j in range(x.shape[0]):
            if cov_distancias[i,j]!=0:
                amp=np.sqrt((variogram[1]*np.cos(cov_angulos[i,j]))**2+(variogram[0]*np.sin(cov_angulos[i,j]))**2)
                K[i,j]=v[:].var()*(1-np.e**(-3*cov_distancias[i,j]/amp))
    K = K + K.T

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
             distancias = np.sqrt((i-x[:])**2+(j-y[:])**2)
             angulos = np.arctan2(i-y[:],j-x[:])
             amplitudes = np.sqrt((variogram[1]*np.cos(angulos[:]))**2+(variogram[0]*np.sin(angulos[:]))**2)
             M = v[:].var()*(1-np.e**(-3*distancias[:]/amplitudes[:]))
             W = LA.solve(K,M)
             grid[i,j] = np.sum(W*(v[:]-v[:].mean()))+v[:].mean()
    return grid

#np.random.seed(123433789) # GIVING A SEED NUMBER FOR THE EXPERIENCE TO BE REPRODUCIBLE
#x,y = np.random.randint(0,75,10),np.random.randint(0,60,10) # CREATE POINT SET.
#v = np.random.randint(0,10,10) # THIS IS MY VARIABLE

def retX(): #Zwraca punkty pomiarowe na osi x (przyblizone wartosci)
    x = array([58, 58, 57, 47, 50, 40, 43, 34, 20, 24, 17])
    return x
def retY(): #punkty pomiarowe  a osi y
    y = array([50, 42, 25, 24, 20, 21, 17, 33, 34, 38, 25])
    return y

def updateV(): #updatuje nowe wartosci smogu
    #v = array([94, 61, 81, 70, 76, 78, 97, 70, 74, 63, 67]) #PM10 20.11 g.21.00
    v = np.random.randint(0,100,11)  #dla losowych
    return v  
    
def update(aC): #updatuje wartosc smogu, znowu wylicza Kriging i rysuje nowy plot
    x=retX()
    y=retY()
    v = updateV()
    grid = np.zeros((75,60),dtype='float32') # float32 gives us a lot precision 
    grid = SimpleKriging(x,y,v,(50,30),grid)
    plt.imshow(grid.T,origin='lower',interpolation='nearest',cmap='jet')
    plt.scatter(x,y,c=v,cmap='jet',s=120)
    plt.xlim(0,grid.shape[0])
    plt.ylim(0,grid.shape[1])
    plt.grid()
    


def main():
    fig = plt.figure()
    ani = FuncAnimation(fig, update, interval=3, save_count=3) #animacja
    #jak zrobic zeby nie byla powtarzana w nieskonczonosc?
    plt.show()
        


if __name__ == "__main__":
    main()

