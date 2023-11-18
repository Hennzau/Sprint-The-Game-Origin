import pygame
import numpy as np

from effects.point_light import PointLight

"""
The LightSystem class manages every light in the game (their color and their position)
"""


class LightSystem:
    def __init__(self):
        self.lights = {}

        # we generate the blank mask of lights once

        self.precision = 60
        self.radius = 300

        self.blank_base_model = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)

        for k in range(self.precision):
            sub_radius = self.radius * (self.precision - k) / self.precision
            temp_surface = pygame.Surface((sub_radius * 2, sub_radius * 2), pygame.SRCALPHA)

            pygame.draw.circle(temp_surface,
                               (int(255 / self.precision), int(255 / self.precision), int(255 / self.precision)),
                               (sub_radius, sub_radius), sub_radius, 0)

            self.blank_base_model.blit(temp_surface, (self.radius - sub_radius, self.radius - sub_radius),
                                       special_flags=pygame.BLEND_RGBA_ADD)

    def add_light(self, name, color, position, radius, intensity):
        self.lights[name] = PointLight(self.blank_base_model, color, position, radius, intensity)

    def render(self, surface):
        for _, light in self.lights.items():
            light.render(surface)
