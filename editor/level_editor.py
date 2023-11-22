# Imports #
import pygame
import json
import os

from level.level import Level
from level.obstacle import Obstacle, colors, pixel_size
from level.player import Player
from level.level_loader import build_level

from render.level_render import LevelRender


class LevelEditor:
    """
    The LevelEditor class is used like the Game class, but it removes some things and offers an interface
    to create a new level.
    """

    def __init__(self, size, edit=None):
        """
        the LevelEditor __init__ function initializes the LevelEditor
        with all the parameters you need to create/edit a level

        Parameters:
        size ((int,int)): the size of the grid you want to create
        edit (str or None): if None create an empty level, if not, edit a level
        """

        self.size = size
        self.level = Level(size, [], [], [])

        if edit is not None:
            self.level = build_level(edit)
            self.size = self.level.grid.size

        self.colors = ["red", "yellow", "green", "blue", "darkgrey"]
        self.color_cursor = 0
        self.color_switcher = False
        self.level_render = LevelRender(self.level)

        self.select_add_player = False
        self.select_start = None
        self.select_end = None

    def new_player(self, color, initial_position, final_position):
        """
        the new_player function takes everything a player needs to be created and adds it in real-time to the level

        Parameters:
        color (str): the color in the string format
        initial_position ((int,int)): the starting position (unit = pixel_size)
        final_position ((int,int)): the ending position (unit = pixel_size)
        """

        self.level.initial_colors.append(color)
        self.level.initial_positions.append(initial_position)
        self.level.final_positions.append(final_position)
        self.level.grid.obstacles[initial_position[0], initial_position[1]] = Obstacle(color, start=True)
        self.level.grid.obstacles[final_position[0], final_position[1]] = Obstacle(color, end=True)
        self.level.players.append(Player(colors[color], initial_position[0] * pixel_size,
                                         initial_position[1] * pixel_size))

        self.level_render = LevelRender(self.level)  # update the image of the grid

    def new_tile(self, position):
        """
        the new_tile function create a new obstacle on the grid depending on the parameters of the level editor

        Parameters:
        position ((int,int)): the position of the new obstacle/tile (unit = pixel_size)
        """

        self.level.grid.obstacles[position[0], position[1]] = Obstacle(self.colors[self.color_cursor],
                                                                       self.color_switcher)
        self.level_render = LevelRender(self.level)

    def erase_tile(self, position):
        """
        the erase_tile function remove an obstacle by replacing its value in the grid by 'None'

        Parameters:
        position ((int,int)): the position of the obstacle/tile to remove (unit = pixel_size)
        """

        self.level.grid.obstacles[position[0], position[1]] = None
        self.level_render = LevelRender(self.level)  # update the image of the grid

    def remove_last_player(self):
        """
        the remove_last_player function delete the last player created
        """

        self.level.players.pop()
        self.level.grid.obstacles[self.level.final_positions.pop()] = None
        self.level.grid.obstacles[self.level.initial_positions.pop()] = None
        self.level.initial_colors.pop()

        self.level_render = LevelRender(self.level)  # update the image of the grid

    def save(self):
        """
        the save function save to the JSON format the current level in the level editor
        """

        level_json = {
            "size": [self.size[0], self.size[1]],  # size
            "initial_positions": []
        }

        # initial positions

        for initial_position in self.level.initial_positions:
            level_json["initial_positions"].append([initial_position[0], initial_position[1]])

        # final positions
        level_json["final_positions"] = []
        for final_position in self.level.final_positions:
            level_json["final_positions"].append([final_position[0], final_position[1]])

        # initial colors
        level_json["initial_colors"] = []
        for initial_color in self.level.initial_colors:
            level_json["initial_colors"].append(initial_color)

        # obstacles
        level_json["obstacles"] = []
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.level.grid.obstacles[i, j] is not None:
                    if not (self.level.grid.obstacles[i, j].color_switcher) and not (
                            self.level.grid.obstacles[i, j].start) and not (self.level.grid.obstacles[i, j].end):
                        level_json["obstacles"].append([i, j, self.level.grid.obstacles[i, j].color_str])
                    if self.level.grid.obstacles[i, j].color_switcher:
                        level_json["obstacles"].append([i, j, self.level.grid.obstacles[i, j].color_str, True])

        # Serializing json
        level_in_json = json.dumps(level_json, indent=4)

        # Writing to JSON file
        
        n = None
        for i in range(1, len(os.listdir("assets/levels/custom")) + 2):
            path = "assets/levels/custom/level_" + str(i) + ".json"
            if not os.path.isfile(path):
                n = i
                break

        if n is not None:
            path = "assets/levels/custom/level_" + str(n) + ".json"

            with open(path, "w") as outfile:
                outfile.write(level_in_json)
