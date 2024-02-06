from huffman_encoding_and_decoding import huffman_encoding_func, huffman_decoding_func

sentences_file = open("data.txt", "r")
sentences = sentences_file.read()

print("fie:", sentences, sep='\n')
print("-" * 200, '\n')

print("Encoding State: ")
tree, encoded_data = huffman_encoding_func(sentences)
print('->', encoded_data)

with open('output_encoded.txt', 'w') as file_out:
    file_out.write(encoded_data)

print("-" * 200, '\n')

print("Decoding State: ")
undecoded_data = ''
with open('output_encoded.txt', 'r') as file_input:
    undecoded_data = file_input.read()
print('-->', undecoded_data)
decoded_data = huffman_decoding_func(encoded_data, tree)
print("The content of the data is:",decoded_data, sep='\n')

# print("The content of the encoded data is", encoded_data)
# decoded_data = huffman_decoding_func(encoded_data, tree)

sentences_file.close()
