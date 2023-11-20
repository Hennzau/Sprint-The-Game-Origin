### Imports
import pygame
from render.surface import Surface, flip
from game import Game
from level.obstacle import colors
from sound import sound_button


### drawing function

def draw_end_menu(surface, game):
    # dimensions
    height = surface.height
    width = surface.width
    button_width = 250
    button_height = 80
    sound = True
    surface.py_surface.fill(colors["darkblue"])
    backgroud = pygame.image.load('assets/images/Sprint_Background.png')
    surface.py_surface.blit(backgroud, (0,0))

    # fonts
    font = pygame.font.Font("assets/fonts/BulletTrace7-rppO.ttf", 60)
    font_buttons = pygame.font.Font("assets/fonts/BulletTrace7-rppO.ttf", 30)

    # title
    title = font.render('VICTORY', True, colors["ivory"])
    
    x_title_extended = width / 2 - title.get_width() / 2
    y_title_extended = height / 2 - title.get_height() / 2 - 200
    title_extended_width = title.get_width()
    title_extended_height = title.get_height()

    pygame.draw.rect(surface.py_surface, colors["ivory"],
                                 pygame.Rect(x_title_extended - 40, y_title_extended - 40,
                                             title_extended_width + 80, title_extended_height + 80))

    pygame.draw.rect(surface.py_surface, colors["Black"],
                                 pygame.Rect(x_title_extended - 39, y_title_extended - 39,
                                             title_extended_width + 78, title_extended_height + 78))
    
    pygame.draw.rect(surface.py_surface, colors["ivory"],
                                 pygame.Rect(x_title_extended - 25, y_title_extended - 25,
                                             title_extended_width + 50, title_extended_height + 50))
    
    pygame.draw.rect(surface.py_surface, colors["darkblue"],
                                 pygame.Rect(x_title_extended - 24, y_title_extended - 24,
                                             title_extended_width + 48, title_extended_height + 48))
    
    surface.py_surface.blit(title, ((width - title.get_width()) / 2,
                                    (height - title.get_height()) / 2 - 200))

    # play again button
    play_again_button = font_buttons.render("Play again", True, colors["ivory"])

    text_width = play_again_button.get_width()
    text_height = play_again_button.get_height()

    x_button1 = (width - play_again_button.get_width()) / 2 - 200
    y_button1 = (height - play_again_button.get_height()) / 2

    x_rect1 = x_button1 - (button_width - text_width) / 2
    y_rect1 = y_button1 - (button_height - text_height) / 2

    pygame.draw.rect(surface.py_surface, colors["ivory"], pygame.Rect(x_rect1, y_rect1, button_width, button_height))
    pygame.draw.rect(surface.py_surface, colors["Black"],
                     pygame.Rect(x_rect1 + 1, y_rect1 + 1, button_width - 2, button_height - 2))
    pygame.draw.rect(surface.py_surface, colors["ivory"],
                     pygame.Rect(x_rect1 + 5, y_rect1 + 5, button_width - 10, button_height - 10))
    pygame.draw.rect(surface.py_surface, colors["darkblue"],
                     pygame.Rect(x_rect1 + 6, y_rect1 + 6, button_width - 12, button_height - 12))

    surface.py_surface.blit(play_again_button, (x_button1, y_button1))

    # menu button

    menu_button = font_buttons.render("Menu", True, colors["ivory"])

    text_width = menu_button.get_width()
    text_height = menu_button.get_height()

    x_button2 = (width - menu_button.get_width()) / 2 + 200
    y_button2 = (height - menu_button.get_height()) / 2

    x_rect2 = x_button2 - (button_width - text_width) / 2
    y_rect2 = y_button2 - (button_height - text_height) / 2

    pygame.draw.rect(surface.py_surface, colors["ivory"], pygame.Rect(x_rect2, y_rect2, button_width, button_height))
    pygame.draw.rect(surface.py_surface, colors["Black"],
                     pygame.Rect(x_rect2 + 1, y_rect2 + 1, button_width - 2, button_height - 2))
    pygame.draw.rect(surface.py_surface, colors["ivory"],
                     pygame.Rect(x_rect2 + 5, y_rect2 + 5, button_width - 10, button_height - 10))
    pygame.draw.rect(surface.py_surface, colors["darkblue"],
                     pygame.Rect(x_rect2 + 6, y_rect2 + 6, button_width - 12, button_height - 12))

    surface.py_surface.blit(menu_button, (x_button2, y_button2))

    # next level button
    # TODO: Henrik you have to 'copy' code from above to make a 'next level' button
    #  that will make the user go to the next level

    if pygame.Rect(x_rect1, y_rect1, button_width, button_height).collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(surface.py_surface, colors["ivory"],
                         pygame.Rect(x_rect1, y_rect1, button_width, button_height))
        pygame.draw.rect(surface.py_surface, colors["Black"],
                         pygame.Rect(x_rect1 + 1, y_rect1 + 1, button_width - 2, button_height - 2))
        pygame.draw.rect(surface.py_surface, colors["ivory"],
                         pygame.Rect(x_rect1 + 5, y_rect1 + 5, button_width - 10, button_height - 10))
        pygame.draw.rect(surface.py_surface, colors["Volkswagen Taupe"],
                         pygame.Rect(x_rect1 + 6, y_rect1 + 6, button_width - 12, button_height - 12))

        surface.py_surface.blit(play_again_button, (x_button1, y_button1))
        if pygame.mouse.get_pressed()[0]:
            game.cursor = game.last_level
            game.stage = "Launched"
            game.load_interface()
        sound = False

    if pygame.Rect(x_rect2, y_rect2, button_width, button_height).collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(surface.py_surface, colors["ivory"],
                         pygame.Rect(x_rect2, y_rect2, button_width, button_height))
        pygame.draw.rect(surface.py_surface, colors["Black"],
                         pygame.Rect(x_rect2 + 1, y_rect2 + 1, button_width - 2, button_height - 2))
        pygame.draw.rect(surface.py_surface, colors["ivory"],
                         pygame.Rect(x_rect2 + 5, y_rect2 + 5, button_width - 10, button_height - 10))
        pygame.draw.rect(surface.py_surface, colors["Volkswagen Taupe"],
                         pygame.Rect(x_rect2 + 6, y_rect2 + 6, button_width - 12, button_height - 12))

        surface.py_surface.blit(menu_button, (x_button2, y_button2))
        if pygame.mouse.get_pressed()[0]:
            game.stage = "Main Menu"
        sound = False

    if not game.sound and not sound:
            game.sound = True
            sound_button()
    
    if sound:
         game.sound = False
    

    # TODO: Henrik, there you have to do the 'logical part' of the button : copy the code from above to make
    # the button change when the mouse is on it, and when the mouse is pressed, use this :
    # game.cursor = ... [increase game.cursor if possible]
    # game.stage = "Launched"
    # game.load_interface()
