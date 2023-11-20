from level.level import Level
from level.obstacle import Obstacle, colors

import numpy as np


class TestGridAdd:
    """
    This test tests the add of an obstacle in an empty grid by verifying the correct type of the obstacle (empty, red...)
    """

    def __init__(self):
        self.level = Level((3, 3), [], [], [])

    def test_add(self):
        self.level.grid.obstacles[2, 2] = Obstacle("blue")
        assert self.level.grid.obstacles[2, 2].color == colors["blue"]


test = TestGridAdd()
test.test_add()


class TestGridMove:
    """
    This test tests the calculation of the destination in an example grid when there is an obstacle
    """

    def __init__(self):
        self.level = Level((3, 3), [(0, 0)], ["red"], [(2, 2)])
        self.level.grid.obstacles[2, 0] = Obstacle("darkgrey")
        self.player = self.level.players[0]

    def test(self):
        self.test_down()
        self.test_up()
        self.test_right()
        self.test_left()

    def test_down(self):
        self.player.move_down(self.level.grid)
        assert (self.player.level_destination() == np.array([0, 2])).all()

    def test_up(self):
        self.player.move_up(self.level.grid)
        assert (self.player.level_destination() == np.array([0, 0])).all()

    def test_right(self):
        self.player.move_right(self.level.grid)
        assert (self.player.level_destination() == np.array([1, 0])).all()  # considering the obstacle / Fail if [2,0]

    def test_left(self):
        self.player.move_left(self.level.grid)
        assert (self.player.level_destination() == np.array([0, 0])).all()


test_grid = TestGridMove()
test_grid.test()  # test if the player enters the correct destination
