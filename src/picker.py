#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:23:26 2018

@author: hushmans
"""
import tkinter as tk #do gui
import main

class Picker(tk.Frame):

    def __init__(self, parent):

        pm=tk.IntVar()
        timeR=tk.IntVar()
        pm.set(10)
        timeR.set(7)

        #Uruchamia symulacje z odpowiednimi parametrami
        def simulation():
            self.destroy()
            print(pm.get())
            print(timeR.get())
            main.mainSim(pm.get(),timeR.get())

        tk.Frame.__init__(self, parent)
        #tworzy przyciski wyboru i prompty
        def pmset(a):
            pm.set(a)
        def timeRset(a):
            timeR.set(a)
            
        #Otwiera nowe okno do podawania atrybutow propagacji    
        def propagation():
            win = tk.Toplevel(self)
            
            #Propagacja
            w = tk.StringVar()
            temp = tk.IntVar()
            prec = tk.IntVar()
            
            win.prompt3 = tk.Label(win, text="Start a 5h propagation with:", anchor="center")
            win.windPrompt = tk.Label(win, text="Wind[kt](format:05E):")
            win.wind = tk.Entry(win, bd =3, textvariable=w)
            win.tempPrompt = tk.Label(win, text="Temperature[*C]:")
            win.temperature = tk.Entry(win, bd =3, textvariable=temp)
            win.precipPrompt = tk.Label(win, text="Precipitation[mm]:")
            win.precipitation = tk.Entry(win, bd =3, textvariable=prec)
            
            #Uruchamia propagacje z odpowiednimi atrybutami
            def propagateStart():
                w = win.wind.get()
                temp = int(win.temperature.get())
                prec = int(win.precipitation.get())
                print(w)
                print(temp)
                print(prec)
                win.destroy()
                self.destroy()
                #Wywoluje funkcje z main, ktora liczy brakujace dane i uruchamia propagacje
                main.propagationSim(w, temp, prec, 10)
                
            win.startProp = tk.Button(win, text="Start propagation", command=propagateStart) #command
        
            #Umieszcza przyciski i text w oknie
            win.prompt3.pack(fill="x")
            win.windPrompt.pack(side="top")
            win.wind.pack(side="top")
            win.tempPrompt.pack(side="top")
            win.temperature.pack(side="top")
            win.precipPrompt.pack(side="top")
            win.precipitation.pack(side="top")
            win.startProp.pack()
            
        
        #wybor typu pylow
        pm = tk.IntVar()
        self.prompt = tk.Label(self, text="Pick a pm type:", anchor="center")
        self.pm10 = tk.Radiobutton(self, text="PM 10", variable=pm, value=10, command=lambda:pmset(10))
        self.pm25 = tk.Radiobutton(self, text="PM2.5",variable=pm, value=25, command=lambda:pmset(25))
        
        #wybor czasu trwania pomiarow
        tim = tk.IntVar()
        self.prompt2 = tk.Label(self, text="Pick a time range:", anchor="center")
        self.hour = tk.Radiobutton(self, text="24h", variable=tim, value=24, command=lambda:timeRset(24))
        self.week = tk.Radiobutton(self, text="Week", variable=tim, value=7, command=lambda:timeRset(7))
        
        self.start = tk.Button(self, text="Start simulation", command=simulation)
        
        self.propagate = tk.Button(self, text="Propagation", command=propagation)
        
        #ustawia elementy w oknie
        self.prompt.pack(side="top", fill="x")
        self.pm10.pack(side="top")
        self.pm25.pack(side="top")
        
        self.prompt2.pack(fill="x")
        self.hour.pack(side="top")
        self.week.pack(side="top")
        
        self.start.pack()
    
        self.propagate.pack(fill="x")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Air Pollution Simulation")
    Picker(root).pack(fill="both", expand=True)
    root.mainloop()
