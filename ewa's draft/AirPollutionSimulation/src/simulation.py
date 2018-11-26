#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:13:34 2018

@author: hushmans
"""
import csv
from src.sensor import Sensor
import pyglet

class Simulation:
    def __init__(self, window_width, window_height, sensors_file):
        with open(sensors_file) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                self.sensors = []
                for row in csv_reader:
                    if line_count != 0:
                        x = row[0]
                        y = row[1]
                        sensor = (int(x),int(y))
                        self.sensors.append(sensor)
                        line_count += 1
                    else:
                        line_count += 1

        print(line_count)
        line_count = line_count-1
        sensors_amount = 3
         
        if line_count != sensors_amount:
             raise ValueError("Not enough sensor data")
             
        img = pyglet.image.load('./graphics/green.png')
        img.anchor_x = img.width // 2
        img.anchor_y = img.height // 2
        
        for i in self.sensors:
            self.sprite = pyglet.sprite.Sprite(img, i[0],  i[1])
            
            
         
    def draw(self, x, y):
        self.sprite.x = x
        self.sprite.y = y
        self.sprite.draw()
            