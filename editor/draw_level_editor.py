from editor.level_editor import LevelEditor
import pygame
from level.obstacle import pixel_size, colors

def draw_level_editor (level_editor, surface):
    level_editor.level_render.render(surface.py_surface)

    ## color choice

    #button
    pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(surface.width-120, 60, pixel_size+40, 5*pixel_size+4*40+40))
    pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(surface.width-119, 61, pixel_size+38, 5*pixel_size+4*40+38))
    pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(surface.width-115, 65, pixel_size+30, 5*pixel_size+4*40+30))
    pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(surface.width-114, 66, pixel_size+28, 5*pixel_size+4*40+28))
    
    #color rectangles
    pygame.draw.rect(surface.py_surface, colors["red"], 
                     pygame.Rect(surface.width-100, 80, pixel_size, pixel_size))
    pygame.draw.rect(surface.py_surface, colors["yellow"], 
                     pygame.Rect(surface.width-100, 160, pixel_size, pixel_size))
    pygame.draw.rect(surface.py_surface, colors["green"], 
                     pygame.Rect(surface.width-100, 240, pixel_size, pixel_size))
    pygame.draw.rect(surface.py_surface, colors["blue"], 
                     pygame.Rect(surface.width-100, 320, pixel_size, pixel_size))
    pygame.draw.rect(surface.py_surface, colors["darkgrey"], 
                     pygame.Rect(surface.width-100, 400, pixel_size, pixel_size))
    
    if pygame.Rect(surface.width-100, 80, pixel_size, pixel_size).collidepoint(pygame.mouse.get_pos()) or level_editor.color_cursor == 0:
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(surface.width-100-1, 80-1, pixel_size+2, pixel_size+2))
        pygame.draw.rect(surface.py_surface, colors[level_editor.colors[0]], 
                     pygame.Rect(surface.width-100, 80, pixel_size, pixel_size))
        if pygame.mouse.get_pressed()[0]:
            level_editor.color_cursor = 0

    if pygame.Rect(surface.width-100, 160, pixel_size, pixel_size).collidepoint(pygame.mouse.get_pos()) or level_editor.color_cursor == 1:
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(surface.width-100-1, 160-1, pixel_size+2, pixel_size+2))
        pygame.draw.rect(surface.py_surface, colors[level_editor.colors[1]], 
                     pygame.Rect(surface.width-100, 160, pixel_size, pixel_size))
        if pygame.mouse.get_pressed()[0]:
            level_editor.color_cursor = 1

    if pygame.Rect(surface.width-100, 240, pixel_size, pixel_size).collidepoint(pygame.mouse.get_pos()) or level_editor.color_cursor == 2:
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(surface.width-100-1, 240-1, pixel_size+2, pixel_size+2))
        pygame.draw.rect(surface.py_surface, colors[level_editor.colors[2]], 
                     pygame.Rect(surface.width-100, 240, pixel_size, pixel_size))
        if pygame.mouse.get_pressed()[0]:
            level_editor.color_cursor = 2

    if pygame.Rect(surface.width-100, 320, pixel_size, pixel_size).collidepoint(pygame.mouse.get_pos()) or level_editor.color_cursor == 3:
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(surface.width-100-1, 320-1, pixel_size+2, pixel_size+2))
        pygame.draw.rect(surface.py_surface, colors[level_editor.colors[3]], 
                     pygame.Rect(surface.width-100, 320, pixel_size, pixel_size))
        if pygame.mouse.get_pressed()[0]:
            level_editor.color_cursor = 3

    if pygame.Rect(surface.width-100, 400, pixel_size, pixel_size).collidepoint(pygame.mouse.get_pos()) or level_editor.color_cursor == 4:
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(surface.width-100-1, 400-1, pixel_size+2, pixel_size+2))
        pygame.draw.rect(surface.py_surface, colors[level_editor.colors[4]], 
                     pygame.Rect(surface.width-100, 400, pixel_size, pixel_size))
        if pygame.mouse.get_pressed()[0]:
            level_editor.color_cursor = 4

    ## type choice
    font_buttons = pygame.font.Font("assets/fonts/BulletTrace7-rppO.ttf", 30)

    #obstacle
    obstacle_button = font_buttons.render ("Obstacle", True, colors["ivory"])
    obstacle_width = obstacle_button.get_width()
    obstacle_height = obstacle_button.get_height()
    x_rect1 = surface.width-450
    y_rect1 = 60

    pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect1, y_rect1, obstacle_width + 30, obstacle_height +30 ))
    pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(x_rect1+1, y_rect1+1, obstacle_width+28, obstacle_height+28))
    pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect1+5, y_rect1+5, obstacle_width+20, obstacle_height+20))
    pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(x_rect1+6, y_rect1+6, obstacle_width+18, obstacle_height+18))
    
    surface.py_surface.blit(obstacle_button, (x_rect1+15, y_rect1+15))

    if pygame.Rect(x_rect1, y_rect1, obstacle_width+30, obstacle_height+30).collidepoint(pygame.mouse.get_pos()) or level_editor.color_switcher == False:
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect1, y_rect1, obstacle_width + 30, obstacle_height +30 ))
        pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(x_rect1+1, y_rect1+1, obstacle_width+28, obstacle_height+28))
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect1+5, y_rect1+5, obstacle_width+20, obstacle_height+20))
        pygame.draw.rect(surface.py_surface, colors["Volkswagen Taupe"], 
                     pygame.Rect(x_rect1+6, y_rect1+6, obstacle_width+18, obstacle_height+18))

        surface.py_surface.blit(obstacle_button, (x_rect1+15, y_rect1+15))

        if pygame.mouse.get_pressed()[0]:
            level_editor.color_switcher = False

    #color switcher

    switcher_button = font_buttons.render ("Color switcher", True, colors["ivory"])
    switcher_width = switcher_button.get_width()
    switcher_height = switcher_button.get_height()
    x_rect2 = x_rect1
    y_rect2 = 60+obstacle_height+60

    pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect2, y_rect2, switcher_width + 30, switcher_height +30 ))
    pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(x_rect2+1, y_rect2+1, switcher_width+28, switcher_height+28))
    pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect2+5, y_rect2+5, switcher_width+20, switcher_height+20))
    pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(x_rect2+6, y_rect2+6, switcher_width+18, switcher_height+18))
    
    surface.py_surface.blit(switcher_button, (x_rect2+15, y_rect2+15))

    if pygame.Rect(x_rect2, y_rect2, switcher_width+30, switcher_height+30).collidepoint(pygame.mouse.get_pos()) or level_editor.color_switcher == True:
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect2, y_rect2, switcher_width + 30, switcher_height +30 ))
        pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(x_rect2+1, y_rect2+1, switcher_width+28, switcher_height+28))
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect2+5, y_rect2+5, switcher_width+20, switcher_height+20))
        pygame.draw.rect(surface.py_surface, colors["Volkswagen Taupe"], 
                     pygame.Rect(x_rect2+6, y_rect2+6, switcher_width+18, switcher_height+18))
        
        surface.py_surface.blit(switcher_button, (x_rect2+15, y_rect2+15))

        if pygame.mouse.get_pressed()[0]:
            level_editor.color_switcher = True
    
