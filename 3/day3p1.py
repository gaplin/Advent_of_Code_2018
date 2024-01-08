import re

input = open('input2.txt').read().splitlines()

claims = []
for line in input:
    claims.append([int(x) for x in re.findall(r'[0-9]+', line)])

already_taken_space = set()
duplicates = set()
for id, ii, i, width, height in claims:
    for new_i in range(i, i + height):
        for new_ii in range(ii, ii + width):
            position = (new_i, new_ii)
            if position in already_taken_space:
                duplicates.add(position)
            else:
                already_taken_space.add(position)

print(len(duplicates))