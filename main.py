# Main loop of the game #

# Imports #
import pygame

import render.surface
from game import Game
from render.surface import Surface
from level.obstacle import colors


# ----------------- #


def main():
    surface = Surface(1280, 720, "test")
    game = Game()

    delta_time = 0
    running = True

    while running:
        for event in render.surface.events():
            if event.type == pygame.QUIT:
                running = False

        surface.clear(colors["darkgrey"])

        start = pygame.time.get_ticks()

        game.update(delta_time)
        game.render()

        pygame.draw.rect(surface.surface, colors["red"], pygame.Rect(200, 150, 100, 50))

        end = pygame.time.get_ticks()
        delta_time = (end - start) / 1000

        render.surface.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
