from level.level import Level
from level.player import Player

from render.grid_render import GridRender

from render.draw_player import draw_player


class LevelRender:
    """"
    To make things faster, a LevelRender class is necessary : it will manage the calculus of each frame by taking a cache
    image already calculated
    """

    def __init__(self, level):
        """
        The LevelRender __init__ function will create a new GridRender object to enable fast rendering. The LevelRender
        object must be created after the complete loading of the level (and the grid of the level)

        Parameters:
        level (Level): the level Object to render
        """

        self.level = level

        self.grid_render = GridRender(level.grid)

    def render(self, surface):
        """
        The render function will render the grid through the GridRender object and the players with a basic function

        Parameters:
        surface (py_surface): the PyGame Surface you want to draw the level on
        """

        self.grid_render.render(surface, self.level.time)

        for player in self.level.players:
            draw_player(player, surface)

        self.level.particle_system.render(surface)
        self.level.light_system.render(surface)
