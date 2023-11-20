from editor.level_editor import LevelEditor
import pygame
from level.obstacle import pixel_size, colors
from game import Game

def draw_level_editor (level_editor, surface, game):
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
    
    # when mouse is on the button or the button is selected

    #red
    if pygame.Rect(surface.width-100, 80, pixel_size, pixel_size).collidepoint(pygame.mouse.get_pos()) or level_editor.color_cursor == 0:
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(surface.width-100-1, 80-1, pixel_size+2, pixel_size+2))
        pygame.draw.rect(surface.py_surface, colors[level_editor.colors[0]], 
                     pygame.Rect(surface.width-100, 80, pixel_size, pixel_size))
        if pygame.mouse.get_pressed()[0]:
            level_editor.color_cursor = 0

    #yellow
    if pygame.Rect(surface.width-100, 160, pixel_size, pixel_size).collidepoint(pygame.mouse.get_pos()) or level_editor.color_cursor == 1:
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(surface.width-100-1, 160-1, pixel_size+2, pixel_size+2))
        pygame.draw.rect(surface.py_surface, colors[level_editor.colors[1]], 
                     pygame.Rect(surface.width-100, 160, pixel_size, pixel_size))
        if pygame.mouse.get_pressed()[0]:
            level_editor.color_cursor = 1

    #green
    if pygame.Rect(surface.width-100, 240, pixel_size, pixel_size).collidepoint(pygame.mouse.get_pos()) or level_editor.color_cursor == 2:
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(surface.width-100-1, 240-1, pixel_size+2, pixel_size+2))
        pygame.draw.rect(surface.py_surface, colors[level_editor.colors[2]], 
                     pygame.Rect(surface.width-100, 240, pixel_size, pixel_size))
        if pygame.mouse.get_pressed()[0]:
            level_editor.color_cursor = 2

    #blue
    if pygame.Rect(surface.width-100, 320, pixel_size, pixel_size).collidepoint(pygame.mouse.get_pos()) or level_editor.color_cursor == 3:
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(surface.width-100-1, 320-1, pixel_size+2, pixel_size+2))
        pygame.draw.rect(surface.py_surface, colors[level_editor.colors[3]], 
                     pygame.Rect(surface.width-100, 320, pixel_size, pixel_size))
        if pygame.mouse.get_pressed()[0]:
            level_editor.color_cursor = 3

    #grey (not clickable if color switcher = True)
    if pygame.Rect(surface.width-100, 400, pixel_size, pixel_size).collidepoint(pygame.mouse.get_pos()) or level_editor.color_cursor == 4:
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(surface.width-100-1, 400-1, pixel_size+2, pixel_size+2))
        pygame.draw.rect(surface.py_surface, colors[level_editor.colors[4]], 
                     pygame.Rect(surface.width-100, 400, pixel_size, pixel_size))
        if pygame.mouse.get_pressed()[0] and level_editor.color_switcher == False:
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

    #if mouse is on the button or the button is selected
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

    #if mouse is on the button or the button  is selected
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

        if pygame.mouse.get_pressed()[0] and level_editor.color_cursor != 4:
            level_editor.color_switcher = True
    
    if pygame.Rect(0,0, level_editor.size[0]*pixel_size, level_editor.size[1]*pixel_size).collidepoint(pygame.mouse.get_pos()):
        i = int(pygame.mouse.get_pos()[0]/pixel_size)
        j = int(pygame.mouse.get_pos()[1]/pixel_size)
        if level_editor.color_switcher == False :
            pygame.draw.rect(surface.py_surface, colors[level_editor.colors[level_editor.color_cursor]], 
                     pygame.Rect(i*pixel_size, j*pixel_size, pixel_size, pixel_size))
        if level_editor.color_switcher == True :
            surface.py_surface.blit(level_editor.level_render.grid_render.base_color_switcher, (i*pixel_size, j*pixel_size))
            pygame.draw.circle(surface.py_surface, colors["darkblue"],
                                           (i * pixel_size + pixel_size / 2, j * pixel_size + pixel_size / 2),
                                           pixel_size / 2.5, 0)

            pygame.draw.circle(surface.py_surface, colors[level_editor.colors[level_editor.color_cursor]],
                                           (i * pixel_size + pixel_size / 2, j * pixel_size + pixel_size / 2),
                                           pixel_size / 4, 0)
            
    ## add player

    add_player_button = font_buttons.render ("Add player", True, colors["ivory"])
    add_player_width = add_player_button.get_width()
    add_player_height = add_player_button.get_height()
    x_rect3 = 100
    y_rect3 = surface.height-200

    pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect3, y_rect3, add_player_width + 30, add_player_height +30 ))
    pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(x_rect3+1, y_rect3+1, add_player_width+28, add_player_height+28))
    pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect3+5, y_rect3+5, add_player_width+20, add_player_height+20))
    pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(x_rect3+6, y_rect3+6, add_player_width+18, add_player_height+18))
    
    surface.py_surface.blit(add_player_button, (x_rect3+15, y_rect3+15))

    #if mouse is on the button
    if pygame.Rect(x_rect3, y_rect3, add_player_width + 30, add_player_height +30 ).collidepoint(pygame.mouse.get_pos()) and level_editor.color_cursor != 4:
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect3, y_rect3, add_player_width + 30, add_player_height +30 ))
        pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(x_rect3+1, y_rect3+1, add_player_width+28, add_player_height+28))
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect3+5, y_rect3+5, add_player_width+20, add_player_height+20))
        pygame.draw.rect(surface.py_surface, colors["Volkswagen Taupe"], 
                     pygame.Rect(x_rect3+6, y_rect3+6, add_player_width+18, add_player_height+18))
    
        surface.py_surface.blit(add_player_button, (x_rect3+15, y_rect3+15))

        if pygame.mouse.get_pressed()[0]  :
            level_editor.select_add_player = True
            level_editor.select_start = None
            level_editor.select_end = None

    if pygame.Rect(0,0, level_editor.size[0]*pixel_size, level_editor.size[1]*pixel_size).collidepoint(pygame.mouse.get_pos()) and level_editor.select_add_player and level_editor.select_start == None:
        if pygame.mouse.get_pressed()[0] :
            i = int(pygame.mouse.get_pos()[0]/pixel_size)
            j = int(pygame.mouse.get_pos()[1]/pixel_size)
            level_editor.select_start = (i,j)

    if pygame.Rect(0,0,level_editor.size[0]*pixel_size, level_editor.size[1]*pixel_size).collidepoint(pygame.mouse.get_pos()) and level_editor.select_add_player and level_editor.select_start != None:
        if pygame.mouse.get_pressed()[0] :
            i = int(pygame.mouse.get_pos()[0]/pixel_size)
            j = int(pygame.mouse.get_pos()[1]/pixel_size)
            if level_editor.select_start != (i,j):
                level_editor.select_end = (i,j)
                level_editor.new_player (level_editor.colors[level_editor.color_cursor], level_editor.select_start, level_editor.select_end)
                level_editor.select_add_player = False

            


    ## delete player 

    delete_player_button = font_buttons.render ("Delete player", True, colors["ivory"])
    delete_player_width = delete_player_button.get_width()
    delete_player_height = delete_player_button.get_height()
    x_rect4 = 100
    y_rect4 = surface.height-100

    pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect4, y_rect4, delete_player_width + 30, delete_player_height +30 ))
    pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(x_rect4+1, y_rect4+1, delete_player_width+28, delete_player_height+28))
    pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect4+5, y_rect4+5, delete_player_width+20, delete_player_height+20))
    pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(x_rect4+6, y_rect4+6, delete_player_width+18, delete_player_height+18))
    
    surface.py_surface.blit(delete_player_button, (x_rect4+15, y_rect4+15))

    if pygame.Rect(x_rect4, y_rect4, delete_player_width + 30, delete_player_height +30 ).collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect4, y_rect4, delete_player_width + 30, delete_player_height +30 ))
        pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(x_rect4+1, y_rect4+1, delete_player_width+28, delete_player_height+28))
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect4+5, y_rect4+5, delete_player_width+20, delete_player_height+20))
        pygame.draw.rect(surface.py_surface, colors["Volkswagen Taupe"], 
                     pygame.Rect(x_rect4+6, y_rect4+6, delete_player_width+18, delete_player_height+18))
    
        surface.py_surface.blit(delete_player_button, (x_rect4+15, y_rect4+15))

        if pygame.mouse.get_pressed()[0] and len (level_editor.level.players)!=0:
            level_editor.remove_last_player()



    ## save button

    save_button = font_buttons.render ("Save level", True, colors["ivory"])
    save_width = save_button.get_width()
    save_height = save_button.get_height()
    x_rect5 = surface.width - save_width-50
    y_rect5 = surface.height-200

    pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect5, y_rect5, save_width + 30, save_height +30 ))
    pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(x_rect5+1, y_rect5+1, save_width+28, save_height+28))
    pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect5+5, y_rect5+5, save_width+20, save_height+20))
    pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(x_rect5+6, y_rect5+6, save_width+18, save_height+18))
    
    surface.py_surface.blit(save_button, (x_rect5+15, y_rect5+15))
    if pygame.Rect(x_rect5+5, y_rect5+5, save_width+20, save_height+20).collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect5, y_rect5, save_width + 30, save_height +30 ))
        pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(x_rect5+1, y_rect5+1, save_width+28, save_height+28))
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect5+5, y_rect5+5, save_width+20, save_height+20))
        pygame.draw.rect(surface.py_surface, colors["Volkswagen Taupe"], 
                     pygame.Rect(x_rect5+6, y_rect5+6, save_width+18, save_height+18))
        surface.py_surface.blit(save_button, (x_rect5+15, y_rect5+15))

        if pygame.mouse.get_pressed()[0]:
            level_editor.save()
            game.stage = "Main Menu"
        
    ## Exit button
    exit_button = font_buttons.render ("Exit", True, colors["ivory"])
    exit_width = exit_button.get_width()
    exit_height = exit_button.get_height()
    x_rect6 = surface.width - save_width-50
    y_rect6 = surface.height-100

    pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect6, y_rect6, exit_width + 30, exit_height +30 ))
    pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(x_rect6+1, y_rect6+1, exit_width+28, exit_height+28))
    pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect6+5, y_rect6+5, exit_width+20, exit_height+20))
    pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(x_rect6+6, y_rect6+6, exit_width+18, exit_height+18))
    
    surface.py_surface.blit(exit_button, (x_rect6+15, y_rect6+15))

    if pygame.Rect(x_rect6, y_rect6, exit_width + 30, exit_height +30).collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect6, y_rect6, exit_width + 30, exit_height +30 ))
        pygame.draw.rect(surface.py_surface, colors["darkblue"], 
                     pygame.Rect(x_rect6+1, y_rect6+1, exit_width+28, exit_height+28))
        pygame.draw.rect(surface.py_surface, colors["ivory"], 
                     pygame.Rect(x_rect6+5, y_rect6+5, exit_width+20, exit_height+20))
        pygame.draw.rect(surface.py_surface, colors["Volkswagen Taupe"], 
                     pygame.Rect(x_rect6+6, y_rect6+6, exit_width+18, exit_height+18))
        surface.py_surface.blit(exit_button, (x_rect6+15, y_rect6+15))

        if pygame.mouse.get_pressed()[0]:
            pygame.time.wait(500)
            game.stage = "Main Menu"
        


        
            


