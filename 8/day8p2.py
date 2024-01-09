nums = [int(x) for x in open('input2.txt').read().strip().split(' ')]

class Node:
    pass

def get_tree(nums: list, current_idx: list) -> Node:
    root = Node()
    root.children = []
    root.metadata = []

    n_children = nums[current_idx[0]]
    current_idx[0] += 1
    n_metedata = nums[current_idx[0]]
    current_idx[0] += 1

    for _ in range(n_children):
        child = get_tree(nums, current_idx)
        root.children.append(child)
    
    for _ in range(n_metedata):
        root.metadata.append(nums[current_idx[0]])
        current_idx[0] += 1
    
    return root


def get_root_value(root: Node) -> int:
    if len(root.children) == 0:
        return sum(root.metadata)
    
    result = 0
    cache = {}
    n_children = len(root.children)
    for entry in root.metadata:
        if entry <= 0 or entry > n_children:
            continue
        if entry in cache:
            result += cache[entry]
        else:
            child_value = get_root_value(root.children[entry - 1])
            cache[entry] = child_value
            result += child_value
    
    return result

root = get_tree(nums, [0])

result = get_root_value(root)

print(result)