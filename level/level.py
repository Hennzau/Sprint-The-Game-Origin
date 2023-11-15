from level.grid import Grid
from level.player import Player
from level.obstacle import colors

"""
A Level is an object that contains the grid and players data
"""


class Level:
    # starting positions of the players inside the grid
    def __init__(self, size, initial_positions, initial_colors, final_position):
        self.grid = Grid(size)
        self.players = []
        self.final_position = final_position
        for k in range(
                len(initial_positions)):  # sometimes there is two players and we can imagine a level with even more

            self.players.append(Player(
                initial_colors[k], initial_positions[k][0], initial_positions[k][1], 0, 0))

    def update(self, delta_time):
        for player in self.players:
            player.update(delta_time, self)
