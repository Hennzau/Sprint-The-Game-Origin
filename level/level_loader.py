import json
"""

from level.level import Level
from level.obstacle import Obstacle, colors

"""

def build_level (level_json): #level_json format : 'data.json'
    json_file = open(level_json)
    data = json.load(json_file) #data is a json object, like a dictionary

    for obstacle in data["obstacles"]:
        print(obstacle)