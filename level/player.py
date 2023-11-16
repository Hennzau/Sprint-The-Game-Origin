# Management of the player object #

# Import #
import numpy as np
from level.grid import Grid
from level.obstacle import Obstacle, pixel_size
from sound import sound_collision


# ---------------- #


class Player:
    # Player object has a color, a position and a velocity
    def __init__(self, color, x_init, y_init, x_velocity, y_velocity):
        self.color = color

        self.position = np.array([x_init, y_init])
        self.destination = np.array([x_init, y_init])

        self.is_moving = False
        self.speed = 400

    def surface_position(self):
        return self.position

    def level_position(self):
        x = int(self.position[0] / pixel_size)
        y = int(self.position[1] / pixel_size)

        return np.array([x, y])

    def calculate_destination(self, grid, direction):
        x, y = self.level_position()

        if direction == "right":
            i = 1
            while i < grid.size[0] - x - 1:
                if grid.obstacles[x + i, y] is not None:
                    if not grid.obstacles[x + i, y].color_switcher and not grid.obstacles[x + i, y].end:
                        return np.array([x + i - 1, y])
                i += 1

            return np.array([x + i, y])

        if direction == "left":
            i = -1
            while x + i >= 1:
                if grid.obstacles[x + i, y] is not None:
                    if not grid.obstacles[x + i, y].color_switcher and not grid.obstacles[x + i, y].end:
                        return np.array([x + i + 1, y])
                i -= 1

            return np.array([x + i, y])

        if direction == "down":
            i = 1
            while i < grid.size[1] - y - 1:
                if grid.obstacles[x, y + i] is not None:
                    if not grid.obstacles[x, y + i].color_switcher and not grid.obstacles[x, y + i].end:
                        return np.array([x, y + i - 1])
                i += 1

            return np.array([x, y + i])

        if direction == "up":
            i = -1
            while y + i >= 1:
                if grid.obstacles[x, y + i] is not None:
                    if not grid.obstacles[x, y + i].color_switcher and not grid.obstacles[x, y + i].end:
                        return np.array([x, y + i + 1])
                i -= 1

            return np.array([x, y + i])

    def move_up(self, grid):
        if not self.is_moving:
            self.destination = self.calculate_destination(grid, "up") * pixel_size
            self.is_moving = True

    def move_down(self, grid):
        if not self.is_moving:
            self.destination = self.calculate_destination(grid, "down") * pixel_size
            self.is_moving = True

    def move_left(self, grid):
        if not self.is_moving:
            self.destination = self.calculate_destination(grid, "left") * pixel_size
            self.is_moving = True

    def move_right(self, grid):
        if not self.is_moving:
            self.destination = self.calculate_destination(grid, "right") * pixel_size
            self.is_moving = True

    def update(self, delta_time, grid):
        if (self.position == self.destination).all():
            if self.is_moving:
                sound_collision()
                self.is_moving = False
        else:
            dir = (self.destination - self.position) / np.linalg.norm(self.destination - self.position)

            if (dir == np.array([1, 0])).all():
                delta_x = self.speed * delta_time
                if self.position[0] + delta_x > self.destination[0]:
                    self.position[0] = self.destination[0]
                else:
                    self.position[0] = self.position[0] + delta_x

            if (dir == np.array([0, 1])).all():
                delta_y = self.speed * delta_time
                if self.position[1] + delta_y > self.destination[1]:
                    self.position[1] = self.destination[1]
                else:
                    self.position[1] = self.position[1] + delta_y

            if (dir == np.array([-1, 0])).all():
                delta_x = self.speed * delta_time
                if self.position[0] - delta_x < self.destination[0]:
                    self.position[0] = self.destination[0]
                else:
                    self.position[0] = self.position[0] - delta_x

            if (dir == np.array([0, -1])).all():
                delta_y = self.speed * delta_time
                if self.position[1] - delta_y < self.destination[1]:
                    self.position[1] = self.destination[1]
                else:
                    self.position[1] = self.position[1] - delta_y

        x, y = self.level_position()
        if grid.obstacles[x, y] is not None:
            if grid.obstacles[x, y].color_switcher:
                self.color = grid.obstacles[x, y].color
