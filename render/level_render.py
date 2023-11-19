from level.level import Level
from level.player import Player

from render.grid_render import GridRender

from render.draw_player import draw_player

""""
To make things faster, a LevelRender class is necessary : it will manage the calculus of each frame by taking a cache
image already calculated
"""


class LevelRender:
    def __init__(self, level):  # must be created after the complete loading of the level (and the grid of the level)
        self.level = level

        self.grid_render = GridRender(level.grid)

    def render(self, surface):  # requires a pygame surface (ie py_surface)
        self.grid_render.render(surface, self.level.time)

        for player in self.level.players:
            draw_player(player, surface)

        self.level.particle_system.render(surface)
        self.level.light_system.render(surface)
