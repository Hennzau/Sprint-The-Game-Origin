### Imports
import pygame
from surface import Surface, flip


colors = {"red": (220, 20, 60), "blue": (106, 90, 205), "green": (154, 205, 50), "yellow": (255, 215, 0),
          "darkgrey": (105, 105, 105), "darkblue": (2, 4, 55), "white_yellow": (255,255,204)}

surface = Surface(1280, 720, "test")

###characteristics
height = 500
width = 800


### drawing function

def draw_end_menu(surface):
    x_position = (surface.width-width)/2
    y_position = (surface.height-height)/2
    pygame.draw.rect(surface.surface,colors["darkblue"],pygame.Rect(x_position,y_position,width,height))

    # Victory
    font_victory = pygame.font.Font("GamepauseddemoRegular-RpmY6.otf", 80)
    victory = font_victory.render("VICTORY", True, colors["white_yellow"])

    # info 1 : "to play again press r"
    font_info1 = pygame.font.Font("GamepauseddemoRegular-RpmY6.otf", 50)
    info1 = font_info1.render("To play again press R", True, colors["white_yellow"])

    # info 2 : "to return to the main menu press M"
    font_info2 = pygame.font.Font("GamepauseddemoRegular-RpmY6.otf", 50)
    info2 = font_info2.render("To return to the main menu press M", True, colors["white_yellow"])

    # blit
    surface.surface.blit(victory, (x_position+(width-victory.get_width())/2,y_position + 50))
    surface.surface.blit(info1, (x_position+(width-info1.get_width())/2,y_position + 200))
    surface.surface.blit(info2, (x_position+(width-info2.get_width())/2,y_position + 250))

#continuer = True
#while continuer :
#    surface.clear(colors["darkblue"])
#    draw_end_menu(surface)
#    flip()
#    for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                continuer = False