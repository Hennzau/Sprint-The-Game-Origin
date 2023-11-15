from render.draw_player import draw_player
from render.draw_grid import draw_grid
from level.level import Level

"""
draw_level uses both draw_grid and draw_player in order to render the entire level to the user.
"""
def draw_level(level, surface):
    draw_grid(level.grid, surface)
    for k in range(len(level.players)):
        draw_player(level.players[k], surface)
