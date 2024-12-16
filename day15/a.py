input = open("input.txt").read().split('\n\n')
grid = [ list(line) for line in input[0].split('\n') ]
moves = list(input[1])

rows = len(grid)
cols = len(grid[0])

def print_grid(grid):
    for line in grid:
        print(''.join(line))
    print()

robo_pos = [0, 0]
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == '@':
            robo_pos = [row, col]
            break

def can_move(grid, row, col, dr, dc):
    dest_col = col + dc
    dest_row = row + dr
    if dest_col < 0 or dest_row < 0 or dest_row >= len(grid) or dest_col >= len(grid[0]) or grid[dest_row][dest_col] == '#':
        return False
    if grid[dest_row][dest_col] == '.':
        return True
    return can_move(grid, dest_row, dest_col, dr, dc)
    
def can_move_left(grid, row, col):
    return can_move(grid, row, col, 0, -1)

def can_move_right(grid, row, col):
    return can_move(grid, row, col, 0, 1)

def can_move_up(grid, row, col):
    return can_move(grid, row, col, -1, 0)

def can_move_down(grid, row, col):
    return can_move(grid, row, col, 1, 0)

def move_to(grid, row, col, dr, dc):
    dest_col = col + dc
    dest_row = row + dr
    if dest_col < 0 or dest_row < 0 or dest_row >= len(grid) or dest_col >= len(grid[0]) or grid[dest_row][dest_col] == '#':
        return
    if grid[dest_row][dest_col] == 'O':
        move_to(grid, dest_row, dest_col, dr, dc)
    if grid[dest_row][dest_col] == '.':
        grid[dest_row][dest_col] = grid[row][col]
        grid[row][col] = '.'

def move_left(grid, row, col):
    return move_to(grid, row, col, 0, -1)

def move_right(grid, row, col):
    return move_to(grid, row, col, 0, 1)

def move_up(grid, row, col):
    return move_to(grid, row, col, -1, 0)

def move_down(grid, row, col):
    return move_to(grid, row, col, 1, 0)

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
        if grid[row][col] == 'O':
            cost += 100 * row + col
print(cost)