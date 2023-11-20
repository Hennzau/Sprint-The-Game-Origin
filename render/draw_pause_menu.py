### Imports
import pygame
from render.surface import Surface, flip
from game import Game
from level.obstacle import colors
from sound import sound_button

### drawing function

def draw_pause_menu(surface, game):
    # dimensions
    height, width= surface.height, surface.width
    button_width, button_height = 250, 80
    sound = True
    
    surface.py_surface.fill(colors["darkblue"])

    # fonts
    font = pygame.font.Font("assets/fonts/BulletTrace7-rppO.ttf", 60)
    font_buttons = pygame.font.Font("assets/fonts/BulletTrace7-rppO.ttf", 30)

    # title
    title = font.render('PAUSE', True, colors["ivory"])
    surface.py_surface.blit(title, ((width - title.get_width()) / 2,
                                    (height - title.get_height()) / 2 - 200))

    # resume button
    resume_button = font_buttons.render("Resume", True, colors["ivory"])

    text_width = resume_button.get_width()
    text_height = resume_button.get_height()

    x_button1 = (width - resume_button.get_width()) / 2 - 200
    y_button1 = (height - resume_button.get_height()) / 2

    x_rect1 = x_button1 - (button_width - text_width) / 2
    y_rect1 = y_button1 - (button_height - text_height) / 2

    pygame.draw.rect(surface.py_surface, colors["ivory"], pygame.Rect(x_rect1, y_rect1, button_width, button_height))
    pygame.draw.rect(surface.py_surface, colors["Black"],
                     pygame.Rect(x_rect1 + 1, y_rect1 + 1, button_width - 2, button_height - 2))
    pygame.draw.rect(surface.py_surface, colors["ivory"],
                     pygame.Rect(x_rect1 + 5, y_rect1 + 5, button_width - 10, button_height - 10))
    pygame.draw.rect(surface.py_surface, colors["darkblue"],
                     pygame.Rect(x_rect1 + 6, y_rect1 + 6, button_width - 12, button_height - 12))

    surface.py_surface.blit(resume_button, (x_button1, y_button1))
    
    if pygame.Rect(x_rect1, y_rect1, button_width, button_height).collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(surface.py_surface, colors["ivory"],
                        pygame.Rect(x_rect1, y_rect1, button_width, button_height))
        pygame.draw.rect(surface.py_surface, colors["Black"],
                        pygame.Rect(x_rect1 + 1, y_rect1 + 1, button_width - 2, button_height - 2))
        pygame.draw.rect(surface.py_surface, colors["ivory"],
                        pygame.Rect(x_rect1 + 5, y_rect1 + 5, button_width - 10, button_height - 10))
        pygame.draw.rect(surface.py_surface, colors["Volkswagen Taupe"],
                         pygame.Rect(x_rect1 + 6, y_rect1 + 6, button_width - 12, button_height - 12))

        surface.py_surface.blit(resume_button, (x_button1, y_button1))
        if pygame.mouse.get_pressed()[0]:
           
            "on retorurne à la partie (faire appel à la partie stockée)"
        
        sound = False

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