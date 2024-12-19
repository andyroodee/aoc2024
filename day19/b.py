from functools import cache

input = open("input.txt").read().split('\n\n')
patterns = set([ pattern.strip() for pattern in input[0].split(',') ])
designs = [ d.strip() for d in input[1].split('\n') ]

@cache
def get_count(design):
    if design == "":
        return 1
    sum = 0
    for i in range(len(design)):
        d = design[:i+1]
        if d in patterns:
            sum += get_count(design[i+1:])
    return sum

sum = 0
for d in designs:
    sum += get_count(d)

print(sum)
