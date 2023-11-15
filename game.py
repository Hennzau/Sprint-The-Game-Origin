# importations

from level.level import Level
from level.obstacle import colors


# class game which updates the game (logic and render) at each passage through the main loop

class Game:
    def __init__(self):
        self.levels = []
        self.levels.append(Level((20, 20), [(0, 0)], [colors["red"]]))

    def update(self, delta_time):     
        pass
    
    def is_open(self):
        for event in events():
            if event.type == pygame.QUIT:
                return False
            else: 
                return True
    
    def render(self):
        # update le rendu
        pass
