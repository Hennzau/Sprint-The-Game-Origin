# dictionary of the used colors, in RGB (format understood by pygame)
colors = {"red": (220, 20, 60), "blue": (106, 90, 205), "green": (154, 205, 50), "yellow": (255, 215, 0),
          "darkgrey": (105, 105, 105), "darkblue": (25, 25, 112)}
pixel_size = 30


# class obstacle that will be used in the grid, color is a key of the dictionnary
class Obstacle:
    def __init__(self, color, color_switcher=False, end=False):
        self.color = colors[color]
        self.color_switcher = color_switcher
        self.end = end
