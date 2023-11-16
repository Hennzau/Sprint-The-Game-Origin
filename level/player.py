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
        self.render_position = np.array([x_init, y_init])
        self.destination = np.array([x_init, y_init])

        self.is_moving = False
        self.start_speed = 600
        self.speed = self.start_speed

        self.bounces = False
        self.bounce_amplitude = 0
        self.bounce_time = 0
        self.bounce_direction = np.array([0, 0])

    def surface_position(self):
        return self.position

    def level_position(self):
        x = int(self.position[0] / pixel_size)
        y = int(self.position[1] / pixel_size)

        return np.array([x, y])

    def calculate_destination(self, grid, direction):
        x, y = self.level_position()

        active_color = self.color

        if direction == "right":
            i = 0
            while i < grid.size[0] - x - 1:
                if grid.obstacles[x + i, y] is not None:
                    if grid.obstacles[x + i, y].color_switcher:
                        active_color = grid.obstacles[x + i, y].color

                    if not grid.obstacles[x + i, y].color_switcher and not grid.obstacles[x + i, y].end and not (
                            grid.obstacles[x + i, y].color == active_color):
                        return np.array([x + i - 1, y])
                i += 1

            return np.array([x + i, y])

        if direction == "left":
            i = 0
            while x + i >= 1:
                if grid.obstacles[x + i, y] is not None:
                    if grid.obstacles[x + i, y].color_switcher:
                        active_color = grid.obstacles[x + i, y].color

                    if not grid.obstacles[x + i, y].color_switcher and not grid.obstacles[x + i, y].end and not (
                            grid.obstacles[x + i, y].color == active_color):
                        return np.array([x + i + 1, y])
                i -= 1

            return np.array([x + i, y])

        if direction == "down":
            i = 0
            while i < grid.size[1] - y - 1:
                if grid.obstacles[x, y + i] is not None:
                    if grid.obstacles[x, y + i].color_switcher:
                        active_color = grid.obstacles[x, y + i].color

                    if not grid.obstacles[x, y + i].color_switcher and not grid.obstacles[x, y + i].end and not (
                            grid.obstacles[x, y + i].color == active_color):
                        return np.array([x, y + i - 1])
                i += 1

            return np.array([x, y + i])

        if direction == "up":
            i = 0
            while y + i >= 1:
                if grid.obstacles[x, y + i] is not None:
                    if grid.obstacles[x, y + i].color_switcher:
                        active_color = grid.obstacles[x, y + i].color

                    if not grid.obstacles[x, y + i].color_switcher and not grid.obstacles[x, y + i].end and not (
                            grid.obstacles[x, y + i].color == active_color):
                        return np.array([x, y + i + 1])
                i -= 1

            return np.array([x, y + i])

    def move_up(self, grid):
        self.bounce_direction = np.array([0, -1])

        if not self.is_moving:
            self.destination = self.calculate_destination(grid, "up") * pixel_size
            self.is_moving = True

    def move_down(self, grid):
        self.bounce_direction = np.array([0, 1])

        if not self.is_moving:
            self.destination = self.calculate_destination(grid, "down") * pixel_size
            self.is_moving = True

    def move_left(self, grid):
        self.bounce_direction = np.array([-1, 0])

        if not self.is_moving:
            self.destination = self.calculate_destination(grid, "left") * pixel_size
            self.is_moving = True

    def move_right(self, grid):
        self.bounce_direction = np.array([1, 0])

        if not self.is_moving:
            self.destination = self.calculate_destination(grid, "right") * pixel_size
            self.is_moving = True

    def update(self, delta_time, grid):
        if self.bounces:
            self.bounce_time = self.bounce_time + delta_time
            if self.bounce_amplitude == 0:
                self.bounce_amplitude = 5
            else:
                self.bounce_amplitude = self.bounce_amplitude - 20 * delta_time

            if self.bounce_time >= 0.25:
                self.bounce_time = 0
                self.bounce_amplitude = 0
                self.bounces = False

        self.render_position = self.position + self.bounce_direction * self.bounce_amplitude * np.sin(
            -20 * self.bounce_time)

        if (self.position == self.destination).all():
            if self.is_moving:
                sound_collision()
                self.bounces = True
                self.is_moving = False
                self.speed = self.start_speed
        else:
            self.speed += self.start_speed * 4 * delta_time
            distance = np.linalg.norm(self.destination - self.position)
            direction = (self.destination - self.position) / distance
            delta = self.speed * delta_time

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

        x, y = self.level_position()
        if grid.obstacles[x, y] is not None:
            if grid.obstacles[x, y].color_switcher:
                self.color = grid.obstacles[x, y].color
