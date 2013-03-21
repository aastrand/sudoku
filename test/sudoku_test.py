import copy
import unittest

from sudoku import grid_factory, find_unassigned_pos, solve
from sudoku.util import printgrid


class SudokuTest(unittest.TestCase):
    def setUp(self):
        grid = grid_factory()
        grid[0][4] = 2
        grid[1] = range(1, 10)
        grid[2] = range(4, 9)
        grid[2].append(0)
        grid[2].extend(range(1, 4))
        grid[8][8] = 9

        self.grid = grid
        printgrid(grid)

    def easy(self):
        grid = grid_factory()
        grid[0][1] = 8
        grid[0][3] = 4
        grid[0][6] = 6
        grid[0][8] = 2

        grid[1][0] = 5
        grid[1][3] = 9
        grid[1][8] = 7

        grid[2][0] = 2
        grid[2][2] = 7
        grid[2][5] = 1
        grid[2][6] = 9
        grid[2][7] = 8

        grid[3][1] = 5
        grid[3][3] = 1
        grid[3][6] = 3
        grid[3][7] = 2
        grid[3][8] = 6

        grid[4][0] = 3
        grid[4][8] = 9

        grid[5][0] = 7
        grid[5][1] = 9
        grid[5][2] = 6
        grid[5][5] = 3
        grid[5][7] = 4

        grid[6][1] = 3
        grid[6][2] = 8
        grid[6][3] = 7
        grid[6][6] = 2
        grid[6][8] = 5

        grid[7][0] = 9
        grid[7][5] = 2
        grid[7][8] = 4

        grid[8][0] = 4
        grid[8][2] = 1
        grid[8][5] = 5
        grid[8][7] = 3

        return grid

    def hard(self):
        grid = grid_factory()
        grid[0][2] = 3
        grid[0][5] = 9
        grid[0][7] = 8
        grid[0][8] = 1

        grid[1][3] = 2
        grid[1][7] = 6

        grid[2][0] = 5
        grid[2][4] = 1
        grid[2][6] = 7

        grid[3][0] = 8
        grid[3][1] = 9

        grid[4][2] = 5
        grid[4][3] = 6
        grid[4][5] = 1
        grid[4][6] = 2

        grid[5][7] = 3
        grid[5][8] = 7

        grid[6][2] = 9
        grid[6][4] = 2
        grid[6][8] = 8

        grid[7][1] = 7
        grid[7][5] = 4

        grid[8][0] = 2
        grid[8][1] = 5
        grid[8][3] = 8
        grid[8][6] = 6

        return grid

    def test_find_unassigned_pos(self):
        grid = self.grid

        self.assertEquals((-1, -1), find_unassigned_pos(grid, 10, 10))
        self.assertEquals((2, 5), find_unassigned_pos(grid, 0, 10))
        self.assertEquals((-1, -1), find_unassigned_pos(grid, 8, 8))
        self.assertEquals((0, 0), find_unassigned_pos(grid, 0, 0))
        self.assertEquals((2, 5), find_unassigned_pos(grid, 1, 5))
        self.assertEquals((3, 0), find_unassigned_pos(grid, 2, 6))
        self.assertEquals((3, 0), find_unassigned_pos(grid, 3, 0))

    def test_solve(self):
        grid = grid_factory()
        l = range(1, 10)
        for i in xrange(0, 3):
            grid[i] = l
            for j in xrange(0, 3):
                l = copy.deepcopy(l)
                l.append(l.pop(0))
        printgrid(grid)

        self.assertTrue(solve(grid))
        self.assertTrue(solve(self.easy()))
        self.assertTrue(solve(self.hard()))
        grid = self.easy()
        grid[8][0] = 0
        grid[8][1] = 4
        self.assertFalse(solve(grid))
