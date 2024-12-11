from functools import cache

stones = [ stone for stone in open("input.txt").read().split() ]

@cache
def cost(stone, d):
    if d == 0:
        return 1
    if stone == '0':
        return cost('1', d-1)
    elif len(stone) % 2 == 0:
        mid = len(stone) // 2
        left = int(stone[:mid])
        right = int(stone[mid:])
        return cost(str(left), d-1) + cost(str(right), d-1)
    else:
        return cost(str(int(stone) * 2024), d-1)

print(sum(cost(stone, 75) for stone in stones))
