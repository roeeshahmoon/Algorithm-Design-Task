from compression import get_codes, Node, Tree, build_tree_traversal
""""
    Assignment Algorithm Design – Programming Assignment
    Author: Roee Shahmoon, ID: 206564759
    Author: Noam Klainer, ID: 316015411
"""


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


def main():
    print("Decoding State:\n")
    with open('/Users/roeeshahmoon/PycharmProjects/Huffman_Code/file_encoded.txt', 'r') as file_input:
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
    with open('/Users/roeeshahmoon/PycharmProjects/Huffman_Code/file_decoded.txt', 'w') as file_decoded:
        file_decoded.write(decoded_data)


if __name__ == "__main__":
    main()
