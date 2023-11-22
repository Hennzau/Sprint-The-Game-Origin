import pygame
import numpy as np

from effects.point_light import PointLight


class LightSystem:
    """
    The LightSystem class manages every light in the game (their color and their position)
    """

    def __init__(self):
        """
        The LightSystem __init__ function initializes a blank base model of a single light. The point lights
        will next blit this model on the main surface after some modifications.
       """

        self.lights = {}

        # we generate the blank mask of lights once

        self.precision = 60
        self.radius = 300

        self.blank_base_model = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)

        for k in range(self.precision):  # consists in a superposition of blank disks BLEND_ADD

            sub_radius = self.radius * (self.precision - k) / self.precision
            temp_surface = pygame.Surface((sub_radius * 2, sub_radius * 2), pygame.SRCALPHA)

            pygame.draw.circle(temp_surface,
                               (int(255 / self.precision), int(255 / self.precision), int(255 / self.precision)),
                               (sub_radius, sub_radius), sub_radius, 0)

            self.blank_base_model.blit(temp_surface, (self.radius - sub_radius, self.radius - sub_radius),
                                       special_flags=pygame.BLEND_RGBA_ADD)

    def add_light(self, name, color, position, radius, intensity):
        """
        The add_light function takes everything a Light Point needs to be created and add it to the light system:
        The light system is managed by a dictionary in order to be able to access a light by its name

        Parameters:
            name (str): the name of the light (unique)
            color (RGB): the color in the RGB format
            position ((int,int)): position of the light (unit is pixel)
            radius (int): radius of the light (unit is pixel)
            intensity (float): between 0 and 1, represents the intensity of the light
        """

        self.lights[name] = PointLight(self.blank_base_model, color, position, radius, intensity)

    def render(self, surface):
        """
        Render all lights in the light system

        Parameters:
            surface (py_surface): the surface to draw lights on
        """

        for light in self.lights.values():
            light.render(surface)
