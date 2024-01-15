import re
import sys

sys.setrecursionlimit(3000)
input = open('input2.txt').read().splitlines()

clay = []
n = 3000
grid = [['.' for _ in range(n)] for _ in range(n)]

for line in input:
    nums = [int(x) for x in re.findall(r'\d+', line)]
    if line[0] == 'x':
        clay.append(((nums[0], nums[0]), (nums[1], nums[2])))
    else:
        clay.append(((nums[1], nums[2]), (nums[0], nums[0])))
    
min_y = min(map(lambda x: x[1][0], clay))
max_y = max(map(lambda x: x[1][1], clay))

grid[0][500] = '+'
for (x0, x1), (y0, y1) in clay:
    for i in range(y0, y1 + 1):
        for ii in range(x0, x1 + 1):
            grid[i][ii] = '#'

def flow(grid, max_y, i, ii):
    grid[i][ii] = '|'
    if i > max_y:
        return
    
    if grid[i + 1][ii] == '.':
        flow(grid, max_y, i + 1, ii)
    if grid[i + 1][ii] == '|':
        return
    
    l = ii - 1
    left_sink = False
    while True:
        if grid[i][l] == '.':
            grid[i][l] = '|'
        else:
            break
        if grid[i + 1][l] == '.':
            flow(grid, max_y, i + 1, l)
            if grid[i + 1][l] == '|':
                left_sink = True
                break
        l -= 1
    
    r = ii + 1
    right_sink = False
    while True:
        if grid[i][r] == '.':
            grid[i][r] = '|'
        else:
            break
        if grid[i + 1][r] == '.':
            flow(grid, max_y, i + 1, r)
            if grid[i + 1][r] == '|':
                right_sink = True
                break
        r += 1
    if left_sink == False and right_sink == False:
        for x in range(l + 1, r):
            grid[i][x] = '~'

flow(grid, max_y, 1, 500)

result = 0
for i in range(min_y, max_y + 1):
        for ii in range(n):
            if grid[i][ii] in '|~':
                result += 1

print(result)