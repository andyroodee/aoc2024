stones = [ stone for stone in open("input.txt").read().split() ]

def blink(stones):
    result = []
    for stone in stones:
        if stone == '0':
            result.append('1')
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            left = int(stone[:mid])
            right = int(stone[mid:])
            result.append(str(left))
            result.append(str(right))
        else:
            result.append(str(int(stone) * 2024))
    return result

for i in range(25):
    stones = blink(stones)

print(len(stones))
