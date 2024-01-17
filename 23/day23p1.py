import re

input = open('input2.txt').read().splitlines()

nanobots = []
for line in input:
    x, y, z, r = [int(x) for x in re.findall(r'[0-9-]+', line)]
    nanobots.append((x, y, z, r))

nanobots.sort(key=lambda x: x[3], reverse=True)

x1, y1, z1, r1 = nanobots[0]
result = 1
for x2, y2, z2, _ in nanobots[1:]:
    distance = abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)
    if distance <= r1:
        result +=1 

print(result)