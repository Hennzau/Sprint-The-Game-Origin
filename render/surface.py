import pygame


def flip():
    """
    Flip the surface (Double Buffering)
    """

    pygame.display.flip()


def events():
    """
    The events function returns pygame events
    """

    return pygame.event.get()


class Surface:
    """
    It's easier to manipulate a customs Surface object instead of a raw py_surface object
    """

    def __init__(self, width, height, title):
        """
        The Surface __init__ function will create a window and the surface associated to this window (display).

        Parameters:
        width (int): the width of the window (unit = pixel)
        height (int): the height of the window (unit = pixel)
        title (str): the title of the window
        """

        icon = pygame.image.load('assets/images/Sprint_Icon.png')
        pygame.display.set_icon(icon)

        pygame.init()
        pygame.font.init()

        self.width = width
        self.height = height
        self.title = title
        self.py_surface = pygame.display.set_mode((width, height))

        pygame.display.set_caption(self.title)

    def clear(self, background_color):
        """
        The clear function will clear the window's surface according to the 'background_color' passed

        Parameters:
        background_color (RGB): the background_color for the clear, in RGB format
        """

        self.py_surface.fill(background_color)
