# Imports
from level.grid import Grid
from level.obstacle import pixel_size, colors
import pygame
from math import *
import numpy as np


# function draw_grid which renders the grid object on the window

def draw_grid(grid, surface):
    height, width = grid.size
    for i in range(height):
        for j in range(width):
            if grid.obstacles[i, j] is not None:

                if grid.obstacles[i, j].start:
                    pygame.draw.rect(surface, colors["darkblue"],
                                     pygame.Rect(i * pixel_size,
                                                 j * pixel_size, pixel_size,
                                                 pixel_size))

                    pygame.draw.arc(surface, colors["Volkswagen Taupe"],
                                    pygame.Rect(i * pixel_size + pixel_size / 8,
                                                j * pixel_size + pixel_size / 8,
                                                pixel_size / 2,
                                                pixel_size / 2), pi / 2, 7 * pi / 4, 2)
                    pygame.draw.circle(surface, colors["Volkswagen Taupe"], (

                        i * pixel_size + pixel_size * 11 / 32,
                        j * pixel_size + pixel_size * 11 / 32), 3)

                    pygame.draw.arc(surface, grid.obstacles[i, j].color,
                                    pygame.Rect(i * pixel_size + pixel_size * 7 / 16,
                                                j * pixel_size + pixel_size * 7 / 16,
                                                pixel_size / 2,
                                                pixel_size / 2), -pi / 2, 3 * pi / 4, 2)

                    pygame.draw.circle(surface, grid.obstacles[i, j].color, (
                        i * pixel_size + pixel_size * 21 / 32,
                        j * pixel_size + pixel_size * 21 / 32), 3)
                elif grid.obstacles[i, j].end:
                    pygame.draw.rect(surface, colors["darkblue"],
                                     pygame.Rect(i * pixel_size,
                                                 j * pixel_size,
                                                 pixel_size, pixel_size))

                    L = []
                    for k in range(10):
                        if k % 2 == 0:
                            L += [
                                (i * pixel_size + pixel_size / 2 + (pixel_size / 2) * np.cos(
                                    2 * pi * k / 10 - pi / 2),
                                 j * pixel_size + pixel_size / 2 + (pixel_size / 2) * np.sin(
                                     2 * pi * k / 10 - pi / 2))]
                        else:
                            L += [
                                (i * pixel_size + pixel_size / 2 + (pixel_size / 5) * np.cos(
                                    2 * pi * k / 10 - pi / 2),
                                 j * pixel_size + pixel_size / 2 + (pixel_size / 5) * np.sin(
                                     2 * pi * k / 10 - pi / 2))]

                    pygame.draw.polygon(surface, grid.obstacles[i, j].color, L, 0)

                else:
                    pygame.draw.rect(surface, grid.obstacles[i, j].color,
                                     pygame.Rect(i * pixel_size, j * pixel_size, pixel_size, pixel_size))
            else:
                pygame.draw.rect(surface, colors["darkblue"],
                                 pygame.Rect(i * pixel_size, j * pixel_size, pixel_size, pixel_size))
