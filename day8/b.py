input = [ line.strip() for line in open("input.txt").readlines() ]
grid_size = (len(input), len(input[0]))

antennas = {}
for row in range(grid_size[0]):
    for col in range(grid_size[1]):
        entry = input[row][col]
        if entry == '.':
            continue
        if entry in antennas:
            locations = antennas[entry]
            locations.add((row, col))
        else:
            locations = set()
            locations.add((row, col))
            antennas[entry] = locations

antinode_locs = set()
for locs in antennas.values():
    locs = list(locs)
    for i in range(len(locs)):
        for j in range(i+1, len(locs)):
            a = locs[i]
            b = locs[j]
            d = (a[0] - b[0], a[1] - b[1])
            go = d
            antinode_locs.add(a)
            while True:
                where = (a[0] + go[0], a[1] + go[1])
                go = (go[0] + d[0], go[1] + d[1])
                if where[0] >= grid_size[0] or where[1] >= grid_size[1] or where[0] < 0 or where[1] < 0:
                    break
                antinode_locs.add(where)
                
            d = (-d[0], -d[1])
            go = d
            while True:
                where = (a[0] + go[0], a[1] + go[1])
                go = (go[0] + d[0], go[1] + d[1])
                if where[0] >= grid_size[0] or where[1] >= grid_size[1] or where[0] < 0 or where[1] < 0:
                    break
                antinode_locs.add(where)

print(len(antinode_locs))