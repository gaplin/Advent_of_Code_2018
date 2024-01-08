from itertools import cycle

input = [int(x) for x in open('input2.txt').read().splitlines()]

value = 0
reached_freq = {value}
result = 0
for x in cycle(input):
    value += x
    if value in reached_freq:
        result = value
        break
    reached_freq.add(value)

print(result)
