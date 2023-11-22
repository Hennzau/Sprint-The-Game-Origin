# Imports

import pygame

from level.obstacle import colors
from sound import sound_button

from render.box import draw_covered_box, draw_empty_box, draw_text_box


def draw_end_menu(surface, game):
    """
    the draw_end_menu function draw the victory menu of the game on the given surface
    It also manages actions on the game

    Parameters:
    surface (Surface): the surface on which you want to draw the end menu
    game (Game): the Game object
    """

    # dimensions

    height = surface.height
    width = surface.width
    button_width = 250
    button_height = 80

    sound = True

    surface.py_surface.fill(colors["darkblue"])

    backgroud = pygame.image.load('assets/images/Sprint_Background.png')
    surface.py_surface.blit(backgroud, (0, 0))

    # fonts
    font = pygame.font.Font("assets/fonts/BulletTrace7-rppO.ttf", 60)
    font_buttons = pygame.font.Font("assets/fonts/BulletTrace7-rppO.ttf", 30)

    # title
    title = font.render('VICTORY', True, colors["ivory"])

    x_title_extended = width / 2 - title.get_width() / 2
    y_title_extended = height / 2 - title.get_height() / 2 - 200
    title_extended_width = title.get_width()
    title_extended_height = title.get_height()

    draw_text_box(surface.py_surface, x_title_extended, y_title_extended, title_extended_width, title_extended_height)
    surface.py_surface.blit(title, ((width - title.get_width()) / 2, (height - title.get_height()) / 2 - 200))

    # play again button
    play_again_button = font_buttons.render("Play again", True, colors["ivory"])

    text_width = play_again_button.get_width()
    text_height = play_again_button.get_height()

    x_button1 = (width - play_again_button.get_width()) / 2 - 300
    y_button1 = (height - play_again_button.get_height()) / 2

    x_rect1 = x_button1 - (button_width - text_width) / 2
    y_rect1 = y_button1 - (button_height - text_height) / 2

    draw_empty_box(surface.py_surface, x_rect1, y_rect1, button_width, button_height)
    surface.py_surface.blit(play_again_button, (x_button1, y_button1))

    # menu button

    menu_button = font_buttons.render("Menu", True, colors["ivory"])

    text_width = menu_button.get_width()
    text_height = menu_button.get_height()

    x_button2 = (width - menu_button.get_width()) / 2 + 300
    y_button2 = (height - menu_button.get_height()) / 2

    x_rect2 = x_button2 - (button_width - text_width) / 2
    y_rect2 = y_button2 - (button_height - text_height) / 2

    draw_empty_box(surface.py_surface, x_rect2, y_rect2, button_width, button_height)
    surface.py_surface.blit(menu_button, (x_button2, y_button2))

    # next level button
    # allows the user go to the next level

    next_level = font_buttons.render("Next level", True, colors["ivory"])

    text_width = next_level.get_width()
    text_height = next_level.get_height()

    x_button3 = (width - next_level.get_width()) / 2
    y_button3 = (height - next_level.get_height()) / 2

    x_rect3 = x_button3 - (button_width - text_width) / 2
    y_rect3 = y_button3 - (button_height - text_height) / 2

    draw_empty_box(surface.py_surface, x_rect3, y_rect3, button_width, button_height)
    surface.py_surface.blit(next_level, (x_button3, y_button3))

    if pygame.Rect(x_rect1, y_rect1, button_width, button_height).collidepoint(pygame.mouse.get_pos()):
        draw_covered_box(surface.py_surface, x_rect1, y_rect1, button_width, button_height)
        surface.py_surface.blit(play_again_button, (x_button1, y_button1))

        if pygame.mouse.get_pressed()[0]:
            game.cursor = game.last_level
            game.stage = "Launched"
            game.load_interface()

        sound = False

    if pygame.Rect(x_rect2, y_rect2, button_width, button_height).collidepoint(pygame.mouse.get_pos()):
        draw_covered_box(surface.py_surface, x_rect2, y_rect2, button_width, button_height)
        surface.py_surface.blit(menu_button, (x_button2, y_button2))

        if pygame.mouse.get_pressed()[0]:
            game.stage = "Main Menu"
        sound = False

    if not game.sound and not sound:
        game.sound = True
        sound_button()

    if sound:
        game.sound = False

    # the button change when the mouse is on it, and when the mouse is pressed, use this button to move on to the
    # next level.

    if pygame.Rect(x_rect3, y_rect3, button_width, button_height).collidepoint(pygame.mouse.get_pos()):
        draw_covered_box(surface.py_surface, x_rect3, y_rect3, button_width, button_height)
        surface.py_surface.blit(next_level, (x_button3, y_button3))

        if pygame.mouse.get_pressed()[0]:
            if game.last_level + 1 < len(game.levels):
                game.cursor = game.last_level + 1
                game.stage = "Launched"
                game.load_interface()
            else:
                game.stage = "Main Menu"
