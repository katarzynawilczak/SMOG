import pyglet

#Mapa: pobiera(szerokość, wysokość, odnośnik do mapy)
class Map:
    def __init__(self, window_width, window_height, map_file):

        
        self.krk_map = pyglet.image.load(map_file)
        self.krk_map.anchor_x = self.krk_map.width // 2
        self.krk_map.anchor_y = self.krk_map.height // 2


    def draw(self, window_width, window_height, x, y):
        self.krk_map.blit(x, y)

