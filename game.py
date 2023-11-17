# importations
import pygame
from level.level import Level, victory_event
from level.obstacle import colors
from render.surface import events

from level.player import Player
from level.obstacle import Obstacle, pixel_size

from render.draw_level import draw_level

from sound import sound_victory
from render.surface import Surface
from level.grid import Grid

from level.level_loader import build_level


# class game which updates the game (logic and render) at each passage through the main loop

# new events


class Game:
    def __init__(self):
        self.levels = []
        self.cursor = None
        self.stage = "Launched"
        self.is_open = True

        # Level 0

        self.cursor = 2

        self.levels.append(build_level("assets/levels/level0.json"))
        self.levels.append(build_level("assets/levels/level1.json"))
        self.levels.append(build_level("assets/levels/level2.json"))

    def update(self, delta_time):
        for event in events():
            if event.type == pygame.QUIT:
                self.is_open = False
            if event.type == pygame.USEREVENT:
                sound_victory()
            if event.type == pygame.KEYDOWN:
                for player in (self.levels[self.cursor]).players:
                    if event.key == pygame.K_LEFT:
                        player.move_left(self.levels[self.cursor].grid)
                    if event.key == pygame.K_RIGHT:
                        player.move_right(self.levels[self.cursor].grid)
                    if event.key == pygame.K_UP:
                        player.move_up(self.levels[self.cursor].grid)
                    if event.key == pygame.K_DOWN:
                        player.move_down(self.levels[self.cursor].grid)


        self.levels[self.cursor].update(delta_time)

    def render(self, surface):
        draw_level(self.levels[self.cursor], surface.py_surface)

        temp_surface = surface.py_surface.subsurface(pygame.Rect(0, 0,
                                                                 self.levels[self.cursor].grid.size[0] * pixel_size,
                                                                 self.levels[self.cursor].grid.size[
                                                                     1] * pixel_size)).copy()

        surface.py_surface.fill((0, 0, 0))

        pygame.draw.rect(surface.py_surface, (255, 255, 255), pygame.Rect(
            int((surface.width - (self.levels[self.cursor].grid.size[0]) * pixel_size) / 2) - 5, int(
                (surface.height - (self.levels[self.cursor].grid.size[1]) * pixel_size) / 2) - 5,
            self.levels[self.cursor].grid.size[0] * pixel_size + 10,
            self.levels[self.cursor].grid.size[1] * pixel_size + 10))

        surface.py_surface.blit(temp_surface,
                                (int((surface.width - self.levels[self.cursor].grid.size[0] * pixel_size) / 2), int(
                                    (surface.height - self.levels[self.cursor].grid.size[1] * pixel_size) / 2)))
