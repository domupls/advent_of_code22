# tree visibility - on edge, all trees in four dirs
# are shorter

from sys import argv


filename = argv[1]


# part one
def is_in_matrix(grid, x, y):
    return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[x])


def check_direction(grid, x, y):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    if x == 0 or x == len(grid)-1 or y == 0 or y == len(grid[x])-1:
        return True
    for dir in directions:
        myx, myy = x+dir[0], y+dir[1]
        while is_in_matrix(grid, myx, myy) and grid[myx][myy] < grid[x][y]:
            myx, myy = myx+dir[0], myy+dir[1]
            if not is_in_matrix(grid, myx, myy):
                return True
    return False


def tree_visibility():
    with open(filename) as f:
        file = f.read()
    grid = [[int(x) for x in line] for line in file.split()]
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if check_direction(grid, i, j):
                count += 1
    return count


print(tree_visibility())
