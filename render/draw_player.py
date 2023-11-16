from level.player import Player
import pygame
from level.obstacle import pixel_size

""""
draw_player is called upon to reprsent the player at all times for the viewer.
"""


def draw_player(player, surface):
    pygame.draw.rect(surface, player.color, pygame.Rect(player.render_position[0], player.render_position[1], pixel_size, pixel_size))
