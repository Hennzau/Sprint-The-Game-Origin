from level.grid import Grid
from level.player import Player
from level.obstacle import colors, pixel_size, Obstacle
import numpy as np
import pygame

"""
A Level is an object that contains the grid and players data
"""

victory_event = pygame.event.Event(pygame.USEREVENT)


class Level:
    # starting positions of the players inside the grid
    def __init__(self, size, initial_positions, initial_colors, final_positions):
        self.grid = Grid(size)
        self.players = []
        self.final_positions = final_positions
        self.initial_positions = initial_positions
        self.initial_colors = initial_colors
        self.finished = False
        for k in range(
                len(initial_positions)):  # sometimes there is two players and we can imagine a level with even more
            # creation of the list of colors in rgb format
            initial_colors_rgb = colors[self.initial_colors[k]]

            self.players.append(Player(
                initial_colors_rgb, initial_positions[k][0] * pixel_size, initial_positions[k][1] * pixel_size, 0,
                0))

            self.grid.obstacles[initial_positions[k][0], initial_positions[k][1]] = Obstacle(self.initial_colors[k],
                                                                                             False,
                                                                                             True, False)

            self.grid.obstacles[final_positions[k][0], final_positions[k][1]] = Obstacle(self.initial_colors[k], False,
                                                                                         False, True)

    def update(self, delta_time):
        finished = True
        for i in range(len(self.players)):
            player = self.players[i]
            player.update(delta_time, self.grid)
            if int(player.position[0] / pixel_size) != self.final_positions[i][0] or int(
                    player.position[1] / pixel_size) != self.final_positions[i][1]:
                finished = False
        if finished and not self.finished:
            pygame.event.post(victory_event)
            self.finished = True
