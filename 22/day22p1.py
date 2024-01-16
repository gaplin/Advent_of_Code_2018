input = open('input2.txt').read().splitlines()

depth = int(input[0].split(' ')[1])
m, n = [int(x) for x in input[1].split(' ')[1].split(',')]
n += 1
m += 1

grid = [['.' for _ in range(m)] for _ in range(n)]
erosion_levels = [[0 for _ in range(m)] for _ in range(n)]
mod = 20183

for i in range(1, n):
    erosion_levels[i][0] = (i * 48271 + depth) % mod

for ii in range(1, m):
    erosion_levels[0][ii] = (ii * 16807 + depth) % mod

erosion_levels[0][0] = depth % mod
for i in range(1, n):
    for ii in range(1, m):
        erosion_levels[i][ii] = (erosion_levels[i][ii - 1] * erosion_levels[i - 1][ii] + depth) % mod

erosion_levels[n - 1][m - 1] = depth % mod

for i in range(n):
    for ii in range(m):
        remainder = erosion_levels[i][ii] % 3
        if remainder == 0: # rocky
            grid[i][ii] = '.'
        elif remainder == 1: # wet
            grid[i][ii] = '='
        else: # narrow
            grid[i][ii] = '|'

result = 0
for row in grid:
    for char in row:
        if char == '=':
            result += 1
        elif char == '|':
            result += 2

print(result)
