from menu.main_menu import Main_menu
from level.obstacle import colors
import pygame


def draw_main_menu(surface):
    pygame.font.init()

    width, height = surface.width, surface.height

    surface.surface.fill(colors["darkblue"])

    font = pygame.font.Font("assets/fonts/GamepauseddemoRegular-RpmY6.otf", 50)
    font_levels = pygame.font.Font("assets/fontsGamepauseddemoRegular-RpmY6.otf", 20)

    title = font.render('SPRINT THE GAME', True, colors["white_yellow"])
    start_button = font.render(
        'Press Space to Start', True, colors["white_yellow"])

    surface.blit(title, (width / 2 - title.get_width() / 2,
                         height / 2 - title.get_height() / 2 - 100))

    surface.blit(start_button, (width / 2 - start_button.get_width() /
                                2, height / 2 + start_button.get_height() / 2 - 75))

    pygame.display.update()
