input = open('input2.txt').read().splitlines()

def common_full_box_text(box_A: str, box_B: str):
    common_text = ''
    misses = 0
    for a, b in zip(box_A, box_B):
        if a == b:
            common_text += a
        else:
            misses += 1
            if misses > 1:
                return None
    return common_text


result = ''
for idx, box_A in enumerate(input[1:]):
    for box_B in input[:idx]:
        common_text = common_full_box_text(box_A, box_B)
        if common_text != None:
            result = common_text
            break
    else:
        continue
    break

print(result)