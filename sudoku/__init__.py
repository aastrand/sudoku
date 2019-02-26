__import__('pkg_resources').declare_namespace(__name__)

from collections import defaultdict
from util import printgrid, is_valid_at_pos

SIZE = 9


def grid_factory(size=SIZE):
    def factory():
        return [0] * size
    return defaultdict(factory)


def find_unassigned_pos(grid, row, col):
    """
    Finds the next 0 position from row, col
    If no position is found, (-1, -1) is returned
    """
    vals = [col]

    def getcol():
        return vals.pop(0) if len(vals) > 0 else 0

    for r in xrange(row, SIZE):
        for c in xrange(getcol(), SIZE):
            if grid[r][c] == 0:
                return r, c
    return -1, -1


def solve(grid, row=0, col=0):
    """
    Basic backtracking algo approach
    """
    row, col = find_unassigned_pos(grid, row, col)
    if row < 0:
        print 'SUCCESS:'
        printgrid(grid)
        return True

    # try all values, walking through the cells while
    # looking for valid positions
    for v in xrange(1, SIZE + 1):
        if is_valid_at_pos(grid, row, col, v):
            grid[row][col] = v
            if solve(grid, row, col):
                return True
            # backtrack here
            grid[row][col] = 0

    # and here
    return False
