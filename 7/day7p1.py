import re
from heapq import heappop, heappush

input = open('input2.txt').read().splitlines()

G = {}
incoming_edges = {}
for line in input:
    u, v = re.findall(r'[A-Z]', line)[1:]
    if u not in G:
        G[u] = []
        incoming_edges[u] = 0
    if v not in G:
        G[v] = []
        incoming_edges[v] = 0
    G[u].append(v)
    incoming_edges[v] += 1

Q = []
for u, count in incoming_edges.items():
    if count == 0:
        heappush(Q, u)

result = ''
while len(Q) > 0:
    u = heappop(Q)
    result += u
    for v in G[u]:
        incoming_edges[v] -= 1
        if incoming_edges[v] == 0:
            heappush(Q, v)

print(result)