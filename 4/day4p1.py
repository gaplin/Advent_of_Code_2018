import re

input = open('input2.txt').read().splitlines()

entries = []

for line in input:
    entry = []
    nums = [int(x) for x in re.findall(r'[0-9]+', line)]
    time = tuple(nums[:5])
    entry.append(time)
    if len(nums) == 6:
        entry.append(nums[5])
    elif 'wakes' in line:
        entry.append(True)
    else:
        entry.append(False)
    entries.append(entry)

entries.sort(key=lambda x: x[0])
    
current_idx = -1
start_time = -1
times = {}
for entry in entries:
    if type(entry[1]) == int:
        current_idx = entry[1]
        if current_idx not in times:
            times[current_idx] = [0 for _ in range(60)]
    elif entry[1] == False:
        start_time = entry[0][4]
    else:
        end_time = entry[0][4]
        for i in range(start_time, end_time):
            times[current_idx][i] += 1

current_max = 0
result_id = 0
result_position = 0
for id, minutes in times.items():
    guard_max = 0
    guard_minute = 0
    asleep_minutes = sum(minutes)
    for i in range(60):
        if minutes[i] > guard_max:
            guard_max = minutes[i]
            guard_minute = i
    if asleep_minutes > current_max:
        current_max = asleep_minutes
        result_id = id
        result_position = guard_minute

result = result_id * result_position
print(result)