from __future__ import division 
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib as mpl
import scipy.linalg as LA
from matplotlib.animation import FuncAnimation
import csv
import propagation

#zmienne globalne:
results= []
rownum =0
atmFactors=[]
wind=[]
fig=plt.figure(num='Simulation')
img = plt.imread('../images/krk_color_scaled.png') 

   
#algorytm SimpleKriging
#zrodlo: https://sourceforge.net/p/geoms2/wiki/Kriging/
def SimpleKriging(x,y,v,variogram,grid):

    cov_angles = np.zeros((x.shape[0],x.shape[0]))
    cov_distances = np.zeros((x.shape[0],x.shape[0]))
    K = np.zeros((x.shape[0],x.shape[0]))
    for i in range(x.shape[0]-1):
        cov_angles[i,i:]=np.arctan2((y[i:]-y[i]),(x[i:]-x[i]))
        cov_distances[i,i:]=np.sqrt((x[i:]-x[i])**2+(y[i:]-y[i])**2)
    for i in range(x.shape[0]):
        for j in range(x.shape[0]):
            if cov_distances[i,j]!=0:
                amp=np.sqrt((variogram[1]*np.cos(cov_angles[i,j]))**2+(variogram[0]*np.sin(cov_angles[i,j]))**2)
                K[i,j]=v[:].var()*(1-np.e**(-3*cov_distances[i,j]/amp))
    K = K + K.T

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
             distances = np.sqrt((i-x[:])**2+(j-y[:])**2)
             angles = np.arctan2(i-y[:],j-x[:])
             amplitudes = np.sqrt((variogram[1]*np.cos(angles[:]))**2+(variogram[0]*np.sin(angles[:]))**2)
             M = v[:].var()*(1-np.e**(-3*distances[:]/amplitudes[:]))
             W = LA.solve(K,M)
             grid[i,j] = np.sum(W*(v[:]-v[:].mean()))+v[:].mean()
    return grid

def retX(): #Zwraca punkty pomiarowe na osi x (przyblizone wartosci)
    x = array([58, 58, 57, 47, 50, 40, 43, 34, 20, 24, 17])
    return x
def retY(): #Zwraca punkty pomiarowe  a osi y
    y = array([50, 42, 25, 24, 20, 21, 17, 33, 34, 38, 25])
    return y

def updateV(): #aktualizuje nowe wartosci smogu
    #v = np.random.randint(0,100,11)  #dla losowych
    global results
    global rownum
    v = results[rownum]
    rownum +=1
    return array(v)  
    
def update(i): #Pobiera nowa wartosc smogu, ponownie stosuje algorytm Kriging i rysuje nowy wykres (dla danych rzeczywistych)
    global img, fig, atmFactors
    x=retX()
    y=retY()
    v = updateV()
    smogColorMap = newColorMap()
    fig.clf()
    plt.imshow(img, extent=[0, 75, 0, 60])
    grid = np.zeros((75,60),dtype='float32') 
    grid = SimpleKriging(x,y,v,(50,30),grid)
    plt.imshow(grid.T,origin='lower', interpolation='gaussian',cmap=smogColorMap, alpha=0.5, vmin=0, vmax=300)
    scatter = plt.scatter(x,y,c=v,cmap=smogColorMap, vmin=0, vmax=300)
    cb = plt.colorbar(scatter, fraction=0.035, pad=0.04)
    cb.set_label('SMOG scale')
    plt.xlim(0,grid.shape[0])
    plt.ylim(0,grid.shape[1])

	#wypisanie czynników atmosferycznych
    plt.gcf().text(0.02, 0.95, "Temperature:  "\
            +atmFactors[i+1][0]+"\N{DEGREE SIGN}C", fontsize=14)
    plt.gcf().text(0.40, 0.95, "Wind:  "+atmFactors[i+1][1]\
            +"kt "+atmFactors[i+1][2], fontsize=14)
    plt.gcf().text(0.65, 0.95, "Precipitation:  "+atmFactors[i+1][3]\
            +"mm", fontsize=14)
    plt.gcf().text(0.20, 0.9, "Air humidity:  "+atmFactors[i+1][4]\
            +"%", fontsize=14)
    plt.gcf().text(0.58, 0.9, "Air pressure:  "\
            +atmFactors[i+1][5]+"hPa", fontsize=14)
    
def updateSim(i): #Pobiera nowa wartosc smogu, ponownie stosuje algorytm Kriging i rysuje nowy wykres (dla danych predykcyjnych)
    global img, fig, atmFactors
    x=retX()
    y=retY()
    v = updateV()
    smogColorMap = newColorMap()
    fig.clf()
    plt.imshow(img, extent=[0, 75, 0, 60])
    grid = np.zeros((75,60),dtype='float32') 
    grid = SimpleKriging(x,y,v,(50,30),grid)
    plt.imshow(grid.T,origin='lower', interpolation='gaussian',cmap=smogColorMap, alpha=0.5, vmin=0, vmax=300)
    scatter = plt.scatter(x,y,c=v,cmap=smogColorMap, vmin=0, vmax=300)
    cb = plt.colorbar(scatter, fraction=0.035, pad=0.04)
    cb.set_label('SMOG scale')
    plt.xlim(0,grid.shape[0])
    plt.ylim(0,grid.shape[1])
   

def newColorMap():		#zwraca nową skalę kolorów dla danych wartości smogu
    cdict = {'red':   ((0.0, 0.0, 0.0),
                   (0.167, 1.0, 1.0),
                   (0.5, 1.0, 1.0),
                   (0.67, 1.0, 1.0),
                   (1.0, 0.5, 0.5)),
         'green': ((0.0, 1.0, 1.0),
                   (0.167, 1.0, 1.0),
                   (0.5, 0.5, 0.5),
                   (0.67, 0.0, 0.0),
                   (1.0, 0.0, 0.0)),
         'blue':  ((0.0, 0.0, 0.0),
                   (0.167, 0.0, 0.0),
                   (0.5, 0.0, 0.0),
                   (0.67, 0.0, 0.0),
                   (1.0, 0.7, 0.7)) }
    smogColorMap = LinearSegmentedColormap('SmogColorMap', cdict)
    return smogColorMap

def readcsv(filename):	#odczytanie pliku.csv
    results = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter = ";")
        for row in reader:
            results.append(row)
    return results;

def matrixToInt(matrix):		#zamiana macierzy z wartościami String na macierz z wartościami Int
    newMatrix=[[0]*len(matrix[0]) for i in range(len(matrix))]
    for i in range(0, len(matrix)):
        for j in range (0, len(matrix[0])):
            newMatrix[i][j]=int(matrix[i][j])
    return newMatrix

def propagationSim(wind, temp, precip, pm):		#symulacja propagacji wartości smogu
    global results, atmFactors, fig
    if pm==10:
        results = readcsv('../data_csv/pm10_prop.csv')
        print("propagation = 5h, pm=10")
    elif pm==25: 
        results = readcsv('../data_csv/pm25_prop.csv')
        print("propagation = 5h, pm=25")
    
    results = matrixToInt(results);
    #Podzielenie wiatru na predkosc i kierunek
    windSp,windDir = wind[:2], wind[2:]
    for i in range (0,5):
        atmFactors.append([temp,int(windSp),windDir,precip,90,1000])
        i = i+1
    frames = 5
    
    #uruchomienie 'propagation': funkcja generuje na podstawie podanych wartosci
    #smogu oraz czynnikow atmosferycznych kolejne wartosci z nastepnych godzinach
    results = propagation.propagation(atmFactors, results)
    print(results)
    
    plt.grid()
    ani = FuncAnimation(fig, updateSim, frames = frames, interval=300, repeat = False)
    plt.show()
    plt.close(fig)
    
def mainSim(pm,period):                                  #symulacja rzeczywistych wartosci smogu
    global results, atmFactors, fig

    if period==7 and pm==10:
        results = readcsv('../data_csv/pm10_week.csv')  #zmiana pliku z danymi pomiarowymi
        print("period = 7 tydzien, pm = 10")
    elif period==7 and pm==25:
        results = readcsv('../data_csv/pm25_week.csv')
        print("period = 7 tydzien, pm = 2.5")
    elif period==24 and pm==10:
        results = readcsv('../data_csv/pm10_day.csv')
        print("period = 24 dzien, pm = 10")
    elif period==24 and pm==25:
        results = readcsv('../data_csv/pm25_day.csv')
        print("period = 24 dzien, pm = 2.5")
    
    results = matrixToInt(results);

    if period == 7:
        atmFactors = readcsv('../data_csv/factors_week.csv')
        frames=12
    else:
        atmFactors = readcsv('../data_csv/factors_day.csv')
        frames=24
    plt.grid()
    
    ani = FuncAnimation(fig, update, frames = frames, interval=300, repeat = False) #uruchomienie animacji
    
    plt.show()
    plt.close(fig)
