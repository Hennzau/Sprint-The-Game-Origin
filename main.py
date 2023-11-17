# Main loop of the game #

# Imports #
import pygame

from game import Game
from render.draw_main_menu import draw_main_menu
from render.surface import Surface
from render.surface import events, flip
from level.obstacle import colors


# ----------------- #

def main():
    surface = Surface(1280, 720, "test")

    game = Game()
    clock = pygame.time.Clock()

    while game.is_open:
        surface.clear((0, 0, 0))

        if game.stage == "Launched":
            game.update(float(1 / 60))
            game.render(surface)

        if game.stage == "Main Menu":
            game.update(float(1 / 60))
            draw_main_menu(surface)

        flip()

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
