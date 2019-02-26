import unittest

from sudoku import grid_factory
from sudoku.util import *


class UtilTest(unittest.TestCase):
    def setUp(self):
        grid = grid_factory()
        grid[0][4] = 2
        grid[1] = range(1, 10)
        grid[2] = range(4, 9)
        grid[2].append(0)
        grid[2].extend(range(1, 4))

        self.grid = grid
        printgrid(grid)

    def test_check_row(self):
        grid = self.grid

        self.assertFalse(check_row(grid, 1, 5))
        self.assertFalse(check_row(grid, 2, 5))
        self.assertTrue(check_row(grid, 2, 9))
        self.assertTrue(check_row(grid, 0, 5))

    def test_check_col(self):
        grid = self.grid

        self.assertFalse(check_col(grid, 0, 1))
        self.assertTrue(check_col(grid, 0, 7))
        self.assertTrue(check_col(grid, 1, 3))

    def test_check_subgrid(self):
        grid = self.grid
        for i in xrange(1, 7):
            self.assertFalse(check_subgrid(grid, 0, 0, i))
        for i in xrange(7, 10):
            self.assertTrue(check_subgrid(grid, 0, 0, i))

    def test_is_valid_at_pos(self):
        grid = self.grid

        self.assertRaises(AssertionError, is_valid_at_pos, grid, 0, 0, 0)
        self.assertRaises(AssertionError, is_valid_at_pos, grid, -1, 0, 1)
        self.assertRaises(AssertionError, is_valid_at_pos, grid, 0, 100, 1)
        for c in xrange(0, 3):
            for v in xrange(1, 7):
                self.assertFalse(is_valid_at_pos(grid, 0, c, v))
            for v in xrange(7, 10):
                self.assertTrue(is_valid_at_pos(grid, 0, c, v))
