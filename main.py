# Main loop of the game #

# Imports #
import pygame

from game import Game
from menu.main_menu import MainMenu
from render.draw_main_menu import draw_main_menu
from render.surface import Surface
from render.surface import events, flip
from level.obstacle import colors
from render.draw_end_menu import draw_end_menu
from editor.draw_level_editor import draw_level_editor
from editor.level_editor import LevelEditor


# ----------------- #

def main():
    surface = Surface(1280, 720, "Sprint The Game")

    game = Game(surface)
    level_editor = LevelEditor((20,12))
    menu = MainMenu(game)
    clock = pygame.time.Clock()

    timer = 0

    frame_cap = 120

    while game.is_open:
        surface.clear((0, 0, 0))

        if clock.get_fps() > 0:
            game.update(float(1 / clock.get_fps()))
        else:
            game.update(float(1 / 60))

        if game.stage == "Launched":
            game.render()
            if timer == 0:
                print("Game launched, currently rendering", int(clock.get_fps()), "FPS")

        if game.stage == "Main Menu":
            draw_main_menu(surface, menu, game)

        if game.stage == "End Menu":
            draw_end_menu(surface, game)

        if game.stage == "Level Editor":
            draw_level_editor(level_editor, surface)

        flip()

        clock.tick(frame_cap)

        timer = (timer + 1) % frame_cap

    pygame.quit()


if __name__ == '__main__':
    main()
