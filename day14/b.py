from PIL import Image

input = open("input.txt").read().split('\n')

def parse_xy(s):
    x = int(s[s.index('=')+1:s.index(',')])
    y = int(s[s.index(',')+1:])    
    return (x, y)

width = 101
height = 103
half_width = width // 2
half_height = height // 2

# yes, I actually made images and looked at them until I found the tree in this range
for step in range(6000, 7000):
    image = [['.' for x in range(width)] for y in range(height)]
    quads = [0, 0, 0, 0]
    for robot in input:
        parts = robot.split()
        if len(parts) != 2:
            continue
        (px, py) = parse_xy(parts[0])
        (vx, vy) = parse_xy(parts[1])
        x = (px + vx * step) % width
        y = (py + vy * step) % height
        image[y][x] = '#'
    out = Image.new("RGB", (128, 128), "black")
    pixels = out.load()
    for row in range(height):
        for col in range(width):
            if image[row][col] == '#':                
                pixels[row, col] = (255, 255, 255)
    out.save(f'images/{step}.jpeg', "JPEG")


