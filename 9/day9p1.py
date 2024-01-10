import re

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = self
        self.prev = self

    def __str__(self) -> str:
        return '[{}, {}, {}]'.format(self.value, self.prev.value, self.next.value)
    
    def __repr__(self) -> str:
        return self.__str__()
    
def place_after(A: Node, B: Node):
    next = A.next
    prev = A
    B.next = next
    B.prev = prev
    prev.next = B
    next.prev = B

def remove(A: Node):
    prev = A.prev
    next = A.next
    A.next = None
    A.prev = None
    prev.next = next
    next.prev = prev

def get_n_th_prev(root: Node, n: int) -> Node:
    current = root
    for _ in range(n):
        current = current.prev      

    return current

def print_marbles(start: Node):
    start_copy = start
    start = start.next
    while start != start_copy:
        start = start.next

input = open('input2.txt').read().strip()

players, last_marble = map(int, re.findall(r'\d+', input))
scores = [0 for _ in range(players)]
l = Node(0)
current_marble = l

for i in range(1, last_marble + 1):
    if i % 23 != 0:
        new_marble = Node(i)
        place_after(current_marble.next, new_marble)
        current_marble = new_marble
    else:
        player = (i - 1) % players
        scores[player] += i
        marble_to_remove = get_n_th_prev(current_marble, 7)
        current_marble = marble_to_remove.next
        remove(marble_to_remove)
        scores[player] += marble_to_remove.value


result = max(scores)
print(result)