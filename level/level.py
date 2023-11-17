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
    # Those parameters define the size of the grid that belongs to this level and also all the parameters for the
    # players (the count, their colors at the beginning, their initial positions and event the final position they
    # have to go to)
    def __init__(self, size, initial_positions, initial_colors, final_positions):
        self.grid = Grid(size)
        self.players = []

        self.final_positions = final_positions
        self.initial_positions = initial_positions
        self.initial_colors = initial_colors
        self.finished = False  # it's an indicator of the state of the level

        self.time = 0  # a level can have the concept of time : it helps to make dynamic things

        for k in range(
                len(initial_positions)):  # sometimes there are two players and we can imagine a level with even more

            self.players.append(Player(colors[self.initial_colors[k]], initial_positions[k][0] * pixel_size,
                                       initial_positions[k][1] * pixel_size))

            self.grid.obstacles[initial_positions[k][0], initial_positions[k][1]] = Obstacle(self.initial_colors[k],
                                                                                             False,
                                                                                             True, False)

            self.grid.obstacles[final_positions[k][0], final_positions[k][1]] = Obstacle(self.initial_colors[k], False,
                                                                                         False, True)

    def update(self, delta_time):  # this function is called 60 times per second in average, so delta_time = 1/60
        finished = True

        for i in range(len(self.players)):  # check if all players are at their final positions at the same time
            player = self.players[i]
            player.update(delta_time, self.grid)
            if int(player.position[0] / pixel_size) != self.final_positions[i][0] or int(
                    player.position[1] / pixel_size) != self.final_positions[i][1]:
                finished = False

        if finished and not self.finished:  # if yes, trigger an event to tell the game to stop the current level
            pygame.event.post(victory_event)
            self.finished = True

        self.time += delta_time
