import pygame 
from pygame.locals import *

class Window:
    def __init__(self,width,height,title):
        pygame.init()
        self.width = width
        self.height = height
        self.title = title
        
        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption(self.title)
        pygame.display.update()
    
    def clear(self, background_color):
        self.window.fill(background_color)
        