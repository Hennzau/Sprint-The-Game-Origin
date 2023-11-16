from render.draw_player import draw_player
from render.draw_grid import draw_grid
from level.level import Level
from level.obstacle import pixel_size, colors
import pygame
import numpy as np
from math import *
"""
draw_level uses both draw_grid and draw_player in order to render the entire level to the user.
"""


def draw_level(level, surface):
    draw_grid(level.grid, surface)
    for k in range(len(level.players)):
        draw_player(level.players[k], surface)
        
        pygame.draw.rect(surface, colors["ivoire"], pygame.Rect(level.initial_positions[k][0]*pixel_size,level.initial_positions[k][1]*pixel_size, pixel_size, pixel_size))
        pygame.draw.rect(surface, colors["ivoire"], pygame.Rect(level.final_positions[k][0]*pixel_size, level.final_positions[k][1]*pixel_size, pixel_size, pixel_size))
        
        pygame.draw.arc(surface, colors["Volkswagen Taupe"], pygame.Rect(level.initial_positions[k][0]*pixel_size + pixel_size/8,level.initial_positions[k][1]*pixel_size + pixel_size/8, pixel_size/2, pixel_size/2), pi/2, 7*pi/4, 2)
        pygame.draw.circle(surface, colors["Volkswagen Taupe"], (level.initial_positions[k][0]*pixel_size + pixel_size*5/16,level.initial_positions[k][1]*pixel_size + pixel_size*5/16), 2)
        
        pygame.draw.arc(surface, colors["red"], pygame.Rect(level.initial_positions[k][0]*pixel_size + pixel_size*3/8 ,level.initial_positions[k][1]*pixel_size + pixel_size*3/8, pixel_size/2, pixel_size/2 ),-pi/2, 3*pi/4, 2)
        pygame.draw.circle(surface, colors["red"], (level.initial_positions[k][0]*pixel_size + pixel_size*10/16,level.initial_positions[k][1]*pixel_size + pixel_size*10/16), 2)
        L=[]
        for i in range (10):
            if i%2 == 0:
                L+=[(level.final_positions[k][0]*pixel_size + pixel_size/2 + (pixel_size/2)*np.cos(2*pi*i/10 - pi/2), level.final_positions[k][1]*pixel_size + pixel_size/2 + (pixel_size/2)*np.sin(2*pi*i/10 - pi/2))]
            else :
                L+=[(level.final_positions[k][0]*pixel_size + pixel_size/2 + (pixel_size/5)*np.cos(2*pi*i/10-pi/2), level.final_positions[k][1]*pixel_size + pixel_size/2 + (pixel_size/5)*np.sin(2*pi*i/10-pi/2))]
        pygame.draw.polygon(surface, colors["red"], L , 0)
        