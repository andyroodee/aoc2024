from queue import PriorityQueue

bytes = [ list(map(int, line.strip().split(','))) for line in open("input.txt").readlines() ]
rows = 71
cols = 71
limit = 1024
r = 0
c = 0
grid = [ ['.'] * cols for _ in range(rows) ]

for i in range(limit):
    x, y = bytes[i]
    grid[y][x] = '#'

frontier = PriorityQueue()
frontier.put((0, r, c))
cost = {}
cost[(r, c)] = 0
came_from = {}
came_from[(r,c)] = None

while frontier.qsize() > 0:
    current = frontier.get()

    cr = current[1]
    cc = current[2]

    if cr == rows - 1 and cc == cols - 1:
        path_len = 0
        node = (cr,cc)
        while node != (0, 0):
            path_len += 1
            node = came_from[node]        
        print(path_len)

    for (dr, dc) in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr = cr + dr
        nc = cc + dc
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == '#':
            continue
        new_cost = cost[(cr, cc)] + 1
        if (nr, nc) not in cost or new_cost < cost[(nr, nc)]:
            cost[(nr,nc)] = new_cost
            priority = new_cost
            frontier.put((priority, nr ,nc))
            came_from[(nr, nc)] = (cr, cc)