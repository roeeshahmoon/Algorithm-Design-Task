from collections import deque
""""
    Assignment Algorithm Design – Programming Assignment
    Author: Roee Shahmoon, ID: 206564759
    Author: Noam Klainer, ID: 316015411
"""


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Queue:

    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


class Tree:

    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while len(q) > 0:
            node, level = q.deq()
            if node is None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s


def huffman_decode(data: str, tree_root: Node):
    if data == '':
        return ''
    dict_codes = get_codes(tree_root)
    reversed_dict = {}
    for value, key in dict_codes.items():
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


def build_tree_traversal(inorder, preorder):
    if not preorder or not inorder:
        return None

    root_val = preorder.pop(0)
    root = Node(root_val)
    root_idx = inorder.index(root_val)

    root.left = build_tree_traversal(inorder[:root_idx], preorder[:root_idx])
    root.right = build_tree_traversal(inorder[root_idx + 1:], preorder[root_idx:])

    return root


def read_list(content):
    result = []
    parts = content.split('#')
    for part in parts:
        if part != '\n':
            num, char = part.split('~')
            char = char.replace('$', '\n')
            result.append((int(num), char))
        else:
            return result


def get_codes(root):
    if root is None:
        return {}
    frequency, characters = root.value
    char_dict = dict([(i, '') for i in list(characters)])

    left_branch = get_codes(root.get_left_child())

    for key, value in left_branch.items():
        char_dict[key] += '0' + left_branch[key]

    right_branch = get_codes(root.get_right_child())

    for key, value in right_branch.items():
        char_dict[key] += '1' + right_branch[key]

    return char_dict


def main():
    print("Decoding State:\n")
    with open('206564759_316015411_compressed.txt', 'r') as file_input:
        undecoded_data = file_input.readlines()
        lst_inorder = read_list(undecoded_data[1])
        lst_preorder = read_list(undecoded_data[2])
    print("lst_inorder:", lst_inorder)
    print("lst_preorder:", lst_preorder)

    root_build = build_tree_traversal(lst_inorder, lst_preorder)
    tree_build = Tree()
    tree_build.root = root_build
    print('\n', tree_build)

    decoded_data = huffman_decode(undecoded_data[0][:-1], root_build)
    with open('206564759_316015411_decompressed.txt', 'w') as file_decoded:
        file_decoded.write(decoded_data)


if __name__ == "__main__":
    main()
