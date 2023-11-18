import pygame
import numpy as np

"""
In Sprint The Game, every source of light is actually a PointLight, which means the source is present in the grid
"""


class PointLight:
    # take an initial color (RGB) and an initial position
    def __init__(self, base_model, color, position, radius, intensity):
        self.color = color
        self.position = position
        self.intensity = intensity
        self.radius = radius
        self.intensity = intensity

        # We create the 'mask' image that contains de light map
        # Then we will be able to merge 'image' into a surface to add some light on it

        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)

        # scale the model to the wanted radius

        self.base_model = pygame.transform.scale(base_model, (self.radius * 2, self.radius * 2))

        self.image.blit(self.base_model, (0, 0),
                        special_flags=pygame.BLEND_RGBA_ADD)

        temp_surface = pygame.Surface((self.radius * 2, self.radius * 2))
        temp_surface.fill(
            (min(self.color[0] * self.intensity, 255), min(self.color[1] * self.intensity, 255),
             min(self.color[2] * self.intensity, 255)))

        self.image.blit(temp_surface, (0, 0), special_flags=pygame.BLEND_RGB_MULT)

    def change_color(self, color):
        if self.color != color:
            self.color = color

            self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)

            # scale the model to the wanted radius
            self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)

            self.image.blit(self.base_model, (0, 0),
                            special_flags=pygame.BLEND_RGBA_ADD)

            temp_surface = pygame.Surface((self.radius * 2, self.radius * 2))
            temp_surface.fill(
                (min(self.color[0] * self.intensity, 255), min(self.color[1] * self.intensity, 255),
                 min(self.color[2] * self.intensity, 255)))

            self.image.blit(temp_surface, (0, 0), special_flags=pygame.BLEND_RGB_MULT)

    def move(self, position):
        self.position = position

    def render(self, surface):  # merge the 'self.image' mask on the surface at the right position
        surface.blit(self.image, (self.position[0] - self.radius, self.position[1] - self.radius),
                     special_flags=pygame.BLEND_RGBA_ADD)
