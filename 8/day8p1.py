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


def get_sum_of_metadata(root: Node) -> int:
    result = sum(root.metadata)
    for child in root.children:
        result += get_sum_of_metadata(child)
    
    return result

root = get_tree(nums, [0])

result = get_sum_of_metadata(root)

print(result)