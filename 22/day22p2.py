from heapq import heappop, heappush

input = open('input2.txt').read().splitlines()

depth = int(input[0].split(' ')[1])
target_x, target_y = [int(x) for x in input[1].split(' ')[1].split(',')]
n = 1000
m = 1000

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
        if i == target_y and ii == target_x:
            erosion_levels[i][ii] = depth % mod
        else:
            erosion_levels[i][ii] = (erosion_levels[i][ii - 1] * erosion_levels[i - 1][ii] + depth) % mod

for i in range(n):
    for ii in range(m):
        remainder = erosion_levels[i][ii] % 3
        if remainder == 0: # rocky
            grid[i][ii] = '.'
        elif remainder == 1: # wet
            grid[i][ii] = '='
        else: # narrow
            grid[i][ii] = '|'


def get_shortest_path(grid, source, target, directions, required_items) -> int:
    distances = {source: 0}
    Q = [(0, source)]

    while len(Q) > 0:
        distance, (i, ii, items) = heappop(Q) # node -> (i, ii, items) -> items = c, t, n
        node = (i, ii, items)
        if distance != distances[node]:
            continue
        if node == target:
            return distance

        for di, dii in directions:
            new_i, new_ii = i + di, ii + dii
            if new_i < 0 or new_ii < 0:
                continue
            if items in required_items[grid[new_i][new_ii]]:
                new_node = (new_i, new_ii, items)
                new_distance = distance + 1
                if new_node not in distances or distances[new_node] > new_distance:
                    distances[new_node] = new_distance
                    heappush(Q, (new_distance, new_node))
        
        u_type = grid[i][ii]
        for item in required_items[u_type]:
            if item in items:
                continue
            new_node = (i, ii, item)
            new_distance = distance + 7
            if new_node not in distances or distances[new_node] > new_distance:
                distances[new_node] = new_distance
                heappush(Q, (new_distance, new_node))

required_items = {
    '.': 'ct',
    '=': 'cn',
    '|': 'tn'
}

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

result = get_shortest_path(grid, (0, 0, 't'), (target_y, target_x, 't'), directions, required_items)

print(result)