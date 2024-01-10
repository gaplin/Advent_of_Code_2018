input = open('input2.txt').read().splitlines()

current_gen = input[0].split(': ')[1]

positive_rules = set()

for line in input[2:]:
    if line.endswith('#'):
        positive_rules.add(line.split(' ')[0])

def get_value(state: str, offset: int) -> int:
    result = 0
    for idx, char in enumerate(state):
        if char == '#':
            result += idx - offset
    return result

visited_states = {}
N = 50000000000
n_generations = N
offset = 0
generations_values = []
result = 0
for gen in range(n_generations):
    current_gen = '....' + current_gen + '....'
    n = len(current_gen)
    next_gen = ''
    applied_rules = []
    for i in range(2, n - 2):
        state = current_gen[i - 2:i + 3]
        if state in positive_rules:
            applied_rules.append(state)
            next_gen += '#'
        else:
            next_gen += '.'
    key = tuple(applied_rules)
    gen_value = get_value(next_gen, offset + 2)
    generations_values.append(gen_value)
    if key in visited_states and result == 0:
        starting_gen, _ = visited_states[key]
        result = generations_values[starting_gen - 1]
        cycle_length = gen - starting_gen
        cycle_value = gen_value - generations_values[starting_gen]
        n_generations -= starting_gen
        result += (n_generations // cycle_length) * cycle_value
        if n_generations % cycle_length != 0:
            result += generations_values[starting_gen + n_generations % cycle_length] - generations_values[starting_gen]
        break
    else:
        visited_states[key] = (gen, gen_value)
    offset += 2
    current_gen = next_gen

print(result)