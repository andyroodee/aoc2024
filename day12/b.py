from queue import Queue

grid = [ list(line.strip()) for line in open("input.txt").readlines() ]

def get_region_data(grid, visited, row, col):
    area = 0
    vl = []
    vr = []
    ht = []
    hb = []
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
                    if nr > r:
                        hb.append((nr, nc))
                    elif nr < r:
                        ht.append((nr, nc))
                    elif nc > c:
                        vr.append((nr, nc))
                    else:
                        vl.append((nr, nc))
            else:
                if nr > r:
                    hb.append((nr, nc))
                elif nr < r:
                    ht.append((nr, nc))
                elif nc > c:
                    vr.append((nr, nc))
                else:
                    vl.append((nr, nc))
    return (area, vl, vr, ht, hb)


cost = 0
visited = set()

for row in range(len(grid)):
    for col in range(len(grid[row])):
        where = (row, col)
        if where in visited:
            continue
        (area, vl, vr, ht, hb) = get_region_data(grid, visited, row, col)
        vl.sort(key=lambda pos: (pos[1], pos[0]))
        vr.sort(key=lambda pos: (pos[1], pos[0]))
        ht.sort(key=lambda pos: (pos[0], pos[1]))
        hb.sort(key=lambda pos: (pos[0], pos[1]))
        vert_sides = 1
        for i in range(len(vl) - 1):
            if vl[i+1][1] != vl[i][1] or abs(vl[i+1][0] - vl[i][0]) > 1:
                vert_sides += 1    
        vert_sides += 1           
        for i in range(len(vr) - 1):
            if vr[i+1][1] != vr[i][1] or abs(vr[i+1][0] - vr[i][0]) > 1:
                vert_sides += 1        
        hor_sides = 1
        for i in range(len(ht) - 1):
            if ht[i+1][0] != ht[i][0] or abs(ht[i+1][1] - ht[i][1]) > 1:
                hor_sides += 1        
        hor_sides += 1
        for i in range(len(hb) - 1):
            if hb[i+1][0] != hb[i][0] or abs(hb[i+1][1] - hb[i][1]) > 1:
                hor_sides += 1     
        sides = vert_sides + hor_sides
        cost += sides * area

print(cost)