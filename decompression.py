from compression import get_codes

# The function traverses over the encoded data and checks if a certain piece of binary code could actually be a letter
def huffman_decoding_func(data, tree):
    if data == '':
        return ''
    dict = get_codes(tree.root)
    reversed_dict = {}
    for value, key in dict.items():
        reversed_dict[key] = value
    start_index = 0
    end_index = 1
    max_index = len(data)
    s = ''

    while start_index != max_index:
        if data[start_index: end_index] in reversed_dict:
            s += reversed_dict[data[start_index : end_index]]
            start_index = end_index
        end_index += 1

    return s

