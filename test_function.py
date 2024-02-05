from huffman_encoding_and_decoding import huffman_encoding_func, huffman_decoding_func

sentences_file = open("data.txt", "r")
sentences = sentences_file.read()

print("Encoding process: ")
tree, encoded_data = huffman_encoding_func(sentences)
print("The content of the data is: {}".format(sentences))

print("Decoding process: ")
print("The content of the encoded data is: {}".format(encoded_data))
decoded_data = huffman_decoding_func(encoded_data, tree)
print("The content of the data is: {}".format(decoded_data))

sentences_file.close()