from grid import Grid
from player import Player
from obstacle import colors



class Level:
    def __init__(self, size, initial_positions, initial_colors):
        self.grid=Grid(size)
        self.players=[]
        for k in range(len(initial_positions)):
            self.players.append(Player(initial_colors[k], initial_positions[k][0], initial_positions[k][1], 0, 0))
            

