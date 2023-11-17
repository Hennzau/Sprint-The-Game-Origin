import pygame


def flip():
    pygame.display.flip()


def events():
    return pygame.event.get()


class Surface:
    def __init__(self, width, height, title):
        pygame.init()
        pygame.font.init()

        self.width = width
        self.height = height
        self.title = title
        self.py_surface = pygame.display.set_mode((width, height))

        pygame.display.set_caption(self.title)

    def clear(self, background_color):
        self.py_surface.fill(background_color)
