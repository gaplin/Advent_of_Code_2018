import re

input = open('input2.txt').read().splitlines()

points = []
for line in input:
    points.append([int(x) for x in re.findall(r'[0-9-]+', line)])


def calc_all_distances(points: list):
    result = 0
    for i, point_A in enumerate(points):
        for point_B in points[:i]:
            result += abs(point_A[0] - point_B[0]) + abs(point_A[1] - point_B[1])
    
    return result

def move_forward(points: list):
    for point in points:
        point[0] += point[2]
        point[1] += point[3]

def move_backward(points: list):
    for point in points:
        point[0] -= point[2]
        point[1] -= point[3]

def print_grid(points: list):
    min_x = min([x[0] for x in points])
    min_y = min([x[1] for x in points])
    max_x = max([x[0] for x in points])
    max_y = max([x[1] for x in points])

    n = max_y - min_y + 1
    m = max_x - min_x + 1

    grid = [['.' for _ in range(m)] for _ in range(n)]

    for x, y, _, _ in points:
        grid[y - min_y][x - min_x] = '#'

    for row in grid:
        print(''.join(row))

prev = 999999999999999999
i = 0
while True:
    move_forward(points)
    dist = calc_all_distances(points)
    if dist > prev:
        break
    prev = dist
    i += 1

move_backward(points)
print_grid(points)