### Imports
import pygame
from surface import Surface
from level.obstacle import colors

### drawing function

class loading_square:
    def __init__(self, initial_position, initial_color): # initial_position is a tuple, initial_color is a string object
        self.position = initial_position
        self.color = colors[initial_color]

def draw_reload_page(surface):
