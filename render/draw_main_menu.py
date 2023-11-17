from menu.main_menu import Main_menu
from level.obstacle import colors
import pygame


def draw_main_menu(surface, menu, game):
    pygame.font.init()

    width, height = surface.width, surface.height
    button_width, button_height = 131, 30

    surface.py_surface.fill(colors["darkerblue"])

    font = pygame.font.Font("assets/fonts/BulletTrace7-rppO.ttf", 60)
    font_levels = pygame.font.Font("assets/fonts/BulletTrace7-rppO.ttf", 30)

    title = font.render('SPRINT THE GAME', True, colors["ivoire"])
    start_button = font.render(
        'Select Level to Start', True, colors["ivoire"])


    surface.blit(title, (width / 2 - title.get_width() / 2,
                         height / 2 - title.get_height() / 2 - 200))

    surface.blit(start_button, (width / 2 - start_button.get_width() /
                                2, height / 2 + start_button.get_height() / 2 - 175))
    
    n = len(menu.levels)
    p = int(n/2)

    for i in range(p):
        level = f"Level " + str(i+1)
        levels_button = font_levels.render(level, True, colors["ivoire"])
        k = width/2 - 131/2 + (- p + 2*i)*131 + 131
        pygame.draw.rect(surface.py_surface, colors["ivoire"], pygame.Rect(k - 26 , height / 2 - (levels_button.get_height()/2 - 100) - 26, button_width + 52, button_height + 52 ))
        pygame.draw.rect(surface.py_surface, colors["Black"], pygame.Rect(k - 25 , height / 2 - (levels_button.get_height()/2 - 100) - 25, button_width + 50, button_height + 50 ))
        pygame.draw.rect(surface.py_surface, colors["ivoire"], pygame.Rect(k - 21 , height / 2 - (levels_button.get_height()/2 - 100) - 21, button_width + 42, button_height + 42 ))
        pygame.draw.rect(surface.py_surface, colors["darkblue"], pygame.Rect(k - 20 , height / 2 - (levels_button.get_height()/2 - 100) - 20, button_width + 40, button_height + 40 ))
        surface.blit(levels_button, (k, height / 2 - (levels_button.get_height()/2 - 100)))
        if pygame.Rect(k - 26 , height / 2 - (levels_button.get_height()/2 - 100) - 26, button_width + 52, button_height + 52 ).collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(surface.py_surface, colors["ivoire"], pygame.Rect(k - 26 , height / 2 - (levels_button.get_height()/2 - 100) - 26, button_width + 52, button_height + 52 ))
            pygame.draw.rect(surface.py_surface, colors["Black"], pygame.Rect(k - 25 , height / 2 - (levels_button.get_height()/2 - 100) - 25, button_width + 50, button_height + 50 ))
            pygame.draw.rect(surface.py_surface, colors["ivoire"], pygame.Rect(k - 21 , height / 2 - (levels_button.get_height()/2 - 100) - 21, button_width + 42, button_height + 42 ))
            pygame.draw.rect(surface.py_surface, colors["Volkswagen Taupe"], pygame.Rect(k - 20 , height / 2 - (levels_button.get_height()/2 - 100) - 20, button_width + 40, button_height + 40 ))
            surface.blit(levels_button, (k, height / 2 - (levels_button.get_height()/2 - 100)))
            if pygame.mouse.get_pressed()[0] : 
                menu.level_selected = i
                menu.start_game = True
                menu.launch_game(game)



    if (n-p) > 0:    
        for i in range(n-p):
            level = f"Level " + str(i+p+1)
            levels_button = font_levels.render(level, True, colors["ivoire"])
            k = width/2 - 131/2 + (-(n-p)+2*i)*131 + 131
            pygame.draw.rect(surface.py_surface, colors["ivoire"], pygame.Rect(k - 26 , height / 2 - (levels_button.get_height()/2 - 225) - 26, button_width + 52, button_height + 52 ))
            pygame.draw.rect(surface.py_surface, colors["Black"], pygame.Rect(k - 25 , height / 2 - (levels_button.get_height()/2 - 225) - 25, button_width + 50, button_height + 50 ))
            pygame.draw.rect(surface.py_surface, colors["ivoire"], pygame.Rect(k - 21 , height / 2 - (levels_button.get_height()/2 - 225) - 21, button_width + 42, button_height + 42 ))
            pygame.draw.rect(surface.py_surface, colors["darkblue"], pygame.Rect(k - 20 , height / 2 - (levels_button.get_height()/2 - 225) - 20, button_width + 40, button_height + 40 ))
            surface.blit(levels_button, (k, height/2 - (levels_button.get_height())/2 + 225))
            if pygame.Rect(k - 26 , height / 2 - (levels_button.get_height()/2 - 225) - 26, button_width + 52, button_height + 52 ).collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(surface.py_surface, colors["ivoire"], pygame.Rect(k - 26 , height / 2 - (levels_button.get_height()/2 - 225) - 26, button_width + 52, button_height + 52 ))
                pygame.draw.rect(surface.py_surface, colors["Black"], pygame.Rect(k - 25 , height / 2 - (levels_button.get_height()/2 - 225) - 25, button_width + 50, button_height + 50 ))
                pygame.draw.rect(surface.py_surface, colors["ivoire"], pygame.Rect(k - 21 , height / 2 - (levels_button.get_height()/2 - 225) - 21, button_width + 42, button_height + 42 ))
                pygame.draw.rect(surface.py_surface, colors["Volkswagen Taupe"], pygame.Rect(k - 20 , height / 2 - (levels_button.get_height()/2 - 225) - 20, button_width + 40, button_height + 40 ))
                surface.blit(levels_button, (k, height / 2 - (levels_button.get_height()/2 - 225)))
                if pygame.mouse.get_pressed()[0] : 
                    menu.level_selected = i+p
                    menu.start_game = True
                    menu.launch_game(game)
            
