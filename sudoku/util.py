# utility functions for determining structural validity
sub_lookup = {0: 0, 1: 0, 2: 0,
              3: 3, 4: 3, 5: 3,
              6: 6, 7: 6, 8: 6}
values = set(range(1, 10))
ranges = set(range(0, 9))


def _check(list, val):
    for l in list:
        if l == val:
            return False
    return True


def check_row(grid, row, val):
    return _check(grid[row], val)


def check_col(grid, col, val):
    return _check([grid[i][col] for i in xrange(0, 9)], val)


def check_subgrid(grid, row, col, val):
    """
    Checks if the value can be placed within
    the 3x3 subgrid
    """
    for r in xrange(sub_lookup[row], sub_lookup[row] + 3):
        for c in xrange(sub_lookup[col], sub_lookup[col] + 3):
            if val == grid[r][c]:
                return False
    return True


def printgrid(grid):
    for r in xrange(0, 9):
        for v in grid[r]:
            print v,
        print


def is_valid_at_pos(grid, row, col, val):
    assert val in values
    assert row in ranges
    assert col in ranges
    assert grid[row][col] == 0

    # check 3 out of the 4 restrictions
    # (the last one, cells have at most one value, is implicit)
    return (check_row(grid, row, val) and
            check_col(grid, col, val) and
            check_subgrid(grid, row, col, val))
