from level.player import Player
import pygame

from level.obstacle import pixel_size

""""
draw_player is called upon to reprsent the player at all times for the viewer.
"""


def draw_player(player, surface):
    blend_surface = pygame.Surface((pixel_size, pixel_size))
    pygame.draw.rect(blend_surface, (player.color[0] / 2, player.color[1] / 2, player.color[2] / 2),
                     pygame.Rect(0, 0, pixel_size, pixel_size))

    surface.blit(blend_surface,
                 (player.render_position[0], player.render_position[1]),
                 special_flags=pygame.BLEND_RGB_ADD)

    pygame.draw.rect(surface, player.color,
                     pygame.Rect(player.render_position[0] + pixel_size / 10,
                                 player.render_position[1] + pixel_size / 10, pixel_size * 8 / 10, pixel_size * 8 / 10))
