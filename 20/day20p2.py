from queue import Queue

def build_G(G: dict, nodes: set, directions: dict, text: str, idx: list, n: int) -> None:
    while True:
        if idx[0] >= n:
            return nodes
        char = text[idx[0]]
        if char == ')':
            return nodes
        
        idx[0] += 1
        if char == '|':
            return nodes
        if char == '(':
            continuations = set()
            while text[idx[0]] != ')':
                continuations |= build_G(G, nodes, directions, text, idx, n)
            nodes = continuations
            idx[0] += 1
            continue

        assert char in 'NWSE'
        di, dii = directions[char]
        continuations = set()
        for i, ii in nodes:
            new_position = (i + di, ii + dii)
            G[(i, ii)].add(new_position)
            if new_position not in G:
                G[new_position] = set()
            G[new_position].add((i, ii))
            continuations.add(new_position)
        nodes = continuations

def at_least_1000_distance(G: dict, source: tuple) -> int:
    result = 0
    visited = {source}
    Q = Queue()
    Q.put((source, 0))

    while Q.empty() == False:
        u, distance = Q.get()
        if distance >= 1000:
            result += 1
        for v in G[u]:
            if v not in visited:
                visited.add(v)
                Q.put((v, distance + 1))
    return result

text = open('input2.txt').read().strip()[1:-1]
directions = {
    'N': (-1, 0),
    'W': (0, -1),
    'S': (1, 0),
    'E': (0, 1)
}
u = (0, 0)
G = {u: set()}
n = len(text)

_ = build_G(G, {u}, directions, text, [0], n)

print(at_least_1000_distance(G, u))
