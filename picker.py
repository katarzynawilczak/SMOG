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

        def simulation():
            root.destroy()
            print(pm.get())
            print(timeR.get())
            main.main(pm.get(),timeR.get())

        tk.Frame.__init__(self, parent)
        #tworzy przyciski wyboru i prompty
        def pmset(a):
            pm.set(a)
        def timeRset(a):
            timeR.set(a)
        
        #wybor typu pylow
        
        self.prompt = tk.Label(self, text="Pick a pm type:", anchor="center")
        self.pm10 = tk.Radiobutton(self, text="PM 10", command=lambda:pmset(10))
        self.pm25 = tk.Radiobutton(self, text="PM2.5",command=lambda:pmset(25))
        
        #wybor czasu trwania pomiarow
        
        self.prompt2 = tk.Label(self, text="Pick a time range:", anchor="center")
        self.hour = tk.Radiobutton(self, text="24h", command=lambda:timeRset(24))#variable=timeR, value=24)
        self.week = tk.Radiobutton(self, text="Week", command=lambda:timeRset(7))#variable=timeR, value=7)
        
        self.start = tk.Button(self, text="Start simulation", command=simulation)

        #ustawia elementy w oknie
        self.prompt.pack(side="top", fill="x")
        self.pm10.pack(side="top")
        self.pm25.pack(side="top")
        
        self.prompt2.pack(fill="x")
        self.hour.pack(side="top")
        self.week.pack(side="top")
        
        self.start.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Air Pollution Simulation")
    Picker(root).pack(fill="both", expand=True)
    root.mainloop()
    
