# Management of the player object #

# Import #
import numpy as np
from level.grid import Grid
import pygame

# ---------------- #


class Player:
    # Player object has a color, a position and a velocity
    def __init__(self, color, x_init, y_init, x_velocity, y_velocity):
        self.color = color
        self.position = np.array([x_init, y_init])
        self.velocity = np.array([x_velocity, y_velocity])

    def update_velocity(self, x, y):
        self.velocity = np.array([x, y])

    def update(self, delta_time, level):
        if (level.grid).obstacles[int(((self.position + self.velocity * delta_time)/50)[0]), int(((self.position + self.velocity * delta_time)/50)[1])] is not None:
            self.position = self.position
            self.velocity = np.array([0, 0])
        else:
            self.position = self.position + self.velocity * delta_time
        if [int(self.position[0]/50), int(self.position[1]/50)] == level.final_position:
            pygame.quit()
