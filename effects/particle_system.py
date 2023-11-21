import pygame
import numpy as np


class ParticleSystem:
    """
    The ParticleSystem class manages every particle in the game. Particles belong to the visual aspect of the game
    """

    def __init__(self):
        """
        The ParticleSystem __init__ function initializes an empty list of particles PointParticle
        """

        self.particles = []

    def update(self, delta_time):
        """
        The update function manages the update of each particle (motion) and clears the list when all particles are dead

        Parameters:
            delta_time (float): the delta_time
        """

        for particle in self.particles:
            if particle.image is not None:  # check if the particle is not dead
                particle.update(delta_time)

        # if every particle are dead, clear the list
        if len(self.particles) > 0 and len([1 for particle in self.particles if particle.lifetime <= 0]) == len(
                self.particles):
            self.particles = []

    def add(self, particles):
        """
        The add function add multiple particles in the particle system

        Parameters:
            particles (list (PointParticle)): the list of Point Particles
        """

        self.particles.extend(particles)

    def clear(self):
        """
        clear the list
        """

        self.particles = []

    def render(self, surface):
        """
        Render all particles on the given surface

        Parameters:
            surface (py_surface): the surface to draw particles on
        """

        surface.blits(
            [(particle.image, particle.position) for particle in self.particles if particle.image is not None])
