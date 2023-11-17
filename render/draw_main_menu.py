from menu.main_menu import Main_menu
from level.obstacle import colors
import pygame


def draw_main_menu(surface, menu):
    pygame.font.init()

    width, height = surface.width, surface.height

    surface.py_surface.fill(colors["darkblue"])

    font = pygame.font.Font("assets/fonts/GamepauseddemoRegular-RpmY6.otf", 60)
    font_levels = pygame.font.Font("assets/fonts/BulletTrace7-rppO.ttf", 30)

    title = font.render('SPRINT THE GAME', True, colors["ivoire"])
    start_button = font.render(
        'Press Space to Start', True, colors["ivoire"])


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
        surface.blit(levels_button, (k, height / 2 - (levels_button.get_height()/2 - 100)))

    if (n-p) > 0:    
        for i in range(n-p):
            level = f"Level " + str(i+p+1)
            levels_button = font_levels.render(level, True, colors["ivoire"])
            k = width/2 - 131/2 + (-(n-p)+2*i)*131 + 131
            surface.blit(levels_button, (k, height/2 - (levels_button.get_height())/2 + 200))


    pygame.display.update()
