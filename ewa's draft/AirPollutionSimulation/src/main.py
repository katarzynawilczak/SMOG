# -*- coding: utf-8 -*-
import numpy as np
import pyglet
from pyglet.window import mouse
from src.map import Map
from src.simulation import Simulation

class Window(pyglet.window.Window):

    def __init__(self, map_file):
        super().__init__(resizable=False, caption='Air Pollution Simulation', visible=False)
        self.set_minimum_size(640, 480)
        self.set_maximum_size(2260, 3540)
        self.frame_rate = 1/60.0

        #set app icon
        #self.icon = pyglet.image.load('')
        #self.set_icon(self.icon)

        self.map = Map(self.width, self.height, map_file)
        self.set_visible(True)

        self.x =self.width//2
        self.y =self.height//2

        self.simulation = Simulation(self.width, self.height, './src/sensors.txt')
        #self.simulation = Simulation(2260, 3540, self.width, self.height, config_file)


    #ef update(self, dt):
       # self.simulation.update(dt)
        self.img = pyglet.image.load('./graphics/green.png')
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2

    def on_draw(self):
        self.clear()
        self.map.draw(self.width, self.height, self.x, self.y)
        for i in self.simulation.sensors:
            self.simulation.draw(i[0], i[1])


if __name__ == '__main__':

    window = Window('./graphics/krk_color_scaled.jpg')
    #yglet.clock.schedule_interval(window__init__, window.frame_rate)
    pyglet.app.run()

            
        