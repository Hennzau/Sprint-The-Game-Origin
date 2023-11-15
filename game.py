# importations
import pygame
from level.level import Level
from level.obstacle import colors
from render.surface import events

from level.player import Player
from level.obstacle import Obstacle

from render.draw_level import draw_level

from level.level_builder import build_level_0

# class game which updates the game (logic and render) at each passage through the main loop

class Game:
    def __init__(self):
        self.levels = []
        self.cursor = None

        # code moche
        self.cursor = 0

        self.levels.append(build_level_0())

        # code bon

        self.is_open = True

    def update(self, delta_time):
        for event in events():
            if event.type == pygame.QUIT:
                self.is_open = False
            if event.type == pygame.KEYDOWN:
                for player in (self.levels[self.cursor]).players:
                    if event.key == pygame.K_LEFT:
                        player.update_velocity(-400, 0)
                    if event.key == pygame.K_RIGHT:
                        player.update_velocity(400, 0)
                    if event.key == pygame.K_UP:
                        player.update_velocity(0, -400)
                    if event.key == pygame.K_DOWN:
                        player.update_velocity(0, 400)

        self.levels[self.cursor].update(delta_time)

        if self.levels[self.cursor].finished:
            print("Victoire")

    def render(self, surface):
        draw_level(self.levels[self.cursor], surface)
