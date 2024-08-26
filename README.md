# Multimedia Systems Course

Welcome to the Multimedia Systems Course repository. This repository contains coursework and projects related to multimedia systems, focusing on encoding and decoding processes, file handling, and data structures like hash tables.

## Directory Structure

### Project

The `Project` directory includes Python scripts and related files for multimedia encoding and decoding tasks:

- **Files**:
  - **DecoderOutputFile.txt**: This file stores the output generated by the `Decoder.py` script after processing the encoded data.
  - **EncoderInputFile.txt**: This is the input file for the `Encoder.py` script, containing raw data that needs to be encoded.
  - **EncoderOutputFile.txt**: This file holds the output generated by the `Encoder.py` script, which is then used as input for decoding.

- **Decoder.py**: This script is responsible for decoding the data from `EncoderOutputFile.txt` back into its original form, utilizing the methods implemented in `HashTable.py`.

- **Encoder.py**: This script handles the encoding of data from `EncoderInputFile.txt`. It processes the data and generates the encoded output, which is saved in `EncoderOutputFile.txt`.

- **HashTable.py**: This script implements a hash table data structure used by both `Encoder.py` and `Decoder.py` for efficient encoding and decoding processes.

- **README.md**: Documentation detailing the functionality of the Python scripts, including setup instructions, usage guidelines, and an overview of the encoding/decoding process.

## How to Use

1. **Encoder.py**:
   - Input: Provide raw data in `EncoderInputFile.txt`.
   - Output: The encoded data is saved in `EncoderOutputFile.txt`.

2. **Decoder.py**:
   - Input: Takes the encoded data from `EncoderOutputFile.txt`.
   - Output: Decoded data is stored in `DecoderOutputFile.txt`.

3. **HashTable.py**:
   - This script supports the encoding and decoding processes by managing data using a hash table.

Please refer to the comments within each script for detailed information on their implementation and usage.