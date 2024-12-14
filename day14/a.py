input = open("input.txt").read().split('\n')

def parse_xy(s):
    x = int(s[s.index('=')+1:s.index(',')])
    y = int(s[s.index(',')+1:])    
    return (x, y)

width = 101
height = 103
steps = 100
half_width = width // 2
half_height = height // 2

quads = [0, 0, 0, 0]
for robot in input:
    parts = robot.split()
    if len(parts) != 2:
        continue
    (px, py) = parse_xy(parts[0])
    (vx, vy) = parse_xy(parts[1])
    x = (px + vx * steps) % width
    y = (py + vy * steps) % height
    if x < half_width:
        if y < half_height:
            quads[0] += 1
        elif y > half_height:
            quads[3] += 1
    elif x > half_width:
        if y < half_height:
            quads[1] += 1
        elif y > half_height:
            quads[2] += 1

prod = 1
for q in quads:
    prod *= q
print(prod)

