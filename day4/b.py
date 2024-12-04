def check_xmas(grid, row, col):
    down = row + 1 < rows
    up = row - 1 >= 0
    left = col - 1 >= 0
    right = col + 1 < cols
    if up and down and left and right:
        one = grid[row-1][col-1] == 'M' and grid[row+1][col+1] == 'S' or grid[row-1][col-1] == 'S' and grid[row+1][col+1] == 'M'
        two = grid[row+1][col-1] == 'M' and grid[row-1][col+1] == 'S' or grid[row+1][col-1] == 'S' and grid[row-1][col+1] == 'M'
        return one and two
    return False

grid = [ s.strip() for s in open(0).readlines() ]
rows = len(grid)
cols = len(grid[0])

xmas_count = 0
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == 'A' and check_xmas(grid, row, col):
            xmas_count += 1

print(xmas_count)