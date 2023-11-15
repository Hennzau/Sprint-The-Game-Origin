from grid import Grid
from player import Player
from obstacle import colors

"""
A Level is an object that contains the grid and players data
"""


class Level:
    def __init__(self, size, initial_positions, initial_colors):  # starting positions of the players inside the grid
        self.grid = Grid(size)
        self.players = []

        for k in range(
                len(initial_positions)):  # sometimes there is two players and we can imagine a level with even more

            self.players.append(Player(initial_colors[k], initial_positions[k][0], initial_positions[k][1], 0, 0))
