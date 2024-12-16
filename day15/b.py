input = open("input.txt").read().split('\n\n')
grid = [ list(line) for line in input[0].split('\n') ]
moves = list(input[1])

def print_grid(grid):
    for line in grid:
        print(''.join(line))
    print()

rows = len(grid)
cols = len(grid[0])
big_grid = []
for row in range(rows):
    big_row = []
    for col in range(cols):
        if grid[row][col] == '#' or grid[row][col] == '.':
            big_row.append(grid[row][col])
            big_row.append(grid[row][col])
        elif grid[row][col] == 'O':
            big_row.append("[")
            big_row.append("]")
        else:
            big_row.append("@")
            big_row.append(".")
    big_grid.append(big_row)

grid = big_grid
rows = len(grid)
cols = len(grid[0])

robo_pos = [0, 0]
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == '@':
            robo_pos = [row, col]
            break

def can_move_horizontal(grid, row, col, dc):
    dest_col = col + dc
    if dest_col < 0  or dest_col >= len(grid[0]) or grid[row][dest_col] == '#':
        return False
    if grid[row][dest_col] == '.':
        return True
    return can_move_horizontal(grid, row, dest_col, dc)

def can_move_vertical(grid, row, col, dr):
    dest_row = row + dr
    cols_check = [col]
    if grid[row][col] == ']':
        cols_check.append(col-1)
    elif grid[row][col] == '[':
        cols_check.append(col+1)
    good = True
    for c in cols_check:
        if dest_row < 0 or dest_row >= len(grid) or grid[dest_row][c] == '#':
            return False
        if grid[dest_row][c] == '.':
            good &= True
        else:
            good &= can_move_vertical(grid, dest_row, c, dr)
        if good == False: 
            return False
    return True
    
def can_move_left(grid, row, col):
    return can_move_horizontal(grid, row, col, -1)

def can_move_right(grid, row, col):
    return can_move_horizontal(grid, row, col, 1)

def can_move_up(grid, row, col):
    return can_move_vertical(grid, row, col, -1)

def can_move_down(grid, row, col):
    return can_move_vertical(grid, row, col, 1)

def move_to_horizontal(grid, row, col, dr, dc):
    dest_col = col + dc
    dest_row = row + dr
    if dest_col < 0 or dest_row < 0 or dest_row >= len(grid) or dest_col >= len(grid[0]) or grid[dest_row][dest_col] == '#':
        return
    if grid[dest_row][dest_col] == '[' or grid[dest_row][dest_col] == ']':
        move_to_horizontal(grid, dest_row, dest_col, dr, dc)
    if grid[dest_row][dest_col] == '.':
        grid[dest_row][dest_col] = grid[row][col]
        grid[row][col] = '.'
    
def move_to_vertical(grid, row, col, dr):
    dest_row = row + dr
    if dest_row < 0 or dest_row >= len(grid) or grid[dest_row][col] == '#':
        return
    if grid[dest_row][col] == '[':
        move_to_vertical(grid, dest_row, col, dr)
        move_to_vertical(grid, dest_row, col + 1, dr)
    elif grid[dest_row][col] == ']':
        move_to_vertical(grid, dest_row, col, dr)
        move_to_vertical(grid, dest_row, col - 1, dr)
    if grid[dest_row][col] == '.':
        grid[dest_row][col] = grid[row][col]
        grid[row][col] = '.'

def move_left(grid, row, col):
    return move_to_horizontal(grid, row, col, 0, -1)

def move_right(grid, row, col):
    return move_to_horizontal(grid, row, col, 0, 1)

def move_up(grid, row, col):
    return move_to_vertical(grid, row, col, -1)

def move_down(grid, row, col):
    return move_to_vertical(grid, row, col, 1)

for move in moves:
    (row, col) = robo_pos
    if move == '<':
        if can_move_left(grid, row, col):
            move_left(grid, row, col)     
            robo_pos[1] -= 1   
    elif move == '>':
        if can_move_right(grid, row, col):
            move_right(grid, row, col)
            robo_pos[1] += 1   
    elif move == '^':
        if can_move_up(grid, row, col):
            move_up(grid, row, col)
            robo_pos[0] -= 1   
    elif move == 'v': 
        if can_move_down(grid, row, col):
            move_down(grid, row, col)
            robo_pos[0] += 1   

cost = 0
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == '[':
            cost += 100 * row + col
print(cost)