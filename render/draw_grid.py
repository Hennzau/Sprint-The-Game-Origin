# Imports
from level.grid import Grid
from level.obstacle import pixel_size, colors
import pygame


# function draw_grid which renders the grid object on the window

def draw_grid(grid, surface):
    height, width = grid.size
    for i in range(height):
        for j in range(width):
            if grid.obstacles[i, j] is not None:
                pygame.draw.rect(surface, grid.obstacles[i, j].color,
                                 pygame.Rect(i * pixel_size, j * pixel_size, pixel_size, pixel_size))
            else:
                pygame.draw.rect(surface, colors["darkblue"],
                                 pygame.Rect(i * pixel_size, j * pixel_size, pixel_size, pixel_size))
