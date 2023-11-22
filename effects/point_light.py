import pygame
import numpy as np


class PointLight:
    """
    In Sprint The Game, every source of light is actually a PointLight, which means the source is present in the grid
    """

    def __init__(self, base_model, color, position, radius, intensity):
        """
        The PointLight __init__ function takes everything a Light Point needs to be created, in particular,
        it takes a base_model of a blank model light already rendered in an image (a pygame surface)

        Parameters:
            base_model (py_surface): the blank model
            color (RGB): the color in the RGB format
            position ((int,int)): position of the light (unit is pixel)
            radius (int): radius of the light (unit is pixel)
            intensity (float): between 0 and 1, represents the intensity of the light
        """

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

        # color mask to match what the user wants
        temp_surface = pygame.Surface((self.radius * 2, self.radius * 2))
        temp_surface.fill(
            (min(self.color[0] * self.intensity, 255), min(self.color[1] * self.intensity, 255),
             min(self.color[2] * self.intensity, 255)))

        self.image.blit(temp_surface, (0, 0), special_flags=pygame.BLEND_RGB_MULT)

    def change_color(self, color):
        """
        The change_color function reloads the color mask to apply on the base_model

        Parameters:
            color (RGB): the color in the RGB format
        """

        if self.color != color:  # only if the mask changed
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
        """
        The move function changes the position of the light point

        Parameters:
            position ((int,int)): the new position
        """

        self.position = position

    def render(self, surface):
        """
        Render the point light on the given surface

        Parameters:
            surface (py_surface): the surface to draw the light on
        """

        # merge the 'self.image' mask on the surface at the right position
        surface.blit(self.image, (self.position[0] - self.radius, self.position[1] - self.radius),
                     special_flags=pygame.BLEND_RGBA_ADD)
