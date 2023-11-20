## Imports
from level.grid import Grid
from level.level import Level
from level.obstacle import Obstacle, colors
from render.level_render import LevelRender
import pygame
from level.obstacle import pixel_size
from level.player import Player
import json
import os

class LevelEditor :

    def __init__(self, size):
        self.size = size
        self.level = Level(size, [], [], [])
        self.players = []
        self.colors = ["red", "yellow", "green", "blue", "darkgrey"]
        self.color_cursor = 0
        self.color_switcher = False
        self.level_render=LevelRender(self.level)

        self.select_add_player = False
        self.select_start = None
        self.select_end = None


        
        
    def new_player (self, color, initial_position, final_position ): # color must be a string
        self.level.initial_colors.append(color)
        self.level.initial_positions.append(initial_position) 
        self.level.final_positions.append(final_position)
        self.level.grid.obstacles[initial_position[0],initial_position[1]]=Obstacle(color, start=True)
        self.level.grid.obstacles[final_position[0],final_position[1]]=Obstacle(color, end=True)
        self.level.players.append(Player(colors[color], initial_position[0] * pixel_size,
                                       initial_position[1] * pixel_size))

        self.level_render=LevelRender(self.level)

    def new_tile (self,position):
        self.level.grid.obstacles[position[0], position[1]]=Obstacle (self.colors[self.color_cursor], self.color_switcher)
        self.level_render=LevelRender(self.level)

    def erase_tile (self, position):
        self.level.grid.obstacles[position[0], position[1]]=None
        self.level_render=LevelRender(self.level)

    def remove_last_player (self):
        self.level.players.pop()
        self.level.grid.obstacles[self.level.final_positions.pop()] = None
        self.level.grid.obstacles[self.level.initial_positions.pop()] = None
        self.level.initial_colors.pop()

        self.level_render=LevelRender(self.level)
        

    def update (self, delta_time):
        if pygame.Rect(0,0, self.size[0]*pixel_size, self.size[1]*pixel_size).collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not self.select_add_player :
                i = int(pygame.mouse.get_pos()[0]/pixel_size)
                j = int(pygame.mouse.get_pos()[1]/pixel_size)
                if self.level.grid.obstacles[i,j] == None or (self.level.grid.obstacles[i,j] != None and not self.level.grid.obstacles[i,j].end and not self.level.grid.obstacles[i,j].start):
                    self.new_tile((i,j))

            if pygame.mouse.get_pressed()[2] and not self.select_add_player:
                i = int(pygame.mouse.get_pos()[0]/pixel_size)
                j = int(pygame.mouse.get_pos()[1]/pixel_size)
                self.erase_tile((i,j))

    def save (self):
        dico = {}

        #size
        dico["size"]= [self.size[0],self.size[1]]

        #initial positions
        dico["initial_positions"]=[]
        for initial_position in self.level.initial_positions:
            dico["initial_positions"].append([initial_position[0], initial_position[1]])

        #final positions
        dico["final_positions"]=[]
        for final_position in self.level.final_positions:
            dico["final_positions"].append([final_position[0], final_position[1]])

        #initial colors
        dico["initial_colors"]=[]
        for initial_color in self.level.initial_colors:
            dico["initial_colors"].append(initial_color)

        #obstacles
        dico["obstacles"]=[]
        for i in range (self.size[0]):
            for j in range (self.size[1]):
                if self.level.grid.obstacles[i,j] is not None :
                    if not (self.level.grid.obstacles[i,j].color_switcher) and not (self.level.grid.obstacles[i,j].start) and not (self.level.grid.obstacles[i,j].end):
                        dico["obstacles"].append ([i,j,self.level.grid.obstacles[i,j].color_str])
                    if self.level.grid.obstacles[i,j].color_switcher:
                        dico["obstacles"].append([i,j,self.level.grid.obstacle[i,j].color_str,True])


        
        # Serializing json
        level_in_json = json.dumps(dico, indent=4)
 
        # Writing to level.json

        n = len(os.listdir("assets/levels"))
        path = "assets/levels/level_"+str(n+1)+".json"

        with open(path, "w") as outfile:
            outfile.write(level_in_json)
