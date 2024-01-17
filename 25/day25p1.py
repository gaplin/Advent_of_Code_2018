def find(nodes: list, x: int):
    if x == nodes[x]:
        return x
    nodes[x] = find(nodes, nodes[x])
    return nodes[x]

def union(nodes: list, x: int, y: int):
    x = find(nodes, x)
    y = find(nodes, y)
    nodes[y] = x

input = open('input2.txt').read().splitlines()
n = len(input)
cords = []
for line in input:
    cords.append([int(x) for x in line.split(',')])


groups = [i for i in range(n)]

def distance(A, B):
    result = 0
    for a, b in zip(A, B):
        result += abs(a - b)

    return result

for i in range(n - 1):
    for ii in range(i + 1, n):
        if find(groups, i) != find(groups, ii):
            if distance(cords[i], cords[ii]) <= 3:
                union(groups, i, ii)

unique_groups = set()
for i in range(n):
    unique_groups.add(find(groups, i))

print(len(unique_groups))