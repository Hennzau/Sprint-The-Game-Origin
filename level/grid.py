import numpy as np

from level.obstacle import Obstacle

"""
Grid will contain the different obstacles of the level in a board (np.array) of size(height, width).
"""


class Grid:
    def __init__(self, size):
        self.size = size
        self.obstacles = np.empty(self.size, dtype=Obstacle,
                                  like=None)  # none is an empty square in the grid (no obstacle).
