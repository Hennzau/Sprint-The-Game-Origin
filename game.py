# importations
import pygame
from level.level import Level, victory_event
from level.obstacle import colors
from render.surface import events

from level.player import Player
from level.obstacle import Obstacle, pixel_size

from render.draw_level import draw_level

from sound import sound_victory, sound_swipe
from render.surface import Surface
from level.grid import Grid

from level.level_loader import build_level


# class game which updates the game (logic and render) at each passage through the main loop

# new events


class Game:
    def __init__(self):
        self.levels = []
        self.cursor = None
        self.last_level = None
        self.stage = "Main Menu"
        self.is_open = True

        # Level 0

        self.levels.append(build_level("assets/levels/level0.json"))
        self.levels.append(build_level("assets/levels/level1.json"))
        self.levels.append(build_level("assets/levels/level2.json"))

    def reload_levels(self):
        self.levels = []
        self.levels.append(build_level("assets/levels/level0.json"))
        self.levels.append(build_level("assets/levels/level1.json"))
        self.levels.append(build_level("assets/levels/level2.json"))

    def update(self, delta_time):
        for event in events():
            if event.type == pygame.QUIT:
                self.is_open = False
            if event.type == pygame.USEREVENT:
                sound_victory()
                self.reload_levels()
                self.last_level = self.cursor
                self.cursor = None
                self.stage = "End Menu"
            if event.type == pygame.KEYDOWN:
                if self.cursor is not None:
                    if event.key == pygame.K_r:
                        self.levels[self.cursor].ask_for_reload = True
                    for player in (self.levels[self.cursor]).players:
                        if event.key == pygame.K_LEFT:
                            sound_swipe()
                            player.move_left(self.levels[self.cursor].grid)
                        if event.key == pygame.K_RIGHT:
                            sound_swipe()
                            player.move_right(self.levels[self.cursor].grid)
                        if event.key == pygame.K_UP:
                            sound_swipe()
                            player.move_up(self.levels[self.cursor].grid)
                        if event.key == pygame.K_DOWN:
                            sound_swipe()
                            player.move_down(self.levels[self.cursor].grid)
            if event.type == pygame.KEYUP:
                if self.cursor is not None:
                    if event.key == pygame.K_r:
                        self.levels[self.cursor].ask_for_reload = False

        if self.cursor is not None:
            self.levels[self.cursor].update(delta_time)

    def render(self, surface):
        if self.cursor is not None:
            draw_level(self.levels[self.cursor], surface.py_surface)

            temp_surface = surface.py_surface.subsurface(pygame.Rect(0, 0,
                                                                     self.levels[self.cursor].grid.size[0] * pixel_size,
                                                                     self.levels[self.cursor].grid.size[
                                                                         1] * pixel_size)).copy()

            surface.py_surface.fill((0, 0, 0))

        pygame.draw.rect(surface.py_surface, colors["ivoire"], pygame.Rect(
            int((surface.width - (self.levels[self.cursor].grid.size[0]) * pixel_size) / 2) - 5, int(
                (surface.height - (self.levels[self.cursor].grid.size[1]) * pixel_size) / 2) - 5,
            self.levels[self.cursor].grid.size[0] * pixel_size + 10,
            self.levels[self.cursor].grid.size[1] * pixel_size + 10))
        pygame.draw.rect(surface.py_surface, colors["Black"], pygame.Rect(
            int((surface.width - (self.levels[self.cursor].grid.size[0]) * pixel_size) / 2) - 3, int(
                (surface.height - (self.levels[self.cursor].grid.size[1]) * pixel_size) / 2) - 3,
            self.levels[self.cursor].grid.size[0] * pixel_size + 6,
            self.levels[self.cursor].grid.size[1] * pixel_size + 6))
        pygame.draw.rect(surface.py_surface, colors["ivoire"], pygame.Rect(
            int((surface.width - (self.levels[self.cursor].grid.size[0]) * pixel_size) / 2) - 1, int(
                (surface.height - (self.levels[self.cursor].grid.size[1]) * pixel_size) / 2) - 1,
            self.levels[self.cursor].grid.size[0] * pixel_size + 2,
            self.levels[self.cursor].grid.size[1] * pixel_size + 2))

        surface.py_surface.blit(temp_surface,
                                (int((surface.width - self.levels[self.cursor].grid.size[0] * pixel_size) / 2), int(
                                    (surface.height - self.levels[self.cursor].grid.size[1] * pixel_size) / 2)))

        x = (((surface.width - (self.levels[self.cursor].grid.size[0]) * pixel_size) / 2) - 5) / 2 - 75
        y = int((surface.height - (self.levels[self.cursor].grid.size[1]) * pixel_size) / 2) - 5

        pygame.draw.rect(surface.py_surface, colors["ivoire"], pygame.Rect(x, y, 150, 100))
        pygame.draw.rect(surface.py_surface, colors["Black"], pygame.Rect(x + 2, y + 2, 146, 96))
        pygame.draw.rect(surface.py_surface, colors["ivoire"], pygame.Rect(x + 4, y + 4, 142, 92))
        pygame.draw.rect(surface.py_surface, colors["darkblue"], pygame.Rect(x + 5, y + 5, 140, 90))
        time_font = pygame.font.Font("assets/fonts/MotomangucodeBold-3zde3.ttf", 50)
        time = self.levels[self.cursor].time
        minutes = int(time / 60)
        secondes = int(time - 60 * minutes)
        timer_string = str(minutes) + ":" + str(secondes)
        timer = time_font.render(timer_string, True, colors["ivoire"])
        surface.blit(timer, ((2 * x + 150) / 2 - timer.get_width() / 2, (2 * y + 100) / 2 - timer.get_height() / 2))

        font = pygame.font.Font("assets/fonts/BulletTrace7-rppO.ttf", 40)
        play_again_button = font.render("Hold R to Reload", True, colors["ivoire"])
        current_level = "Level " + str(self.cursor + 1)
        level = font.render(current_level, True, colors["ivoire"])

        y_bis = ((surface.height - (self.levels[self.cursor].grid.size[1]) * pixel_size) / 2) - 5 + \
                self.levels[self.cursor].grid.size[1] * pixel_size + 10

        surface.blit(level, (surface.width / 2 - level.get_width() / 2, y / 2 - level.get_height() / 2))
        surface.blit(play_again_button, (
            surface.width / 2 - play_again_button.get_width() / 2,
            (720 + y_bis) / 2 - play_again_button.get_height() / 2))
