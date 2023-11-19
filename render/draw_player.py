import numpy as np
import pygame

from level.obstacle import pixel_size

""""
draw_player is called upon to represent the player at all times for the viewer.
"""

precision = 5


def draw_player(player, surface):
    global precision

    if len(player.last_positions) == player.record_length:
        blur = pygame.Surface((pixel_size, pixel_size))
        pygame.draw.rect(blur, (player.color[0] / 20, player.color[1] / 20, player.color[2] / 20),
                         pygame.Rect(0, 0, pixel_size, pixel_size))

        for k in range(player.record_length - 1):
            initial = player.last_positions[k]
            final = player.last_positions[k + 1]
            delta = (final - initial) / precision

            for i in range(precision):
                blur_pos = initial + delta * i
                surface.blit(blur, (blur_pos[0], blur_pos[1]), special_flags=pygame.BLEND_RGB_ADD)

    blur_surface = pygame.Surface((pixel_size, pixel_size))
    pygame.draw.rect(blur_surface, (player.color[0] / 2, player.color[1] / 2, player.color[2] / 2),
                     pygame.Rect(0, 0, pixel_size, pixel_size))

    surface.blit(blur_surface, (player.render_position[0], player.render_position[1]))

    pygame.draw.rect(surface, player.color,
                     pygame.Rect(player.render_position[0] + pixel_size / 10,
                                 player.render_position[1] + pixel_size / 10, pixel_size * 8 / 10, pixel_size * 8 / 10))
