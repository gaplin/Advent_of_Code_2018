polymer = open('input2.txt').read().strip()

ranges = []
n = len(polymer)
i = 0
while i < n - 1:
    l, r = i, i + 1
    while l >= 0 and r < n:
        if polymer[l].lower() == polymer[r].lower() and polymer[l].islower() != polymer[r].islower():
            l -= 1
            r += 1
            while l >= 0 and len(ranges) > 0:
                if l == ranges[-1][1]:
                    l = ranges[-1][0] - 1
                    ranges.pop()
                else:
                    break
        else:
            break
    if r > i + 1:
        ranges.append((l + 1, r - 1))
    i = r

result = n
for low, high in ranges:
    result -= high - low + 1

print(result)