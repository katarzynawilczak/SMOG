#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 15:40:32 2018

@author: hushmans
"""
 
def propagation(czynnikiAtm, results):
    #czynnikiAtm[godzina][czynnik]
    #0 temp, 1 predkosc wiatru, 2 kierunek wiatru, 3 opad
    for i in range (0,5):
        #jak temperatura > -5 to 
        wind = int(czynnikiAtm[0][1])
        #jak temperatura <= -5 to mroz powoduje, ze smog sie utrzymuje + wiecej palenia w piecach 
        #inwersja termiczna
        if czynnikiAtm[0][0] <= -4:
            for j in range(0,11):
                results[i][j] = results[i][j]*1.1
            for j in range(0,11):        
                results[i+1][j] = results[i][j]    
                
        #jesli wiatr silny to przewieje calkiem i nie ma smogu
        if czynnikiAtm[0][1] > 5: 
            for j in range(0,11): 
                results[i+1][j] = results[i][j]*0.7
   
        #jesli pada deszcz/snieg to brak smogu        
        if czynnikiAtm[0][3] != 0:
            for j in range(0,11): 
                results[i+1][j] = results[i][j]*0.8  
                
        #jesli slaby wiatr to przewieje troche w strone wiatru
        if wind < 5 and wind > 0:
            #jesli wiatr NE/SE to podobnie do E, jesli NW/SW to podobnie do W
            if czynnikiAtm[0][2] == "NE" or czynnikiAtm[0][2] == "SE":
                czynnikiAtm[0][2] = "E"
            elif czynnikiAtm[0][2] == "NW" or czynnikiAtm[0][2] == "SW":
                czynnikiAtm[0][2] = "W"
                
            #przewiewa w strone W
            if czynnikiAtm[0][2] == "E":
                results[i+1][10] = results[i][5]
                results[i+1][9] = results[i][7]
                results[i+1][5] = results[i][3]
                results[i+1][6] = results[i][4]
                results[i+1][4] = results[i][2]
                results[i+1][8] = results[i][7]
                results[i+1][7] = results[i][1]
                results[i+1][0] = results[i][0]*0.8
                results[i+1][1] = results[i][1]*0.8
                results[i+1][3] = results[i][2]
                results[i+1][2] = results[i][2]*0.8
            elif czynnikiAtm[0][2] == "W":
                results[i+1][0] = results[i][7]*0.9
                results[i+1][1] = results[i][7]
                results[i+1][2] = results[i][3]
                results[i+1][3] = results[i][5]
                results[i+1][4] = results[i][6]
                results[i+1][5] = results[i][10]
                results[i+1][6] = results[i][10]*0.9
                results[i+1][7] = results[i][8]
                results[i+1][9] = results[i][8]
                results[i+1][8] = results[i][10]*0.9
                results[i+1][10] = results[i][10]*0.8
            #przewiewa w strone N
            elif czynnikiAtm[0][2] == "S":
                results[i+1][0] = results[i][1]
                results[i+1][9] = results[i][8]*0.9
                results[i+1][8] = results[i][10]
                results[i+1][7] = results[i][5]*0.95
                results[i+1][1] = results[i][2]
                results[i+1][2] = results[i][2]*0.9
                results[i+1][3] = results[i][4]*0.95
                results[i+1][10] = results[i][5]*0.9
                results[i+1][5] = results[i][6]*0.95
                results[i+1][6] = results[i][6]*0.85
                results[i+1][4] = results[i][4]*0.85
            #przewiewa w strone S    
            elif czynnikiAtm[0][2] == "N":
                results[i+1][6] = results[i][5]*0.9
                results[i+1][5] = results[i][7]
                results[i+1][4] = results[i][3]*0.9
                results[i+1][3] = results[i][7]*0.95
                results[i+1][2] = results[i][1]*0.9
                results[i+1][1] = results[i][0]
                results[i+1][10] = results[i][8]*0.95
                results[i+1][8] = results[i][9]*0.95
                results[i+1][7] = results[i][9]*0.95
                results[i+1][9] = results[i][9]*0.85
                results[i+1][0] = results[i][0]*0.85
         
            
    for j in range(0,11):
        results[5][j] = results[4][j]*0.98     
        
    return results
    