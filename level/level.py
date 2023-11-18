from level.grid import Grid
from level.player import Player
from level.obstacle import colors, pixel_size, Obstacle

from effects.light_system import LightSystem
from effects.point_light import PointLight

from effects.particle_system import ParticleSystem
from effects.point_particle import PointParticle

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

        self.ask_for_reload = False
        self.reload_timer = 0
        self.time = 0  # a level can have the concept of time : it helps to make dynamic things

        self.victory_delay = 0.5
        self.victory_timer = 0

        self.light_system = LightSystem()
        self.particle_system = ParticleSystem()

        for k in range(
                len(initial_positions)):  # sometimes there are two players and we can imagine a level with even more

            self.grid.obstacles[self.initial_positions[k][0], self.initial_positions[k][1]] = Obstacle(
                self.initial_colors[k],
                False,
                True, False)

            self.grid.obstacles[self.final_positions[k][0], self.final_positions[k][1]] = Obstacle(
                self.initial_colors[k], False,
                False, True)

            self.light_system.add_light("start" + str(k), colors[self.initial_colors[k]],
                                        (self.initial_positions[k][0] * pixel_size + pixel_size / 2,
                                         self.initial_positions[k][1] * pixel_size + pixel_size / 2),
                                        400, 0.1)

            self.light_system.add_light("end" + str(k), colors[self.initial_colors[k]],
                                        (self.final_positions[k][0] * pixel_size + pixel_size / 2,
                                         self.final_positions[k][1] * pixel_size + pixel_size / 2),
                                        400, 0.1)

            self.light_system.add_light("player" + str(k), colors[self.initial_colors[k]],
                                        (self.initial_positions[k][0] * pixel_size + pixel_size / 2,
                                         self.initial_positions[k][1] * pixel_size + pixel_size / 2),
                                        200, 0.2)

        self.reload_level()

    def reload_level(self):
        self.players = []
        self.particle_system.clear()

        for k in range(
                len(self.initial_positions)):
            self.players.append(Player(colors[self.initial_colors[k]], self.initial_positions[k][0] * pixel_size,
                                       self.initial_positions[k][1] * pixel_size))
            particles = []
            for i in range(100):
                particles.append(PointParticle(colors[self.initial_colors[k]],
                                               (self.initial_positions[k][0] * pixel_size + pixel_size / 2,
                                                self.initial_positions[k][1] * pixel_size + pixel_size / 2),
                                               (np.random.randint(100) * np.sin((2 * 3.14 * i) / 100),
                                                np.random.randint(100) * np.cos((2 * 3.14 * i) / 100)),
                                               3, np.random.randint(150) / 100))

            self.particle_system.add(particles)

        self.finished = False

    def update(self, delta_time):  # this function is called 60 times per second in average, so delta_time = 1/60
        finished = True

        for i in range(len(self.players)):  # check if all players are at their final positions at the same time
            player = self.players[i]
            player.update(delta_time, self.grid)
            if int(player.position[0] / pixel_size) != self.final_positions[i][0] or int(
                    player.position[1] / pixel_size) != self.final_positions[i][1]:
                finished = False

            self.light_system.lights["player" + str(i)].move(
                (player.render_position[0] + pixel_size / 2, player.render_position[1] + pixel_size / 2))

            self.light_system.lights["player" + str(i)].change_color(player.color)

        if finished:  # if yes, trigger an event to tell the game to stop the current level
            if self.victory_timer > self.victory_delay:
                pygame.event.post(victory_event)
                self.victory_timer = 0
                self.finished = True
            elif self.victory_timer == 0:
                for k in range(
                        len(self.initial_positions)):

                    particles = []
                    for i in range(300):
                        particles.append(PointParticle(self.players[k].color,
                                                       (self.final_positions[k][0] * pixel_size + pixel_size / 2,
                                                        self.final_positions[k][1] * pixel_size + pixel_size / 2),
                                                       (np.random.randint(300) * np.sin((2 * 3.14 * i) / 100),
                                                        np.random.randint(300) * np.cos((2 * 3.14 * i) / 100)),
                                                       3, np.random.randint(150) / 100))

                    self.particle_system.add(particles)

            self.victory_timer += delta_time

        self.time += delta_time
        if self.ask_for_reload:
            self.reload_timer += delta_time

        if self.reload_timer >= 1:
            self.reload_level()
            self.ask_for_reload = False
            self.reload_timer = 0
            self.time = 0

        self.particle_system.update(delta_time)
