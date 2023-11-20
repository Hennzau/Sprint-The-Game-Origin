import numpy as np

from level.obstacle import Obstacle


class Grid:
    """
    Grid will contain the different obstacles of the level in a board (np.array) of size(height, width).
    """

    def __init__(self, size):
        """
        The Grid __init__ function will generate a new numpy array of 'Obstacle' object and
        save in memory the size of the grid for faster access later

        Parameters:
        size ((int,int)): width and height size of the grid
       """

        self.size = size
        self.obstacles = np.empty(self.size, dtype=Obstacle,
                                  like=None)  # none is an empty square in the grid (no obstacle).
