from level.player import Player
import pygame

""""
draw_player is called upon to reprsent the player at all times for the viewer.
"""

def draw_player(player, surface):
    pygame.draw.rect(surface, player.color, pygame.Rect(player.position[0], player.position[1], 50, 50))

