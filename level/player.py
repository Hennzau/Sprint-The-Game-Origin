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
        return self.position

    def level_position(self):
        x = int(self.position[0] / pixel_size)
        y = int(self.position[1] / pixel_size)

        return np.array([x, y])

    def advance_x(self, grid, r1, r2):
        x, y = self.level_position()
        i = 0

        active_color = self.color

        for j in range(x, r1, r2):
            if grid.obstacles[j, y] is None:
                i = j - x
                continue
            else:
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

                if not grid.obstacles[j, y].color_switcher and not grid.obstacles[j, y].start and not grid.obstacles[
                    j, y].end and not (
                        grid.obstacles[j, y].color == active_color):
                    break

        return i

    def advance_y(self, grid, r1, r2):
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

    def calculate_destination(self, grid, direction):
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
        # data for the motion_blur (and maybe something else)

        if len(self.last_positions) != self.record_length:
            self.last_positions.append(self.render_position)
        else:
            self.last_positions[self.cursor] = self.render_position
            self.cursor = (self.cursor + 1) % self.record_length

        # logical

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

        self.render_position = self.position + self.bounce_direction * self.bounce_amplitude * np.sin(
            -20 * self.bounce_time)

        if (self.position == self.destination).all():
            if self.is_moving:
                sound_collision()
                self.bounces = True
                self.is_moving = False
                self.speed = self.start_speed
        else:
            self.speed += self.start_speed * 8 * delta_time
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
