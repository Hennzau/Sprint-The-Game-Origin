from menu.main_menu import MainMenu
from level.obstacle import colors
from sound import sound_button, sound_game_launched
import pygame


def draw_main_menu(surface, menu, game):
    sound = False
    width, height = surface.width, surface.height
    button_width, button_height = 131, 30

    surface.py_surface.fill(colors["darkerblue"])
    backgroud = pygame.image.load('assets/images/Sprint_Background.png')
    surface.py_surface.blit(backgroud, (0,0))

    font = pygame.font.Font("assets/fonts/BulletTrace7-rppO.ttf", 60)
    font_levels = pygame.font.Font("assets/fonts/BulletTrace7-rppO.ttf", 30)

    title = font.render('SPRINT THE GAME', True, colors["ivory"])
    start_button = font.render(
        'Select Level to Start', True, colors["ivory"])

    x_title_extended = width / 2 - start_button.get_width() / 2
    y_title_extended = height / 2 - title.get_height() / 2 - 200
    title_extended_width = start_button.get_width()
    title_extended_height = title.get_height() + start_button.get_height() + 25

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

    surface.py_surface.blit(title, (width / 2 - title.get_width() / 2,
                                    height / 2 - title.get_height() / 2 - 200))

    surface.py_surface.blit(start_button, (width / 2 - start_button.get_width() /
                                           2, height / 2 + start_button.get_height() / 2 - 175))

    n = len(menu.levels)
    p = int(n / 2) + 1

    sound = True

    for i in range(p):
        level = f"Level " + str(i + 1)
        levels_button = font_levels.render(level, True, colors["ivory"])
        k = width / 2 - 131 / 2 + (- p + 2 * i) * 131 + 131
        pygame.draw.rect(surface.py_surface, colors["ivory"],
                         pygame.Rect(k - 26, height / 2 - (levels_button.get_height() / 2 - 100) - 26,
                                     button_width + 52, button_height + 52))
        pygame.draw.rect(surface.py_surface, colors["Black"],
                         pygame.Rect(k - 25, height / 2 - (levels_button.get_height() / 2 - 100) - 25,
                                     button_width + 50, button_height + 50))
        pygame.draw.rect(surface.py_surface, colors["ivory"],
                         pygame.Rect(k - 21, height / 2 - (levels_button.get_height() / 2 - 100) - 21,
                                     button_width + 42, button_height + 42))
        pygame.draw.rect(surface.py_surface, colors["darkblue"],
                         pygame.Rect(k - 20, height / 2 - (levels_button.get_height() / 2 - 100) - 20,
                                     button_width + 40, button_height + 40))

        surface.py_surface.blit(levels_button, (k, height / 2 - (levels_button.get_height() / 2 - 100)))

        if pygame.Rect(k - 26, height / 2 - (levels_button.get_height() / 2 - 100) - 26, button_width + 52,
                       button_height + 52).collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(surface.py_surface, colors["ivory"],
                             pygame.Rect(k - 26, height / 2 - (levels_button.get_height() / 2 - 100) - 26,
                                         button_width + 52, button_height + 52))
            pygame.draw.rect(surface.py_surface, colors["Black"],
                             pygame.Rect(k - 25, height / 2 - (levels_button.get_height() / 2 - 100) - 25,
                                         button_width + 50, button_height + 50))
            pygame.draw.rect(surface.py_surface, colors["ivory"],
                             pygame.Rect(k - 21, height / 2 - (levels_button.get_height() / 2 - 100) - 21,
                                         button_width + 42, button_height + 42))
            pygame.draw.rect(surface.py_surface, colors["Volkswagen Taupe"],
                             pygame.Rect(k - 20, height / 2 - (levels_button.get_height() / 2 - 100) - 20,
                                         button_width + 40, button_height + 40))
            surface.py_surface.blit(levels_button, (k, height / 2 - (levels_button.get_height() / 2 - 100)))

            sound = False
            
            if pygame.mouse.get_pressed()[0]:
                menu.level_selected = i
                menu.start_game = True
                menu.launch_game(game)
                sound_game_launched()


    if (n - p) > 0:
        for i in range(n - p):
            level = f"Level " + str(i + p + 1)
            levels_button = font_levels.render(level, True, colors["ivory"])
            k = width / 2 - 131 / 2 + (-(n - p) + 2 * i) * 131 + 131
            pygame.draw.rect(surface.py_surface, colors["ivory"],
                             pygame.Rect(k - 26, height / 2 - (levels_button.get_height() / 2 - 225) - 26,
                                         button_width + 52, button_height + 52))
            pygame.draw.rect(surface.py_surface, colors["Black"],
                             pygame.Rect(k - 25, height / 2 - (levels_button.get_height() / 2 - 225) - 25,
                                         button_width + 50, button_height + 50))
            pygame.draw.rect(surface.py_surface, colors["ivory"],
                             pygame.Rect(k - 21, height / 2 - (levels_button.get_height() / 2 - 225) - 21,
                                         button_width + 42, button_height + 42))
            pygame.draw.rect(surface.py_surface, colors["darkblue"],
                             pygame.Rect(k - 20, height / 2 - (levels_button.get_height() / 2 - 225) - 20,
                                         button_width + 40, button_height + 40))
            surface.py_surface.blit(levels_button, (k, height / 2 - (levels_button.get_height()) / 2 + 225))
            if pygame.Rect(k - 26, height / 2 - (levels_button.get_height() / 2 - 225) - 26, button_width + 52,
                           button_height + 52).collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(surface.py_surface, colors["ivory"],
                                 pygame.Rect(k - 26, height / 2 - (levels_button.get_height() / 2 - 225) - 26,
                                             button_width + 52, button_height + 52))
                pygame.draw.rect(surface.py_surface, colors["Black"],
                                 pygame.Rect(k - 25, height / 2 - (levels_button.get_height() / 2 - 225) - 25,
                                             button_width + 50, button_height + 50))
                pygame.draw.rect(surface.py_surface, colors["ivory"],
                                 pygame.Rect(k - 21, height / 2 - (levels_button.get_height() / 2 - 225) - 21,
                                             button_width + 42, button_height + 42))
                pygame.draw.rect(surface.py_surface, colors["Volkswagen Taupe"],
                                 pygame.Rect(k - 20, height / 2 - (levels_button.get_height() / 2 - 225) - 20,
                                             button_width + 40, button_height + 40))
                surface.py_surface.blit(levels_button, (k, height / 2 - (levels_button.get_height() / 2 - 225)))

                sound = False

                if pygame.mouse.get_pressed()[0]:
                    menu.level_selected = i + p
                    menu.start_game = True
                    menu.launch_game(game)
                    sound_game_launched()

    #Render Level Editor button

    
    level_editor = font_levels.render("Level Editor", True, colors["ivory"])
    x_lvled,y_lvled = (width  - level_editor.get_width() - 50 , height / 2 - level_editor.get_height() / 2 + 320)
    
    pygame.draw.rect(surface.py_surface, colors["ivory"],
                                 pygame.Rect(x_lvled - 21, y_lvled - 21 ,
                                             level_editor.get_width() + 42, level_editor.get_height() + 42))
    pygame.draw.rect(surface.py_surface, colors["Black"],
                                 pygame.Rect(x_lvled - 20, y_lvled - 20,
                                             level_editor.get_width() + 40, level_editor.get_height() + 40))
    pygame.draw.rect(surface.py_surface, colors["ivory"],
                                 pygame.Rect(x_lvled - 16, y_lvled - 16,
                                             level_editor.get_width() + 32, level_editor.get_height() + 32))
    pygame.draw.rect(surface.py_surface, colors["darkblue"],
                                 pygame.Rect(x_lvled - 15, y_lvled - 15,
                                             level_editor.get_width() + 30, level_editor.get_height() + 30))
    surface.py_surface.blit(level_editor, (x_lvled , y_lvled))
    
    if pygame.Rect(x_lvled - 21, y_lvled - 21 , level_editor.get_width() + 42, level_editor.get_height() + 42).collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(surface.py_surface, colors["ivory"],
                                 pygame.Rect(x_lvled - 21, y_lvled - 21 ,
                                             level_editor.get_width() + 42, level_editor.get_height() + 42))
        pygame.draw.rect(surface.py_surface, colors["Black"],
                                 pygame.Rect(x_lvled - 20, y_lvled - 20,
                                             level_editor.get_width() + 40, level_editor.get_height() + 40))
        pygame.draw.rect(surface.py_surface, colors["ivory"],
                                 pygame.Rect(x_lvled - 16, y_lvled - 16,
                                             level_editor.get_width() + 32, level_editor.get_height() + 32))
        pygame.draw.rect(surface.py_surface, colors["Volkswagen Taupe"],
                                 pygame.Rect(x_lvled - 15, y_lvled - 15,
                                             level_editor.get_width() + 30, level_editor.get_height() + 30))
        surface.py_surface.blit(level_editor, (x_lvled, y_lvled))
        
        if pygame.mouse.get_pressed()[0]:
                    menu.launch_level_editor(game)
                    sound_game_launched()

        sound = False 

    if not game.sound and not sound:
            game.sound = True
            sound_button()
    
    if sound:
         game.sound = False
