from collections import defaultdict

input = open('input.txt', 'r')

lines = input.readlines()
left = []
right = defaultdict(int)
for line in lines:
    split = line.split()
    left.append(int(split[0]))
    right[int(split[1])] += 1

total = 0
for v in left:
    total += v * right[v]

print(total)