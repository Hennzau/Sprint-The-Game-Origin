# Main loop of the game #

# Imports #
import pygame

from game import Game

from render.surface import Surface
from render.surface import events, flip
from level.obstacle import colors


# ----------------- #


def main():
    surface = Surface(1280, 720, "test")
    game = Game()

    delta_time = 0
    running = True

    while game.is_open():

        surface.clear(colors["darkgrey"])

        start = pygame.time.get_ticks()

        game.update(delta_time)
        game.render()

        pygame.draw.rect(
            surface.surface, colors["red"], pygame.Rect(200, 150, 100, 50))

        end = pygame.time.get_ticks()
        delta_time = (end - start) / 1000

        flip()

    pygame.quit()


if __name__ == '__main__':
    main()
