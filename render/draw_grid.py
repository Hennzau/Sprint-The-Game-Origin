# Imports
from level.grid import Grid
from level.obstacle import pixel_size, colors
import pygame
from math import *
import numpy as np


# function draw_grid which renders the grid object on the window

def draw_grid(grid, surface, time):
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
                                                pixel_size / 2), pi / 2, 7 * pi / 4, 1)
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
                elif grid.obstacles[i,j].color_switcher:
                    pygame.draw.rect(surface, colors["darkblue"],
                                 pygame.Rect(i * pixel_size, j * pixel_size, pixel_size, pixel_size))
                    
                    temp_surface=pygame.Surface((pixel_size, pixel_size), pygame.SRCALPHA)

                    circle_surface=pygame.Surface((pixel_size,pixel_size), pygame.SRCALPHA)
                    
                    #red arc
                    pygame.draw.circle(circle_surface, colors["red"], (pixel_size/2,pixel_size/2),pixel_size/2,0)
                    temp_surface.blit(circle_surface.subsurface(pygame.Rect(pixel_size/2,0,pixel_size/2,pixel_size/2)),(pixel_size/2, 0))
                    #yellow arc
                    pygame.draw.circle(circle_surface, colors["yellow"], (pixel_size/2,pixel_size/2),pixel_size/2,0)
                    temp_surface.blit(circle_surface.subsurface(pygame.Rect(0,0,pixel_size/2,pixel_size/2)),(0, 0))
                    #green arc
                    pygame.draw.circle(circle_surface, colors["green"], (pixel_size/2,pixel_size/2),pixel_size/2,0)
                    temp_surface.blit(circle_surface.subsurface(pygame.Rect(0,pixel_size/2,pixel_size/2,pixel_size/2)),(0, pixel_size/2))
                    #blue arc
                    pygame.draw.circle(circle_surface, colors["blue"], (pixel_size/2,pixel_size/2),pixel_size/2,0)
                    temp_surface.blit(circle_surface.subsurface(pygame.Rect(pixel_size/2,pixel_size/2,pixel_size/2,pixel_size/2)),(pixel_size/2, pixel_size/2))
                    #rotating the temp_surface and putting it on the surface
                    rotated_surface = pygame.transform.rotate(temp_surface, time*100)
                    new_temp_surface = rotated_surface.get_rect(center = temp_surface.get_rect(center =(i*pixel_size + pixel_size/2, j * pixel_size + pixel_size/2)).center)

                    surface.blit(rotated_surface, new_temp_surface)
                    
                    #circle in the center
                    pygame.draw.circle(surface, colors["darkblue"], (i*pixel_size+pixel_size/2, j*pixel_size+pixel_size/2), pixel_size/2.5,0)
                    pygame.draw.circle(surface, grid.obstacles[i,j].color, (i*pixel_size+pixel_size/2, j*pixel_size+pixel_size/2), pixel_size/4,0)
                    

                else:
                    pygame.draw.rect(surface, grid.obstacles[i, j].color,
                                     pygame.Rect(i * pixel_size, j * pixel_size, pixel_size, pixel_size))
            else:
                pygame.draw.rect(surface, colors["darkblue"],
                                 pygame.Rect(i * pixel_size, j * pixel_size, pixel_size, pixel_size))
