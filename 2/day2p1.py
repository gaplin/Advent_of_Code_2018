input = open('input2.txt').read().splitlines()

twos = 0
threes = 0
for line in input:
    occurs = {}
    for char in line:
        if char not in occurs:
            occurs[char] = 1
        else:
            occurs[char] += 1
    if 2 in occurs.values():
        twos += 1
    if 3 in occurs.values():
        threes += 1

result = twos * threes
print(result)