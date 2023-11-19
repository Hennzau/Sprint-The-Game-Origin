import pygame
import numpy as np

"""
The ParticleSystem class manages every particle in the game. Particles belong to the visual aspect of the game
"""


class ParticleSystem:
    def __init__(self):
        self.particles = []

    def update(self, delta_time):
        for particle in self.particles:
            if particle.image is not None:
                particle.update(delta_time)
        
        if len ([particle.position for particle in self.particles if particle.image is not None]) == len (self.particles):
            self.particles = []

    def add(self, particles):
        self.particles.extend(particles)

    def clear(self):
        self.particles = []

    def render(self, surface):
        surface.blits(
            [(particle.image, particle.position) for particle in self.particles if particle.image is not None])
