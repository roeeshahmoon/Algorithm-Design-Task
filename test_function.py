from compression import huffman_encoding_func, inorder_traversal, preorder_traversal
from decompression import huffman_decoding_func

with open("Alice_in_wonderlands.txt", "r") as Alice_file:
    Data_String = Alice_file.read()

# print("fie:", Data_String, sep='\n')
print("-" * 200, '\n')

print("Encoding State: ")
tree, encoded_data = huffman_encoding_func(Data_String)
# print('->', encoded_data)
lst_inorder = []
lst_preorder = []
inorder_traversal(tree.root, lst_inorder)
preorder_traversal(tree.root, lst_preorder)
print(lst_inorder)
print(lst_preorder)

with open('file_encoded.txt', 'w') as file_encoded:
    file_encoded.write(encoded_data + '\n')
    # file_encoded.write(lst_inorder)


print("-" * 200, '\n')

print("Decoding State: ")
undecoded_data = []
with open('file_encoded.txt', 'r') as file_input:
    undecoded_data = file_input.readlines()
# print('-->', undecoded_data)
decoded_data = huffman_decoding_func(undecoded_data[0], tree)
with open('file_decoded.txt', 'w') as file_decoded:
    file_decoded.write(decoded_data)
## print("The content of the data is:",decoded_data, sep='\n')

## print("The content of the encoded data is", encoded_data)
## decoded_data = huffman_decoding_func(encoded_data, tree)

