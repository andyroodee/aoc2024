A_COST = 3
B_COST = 1

def parse(string, sep):
    index = string.index("X" + sep)
    comma = string.index(',', index)
    x = int(string[index+2 : comma])    
    index = string.index("Y" + sep)
    y = int(string[index+2:])
    return (x, y)

def parse_button(button):
    return parse(button, '+')

def parse_prize(prize):
    return parse(prize, '=')

cost = 0
input = [ line.strip() for line in open("input.txt").readlines() if len(line.strip()) > 0 ]
for i in range(0, len(input), 3):
    a_button = input[i]
    b_button = input[i+1]
    prize = input[i+2]
    (ax, ay) = parse_button(a_button)
    (bx, by) = parse_button(b_button)
    (px, py) = parse_prize(prize)
    # A * ax + B * bx = px
    # A * ay + B * by = py
    b = (px * ay - ax * py) / (ay * bx - ax * by)
    a = (py - b * by) / ay
    if int(b) == b and int(a) == a:
        cost += int(a * A_COST + b * B_COST)

print(cost)
