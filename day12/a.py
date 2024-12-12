from queue import Queue

grid = [ list(line.strip()) for line in open("input.txt").readlines() ]

def get_region_data(grid, visited, row, col):
    area = 0
    perim = 0
    visited.add((row, col))
    frontier = Queue()
    frontier.put((row, col))
    while not frontier.empty():
        (r, c) = frontier.get()
        val = grid[r][c]
        area += 1
        for nr, nc in [(r-1, c), (r+1, c), (r, c+1), (r,c-1)]:
            if nc >=0 and nr >= 0 and nc < len(grid[0]) and nr < len(grid):
                if grid[nr][nc] == val:
                    if (nr, nc) not in visited:
                        frontier.put((nr, nc))
                        visited.add((nr, nc))
                else:
                    perim += 1
            else:
                perim += 1
    return (area, perim)


cost = 0
visited = set()

for row in range(len(grid)):
    for col in range(len(grid[row])):
        where = (row, col)
        if where in visited:
            continue
        (area, perim) = get_region_data(grid, visited, row, col)
        cost += area * perim 

print(cost)