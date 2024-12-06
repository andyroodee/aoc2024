grid = []
pos = (0, 0)
dir = (-1, 0)
visited = set()

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
visited.add(pos)

def change_dir(current_dir):
    if current_dir == up: return right
    if current_dir == right: return down
    if current_dir == down: return left
    if current_dir == left: return up

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

print(len(visited))
