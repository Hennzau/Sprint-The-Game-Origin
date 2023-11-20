## Imports
from level.grid import Grid
from level.level import Level
from level.obstacle import Obstacle, colors
from render.level_render import LevelRender


class LevelEditor :

    def __init__(self, size):
        self.size = size
        self.level = Level(size, [], [], [])
        self.players = []
        self.colors = ["red", "yellow", "green", "blue", "darkgrey"]
        self.color_cursor = 0
        self.color_switcher = False
        self.level_render=LevelRender(self.level)
        
        
    def new_player (self, color, initial_position, final_position ):
        self.level.initial_colors.append(color)
        self.level.initial_positions.append(initial_position)
        self.level.final_positions.append(final_position)
        self.level.grid.obstacle[initial_position[0],initial_position[1]]=Obstacle(colors[color], start=True)
        self.level.grid.obstacle[final_position[0],final_position[1]]=Obstacle(colors[color], end=True)
        self.level_render=LevelRender(self.level)

    def new_tile (self,position):
        self.level.grid.obstacles[position[0], position[1]]=Obstacle (colors[self.colors[self.color_cursor]], self.color_switcher)
        self.level_render=LevelRender(self.level)