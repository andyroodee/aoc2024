word_len = len('XMAS')

def check_xmas(grid, row, col):
    down = row + (word_len - 1) < rows
    up = row - (word_len - 1) >= 0
    left = col - (word_len - 1) >= 0
    right = col + (word_len - 1) < cols
    found = 0
    # down
    if down and grid[row+1][col] == 'M' and grid[row+2][col] == 'A' and grid[row+3][col] == 'S':
        found += 1
    # up
    if up and grid[row-1][col] == 'M' and grid[row-2][col] == 'A' and grid[row-3][col] == 'S':
        found += 1
    # left 
    if left and grid[row][col-1] == 'M' and grid[row][col-2] == 'A' and grid[row][col-3] == 'S':
        found += 1
    # right 
    if right and grid[row][col+1] == 'M' and grid[row][col+2] == 'A' and grid[row][col+3] == 'S':
        found += 1 
    # up-right
    if up and right and grid[row-1][col+1] == 'M' and grid[row-2][col+2] == 'A' and grid[row-3][col+3] == 'S':
        found += 1   
    # up-left
    if up and left and grid[row-1][col-1] == 'M' and grid[row-2][col-2] == 'A' and grid[row-3][col-3] == 'S':
        found += 1    
    # down-right
    if down and right and grid[row+1][col+1] == 'M' and grid[row+2][col+2] == 'A' and grid[row+3][col+3] == 'S':
        found += 1    
    # down-left
    if down and left and grid[row+1][col-1] == 'M' and grid[row+2][col-2] == 'A' and grid[row+3][col-3] == 'S':
        found += 1
    return found

grid = [ s.strip() for s in open(0).readlines() ]
rows = len(grid)
cols = len(grid[0])

xmas_count = 0
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == 'X':
            xmas_count += check_xmas(grid, row, col)

print(xmas_count)