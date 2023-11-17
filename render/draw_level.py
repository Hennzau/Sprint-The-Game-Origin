from render.draw_player import draw_player
from render.draw_grid import draw_grid
from level.level import Level
from level.obstacle import pixel_size, colors
from level.player import Player
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
