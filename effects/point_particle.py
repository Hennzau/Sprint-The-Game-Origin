import pygame
import numpy as np


class PointParticle:
    """
    In Sprint The Game, every source of particle is actually a PointParticle, which means the source is present in the grid
    """

    def __init__(self, color, position, velocity, size, lifetime):
        """
        The PointParticle __init__ function takes everything a Particle Point needs to be created

        Parameters:
            color (RGB): the color in the RGB format
            position ((int,int)): position of the particle (unit is pixel)
            velocity ((int,int)): velocity of the particle (unit is pixel)
            size (int): size of the particle (square) (unit is pixel)
            lifetime (float): the time in seconds that lasts the particle
        """

        self.color = color
        self.position = position
        self.velocity = velocity
        self.size = size
        self.lifetime = lifetime

        self.image = pygame.Surface((size, size))
        self.image.fill(color)

    def update(self, delta_time):
        """
        The update function manages movements of the particle

        Parameters:
            delta_time (float): the delta_time
        """

        if self.lifetime > 0:
            self.position = (
                self.position[0] + self.velocity[0] * delta_time, self.position[1] + self.velocity[1] * delta_time)

            self.lifetime = self.lifetime - delta_time
        else:
            # if the lifetime is <= 0, let's kill the image
            self.image = None
