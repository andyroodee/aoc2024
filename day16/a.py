from queue import PriorityQueue

input = open("input.txt").readlines()
grid = [ list(''.join(row.strip())) for row in input]

rows = len(grid)
cols = len(grid[0])

loc = (0, 0)
goal = (0, 0)
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            loc = (r, c)
        elif grid[r][c] == 'E':
            goal = (r, c)

facing = (0, 1)
frontier = PriorityQueue()
frontier.put((0, loc, facing))
cost = {}
cost[loc] = 0
came_from = {}
came_from[loc] = None

def turn_cost(facing, current, next):
    dir = (next[0] - current[0], next[1] - current[1])
    if facing == dir:
        return 0
    dot = facing[0] * dir[0] + facing[1] * dir[1]
    if dot == 0:
        return 1000
    return 2000

while frontier.qsize() > 0:
    current = frontier.get()

    if current[1] == goal:
        print(cost[goal])
        break

    (r, c) = current[1]
    for (dr, dc) in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == '#':
            continue
        new_cost = cost[(r, c)] + 1
        dir = (nr - r, nc - c)
        face = current[2]
        new_cost += turn_cost(face, (r,c), (nr,nc))
        if (nr, nc) not in cost or new_cost < cost[(nr, nc)]:
            cost[(nr,nc)] = new_cost
            priority = new_cost
            frontier.put((priority, (nr,nc), dir))
            came_from[(nr, nc)] = (r, c)
