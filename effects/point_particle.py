import pygame
import numpy as np

"""
In Sprint The Game, every source of particle is actually a PointParticle, which means the source is present in the grid
"""


class PointParticle:
    def __init__(self, color, position, velocity, size, lifetime):
        self.color = color
        self.position = position
        self.velocity = velocity
        self.size = size
        self.lifetime = lifetime

        self.image = pygame.Surface((size, size))
        self.image.fill(color)

    def update(self, delta_time):
        if self.lifetime > 0:
            self.position = (
                self.position[0] + self.velocity[0] * delta_time, self.position[1] + self.velocity[1] * delta_time)

            self.lifetime = self.lifetime - delta_time
        else:
            # if the lifetime is <= 0, let's kill the image
            self.image = None
