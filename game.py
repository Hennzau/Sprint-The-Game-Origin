# importations
import pygame
from level.level import Level, victory_event
from level.obstacle import colors
from render.surface import events

from level.player import Player
from level.obstacle import Obstacle, pixel_size

from render.draw_level import draw_level

from level.level_builder import build_level_0

from sound import sound_victory
from render.surface import Surface
from level.grid import Grid

# class game which updates the game (logic and render) at each passage through the main loop

# new events


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
            if event.type == pygame.USEREVENT:
                print("Victoire")
                sound_victory()
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

    def render(self, surface):
        draw_level(self.levels[self.cursor], surface.surface)
        temp_surface=surface.surface.copy()
        surface.surface.fill((0,0,0))
        surface.surface.blit(temp_surface, (int((surface.width-(self.levels[self.cursor].grid.size[0])*pixel_size)/2),int((surface.height-(self.levels[self.cursor].grid.size[1])*pixel_size)/2)))
