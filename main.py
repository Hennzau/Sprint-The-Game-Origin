### Main loop of the game###

## Imports ##
import pygame
from game import Game
from render.window import Window
from level.obstacle import colors
## ----------------- ##


def main():
    surface = Window(800, 800, "test")
    game = Game()
    while True:
        start = pygame.time.get_ticks()
        surface.clear(colors["darkgrey"])
        end = pygame.time.get_ticks()
        deltatime = (end-start)/1000
        game.update(deltatime)
        surface.flip()


if __name__ == '__main__':
    main()
