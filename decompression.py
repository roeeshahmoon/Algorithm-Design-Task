from compression import get_codes, Node

def BuildTreee(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder.pop(0)
    root = Node(root_val)
    root_idx = inorder.index(root_val)

    root.left = BuildTreee(preorder[:root_idx], inorder[:root_idx])
    root.right = BuildTreee(preorder[root_idx:], inorder[root_idx + 1:])

    return root
# The function traverses over the encoded data and checks if a certain piece of binary code could actually be a letter
def huffman_decoding_func(data: str, tree_root: Node):
    if data == '':
        return ''
    dict = get_codes(tree_root)
    reversed_dict = {}
    for value, key in dict.items():
        reversed_dict[key] = value
    start_index = 0
    end_index = 1
    max_index = len(data)
    s = ''

    while start_index != max_index:
        if data[start_index: end_index] in reversed_dict:
            s += reversed_dict[data[start_index: end_index]]
            start_index = end_index
        end_index += 1

    return s

