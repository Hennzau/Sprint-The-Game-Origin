from level.grid import Grid
from level.level import Level
from level.obstacle import Obstacle, colors

def build_level_0 ():
    level = Level ((30, 20), [(0, 0)], [colors["red"]], [(29, 19)])

    level.grid.obstacles[15, 19] = Obstacle ("darkgrey")
    level.grid.obstacles[15, 18] = Obstacle ("darkgrey")
    level.grid.obstacles[15, 17] = Obstacle ("darkgrey")
    level.grid.obstacles[15, 16] = Obstacle ("darkgrey")
    level.grid.obstacles[15, 15] = Obstacle ("darkgrey")
    level.grid.obstacles[15, 14] = Obstacle ("darkgrey")
    level.grid.obstacles[15, 13] = Obstacle ("darkgrey")
    level.grid.obstacles[15, 12] = Obstacle ("darkgrey")

    level.grid.obstacles[10, 19] = Obstacle ("yellow")
    level.grid.obstacles[10, 18] = Obstacle ("yellow")
    level.grid.obstacles[10, 17] = Obstacle ("yellow")

    level.grid.obstacles[15, 0] = Obstacle ("blue")
    level.grid.obstacles[15, 1] = Obstacle ("blue")
    level.grid.obstacles[15, 2] = Obstacle ("blue")

    level.grid.obstacles[29, 6] = Obstacle ("darkgrey")
    level.grid.obstacles[28, 6] = Obstacle ("darkgrey")
    level.grid.obstacles[27, 6] = Obstacle ("darkgrey")
    level.grid.obstacles[26, 6] = Obstacle ("darkgrey")
    level.grid.obstacles[25, 6] = Obstacle ("darkgrey")
    level.grid.obstacles[24, 6] = Obstacle ("darkgrey")
    level.grid.obstacles[23, 6] = Obstacle ("darkgrey")
    level.grid.obstacles[22, 6] = Obstacle ("darkgrey")
    level.grid.obstacles[21, 6] = Obstacle ("darkgrey")
    level.grid.obstacles[20, 6] = Obstacle ("darkgrey")

    level.grid.obstacles[17, 3] = Obstacle ("blue")
    level.grid.obstacles[17, 4] = Obstacle ("blue")
    level.grid.obstacles[17, 5] = Obstacle ("blue")

    level.grid.obstacles[4, 3] = Obstacle ("darkgrey")
    level.grid.obstacles[5, 3] = Obstacle ("darkgrey")
    level.grid.obstacles[6, 3] = Obstacle ("darkgrey")
    level.grid.obstacles[7, 3] = Obstacle ("darkgrey")
    level.grid.obstacles[8, 3] = Obstacle ("darkgrey")
    level.grid.obstacles[9, 3] = Obstacle ("darkgrey")
    level.grid.obstacles[10, 3] = Obstacle ("darkgrey")
    level.grid.obstacles[11, 3] = Obstacle ("darkgrey")

    level.grid.obstacles[2, 4] = Obstacle ("yellow", True)
    level.grid.obstacles[11, 0] = Obstacle ("blue", True)

    return build_level_1()

def build_level_1 ():
    level = Level ((30,20), [(7,8)], [colors["red"]], [(0, 19)] )
    
    level.grid.obstacles[25, 19] = Obstacle ("darkgrey")
    level.grid.obstacles[25, 18] = Obstacle ("darkgrey")
    level.grid.obstacles[25, 17] = Obstacle ("darkgrey")
    
    level.grid.obstacles[28, 8] = Obstacle ("darkgrey")
    level.grid.obstacles[29, 8] = Obstacle ("darkgrey")
    
    level.grid.obstacles[18, 17] = Obstacle ("darkgrey")
    
    level.grid.obstacles[8, 0] = Obstacle ("green")
    level.grid.obstacles[8, 1] = Obstacle ("green")
    level.grid.obstacles[8, 2] = Obstacle ("green")
    level.grid.obstacles[8, 3] = Obstacle ("green")
    
    level.grid.obstacles[0, 16] = Obstacle ("green")
    level.grid.obstacles[1, 16] = Obstacle ("green")
    level.grid.obstacles[2, 16] = Obstacle ("green")
    level.grid.obstacles[3, 16] = Obstacle ("green")
    level.grid.obstacles[4, 16] = Obstacle ("green")
    level.grid.obstacles[5, 16] = Obstacle ("green")
    
    level.grid.obstacles[15, 0] = Obstacle ("green")
    level.grid.obstacles[15, 1] = Obstacle ("green")
    level.grid.obstacles[15, 2] = Obstacle ("green")
    level.grid.obstacles[15, 3] = Obstacle ("green")
    
    level.grid.obstacles[18, 12] = Obstacle ("green")
    level.grid.obstacles[19, 12] = Obstacle ("green")
    level.grid.obstacles[20, 12] = Obstacle ("green")
    level.grid.obstacles[21, 12] = Obstacle ("green")
    level.grid.obstacles[22, 12] = Obstacle ("green")
    level.grid.obstacles[23, 12] = Obstacle ("green")
    level.grid.obstacles[24, 12] = Obstacle ("green")
    
    level.grid.obstacles[17,0] = Obstacle ("blue")
    level.grid.obstacles[17,1] = Obstacle ("blue")
    level.grid.obstacles[17,2] = Obstacle ("blue")
    level.grid.obstacles[17,3] = Obstacle ("blue")
    level.grid.obstacles[17,4] = Obstacle ("blue")
    level.grid.obstacles[17,5] = Obstacle ("blue")
    level.grid.obstacles[17,6] = Obstacle ("blue")
    level.grid.obstacles[17,7] = Obstacle ("blue")
    level.grid.obstacles[17,8] = Obstacle ("blue")
    
    level.grid.obstacles[13, 16] = Obstacle ("red")
    level.grid.obstacles[13, 17] = Obstacle ("red")
    level.grid.obstacles[13, 18] = Obstacle ("red")
    level.grid.obstacles[13, 19] = Obstacle ("red")
    
    level.grid.obstacles[5, 16] = Obstacle ("yellow")
    level.grid.obstacles[6, 16] = Obstacle ("yellow")
    level.grid.obstacles[7, 16] = Obstacle ("yellow")
    level.grid.obstacles[8, 16] = Obstacle ("yellow")
    level.grid.obstacles[9, 16] = Obstacle ("yellow")
    level.grid.obstacles[10, 16] = Obstacle ("yellow")
    level.grid.obstacles[11, 16] = Obstacle ("yellow")
    level.grid.obstacles[12, 16] = Obstacle ("yellow")
    
    level.grid.obstacles[6, 5]= Obstacle ("darkgrey")
    level.grid.obstacles[7, 5]= Obstacle ("darkgrey")
    level.grid.obstacles[8, 5]= Obstacle ("darkgrey")
    level.grid.obstacles[9, 5]= Obstacle ("darkgrey")
    level.grid.obstacles[10, 5]= Obstacle ("darkgrey")
    
    level.grid.obstacles[10, 6]= Obstacle ("darkgrey")
    level.grid.obstacles[10, 7]= Obstacle ("darkgrey")
    level.grid.obstacles[10, 8]= Obstacle ("darkgrey")
    level.grid.obstacles[10, 9]= Obstacle ("darkgrey")
    level.grid.obstacles[10, 10] = Obstacle ("darkgrey")
    
    level.grid.obstacles[13, 13] = Obstacle ("darkgrey")
    level.grid.obstacles[13, 14] = Obstacle ("darkgrey")
    level.grid.obstacles[13, 15] = Obstacle ("darkgrey")
    
    level.grid.obstacles[4, 7] = Obstacle ("blue")
    level.grid.obstacles[4, 8] = Obstacle ("blue")
    level.grid.obstacles[4, 9] = Obstacle ("blue")
    level.grid.obstacles[4, 10] = Obstacle ("blue")
    level.grid.obstacles[4, 11] = Obstacle ("blue")
    level.grid.obstacles[4, 12] = Obstacle ("blue")
    
    level.grid.obstacles[5, 12] = Obstacle ("blue")
    level.grid.obstacles[6, 12] = Obstacle ("blue")
    level.grid.obstacles[7, 12] = Obstacle ("blue")
    level.grid.obstacles[8, 12] = Obstacle ("blue")
    
    level.grid.obstacles[25, 16] = Obstacle ("yellow", True)
    level.grid.obstacles[11, 9] = Obstacle ("blue", True)
    level.grid.obstacles[14, 19] = Obstacle ("green", True)
    level.grid.obstacles[14, 0] = Obstacle ("red", True)
    
    return level