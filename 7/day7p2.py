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

not_started_jobs = []
for u, count in incoming_edges.items():
    if count == 0:
        heappush(not_started_jobs, u)

def get_needed_time(u, added_time):
    return ord(u) - ord('A') + 1 + added_time

current_time = 0
added_time = 60
n_workers = 5
not_finished_jobs = []

while len(not_finished_jobs) != 0 or len(not_started_jobs) != 0:
    available_workers = n_workers - len(not_finished_jobs)
    if available_workers == 0 or len(not_started_jobs) == 0:
        finished_time, u = heappop(not_finished_jobs)
        current_time = finished_time
        for v in G[u]:
            incoming_edges[v] -= 1
            if incoming_edges[v] == 0:
                heappush(not_started_jobs, v)
        continue
    u = heappop(not_started_jobs)
    finish_time = current_time + get_needed_time(u, added_time)
    heappush(not_finished_jobs, (finish_time, u))

print(current_time)