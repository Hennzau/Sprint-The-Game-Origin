# Imports
from level.grid import Grid
from level.obstacle import pixel_size
import pygame

#function draw_grid which renders the grid object on the window

def draw_grid(grid, surface):
    height, width = grid.size
    for i in range (height):
        for j in range (width):
            pygame.draw.rect(surface, grid.obstacles[i,j].color, pygame.Rect(i,j,pixel_size,pixel_size))

