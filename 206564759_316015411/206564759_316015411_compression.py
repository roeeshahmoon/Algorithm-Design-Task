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


def inorder_traversal(root, lst_res: []):
    if root:
        inorder_traversal(root.left, lst_res)
        lst_res.append(root.value)
        inorder_traversal(root.right, lst_res)


def preorder_traversal(root, lst_res: []):
    if root:
        lst_res.append(root.value)
        preorder_traversal(root.left, lst_res)
        preorder_traversal(root.right, lst_res)


def return_frequency(data):
    frequency = {}
    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    lst = [(v, k) for k, v in frequency.items()]
    lst.sort(reverse=True)
    return lst


def sort_values(nodes_list, node):
    node_value, char1 = node.value
    index = 0
    max_index = len(nodes_list)
    while True:
        if index == max_index:
            nodes_list.append(node)
            return
        current_val, char2 = nodes_list[index].value
        if current_val <= node_value:
            nodes_list.insert(index, node)
            return
        index += 1


def build_tree(data):
    lst = return_frequency(data)
    nodes_list = []
    for node_value in lst:
        node = Node(node_value)
        nodes_list.append(node)

    while len(nodes_list) != 1:
        first_node = nodes_list.pop()
        second_node = nodes_list.pop()
        val1, char1 = first_node.value
        val2, char2 = second_node.value
        node = Node((val1 + val2, char1 + char2))
        node.set_left_child(second_node)
        node.set_right_child(first_node)
        sort_values(nodes_list, node)

    root = nodes_list[0]
    tree = Tree()
    tree.root = root
    return tree


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


def huffman_encode(data):
    if data == '':
        return None, ''
    tree = build_tree(data)
    dict_codes = get_codes(tree.root)
    codes = ''
    for char in data:
        codes += dict_codes[char]
    return tree, codes


def build_tree_traversal(inorder, preorder):
    if not preorder or not inorder:
        return None

    root_val = preorder.pop(0)
    root = Node(root_val)
    root_idx = inorder.index(root_val)

    root.left = build_tree_traversal(inorder[:root_idx], preorder[:root_idx])
    root.right = build_tree_traversal(inorder[root_idx + 1:], preorder[root_idx:])

    return root


def main():
    sentences_file = open("Alice_in_wonderlands.txt", "r")
    sentences = sentences_file.read()

    print("Encoding State:\n")
    tree_encoded, encoded_data = huffman_encode(sentences)

    lst_inorder = []
    lst_preorder = []
    inorder_traversal(tree_encoded.root, lst_inorder)
    preorder_traversal(tree_encoded.root, lst_preorder)
    print("lst_inorder:", lst_inorder)
    print("lst_preorder:", lst_preorder)

    with open('206564759_316015411_compressed.txt', 'w') as file_encoded:
        file_encoded.write(encoded_data)
        file_encoded.write('\n')

        for elm_in in lst_inorder:
            num = str(elm_in[0])
            file_encoded.write(num)
            file_encoded.write('~')
            char = elm_in[1]
            char = char.replace('\n', '$')
            file_encoded.write(char)
            file_encoded.write('#')
        file_encoded.write('\n')

        for elm_pre in lst_preorder:
            num = str(elm_pre[0])
            file_encoded.write(num)
            file_encoded.write('~')
            char = elm_pre[1]
            char = char.replace('\n', '$')
            file_encoded.write(char)
            file_encoded.write('#')
        file_encoded.write('\n')

    root_build = build_tree_traversal(lst_inorder, lst_preorder)
    tree_build = Tree()
    tree_build.root = root_build
    print('\n', tree_build)


if __name__ == "__main__":
    main()
