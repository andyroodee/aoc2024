grid = []
pos = (0, 0)
dir = (-1, 0)

row = 0
for line in open(0):
    s = line.strip()
    grid.append(s)
    # record the starting position
    col = s.find("^")
    if col != -1:
        pos = (row, col)
    row += 1

up = (-1, 0)
right = (0, 1)
down = (1, 0)
left = (0, -1)
bounds = (len(grid[0]), len(grid))

def change_dir(current_dir):
    if current_dir == up: return right
    if current_dir == right: return down
    if current_dir == down: return left
    if current_dir == left: return up

def get_path(grid, start_pos, start_dir):
    pos = start_pos
    dir = start_dir 
    visited = set()
    visited.add(pos)

    while True:
        # try to move in the given dir    
        next = (pos[0] + dir[0], pos[1] + dir[1])
        # check for out of bounds, which means we're done
        if next[0] >= bounds[0] or next[0] < 0 or next[1] >= bounds[1] or next[1] < 0:
            break

        # adjust dir if this is an obstacle
        if grid[next[0]][next[1]] == '#':
            dir = change_dir(dir)
        else:   
            pos = next
            visited.add(pos)
    
    return visited

def detect_cycle(grid, start_pos, start_dir):
    pos = start_pos
    dir = start_dir 
    visited = set()
    visited.add((pos, up))

    while True:
        # try to move in the given dir    
        next = (pos[0] + dir[0], pos[1] + dir[1])
        # check for out of bounds, which means we're done
        if next[0] >= bounds[0] or next[0] < 0 or next[1] >= bounds[1] or next[1] < 0:
            return False

        # adjust dir if this is an obstacle
        if grid[next[0]][next[1]] == '#':
            dir = change_dir(dir)
        else:   
            pos = next
            if (pos, dir) in visited:
                # cycle detected
                return True
            visited.add((pos, dir))

original_path = get_path(grid, pos, dir)
count = 0
for place in original_path:
    (i, j) = place
    if (i, j) == pos:
        continue
    g = grid[:]
    if grid[i][j] != '#':
        g[i] = g[i][:j] + '#' + g[i][j+1:]
    if detect_cycle(g, pos, dir):
        count += 1

print(count)
