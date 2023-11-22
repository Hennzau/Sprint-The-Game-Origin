from level.grid import Grid
from level.player import Player
from level.obstacle import colors, pixel_size, Obstacle

from sound import sound_victory

from effects.light_system import LightSystem
from effects.point_light import PointLight

from effects.particle_system import ParticleSystem
from effects.point_particle import PointParticle

import numpy as np
import pygame

victory_event = pygame.event.Event(pygame.USEREVENT)


class Level:
    """
    A Level is an object that contains the grid and players data
    """

    # Those parameters define the size of the grid that belongs to this level and also all the parameters for the
    # players (the count, their colors at the beginning, their initial positions and event the final position they
    # have to go to)
    def __init__(self, size, initial_positions, initial_colors, final_positions):
        """
        The Level __init__ function will generate a new complete Level giving a certain player condition and a size

        Parameters:
        size ((int,int)): width and height size of the grid

        initial_positions (list[(int,int),...]):    a python list containing tuples that represents the position of
                                                    the player IN THE GRID (in 0...size[0] and 0...size[1])
        initial_colors (list[str,...]): a python list containing strings that represents the color of the player for the
                                        'colors' dictionary

        final_positions (list[(int,int),...]):  a python list containing tuples that represents the position of
                                                the player IN THE GRID (in 0...size[0] and 0...size[1])
        """

        self.grid = Grid(size)
        self.players = []

        self.final_positions = final_positions
        self.initial_positions = initial_positions
        self.initial_colors = initial_colors
        self.finished = False  # it's an indicator of the state of the level

        self.ask_for_reload = False
        self.reload_timer = 0
        self.time = 0  # a level can have the concept of time : it helps to make dynamic things

        self.hit = 0

        self.victory_delay = 0.5
        self.victory_timer = 0

        self.light_system = LightSystem()
        self.particle_system = ParticleSystem()

        # We initialize special obstacles in the grid like starting points and ending points
        for k in range(
                len(initial_positions)):  # sometimes there are two players and we can imagine a level with even more

            self.grid.obstacles[self.initial_positions[k][0], self.initial_positions[k][1]] = Obstacle(
                self.initial_colors[k],
                False,
                True, False)

            self.grid.obstacles[self.final_positions[k][0], self.final_positions[k][1]] = Obstacle(
                self.initial_colors[k], False,
                False, True)

            # those obstacles have also a soft lighting point

            self.light_system.add_light("start" + str(k), colors[self.initial_colors[k]],
                                        (self.initial_positions[k][0] * pixel_size + pixel_size / 2,
                                         self.initial_positions[k][1] * pixel_size + pixel_size / 2),
                                        400, 0.1)

            self.light_system.add_light("end" + str(k), colors[self.initial_colors[k]],
                                        (self.final_positions[k][0] * pixel_size + pixel_size / 2,
                                         self.final_positions[k][1] * pixel_size + pixel_size / 2),
                                        400, 0.1)

            # each player has a point of light that follows him

            self.light_system.add_light("player" + str(k), colors[self.initial_colors[k]],
                                        (self.initial_positions[k][0] * pixel_size + pixel_size / 2,
                                         self.initial_positions[k][1] * pixel_size + pixel_size / 2),
                                        200, 0.2)

        self.reload_level()  # load / reload this level

    def reload_level(self):
        """
        the 'reload_level' function reload the placement of the players on the level
        """
        self.players = []
        self.particle_system.clear()
        self.victory_timer = 0
        self.time = 0
        self.hit = 0

        for k in range(
                len(self.initial_positions)):

            # play again with players at their starting points

            self.players.append(Player(colors[self.initial_colors[k]], self.initial_positions[k][0] * pixel_size,
                                       self.initial_positions[k][1] * pixel_size))

            # at the beginning of the level, particles explode from the each player position

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

    def update(self, delta_time):
        """
        the 'update' function takes a delta_time, calculated by taking the average times of execution of the main loop
        (basically the FPS variable) and it updates everything : the players, actions (reload, go back),
        the victory event, light points on players and even the multiple particles on every actions

        Parameters:
        delta_time (float): the delta_time
        """
        finished = True

        for i in range(len(self.players)):  # update data for all players
            player = self.players[i]

            # Check if a player start moving, and if so, add particles at his starting position

            if player.is_moving and player.speed == player.start_speed:
                particles = []

                for k in range(8):
                    for j in range(8):
                        particles.append(
                            PointParticle((player.color[0] * 0.7, player.color[1] * 0.7, player.color[2] * 0.7),
                                          (player.position[0] + 5 * k, player.position[1] + 5 * j),
                                          (np.random.randint(-30, 30), np.random.randint(-30, 30)), 1,
                                          np.random.randint(150) / 100))

                self.particle_system.add(particles)

            player.update(delta_time, self.grid)

            # when a player bounces on an obstacle we generate particles

            if player.bounces and player.bounce_time == 0:
                particles = []
                for k in range(50):
                    collision_position = player.position + np.array(
                        [pixel_size / 2, pixel_size / 2]) + player.bounce_direction * pixel_size / 2

                    collision_dir = np.array([1, 1]) - np.abs(player.bounce_direction)
                    if np.random.randint(100) > 50:
                        collision_dir = -collision_dir

                    particles.append(PointParticle(player.color,
                                                   (collision_position[0], collision_position[1]),
                                                   (collision_dir[0] * np.random.randint(300) + np.random.randint(
                                                       100) * np.sin((2 * 3.14 * k) / 10),
                                                    collision_dir[1] * np.random.randint(300) + np.random.randint(
                                                        100) * np.cos((2 * 3.14 * k) / 10)),
                                                   3, np.random.randint(20) / 100))

                self.particle_system.add(particles)

            # check if all players are at their final positions at the same time

            if int(player.position[0] / pixel_size) != self.final_positions[i][0] or int(
                    player.position[1] / pixel_size) != self.final_positions[i][1]:
                if self.victory_timer == 0:  # be sure that the user was not in a winning position the frame before
                    finished = False

            # update the position and the color of the player

            self.light_system.lights["player" + str(i)].move(
                (player.render_position[0] + pixel_size / 2, player.render_position[1] + pixel_size / 2))

            self.light_system.lights["player" + str(i)].change_color(
                player.color)  # this will regenerate the lighting mask when the previous color is different

        if finished:  # if yes, trigger an event to tell the game to stop the current level after a certain delay
            if self.victory_timer > self.victory_delay:
                pygame.event.post(victory_event)
                self.finished = True

            # When the user succeed sound the victory and tones of particles
            elif self.victory_timer == 0:
                sound_victory()

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

        # manages the concept of time of the level
        self.time += delta_time

        # if the user ask for reload, increment the progress bar
        if self.ask_for_reload:
            self.reload_timer += delta_time
        else:
            self.reload_timer = 0

        # finally reload the level
        if self.reload_timer >= 1:
            self.reload_level()
            self.ask_for_reload = False
            self.reload_timer = 0
            self.time = 0
            self.hit = 0

        # at the end we update the particle system : it manages the position of all particles and their lifetime
        self.particle_system.update(delta_time)
