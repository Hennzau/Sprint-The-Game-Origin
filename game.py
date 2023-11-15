# importations
import pygame
from level.level import Level
from level.obstacle import colors
from render.surface import events

from level.player import Player
from level.obstacle import Obstacle

from render.draw_level import draw_level


# class game which updates the game (logic and render) at each passage through the main loop

class Game:
    def __init__(self):
        self.levels = []
        self.cursor = None

        # code moche
        self.cursor = 0

        self.levels.append(Level((20, 20), [(100, 100)], [colors["red"]]))

        self.levels[self.cursor].grid.obstacles[10, 5] = Obstacle("blue")

        # code bon

        self.is_open = True

    def update(self, delta_time):
        for event in events():
            if event.type == pygame.QUIT:
                self.is_open = False
            if event.type == pygame.KEYDOWN:
                for player in (self.levels[self.cursor]).players:
                    if event.key == pygame.K_LEFT:
                        player.update_velocity(-200, 0)
                    if event.key == pygame.K_RIGHT:
                        player.update_velocity(200, 0)
                    if event.key == pygame.K_UP:
                        player.update_velocity(0, -200)
                    if event.key == pygame.K_DOWN:
                        player.update_velocity(0, 200)

        self.levels[self.cursor].update(delta_time)

    def render(self, surface):
        draw_level(self.levels[self.cursor], surface)
