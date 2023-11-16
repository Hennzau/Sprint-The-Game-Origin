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

    clock = pygame.time.Clock()

    while game.is_open:
        surface.clear((0,0,0))

        start = pygame.time.get_ticks()

        game.update(float (1/60))
        game.render(surface)

        flip()

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
