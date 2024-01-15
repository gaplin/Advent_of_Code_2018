grid = open('input2.txt').read().splitlines()
n = len(grid)
for i in range(n):
    grid[i] = [x for x in grid[i]]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

def get_counts(grid: list, n: int, i: int, ii: int, directions: list) -> tuple:
    result = [0, 0, 0]
    for di, dii in directions:
        new_i, new_ii = i + di, ii + dii
        if new_i < 0 or new_i >= n or new_ii < 0 or new_ii >= n:
            continue
        symbol = grid[new_i][new_ii]
        if symbol == '.':
            result[0] += 1
        elif symbol == '|':
            result[1] += 1
        elif symbol == '#':
            result[2] += 1

    return tuple(result)

def step(grid: list, n: int, directions: list) -> list:
    new_grid = [['.' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for ii in range(n):
            empty, trees, lumberyard = get_counts(grid, n, i, ii, directions)
            symbol = grid[i][ii]
            if symbol == '.':
                if trees >= 3:
                    new_grid[i][ii] = '|'
                else:
                    new_grid[i][ii] = symbol
            elif symbol == '|':
                if lumberyard >= 3:
                    new_grid[i][ii] = '#'
                else:
                    new_grid[i][ii] = symbol
            elif symbol == '#':
                if lumberyard >= 1 and trees >= 1:
                    new_grid[i][ii] = symbol
                else:
                    new_grid[i][ii] = '.'

    return new_grid

def get_key(grid):
    key = ''
    for row in grid:
        key += ''.join(row)

    return key

first_key = get_key(grid)
cache = {first_key: 0}
states = [grid]
target = 1000000000
i = 0
while True:
    i += 1
    grid = step(grid, n, directions)
    key = get_key(grid)
    if key in cache:
        cycle_start = cache[key]
        cycle_length = i - cycle_start
        target -= cycle_start
        grid = states[cycle_start + target % cycle_length]
        break
    cache[key] = i
    states.append(grid)

trees, lumberyards = 0, 0

for i in range(n):
    for ii in range(n):
        if grid[i][ii] == '#':
            lumberyards += 1
        elif grid[i][ii] == '|':
            trees += 1

print(trees * lumberyards)