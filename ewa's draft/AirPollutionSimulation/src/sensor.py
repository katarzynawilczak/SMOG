#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:27:48 2018

@author: hushmans
"""
import pyglet

class Sensor:

    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        
        
        self.img = pyglet.image.load('./graphics/green.png')
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2
        
        self.sprite = pyglet.sprite.Sprite(self.img, x=self.posx, y=self.posy)


    def draw(self, windowx, windowy):
        self.sprite.x = windowx + self.posx
        self.sprite.y = windowy + self.posy
        self.sprite.draw()
