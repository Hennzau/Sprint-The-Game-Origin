# Management of the player object #

# Import #
import numpy as np
from level.grid import Grid
from level.obstacle import Obstacle, pixel_size
from sound import sound_collision

from effects.particle_system import ParticleSystem
from effects.point_particle import PointParticle


# ---------------- #

class Player:
    """
    Player object has a color (in RGB format, not in str) and a position.
    The class Player manages movements of the player depending on the input key pressed by the user and the grid by
    creating and calculating a 'destination' variable that the player will reach
    """

    def __init__(self, color, x_init, y_init):
        """
        the Player __init__ function initializes a new player and its parameters for its movements, and its actions
        (like bouncing, the motion blur etc...)

        Parameters:
        color ((int, int, int)): color is in RGB format : it's the initial color of the player
        x_init (int): the initial x position of the player on the surface (in 0...grid.size[0] * pixel_size)
        y_init (int): the initial y position of the player on the surface (in 0...grid.size[1] * pixel_size)
        """
        self.color = color

        self.position = np.array([x_init, y_init])
        self.render_position = np.array([x_init, y_init])

        # the destination parameter is updated when the player wants to move and the 'update' function
        # manages the travel of the player from its current position to the destination position

        self.destination = np.array([x_init,
                                     y_init])

        # some variables that defines the characteristics of the player (like its speed, its ability to move,
        # and its bouncing behaviour and finally some fun data about the last positions of the player)

        self.is_moving = False
        self.start_speed = 1000
        self.speed = self.start_speed

        self.bounces = False
        self.bounce_amplitude = 0
        self.bounce_time = 0
        self.bounce_direction = np.array([0, 0])

        self.record_length = 4
        self.last_positions = []
        self.cursor = 0

    def surface_position(self):
        """
        Returns:
        the coordinates of the player in a np array, on the surface (unit = pixel)
        """
        return self.position

    def level_position(self):
        """
        Returns:
        the coordinates of the player in a np array, on the GRID (unit = pixel_size)
        """
        x = int(self.position[0] / pixel_size)
        y = int(self.position[1] / pixel_size)

        return np.array([x, y])

    def advance_x(self, grid, r1, r2):
        """
        the 'advance_x' function is an internal function that should not be called from anything else than the
        'calculate destination' of the player. It searches for the final obstacle that the player can go on for the
        horizontal axis

        Parameters:
        grid (Grid): the Grid of the current level containing obstacles,
        r1: (int) is the range of the search, depends on r2,
        r2: (int) the step of the search : 1 or -1 depending on the direction of the axis

        Returns:
        the int measure of the destination that the player can reach (can be negative)
        """
        x, y = self.level_position()
        i = 0

        active_color = self.color

        for j in range(x, r1, r2):  # start at the position of the player and move on the horizontal axis
            if grid.obstacles[j, y] is None:  # if there is no obstacle, the player can go there
                i = j - x
                continue
            else:
                # there are some exceptions
                if grid.obstacles[j, y].color_switcher:
                    active_color = grid.obstacles[j, y].color
                    i = j - x
                    continue

                if grid.obstacles[j, y].start:
                    i = j - x
                    continue

                if grid.obstacles[j, y].end:
                    i = j - x
                    continue

                # if it's a basic obstacle let's break the loop : the player can't go on this tile
                if not grid.obstacles[j, y].color_switcher and not grid.obstacles[j, y].start and not grid.obstacles[
                    j, y].end and not (
                        grid.obstacles[j, y].color == active_color):
                    break

        return i

    # same for vertical axis
    def advance_y(self, grid, r1, r2):
        """
        the 'advance_y' function is an internal function that should not be called from anything else than the
        'calculate destination' of the player. It searches for the final obstacle that the player can go on for the
        vertical axis

        Parameters:
        grid (Grid): the Grid of the current level containing obstacles,
        r1: (int) is the range of the search, depends on r2,
        r2: (int) the step of the search : 1 or -1 depending on the direction of the axis

        Returns:
        the int measure of the destination that the player can reach (can be negative)
        """

        x, y = self.level_position()
        i = 0

        active_color = self.color

        for j in range(y, r1, r2):
            if grid.obstacles[x, j] is None:
                i = j - y
                continue
            else:
                if grid.obstacles[x, j].color_switcher:
                    active_color = grid.obstacles[x, j].color
                    i = j - y
                    continue
                if grid.obstacles[x, j].start:
                    i = j - y
                    continue

                if grid.obstacles[x, j].end:
                    i = j - y
                    continue

                if not grid.obstacles[x, j].color_switcher and not grid.obstacles[x, j].start and not grid.obstacles[
                    x, j].end and not (
                        grid.obstacles[x, j].color == active_color):
                    break

        return i

    # manges the calculus regarding the direction
    def calculate_destination(self, grid, direction):
        """
        the 'calculate_destination' function uses 'advance_?' function depending on the direction the user want to move
        to.

        Parameters:
        grid (Grid): the Grid of the current level containing obstacles,
        direction (str): the direction in ["right", "left", "up", "down"]

        Returns:
        np.array([int,int]): the destination on the GRID that the player has to go to
        """

        x, y = self.level_position()

        if direction == "right":
            return np.array([x + self.advance_x(grid, grid.size[0], 1), y])

        if direction == "left":
            return np.array([x + self.advance_x(grid, -1, -1), y])

        if direction == "down":
            return np.array([x, y + self.advance_y(grid, grid.size[1], 1)])

        if direction == "up":
            return np.array([x, y + self.advance_y(grid, -1, -1)])

    def move_up(self, grid):
        """
        the 'move_?' is the interface between the game and the player: this function is called by the game when the user
        presses a key. It updates the 'destination' variable

        Parameters:
        grid (Grid): the Grid of the current level containing obstacles
        """

        self.bounce_direction = np.array([0, -1])  # changes the future bounce direction

        self.destination = self.calculate_destination(grid, "up") * pixel_size
        self.is_moving = True

    def move_down(self, grid):
        """
        the 'move_?' is the interface between the game and the player: this function is called by the game when the user
        presses a key. It updates the 'destination' variable

        Parameters:
        grid (Grid): the Grid of the current level containing obstacles
        """

        self.bounce_direction = np.array([0, 1])

        self.destination = self.calculate_destination(grid, "down") * pixel_size
        self.is_moving = True

    def move_left(self, grid):
        """
        the 'move_?' is the interface between the game and the player: this function is called by the game when the user
        presses a key. It updates the 'destination' variable

        Parameters:
        grid (Grid): the Grid of the current level containing obstacles
        """

        self.bounce_direction = np.array([-1, 0])

        self.destination = self.calculate_destination(grid, "left") * pixel_size
        self.is_moving = True

    def move_right(self, grid):
        """
        the 'move_?' is the interface between the game and the player: this function is called by the game when the user
        presses a key. It updates the 'destination' variable

        Parameters:
        grid (Grid): the Grid of the current level containing obstacles
        """

        self.bounce_direction = np.array([1, 0])

        self.destination = self.calculate_destination(grid, "right") * pixel_size
        self.is_moving = True

    def update(self, delta_time, grid):
        """
        the 'update' function manages actions of the player like the bouncing, it also records the last positions of
        the player for the motion blur effect.
        It also manages the switch of the color when the player move in the grid

        Parameters:
        delta_time (float): the delta_time calculated in main.py
        grid (Grid): the Grid of the current level containing obstacles
        """

        # record the last 'record_length' positions of the player
        if len(self.last_positions) != self.record_length:
            self.last_positions.append(self.render_position)
        else:
            self.last_positions[self.cursor] = self.render_position
            self.cursor = (self.cursor + 1) % self.record_length

        # manages the bounces with a sinusoidal function

        if self.bounces:
            self.bounce_time = self.bounce_time + delta_time
            if self.bounce_amplitude == 0:
                self.bounce_amplitude = 10
            else:
                self.bounce_amplitude = self.bounce_amplitude - 40 * delta_time

            if self.bounce_time >= 0.25:
                self.bounce_time = 0
                self.bounce_amplitude = 0
                self.bounces = False
                self.bounce_direction = np.array([0, 0])

        self.render_position = self.position + self.bounce_direction * self.bounce_amplitude * np.sin(
            -20 * self.bounce_time)

        # manages the movement of the player

        if (self.position == self.destination).all():
            if self.is_moving:
                sound_collision()
                self.bounces = True
                self.is_moving = False
                self.speed = self.start_speed
        else:
            self.speed += self.start_speed * 8 * delta_time  # the speed increases in time
            distance = np.linalg.norm(self.destination - self.position)
            direction = (self.destination - self.position) / distance
            delta = self.speed * delta_time

            self.bounce_direction = direction

            # check that the next frame the player will not cross the destination (if the speed is too high)

            if (direction == np.array([1, 0])).all():
                if self.position[0] + delta > self.destination[0]:
                    self.position[0] = self.destination[0]
                else:
                    self.position[0] = self.position[0] + delta

            if (direction == np.array([0, 1])).all():
                if self.position[1] + delta > self.destination[1]:
                    self.position[1] = self.destination[1]
                else:
                    self.position[1] = self.position[1] + delta

            if (direction == np.array([-1, 0])).all():
                if self.position[0] - delta < self.destination[0]:
                    self.position[0] = self.destination[0]
                else:
                    self.position[0] = self.position[0] - delta

            if (direction == np.array([0, -1])).all():
                if self.position[1] - delta < self.destination[1]:
                    self.position[1] = self.destination[1]
                else:
                    self.position[1] = self.position[1] - delta

        # the player is on a color_switcher

        x, y = self.level_position()

        if grid.obstacles[x, y] is not None:
            if grid.obstacles[x, y].color_switcher:
                self.color = grid.obstacles[x, y].color
