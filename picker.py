#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:23:26 2018

@author: hushmans
"""
import Tkinter as tk #do gui


class Picker(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        #tworzy przyciski wyboru i prompty
        
        #wybor typu pylow
        pm = tk.IntVar();
        self.prompt = tk.Label(self, text="Pick a pm type:", anchor="center")
        self.pm10 = tk.Radiobutton(self, text="PM 10", variable=pm, value=10)
        self.pm25 = tk.Radiobutton(self, text="PM2.5", variable=pm, value=25)
        
        #wybor czasu trwania pomiarow
        timeR=tk.IntVar();
        self.prompt2 = tk.Label(self, text="Pick a time range:", anchor="center")
        self.hour = tk.Radiobutton(self, text="24h", variable=timeR, value=24)
        self.week = tk.Radiobutton(self, text="Week", variable=timeR, value=7)
        
        self.start = tk.Button(self, text="Start simulation")

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
    