# Huffman Coding – Programming Assignment

## Overview

This project implements **Huffman coding compression and decompression** in Python. It consists of two scripts:  
- `ID1_ID2_compression.py` – Compresses a given text file using Huffman coding.  
- `ID1_ID2_decompression.py` – Decompresses a file that was compressed using the previous script.

## Files

- `ID1_ID2_compression.py` – Compresses the input `.txt` file and outputs a compressed file containing both the compressed data and the Huffman tree traversals.
- `ID1_ID2_decompression.py` – Reconstructs the original file from the compressed file by rebuilding the Huffman tree and decoding the data.

## How to Run

1. **Compression:**  
   ```
   python ID1_ID2_compression.py input_file.txt
   ```
   Output: `ID1_ID2_compressed.txt`

2. **Decompression:**  
   ```
   python ID1_ID2_decompression.py ID1_ID2_compressed.txt
   ```
   Output: `ID1_ID2_decompressed.txt` (should be identical to the original input)

## Notes

- Both scripts should be placed in the same directory as the text files.
- The compressed file contains:  
  1. The compressed binary data  
  2. The inorder traversal of the Huffman tree  
  3. The preorder traversal of the Huffman tree  
- The input text does **not** contain digits.

## Requirements

- Python 3.x
- Standard libraries only (or as specified in the assignment)
