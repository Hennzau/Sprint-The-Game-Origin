###Imports###
import json

from level.level import Level
from level.obstacle import Obstacle, colors

### build level function
''' 
this function takes a level written in a json file
it returns the level objet that can be read by our python code
'''

def build_level (level_json): #level_json format : 'data.json'
    json_file = open(level_json)
    data = json.load(json_file) #data is a json object, like a dictionary

    #recuperation of the data
    size = data["size"]
    initial_positions_table = data["initial_positions"]
    final_positions_table = data ["final_positions"]
    initial_colors = data ["colors"]

    #creation of the lists of tuples for initial and final positions
    initial_positions_tuple =[(initial_positions_table[i][0],initial_positions_table[i][1]) for i in range (len(initial_positions_table))]
    final_positions_tuple = [(final_positions_table[i][0],final_positions_table[i][1])for i in range (len(final_positions_table))]
    #creation of the list of colors in rgb format
    initial_colors_rgb = [colors[color_name]for color_name in initial_colors]
    #creation of the level
    level = Level(size,initial_positions_tuple , initial_colors_rgb, final_positions_tuple)

    #creation of the obstacles
    for obstacle in data["obstacles"]:
        if len(obstacle)==3:
            level.grid.obstacles[obstacle[0],obstacle[1]]=Obstacle(obstacle[2])
        if len(obstacle)==4 :
            level.grid.obstacles[obstacle[0],obstacle[1]]=Obstacle(obstacle[2],obstacle[3])
        if len(obstacle)==5:
            level.grid.obstacles[obstacle[0],obstacle[1]]=Obstacle(obstacle[2],obstacle[3],obstacle[4])
    return level
