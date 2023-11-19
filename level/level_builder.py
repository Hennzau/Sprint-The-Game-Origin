from level.grid import Grid
from level.level import Level
from level.obstacle import Obstacle, colors


def build_level_0():
    level = Level((30, 20), [(0, 0)], [colors["red"]], [(29, 19)])

    level.grid.obstacles[15, 19] = Obstacle("darkgrey")
    level.grid.obstacles[15, 18] = Obstacle("darkgrey")
    level.grid.obstacles[15, 17] = Obstacle("darkgrey")
    level.grid.obstacles[15, 16] = Obstacle("darkgrey")
    level.grid.obstacles[15, 15] = Obstacle("darkgrey")
    level.grid.obstacles[15, 14] = Obstacle("darkgrey")
    level.grid.obstacles[15, 13] = Obstacle("darkgrey")
    level.grid.obstacles[15, 12] = Obstacle("darkgrey")

    level.grid.obstacles[10, 19] = Obstacle("yellow")
    level.grid.obstacles[10, 18] = Obstacle("yellow")
    level.grid.obstacles[10, 17] = Obstacle("yellow")

    level.grid.obstacles[15, 0] = Obstacle("blue")
    level.grid.obstacles[15, 1] = Obstacle("blue")
    level.grid.obstacles[15, 2] = Obstacle("blue")

    level.grid.obstacles[29, 6] = Obstacle("darkgrey")
    level.grid.obstacles[28, 6] = Obstacle("darkgrey")
    level.grid.obstacles[27, 6] = Obstacle("darkgrey")
    level.grid.obstacles[26, 6] = Obstacle("darkgrey")
    level.grid.obstacles[25, 6] = Obstacle("darkgrey")
    level.grid.obstacles[24, 6] = Obstacle("darkgrey")
    level.grid.obstacles[23, 6] = Obstacle("darkgrey")
    level.grid.obstacles[22, 6] = Obstacle("darkgrey")
    level.grid.obstacles[21, 6] = Obstacle("darkgrey")
    level.grid.obstacles[20, 6] = Obstacle("darkgrey")

    level.grid.obstacles[17, 3] = Obstacle("blue")
    level.grid.obstacles[17, 4] = Obstacle("blue")
    level.grid.obstacles[17, 5] = Obstacle("blue")

    level.grid.obstacles[4, 3] = Obstacle("darkgrey")
    level.grid.obstacles[5, 3] = Obstacle("darkgrey")
    level.grid.obstacles[6, 3] = Obstacle("darkgrey")
    level.grid.obstacles[7, 3] = Obstacle("darkgrey")
    level.grid.obstacles[8, 3] = Obstacle("darkgrey")
    level.grid.obstacles[9, 3] = Obstacle("darkgrey")
    level.grid.obstacles[10, 3] = Obstacle("darkgrey")
    level.grid.obstacles[11, 3] = Obstacle("darkgrey")

    level.grid.obstacles[2, 4] = Obstacle("yellow", True)
    level.grid.obstacles[11, 0] = Obstacle("blue", True)

    return level
