# dictionary of the used colors, in RGB (format understood by pygame)

colors = {"red": (220, 20, 60), "blue": (106, 90, 205), "green": (154, 205, 50), "yellow": (255, 215, 0),
          "darkgrey": (105, 105, 105), "darkblue": (2, 4, 55), "darkerblue": (0, 0, 51), "ivory": (255, 255, 212),
          "Volkswagen Taupe": (140, 134, 128), "Black": (0, 0, 0)}

# this is the pixel size that defines everything : each tile in the grid has this size and even the player.

pixel_size = 40


# class obstacle that will be used in the grid, color is a key of the dictionnary
class Obstacle:
    """

    an obstacle is defined by its color and its behaviour (if it's a color_switcher etc...), the color is a string
    that refers to a key of 'colors'

    """

    def __init__(self, color, color_switcher=False, start=False, end=False):
        """
        the Obstacle __init__ function initializes an obstacle object depending on its color and its type

        Parameters:
        color (str): the string value of the color in the dictionary 'colors'
        color_switcher (boolean): True if the Obstacle is a color_switcher
        start (boolean): True if the Obstacle is a special start obstacle
        end (boolean): True if the Obstacle is a special end obstacle
        """

        self.color = colors[color]
        self.color_switcher = color_switcher
        self.end = end
        self.start = start
