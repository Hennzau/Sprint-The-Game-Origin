# Management of the player object #

# Import #
import numpy as np
from grid import Grid
from level.obstacle import pixel_size

# ---------------- #


class Player:
    # Player object has a color, a position and a velocity
    def __init__(self, color, x_init, y_init, x_velocity, y_velocity):
        self.color = color
        self.position = np.array([x_init, y_init])
        self.velocity = np.array([x_velocity, y_velocity])

    def update_velocity(self, x, y):
        if (self.velocity==np.array([0,0])).all():
            self.velocity = np.array([x, y])

    def collides(self,next_position,grid):
        x = int (next_position[0]/pixel_size)
        y = int (next_position[1]/pixel_size)

        if grid.obstacles[x, y] is None:
            return False
        
        if grid.obstacles[x,y].color_switcher :
            self.color = grid.obstacles[x,y].color
            return False
        
        if grid.obstacles[x,y].color == self.color :
            return False
        
        return True

    def update(self, delta_time, grid):
        if self.collides(self.position + self.velocity * delta_time, grid):
            self.position = self.position
            self.velocity = np.array([0,0])
        else :
            self.position = self.position + self.velocity * delta_time


