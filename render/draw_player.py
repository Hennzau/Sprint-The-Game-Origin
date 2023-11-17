import numpy as np
import pygame

from level.obstacle import pixel_size

""""
draw_player is called upon to reprsent the player at all times for the viewer.
"""

blur_length = 4
precision = 5
positions = []

cursor = 0


def draw_player(player, surface):
    global blur_length, positions, cursor, precision

    if len(positions) != blur_length:
        positions.append(player.render_position)
    else:
        blur = pygame.Surface((pixel_size, pixel_size))
        pygame.draw.rect(blur, (player.color[0] / 20, player.color[1] / 20, player.color[2] / 20),
                         pygame.Rect(0, 0, pixel_size, pixel_size))

        for k in range(blur_length - 1):
            initial = positions[k]
            final = positions[k + 1]
            delta = (final - initial) / precision

            for i in range(precision):
                blur_pos = initial + delta * i
                surface.blit(blur, (blur_pos[0], blur_pos[1]), special_flags=pygame.BLEND_RGB_ADD)

        positions[cursor * 1] = player.render_position

        cursor = (cursor + 1) % blur_length

    blur_surface = pygame.Surface((pixel_size, pixel_size))
    pygame.draw.rect(blur_surface, (player.color[0] / 2, player.color[1] / 2, player.color[2] / 2),
                     pygame.Rect(0, 0, pixel_size, pixel_size))

    surface.blit(blur_surface, (player.render_position[0], player.render_position[1]))

    pygame.draw.rect(surface, player.color,
                     pygame.Rect(player.render_position[0] + pixel_size / 10,
                                 player.render_position[1] + pixel_size / 10, pixel_size * 8 / 10, pixel_size * 8 / 10))
