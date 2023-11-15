# importations
import pygame
from level.level import Level
from level.obstacle import colors
from render.surface import events
from level.player import Player


# class game which updates the game (logic and render) at each passage through the main loop

class Game:
    def __init__(self):
        self.levels = []
        self.levels.append(Level((20, 20), [(0, 0)], [colors["red"]]))
        self.is_open = True

    def update(self, delta_time):
        for event in events():
            if event.type == pygame.QUIT:
                self.is_open = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Player.update_velocity(-5, 0)
                if event.key == pygame.K_RIGHT:
                    Player.update_velocity(5, 0)
                if event.key == pygame.K_UP:
                    Player.update_velocity(0, 5)
                if event.key == pygame.K_DOWN:
                    Player.update_velocity(0, -5)

    def render(self):
        # update le rendu
        pass
