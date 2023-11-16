import pygame


def flip():
    pygame.display.flip()


def events():
    return pygame.event.get()


class Surface:
    def __init__(self, width, height, title):
        pygame.init()
        self.width = width
        self.height = height
        self.title = title
        self.surface = pygame.display.set_mode((width, height))
        self.blit = self.surface.blit
        pygame.display.set_caption(self.title)

    def clear(self, background_color):
        self.surface.fill(background_color)
