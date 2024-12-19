input = open("input.txt").read().split('\n\n')
patterns = set([ pattern.strip() for pattern in input[0].split(',') ])
designs = [ d.strip() for d in input[1].split('\n') ]

def match(design, patterns):
    if design in patterns:
        return True
    for i in range(len(design)):
        d = design[:i+1]
        if d in patterns:
            return match(design[i+1:], patterns)
    return False

def match_all(design, patterns):
    for i in range(len(design)):
        d = design[:i+1]
        if d in patterns and match(design[i+1:], patterns):
            return True
    return False 

sum = 0
for d in designs:
    if match_all(d, patterns):
        sum += 1

print(sum)