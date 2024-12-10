from queue import Queue

grid = [ list(map(int, list(line.strip()))) for line in open("input.txt").readlines() ]

def get_trailhead_score(grid, row, col):
    score = 0
    visited = set()
    visited.add((row, col))
    frontier = Queue()
    frontier.put((row, col))
    while not frontier.empty():
        (r, c) = frontier.get()
        val = grid[r][c]
        if r - 1 >= 0 and grid[r-1][c] == val + 1 and (r-1, c) not in visited:
            if grid[r-1][c] == 9:
                score += 1
            frontier.put((r-1,c))
            visited.add((r-1,c))
        if r + 1 <len(grid) and grid[r+1][c] == val + 1 and (r+1, c) not in visited:
            if grid[r+1][c] == 9:
                score += 1
            frontier.put((r+1,c))
            visited.add((r+1,c))
        if c - 1 >= 0 and grid[r][c-1] == val + 1 and (r, c-1) not in visited:
            if grid[r][c-1] == 9:
                score += 1
            frontier.put((r,c-1))
            visited.add((r,c-1))
        if c + 1 < len(grid[c]) and grid[r][c+1] == val + 1 and (r, c+1) not in visited:
            if grid[r][c+1] == 9:
                score += 1
            frontier.put((r,c+1))
            visited.add((r,c+1))

    return score

scores = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == 0:
            scores += get_trailhead_score(grid, row, col)

print(scores)