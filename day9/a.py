input = open("input.txt").read().strip()
files = [ [i//2, int(f)] for i, f in enumerate(input) if i % 2 == 0 ]
free = [ int(f) for i, f in enumerate(input) if i % 2 != 0 ]
result = []

for i in range(len(files)):
    f = files[i]
    count = f[1]
    for x in range(count):
        result.append(f[0])
    if i < len(free):
        f = free[i]
        if f > 0:
            for x in range(f):
                result.append(-1)

low = 0
high = len(result) - 1

while low < high:
    if result[low] != -1:
        low += 1
        continue
    if result[high] == -1:
        high -= 1
        continue
    result[low] = result[high]
    result[high] = -1
    low += 1
    high -= 1

sum = 0
for i, x in enumerate(result):
    if x == -1:
        continue
    sum += x * i
    
print(sum)