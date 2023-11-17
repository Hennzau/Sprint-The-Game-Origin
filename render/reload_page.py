### Imports
import pygame
from surface import Surface, flip

import time

colors = {"red": (220, 20, 60), "blue": (106, 90, 205), "green": (154, 205, 50), "yellow": (255, 215, 0),
          "darkgrey": (105, 105, 105), "darkblue": (2, 4, 55), "ivory" : (255,255,212), "Volkswagen Taupe" : (140, 134, 128), 
          "orange":(255,165,0), "purple":(147,112,219)}

### drawing function

class loading_square:
    def __init__(self, initial_position, initial_color): # initial_position is a tuple, initial_color is a string object
        self.position = initial_position
        self.color = colors[initial_color]

    def update (self, position, color):
        self.position = position
        self.color = colors[color]

def draw_reload_page(surface, cursor):
    initial_position = (50,0)
    width = 50
    height = 50
    square = loading_square (initial_position, "red")
    loading_rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]
    for color in loading_rainbow :
        square.update((square.position[0]+10, square.position[1]), color)
        pygame.draw.rect(surface, square.color, pygame.Rect(square.position[0], square.position[1], width, height))

def ask_for_reload(surface):
     percentage = 0
     for i in range (6):
          draw_reload_page(surface,6)
          

surface = Surface(1280, 720, "test")
continuer = True
while continuer :
    surface.clear(colors["darkblue"])
    draw_reload_page(surface.py_surface)
    flip()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
    time.sleep(0.5)