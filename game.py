# importations
import pygame
from level.level import Level
from level.obstacle import colors
from render.surface import events

from level.player import Player
from level.obstacle import Obstacle

from render.draw_level import draw_level

from level.level_builder import build_level_0

from sound import sound_victory


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
                        player.move_left(self.levels[self.cursor].grid)
                    if event.key == pygame.K_RIGHT:
                        player.move_right(self.levels[self.cursor].grid)
                    if event.key == pygame.K_UP:
                        player.move_up(self.levels[self.cursor].grid)
                    if event.key == pygame.K_DOWN:
                        player.move_down(self.levels[self.cursor].grid)

        self.levels[self.cursor].update(delta_time)

        if self.levels[self.cursor].finished:
            print("Victoire")
            sound_victory()

    def render(self, surface):
        draw_level(self.levels[self.cursor], surface)
