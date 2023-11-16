from menu.main_menu import Main_menu
from level.obstacle import colors
import pygame

def draw_main_menu(surface):
    pygame.font.init()
    height,width = (1280,720)
    surface.surface.fill(colors["darkblue"])
    font = pygame.font.Font("GamepauseddemoRegular-RpmY6.otf", 100)
    title = font.render('SPRINT - THE GAME', True, colors["white_yellow"])
    start_button = font.render('Start', True, colors["white_yellow"])
    surface.blit(title, (width/2 - title.get_width()/2, height/2 - title.get_height()/2))
    surface.blit(start_button, (width/2 - start_button.get_width()/2, height/2 + start_button.get_height()/2))
    pygame.display.update()


    