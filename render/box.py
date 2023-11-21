import pygame

from level.obstacle import colors

"""
The 'box.py' module contains some code to manage the creation of buttons and boxes in the game style
in order to remove redundant code
"""


def draw_text_box(surface, x, y, width, height):
    pygame.draw.rect(surface, colors["ivory"], pygame.Rect(x - 40, y - 40, width + 80, height + 80))
    pygame.draw.rect(surface, colors["Black"], pygame.Rect(x - 39, y - 39, width + 78, height + 78))
    pygame.draw.rect(surface, colors["ivory"], pygame.Rect(x - 25, y - 25, width + 50, height + 50))
    pygame.draw.rect(surface, colors["darkblue"], pygame.Rect(x - 24, y - 24, width + 48, height + 48))


def draw_empty_box(surface, x, y, width, height):
    pygame.draw.rect(surface, colors["ivory"], pygame.Rect(x, y, width, height))
    pygame.draw.rect(surface, colors["Black"], pygame.Rect(x + 1, y + 1, width - 2, height - 2))
    pygame.draw.rect(surface, colors["ivory"], pygame.Rect(x + 5, y + 5, width - 10, height - 10))
    pygame.draw.rect(surface, colors["darkblue"], pygame.Rect(x + 6, y + 6, width - 12, height - 12))


def draw_covered_box(surface, x, y, width, height):
    pygame.draw.rect(surface, colors["ivory"], pygame.Rect(x, y, width, height))
    pygame.draw.rect(surface, colors["Black"], pygame.Rect(x + 1, y + 1, width - 2, height - 2))
    pygame.draw.rect(surface, colors["ivory"], pygame.Rect(x + 5, y + 5, width - 10, height - 10))
    pygame.draw.rect(surface, colors["Volkswagen Taupe"], pygame.Rect(x + 6, y + 6, width - 12, height - 12))
