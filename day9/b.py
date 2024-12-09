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

for file_index in range(len(files) - 1, 0, -1):
    file_size = files[file_index][1]

    low = 0
    done = False
    while not done and low < len(result):
        if result[low] != -1:
            low += 1
            continue
        free_size = 0
        for i in range(low, len(result)):
            if result[i] == -1:
                free_size += 1
            else:
                break
        where = result.index(files[file_index][0])
        if file_size <= free_size and where > low:
            for i in range(file_size):
                result[low] = files[file_index][0]
                result[where] = -1
                where += 1
                low += 1  
            done = True
        else:
            low += free_size

sum = 0
seen = set()
last = 0
for i, x in enumerate(result):
    if x == -1:
        continue
    if last != x and x in seen:
        continue
    sum += x * i
    last = x
    seen.add(x)
    
print(sum)