from queue import Queue

input = open('input2.txt').read().splitlines()

cords = []
for line in input:
    cords.append(tuple(map(int, line.split(', '))))
    
n = len(cords)
max_distance = 0

def get_distances(x, y, cords):
    dist = 0
    for x1, y1 in cords:
        dist += abs(x1 - x) + abs(y1 - y)
    return dist

limit = 10000
result = 0
for i in range(1000):
    for ii in range(1000):
        if get_distances(i, ii, cords) <= limit:
            result += 1

print(result)