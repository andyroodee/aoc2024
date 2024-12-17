from queue import PriorityQueue
from collections import deque

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
costs = {(loc, facing): 0}
came_from = {}
best = float("inf")
solution = set()

while frontier.qsize() > 0:
    current = frontier.get()
    cost = current[0]
        
    if cost > costs.get((current[1], current[2]), float("inf")):
        continue

    (r, c) = current[1]
    (dr, dc) = current[2]

    if (r, c) == goal:
        if cost > best:
            break
        best = cost
        solution.add((r, c, dr, dc))

    for new_cost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr)]:
        if grid[nr][nc] == "#": 
            continue
        lowest = costs.get((nr, nc, ndr, ndc), float("inf"))
        if new_cost > lowest: 
            continue
        if new_cost < lowest:
            came_from[(nr, nc, ndr, ndc)] = set()
            costs[(nr, nc, ndr, ndc)] = new_cost
        came_from[(nr, nc, ndr, ndc)].add((r, c, dr, dc))
        frontier.put((new_cost, (nr, nc), (ndr, ndc)))

states = deque(solution)
seen = set(solution)

while states:
    key = states.popleft()
    for last in came_from.get(key, []):
        if last in seen: 
            continue
        seen.add(last)
        states.append(last)

print(len({(r, c) for r, c, _, _ in seen}))