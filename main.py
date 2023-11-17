# Main loop of the game #

# Imports #
import pygame

from game import Game
from menu.main_menu import Main_menu
from render.draw_main_menu import draw_main_menu
from render.surface import Surface
from render.surface import events, flip
from level.obstacle import colors
from render.draw_end_menu import draw_end_menu


# ----------------- #

def main():
    surface = Surface(1280, 720, "test")

    game = Game()
    menu = Main_menu(game)
    clock = pygame.time.Clock()

    while game.is_open:
        surface.clear((0, 0, 0))

        game.update(float(1 / 60))

        if game.stage == "Launched":
            game.render(surface)

        if game.stage == "Main Menu":
            draw_main_menu(surface, menu, game)

        if game.stage == "End Menu":
            draw_end_menu(surface, game)

        flip()

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
