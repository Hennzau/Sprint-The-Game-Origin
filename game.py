# Imports

import os
import pygame

from level.level import victory_event
from level.obstacle import colors, pixel_size
from level.level_loader import build_level

from render.surface import events
from render.level_render import LevelRender

from sound import sound_swipe


class Game:
    """
    The Game object updates the game (logic and render) at each passage through the main loop
    """

    def __init__(self, surface):
        """
        The __init__ method initializes all the variables that are needed by the game object.

        is_open is True while the player has not quit

        Parameters :
        surface (Surface) : the surface on which the game is drawn
        """

        self.levels = []
        self.levels_render = []
        self.cursor = None
        self.last_level = None  # cursor that points on the last played level
        self.stage = "Main Menu"
        self.is_open = True
        self.surface = surface
        self.sound = False

        # manage the return to menu key

        self.ask_for_main_menu = False
        self.main_menu_timer = 0

        # load levels

        self.load_levels()

        # load fonts and base model image of the game interface (things that do not change)

        self.time_font = pygame.font.Font("assets/fonts/MotomangucodeBold-3zde3.ttf", 50)
        self.font = pygame.font.Font("assets/fonts/BulletTrace7-rppO.ttf", 30)

        self.play_again_button = self.font.render("Hold R to Reload", True, colors["ivory"])
        self.return_to_menu = self.font.render("Hold E to go back", True, colors["ivory"])

        self.image = None

        # the load interface generates the mask image of the static interface : it helps to not calculate again and
        # again the image to render

        self.load_interface()

    def load_levels(self):
        """
        The load_levels method pulls the levels in json format and builds them in the Level format.
        The levels are stored in self.levels. Their associated LevelRenders are stored in self.levels_render.

        """
        self.levels = []
        self.levels_render = []

        # build levels from JSON format, first the levels of the game and next the custom levels

        n = len(os.listdir("assets/levels/"))

        for i in range(1, n + 1):
            path = "assets/levels/level_" + str(i) + ".json"
            if os.path.isfile(path):
                # there are two different classes : a Logical object 'Level' that represents the level,
                # and a Rendering object 'LevelRender' that manages the rendering of the level
                # (pre-calculated images etc...)

                self.levels.append(build_level(path))
                self.levels_render.append(LevelRender(self.levels[-1]))

        n = len(os.listdir("assets/levels/custom"))
        for i in range(1, n + 1):
            path = "assets/levels/custom/level_" + str(i) + ".json"
            if os.path.isfile(path):
                # there are two different classes : a Logical object 'Level' that represents the level,
                # and a Rendering object 'LevelRender' that manages the rendering of the level
                # (pre-calculated images etc...)

                self.levels.append(build_level(path))
                self.levels_render.append(LevelRender(self.levels[-1]))

    def load_interface(self):
        """
        The load_interface creates all the images that are static : the buttons, the name of the current level...
        """

        self.image = pygame.Surface((self.surface.width, self.surface.height))

        if self.cursor is not None:
            # First of all, create the frame that will contain the level

            self.surface.py_surface.fill((0, 0, 0))

            pygame.draw.rect(self.image, colors["ivory"], pygame.Rect(
                int((self.surface.width - (self.levels[self.cursor].grid.size[0]) * pixel_size) / 2) - 5, int(
                    (self.surface.height - (self.levels[self.cursor].grid.size[1]) * pixel_size) / 2) - 5,
                self.levels[self.cursor].grid.size[0] * pixel_size + 10,
                self.levels[self.cursor].grid.size[1] * pixel_size + 10))

            pygame.draw.rect(self.image, colors["Black"], pygame.Rect(
                int((self.surface.width - (self.levels[self.cursor].grid.size[0]) * pixel_size) / 2) - 3, int(
                    (self.surface.height - (self.levels[self.cursor].grid.size[1]) * pixel_size) / 2) - 3,
                self.levels[self.cursor].grid.size[0] * pixel_size + 6,
                self.levels[self.cursor].grid.size[1] * pixel_size + 6))

            pygame.draw.rect(self.image, colors["ivory"], pygame.Rect(
                int((self.surface.width - (self.levels[self.cursor].grid.size[0]) * pixel_size) / 2) - 1, int(
                    (self.surface.height - (self.levels[self.cursor].grid.size[1]) * pixel_size) / 2) - 1,
                self.levels[self.cursor].grid.size[0] * pixel_size + 2,
                self.levels[self.cursor].grid.size[1] * pixel_size + 2))

            # create the box of the timer, at the left of the level frame

            x = (((self.surface.width - (self.levels[self.cursor].grid.size[0]) * pixel_size) / 2) - 5) / 2 - 75
            y = int((self.surface.height - (self.levels[self.cursor].grid.size[1]) * pixel_size) / 2) - 5

            pygame.draw.rect(self.image, colors["ivory"], pygame.Rect(x, y, 150, 100))
            pygame.draw.rect(self.image, colors["Black"], pygame.Rect(x + 2, y + 2, 146, 96))
            pygame.draw.rect(self.image, colors["ivory"], pygame.Rect(x + 4, y + 4, 142, 92))
            pygame.draw.rect(self.image, colors["darkblue"], pygame.Rect(x + 5, y + 5, 140, 90))

            # print the current level
            current_level = "Level " + str(self.cursor + 1)
            level = self.font.render(current_level, True, colors["ivory"])
            self.image.blit(level, (
                self.surface.width / 2 - level.get_width() / 2, y / 2 - level.get_height() / 2))

            # create the box of the hit_counter, at the left of the level frame

            x = self.levels[self.cursor].grid.size[0] * pixel_size + (self.surface.width -
                                                                      self.levels[self.cursor].grid.size[
                                                                          0] * pixel_size) / 2 + (
                        self.surface.width - self.levels[self.cursor].grid.size[0] * pixel_size) / 8
            y = int((self.surface.height - (self.levels[self.cursor].grid.size[1]) * pixel_size) / 2) - 5

            pygame.draw.rect(self.image, colors["ivory"], pygame.Rect(x, y, 150, 100))
            pygame.draw.rect(self.image, colors["Black"], pygame.Rect(x + 2, y + 2, 146, 96))
            pygame.draw.rect(self.image, colors["ivory"], pygame.Rect(x + 4, y + 4, 142, 92))
            pygame.draw.rect(self.image, colors["darkblue"], pygame.Rect(x + 5, y + 5, 140, 90))

            # create the two options in the level : Reload the level and return to main menu

            y_bis = ((self.surface.height - (self.levels[self.cursor].grid.size[1]) * pixel_size) / 2) - 20 + \
                    self.levels[self.cursor].grid.size[1] * pixel_size

            self.image.blit(self.play_again_button, (
                self.surface.width / 2 - self.play_again_button.get_width() / 2,
                (720 + y_bis) / 2 - self.play_again_button.get_height() / 2))
            self.image.blit(self.return_to_menu, (
                self.surface.width / 2 - self.play_again_button.get_width() / 2,
                (720 + y_bis) / 2 - self.play_again_button.get_height() / 2 + self.return_to_menu.get_height()))

    def update(self, delta_time):
        """
        The update method manages everything that is not static: key management, players, timer...
        It is called 60 or 120 times each second.

        Parameters :
        delta_time (float): time between 2 executions of the loop
        """

        for event in events():
            if event.type == pygame.QUIT:
                self.is_open = False
            # when there is a victory event, reload the current level and go to end menu
            if event.type == victory_event.type:
                self.levels[self.cursor].reload_level()

                self.last_level = self.cursor
                self.cursor = None
                self.stage = "End Menu"

            if event.type == pygame.KEYDOWN:  # manage keyboard actions
                if self.cursor is not None:
                    if event.key == pygame.K_r:
                        self.levels[self.cursor].ask_for_reload = True
                    if event.key == pygame.K_e:
                        self.ask_for_main_menu = True

                    if not self.levels[self.cursor].victory_timer > 0:
                        is_moving = False

                        for player in self.levels[self.cursor].players:
                            if player.is_moving:
                                is_moving = True

                        if event.key == pygame.K_LEFT:
                            for player in (self.levels[self.cursor]).players:
                                if not is_moving:
                                    sound_swipe()
                                    player.move_left(self.levels[self.cursor].grid)
                        if event.key == pygame.K_RIGHT:
                            for player in (self.levels[self.cursor]).players:
                                if not is_moving:
                                    sound_swipe()
                                    player.move_right(self.levels[self.cursor].grid)
                        if event.key == pygame.K_UP:
                            for player in (self.levels[self.cursor]).players:
                                if not is_moving:
                                    sound_swipe()
                                    player.move_up(self.levels[self.cursor].grid)
                        if event.key == pygame.K_DOWN:
                            for player in (self.levels[self.cursor]).players:
                                if not is_moving:
                                    sound_swipe()
                                    player.move_down(self.levels[self.cursor].grid)

            if event.type == pygame.KEYUP:
                if self.cursor is not None:
                    if event.key == pygame.K_r:
                        self.levels[self.cursor].ask_for_reload = False
                if event.key == pygame.K_e:
                    self.ask_for_main_menu = False

        if self.cursor is not None:  # update the level if the user is playing one
            self.levels[self.cursor].update(delta_time)

            if self.ask_for_main_menu:
                self.main_menu_timer += delta_time
            else:
                self.main_menu_timer = 0

            if self.main_menu_timer >= 1:
                self.levels[self.cursor].reload_level()
                self.last_level = self.cursor
                self.cursor = None
                self.stage = "Main Menu"

                self.ask_for_main_menu = False
                self.main_menu_timer = 0

    def render(self):
        """
        The render method creates the pygame images of the game
        (those that were not considered static and created by load_interface)
        """

        if self.cursor is not None:
            # print the level on a surface (black surface)

            self.levels_render[self.cursor].render(self.surface.py_surface)

            # extract the content
            temp_surface = self.surface.py_surface.subsurface(pygame.Rect(0, 0,
                                                                          self.levels[self.cursor].grid.size[
                                                                              0] * pixel_size,
                                                                          self.levels[self.cursor].grid.size[
                                                                              1] * pixel_size)).copy()
            # Here we merge the base model game interface on the screen

            self.surface.py_surface.blit(self.image, (0, 0))

            # next we merge the level rendering on its place on the screen
            self.surface.py_surface.blit(temp_surface,
                                         (int((self.surface.width - self.levels[self.cursor].grid.size[
                                             0] * pixel_size) / 2), int(
                                             (self.surface.height - self.levels[self.cursor].grid.size[
                                                 1] * pixel_size) / 2)))

            # print the timer

            x = (((self.surface.width - (self.levels[self.cursor].grid.size[0]) * pixel_size) / 2) - 5) / 2 - 75
            y = int((self.surface.height - (self.levels[self.cursor].grid.size[1]) * pixel_size) / 2) - 5
            y_bis = ((self.surface.height - (self.levels[self.cursor].grid.size[1]) * pixel_size) / 2) - 20 + \
                    self.levels[self.cursor].grid.size[1] * pixel_size

            time = self.levels[self.cursor].time

            minutes = int(time / 60)
            seconds = int(time - 60 * minutes)

            timer_string = str(minutes) + ":" + str(seconds)

            timer = self.time_font.render(timer_string, True, colors["ivory"])

            self.surface.py_surface.blit(timer, (
                (2 * x + 150) / 2 - timer.get_width() / 2, (2 * y + 100) / 2 - timer.get_height() / 2))

            # print the hit_counter

            x = self.levels[self.cursor].grid.size[0] * pixel_size + (self.surface.width -
                                                                      self.levels[self.cursor].grid.size[
                                                                          0] * pixel_size) / 2 + (
                        self.surface.width - self.levels[self.cursor].grid.size[0] * pixel_size) / 8
            y = int((self.surface.height - (self.levels[self.cursor].grid.size[1]) * pixel_size) / 2) - 5

            hit = self.levels[self.cursor].hit

            hit_counter_string = str(hit)

            hit_counter = self.time_font.render(hit_counter_string, True, colors["ivory"])

            self.surface.py_surface.blit(hit_counter, (
                (2 * x + 150) / 2 - hit_counter.get_width() / 2, (2 * y + 100) / 2 - hit_counter.get_height() / 2))

            # when the user wants to reload the current level or go to the main menu, draw the text with color progress

            if self.levels[self.cursor].ask_for_reload:
                temp_surface = pygame.Surface(
                    (self.play_again_button.get_width() * self.levels[self.cursor].reload_timer * 1.1,
                     self.play_again_button.get_height()))

                temp_surface.fill(colors["red"])

                self.surface.py_surface.blit(temp_surface,
                                             (self.surface.width / 2 - self.play_again_button.get_width() / 2,
                                              (720 + y_bis) / 2 - self.play_again_button.get_height() / 2),
                                             special_flags=pygame.BLEND_RGB_MULT)

            if self.ask_for_main_menu:
                temp_surface = pygame.Surface(
                    (self.return_to_menu.get_width() * self.main_menu_timer * 1.1,
                     self.return_to_menu.get_height()))

                temp_surface.fill(colors["yellow"])

                self.surface.py_surface.blit(temp_surface, (
                    self.surface.width / 2 - self.play_again_button.get_width() / 2,
                    (720 + y_bis) / 2 - self.play_again_button.get_height() / 2 + self.return_to_menu.get_height()),
                                             special_flags=pygame.BLEND_RGB_MULT)
