#importations
from level.level import Level
from level.grid import Grid
from level.obstacle import colors
from level.player import Player

#class game which updates the game (logic and render) at each passage through the main loop

class Game :
    def __init__(self):
        self.levels = []
        self.levels.append(Level((20,20),[(0,0)],[colors["red"]]))
        
    def update(self,delta_time):
        player.update()

    def render (self):
        #update le rendu
        pass
