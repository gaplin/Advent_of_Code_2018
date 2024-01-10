input = open('input2.txt').read().splitlines()

current_gen = input[0].split(': ')[1]

positive_rules = set()

for line in input[2:]:
    if line.endswith('#'):
        positive_rules.add(line.split(' ')[0])

n_generations = 20
offset = 0
for _ in range(n_generations):
    current_gen = '....' + current_gen + '....'
    offset += 2
    n = len(current_gen)
    next_gen = ''
    for i in range(2, n - 2):
        state = current_gen[i - 2:i + 3]
        next_gen += '#' if state in positive_rules else '.'
    current_gen = next_gen

result = 0
for i, char in enumerate(current_gen):
    if char == '#':
        result += i - offset

print(result)