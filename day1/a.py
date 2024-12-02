input = open('input.txt', 'r')

lines = input.readlines()
left = []
right = []
for line in lines:
    split = line.split()
    left.append(int(split[0]))
    right.append(int(split[1]))

left.sort()
right.sort()
sum = 0
for i in range(len(left)):
    diff = abs(left[i] - right[i])
    sum += diff

print(sum)