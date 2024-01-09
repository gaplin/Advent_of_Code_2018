from queue import Queue

input = open('input2.txt').read().splitlines()

cords = []
for line in input:
    cords.append(tuple(map(int, line.split(', '))))
    
n = len(cords)
max_distance = 10000

for idx, position in enumerate(cords):
    for second_position in cords[:idx]:
        distance = abs(position[0] - second_position[0]) + abs(position[1] - second_position[1])
        max_distance = max(distance, max_distance)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

Q = Queue()
fields = {(x, y): [z, 0] for z, (x, y) in enumerate(cords)}
for i, (x, y) in enumerate(cords):
    Q.put((x, y, i, 0))

while True:
    x, y, idx, distance = Q.get()
    if distance > max_distance + 1:
        Q.put((x, y, idx, distance))
        break

    for dx, dy in directions:
        new_x, new_y, new_distance = x + dx, y + dy, distance + 1

        if (new_x, new_y) not in fields:
            fields[(new_x, new_y)] = [idx, new_distance]
            Q.put((new_x, new_y, idx, new_distance))


infinite = set()
while Q.empty() == False:
    _, _, idx, _ = Q.get()
    infinite.add(idx)

areas = [0 for _ in range(n)]

for (x, y), (idx, _) in fields.items():
    if idx != -1 and idx not in infinite:
        areas[idx] += 1

print(max(areas))