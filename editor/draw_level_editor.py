import pygame

from level.obstacle import pixel_size, colors

from render.box import draw_covered_box, draw_empty_box


def draw_level_editor(level_editor, surface, game):
    """
    the draw_level_editor function draw the given level_editor interface on a surface.
    It also manages actions on the game

    Parameters:
    level_editor (LevelEditor): the LevelEditor object that should be draw
    surface (Surface): the surface on which you want to draw the level_editor
    game (Game): the Game object
    """

    level_editor.level_render.render(surface.py_surface)

    # color choice

    # button

    draw_empty_box(surface.py_surface, surface.width - 120, 60, pixel_size + 40, 5 * pixel_size + 4 * 40 + 40)

    # color rectangles

    pygame.draw.rect(surface.py_surface, colors["red"],
                     pygame.Rect(surface.width - 100, 80, pixel_size, pixel_size))
    pygame.draw.rect(surface.py_surface, colors["yellow"],
                     pygame.Rect(surface.width - 100, 160, pixel_size, pixel_size))
    pygame.draw.rect(surface.py_surface, colors["green"],
                     pygame.Rect(surface.width - 100, 240, pixel_size, pixel_size))
    pygame.draw.rect(surface.py_surface, colors["blue"],
                     pygame.Rect(surface.width - 100, 320, pixel_size, pixel_size))
    pygame.draw.rect(surface.py_surface, colors["darkgrey"],
                     pygame.Rect(surface.width - 100, 400, pixel_size, pixel_size))

    # when mouse is on the button or the button is selected

    # red
    if pygame.Rect(surface.width - 100, 80, pixel_size, pixel_size).collidepoint(
            pygame.mouse.get_pos()) or level_editor.color_cursor == 0:
        pygame.draw.rect(surface.py_surface, colors["ivory"],
                         pygame.Rect(surface.width - 100 - 1, 80 - 1, pixel_size + 2, pixel_size + 2))
        pygame.draw.rect(surface.py_surface, colors[level_editor.colors[0]],
                         pygame.Rect(surface.width - 100, 80, pixel_size, pixel_size))
        if pygame.mouse.get_pressed()[0]:
            level_editor.color_cursor = 0

    # yellow
    if pygame.Rect(surface.width - 100, 160, pixel_size, pixel_size).collidepoint(
            pygame.mouse.get_pos()) or level_editor.color_cursor == 1:
        pygame.draw.rect(surface.py_surface, colors["ivory"],
                         pygame.Rect(surface.width - 100 - 1, 160 - 1, pixel_size + 2, pixel_size + 2))
        pygame.draw.rect(surface.py_surface, colors[level_editor.colors[1]],
                         pygame.Rect(surface.width - 100, 160, pixel_size, pixel_size))
        if pygame.mouse.get_pressed()[0]:
            level_editor.color_cursor = 1

    # green
    if pygame.Rect(surface.width - 100, 240, pixel_size, pixel_size).collidepoint(
            pygame.mouse.get_pos()) or level_editor.color_cursor == 2:
        pygame.draw.rect(surface.py_surface, colors["ivory"],
                         pygame.Rect(surface.width - 100 - 1, 240 - 1, pixel_size + 2, pixel_size + 2))
        pygame.draw.rect(surface.py_surface, colors[level_editor.colors[2]],
                         pygame.Rect(surface.width - 100, 240, pixel_size, pixel_size))
        if pygame.mouse.get_pressed()[0]:
            level_editor.color_cursor = 2

    # blue
    if pygame.Rect(surface.width - 100, 320, pixel_size, pixel_size).collidepoint(
            pygame.mouse.get_pos()) or level_editor.color_cursor == 3:
        pygame.draw.rect(surface.py_surface, colors["ivory"],
                         pygame.Rect(surface.width - 100 - 1, 320 - 1, pixel_size + 2, pixel_size + 2))
        pygame.draw.rect(surface.py_surface, colors[level_editor.colors[3]],
                         pygame.Rect(surface.width - 100, 320, pixel_size, pixel_size))
        if pygame.mouse.get_pressed()[0]:
            level_editor.color_cursor = 3

    # grey (not clickable if color switcher = True)
    if pygame.Rect(surface.width - 100, 400, pixel_size, pixel_size).collidepoint(
            pygame.mouse.get_pos()) or level_editor.color_cursor == 4:
        pygame.draw.rect(surface.py_surface, colors["ivory"],
                         pygame.Rect(surface.width - 100 - 1, 400 - 1, pixel_size + 2, pixel_size + 2))
        pygame.draw.rect(surface.py_surface, colors[level_editor.colors[4]],
                         pygame.Rect(surface.width - 100, 400, pixel_size, pixel_size))
        if pygame.mouse.get_pressed()[0] and level_editor.color_switcher == False:
            level_editor.color_cursor = 4

    # manage the creation of the tile on the grid after the selection

    if pygame.Rect(0, 0, level_editor.size[0] * pixel_size, level_editor.size[1] * pixel_size).collidepoint(
            pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0] and not level_editor.select_add_player:
            i = int(pygame.mouse.get_pos()[0] / pixel_size)
            j = int(pygame.mouse.get_pos()[1] / pixel_size)
            if level_editor.level.grid.obstacles[i, j] is None or (
                    level_editor.level.grid.obstacles[i, j] is not None and not level_editor.level.grid.obstacles[
                i, j].end and not
                    level_editor.level.grid.obstacles[i, j].start):
                level_editor.new_tile((i, j))

        if pygame.mouse.get_pressed()[2] and not level_editor.select_add_player :
            i = int(pygame.mouse.get_pos()[0] / pixel_size)
            j = int(pygame.mouse.get_pos()[1] / pixel_size)
            if level_editor.level.grid.obstacles[i,j] is not None and not level_editor.level.grid.obstacles[
                i, j].end and not level_editor.level.grid.obstacles[i, j].start:
                level_editor.erase_tile((i, j))

    # type choice
    font_buttons = pygame.font.Font("assets/fonts/BulletTrace7-rppO.ttf", 30)

    # obstacle
    obstacle_button = font_buttons.render("Obstacle", True, colors["ivory"])
    obstacle_width = obstacle_button.get_width()
    obstacle_height = obstacle_button.get_height()
    x_rect1 = surface.width - 450
    y_rect1 = 60

    draw_empty_box(surface.py_surface, x_rect1, y_rect1, obstacle_width + 30, obstacle_height + 30)
    surface.py_surface.blit(obstacle_button, (x_rect1 + 15, y_rect1 + 15))

    # if mouse is on the button or the button is selected
    if pygame.Rect(x_rect1, y_rect1, obstacle_width + 30, obstacle_height + 30).collidepoint(
            pygame.mouse.get_pos()) or level_editor.color_switcher == False:
        draw_covered_box(surface.py_surface, x_rect1, y_rect1, obstacle_width + 30, obstacle_height + 30)
        surface.py_surface.blit(obstacle_button, (x_rect1 + 15, y_rect1 + 15))

        if pygame.mouse.get_pressed()[0]:
            level_editor.color_switcher = False

    # color switcher

    switcher_button = font_buttons.render("Color switcher", True, colors["ivory"])
    switcher_width = switcher_button.get_width()
    switcher_height = switcher_button.get_height()
    x_rect2 = x_rect1
    y_rect2 = 60 + obstacle_height + 60

    draw_empty_box(surface.py_surface, x_rect2, y_rect2, switcher_width + 30, switcher_height + 30)
    surface.py_surface.blit(switcher_button, (x_rect2 + 15, y_rect2 + 15))

    # if mouse is on the button or the button  is selected
    if pygame.Rect(x_rect2, y_rect2, switcher_width + 30, switcher_height + 30).collidepoint(
            pygame.mouse.get_pos()) or level_editor.color_switcher == True:
        draw_covered_box(surface.py_surface, x_rect2, y_rect2, switcher_width + 30, switcher_height + 30)
        surface.py_surface.blit(switcher_button, (x_rect2 + 15, y_rect2 + 15))

        if pygame.mouse.get_pressed()[0] and level_editor.color_cursor != 4:
            level_editor.color_switcher = True

    if pygame.Rect(0, 0, level_editor.size[0] * pixel_size, level_editor.size[1] * pixel_size).collidepoint(
            pygame.mouse.get_pos()):
        i = int(pygame.mouse.get_pos()[0] / pixel_size)
        j = int(pygame.mouse.get_pos()[1] / pixel_size)
        if not level_editor.color_switcher:
            pygame.draw.rect(surface.py_surface, colors[level_editor.colors[level_editor.color_cursor]],
                             pygame.Rect(i * pixel_size, j * pixel_size, pixel_size, pixel_size))
        if level_editor.color_switcher:
            surface.py_surface.blit(level_editor.level_render.grid_render.base_color_switcher,
                                    (i * pixel_size, j * pixel_size))
            pygame.draw.circle(surface.py_surface, colors["darkblue"],
                               (i * pixel_size + pixel_size / 2, j * pixel_size + pixel_size / 2),
                               pixel_size / 2.5, 0)

            pygame.draw.circle(surface.py_surface, colors[level_editor.colors[level_editor.color_cursor]],
                               (i * pixel_size + pixel_size / 2, j * pixel_size + pixel_size / 2),
                               pixel_size / 4, 0)

    # add player

    add_player_button = font_buttons.render("Add player", True, colors["ivory"])
    add_player_width = add_player_button.get_width()
    add_player_height = add_player_button.get_height()
    x_rect3 = 100
    y_rect3 = surface.height - 200

    draw_empty_box(surface.py_surface, x_rect3, y_rect3, add_player_width + 30, add_player_height + 30)
    surface.py_surface.blit(add_player_button, (x_rect3 + 15, y_rect3 + 15))

    # if mouse is on the button
    if pygame.Rect(x_rect3, y_rect3, add_player_width + 30, add_player_height + 30).collidepoint(
            pygame.mouse.get_pos()) and level_editor.color_cursor != 4:
        draw_covered_box(surface.py_surface, x_rect3, y_rect3, add_player_width + 30, add_player_height + 30)
        surface.py_surface.blit(add_player_button, (x_rect3 + 15, y_rect3 + 15))

        if pygame.mouse.get_pressed()[0]:
            level_editor.select_add_player = True
            level_editor.select_start = None
            level_editor.select_end = None

    if pygame.Rect(0, 0, level_editor.size[0] * pixel_size, level_editor.size[1] * pixel_size).collidepoint(
            pygame.mouse.get_pos()) and level_editor.select_add_player and level_editor.select_start == None:
        if pygame.mouse.get_pressed()[0]:
            i = int(pygame.mouse.get_pos()[0] / pixel_size)
            j = int(pygame.mouse.get_pos()[1] / pixel_size)
            level_editor.select_start = (i, j)

    if pygame.Rect(0, 0, level_editor.size[0] * pixel_size, level_editor.size[1] * pixel_size).collidepoint(
            pygame.mouse.get_pos()) and level_editor.select_add_player and level_editor.select_start != None:
        if pygame.mouse.get_pressed()[0]:
            i = int(pygame.mouse.get_pos()[0] / pixel_size)
            j = int(pygame.mouse.get_pos()[1] / pixel_size)
            if level_editor.select_start != (i, j):
                level_editor.select_end = (i, j)
                level_editor.new_player(level_editor.colors[level_editor.color_cursor], level_editor.select_start,
                                        level_editor.select_end)
                level_editor.select_add_player = False

    # delete player

    delete_player_button = font_buttons.render("Delete player", True, colors["ivory"])
    delete_player_width = delete_player_button.get_width()
    delete_player_height = delete_player_button.get_height()
    x_rect4 = 100
    y_rect4 = surface.height - 100

    draw_empty_box(surface.py_surface, x_rect4, y_rect4, delete_player_width + 30, delete_player_height + 30)
    surface.py_surface.blit(delete_player_button, (x_rect4 + 15, y_rect4 + 15))

    if pygame.Rect(x_rect4, y_rect4, delete_player_width + 30, delete_player_height + 30).collidepoint(
            pygame.mouse.get_pos()):
        draw_covered_box(surface.py_surface, x_rect4, y_rect4, delete_player_width + 30, delete_player_height + 30)
        surface.py_surface.blit(delete_player_button, (x_rect4 + 15, y_rect4 + 15))

        if pygame.mouse.get_pressed()[0] and len(level_editor.level.players) != 0:
            level_editor.remove_last_player()

    # save button

    save_button = font_buttons.render("Save level", True, colors["ivory"])
    save_width = save_button.get_width()
    save_height = save_button.get_height()
    x_rect5 = surface.width - save_width - 50
    y_rect5 = surface.height - 200

    draw_empty_box(surface.py_surface, x_rect5, y_rect5, save_width + 30, save_height + 30)
    surface.py_surface.blit(save_button, (x_rect5 + 15, y_rect5 + 15))

    if pygame.Rect(x_rect5 + 5, y_rect5 + 5, save_width + 20, save_height + 20).collidepoint(pygame.mouse.get_pos()):
        draw_covered_box(surface.py_surface, x_rect5, y_rect5, save_width + 30, save_height + 30)
        surface.py_surface.blit(save_button, (x_rect5 + 15, y_rect5 + 15))

        if pygame.mouse.get_pressed()[0]:
            level_editor.save()
            game.load_levels()
            game.stage = "Main Menu"

    # Exit button
    exit_button = font_buttons.render("Exit", True, colors["ivory"])
    exit_width = exit_button.get_width()
    exit_height = exit_button.get_height()
    x_rect6 = surface.width - save_width - 50
    y_rect6 = surface.height - 100

    draw_empty_box(surface.py_surface, x_rect6, y_rect6, exit_width + 30, exit_height + 30)
    surface.py_surface.blit(exit_button, (x_rect6 + 15, y_rect6 + 15))

    if pygame.Rect(x_rect6, y_rect6, exit_width + 30, exit_height + 30).collidepoint(pygame.mouse.get_pos()):
        draw_covered_box(surface.py_surface, x_rect6, y_rect6, exit_width + 30, exit_height + 30)
        surface.py_surface.blit(exit_button, (x_rect6 + 15, y_rect6 + 15))

        if pygame.mouse.get_pressed()[0]:
            game.stage = "Main Menu"
            game.load_levels()
