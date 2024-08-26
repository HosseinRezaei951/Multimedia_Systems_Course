# Adaptive Arithmetic Coding Project

This project implements an adaptive arithmetic coding algorithm, which is a lossless data compression technique. The process involves encoding an input text into a binary fractional code and then decoding that code back to the original text. This project includes both an encoder and a decoder, designed to work synchronously by dynamically adjusting symbol probabilities during processing.

## Project Overview

The project includes the following components:

1. **Encoder**: Converts an input text into a binary fractional code based on symbol probabilities.
2. **Decoder**: Reconstructs the original text from the binary fractional code by mirroring the encoding process.

## Features

- **Adaptive Arithmetic Coding**: Dynamically updates symbol probabilities during encoding and decoding, allowing the process to adjust to the data in real-time.
- **High-Precision Arithmetic**: Uses Python's `decimal` module to handle the precision required for arithmetic coding.
- **Chunk Processing**: Processes data in manageable chunks, making the algorithm efficient even for large texts.

## How It Works

### Encoder

- **Purpose**: The encoder reads an input text and converts it into a binary fractional code based on the probabilities of symbols.
- **Process**:
  1. **Initialization**:
     - Sets the number of alphabet symbols (`number_of_alphabet = 96`) and defines a `chunk_size` for processing the input text.
  2. **Reading the Input**:
     - The encoder reads the input text in chunks.
  3. **Encoding Each Chunk**:
     - For each chunk, the encoder calculates a binary fractional code by narrowing down a range based on symbol probabilities.
     - Updates frequency and probability tables after encoding each symbol.
  4. **Final Output**:
     - The encoded binary string is written to `EncoderOutputFile.txt`.

### Decoder

- **Purpose**: The decoder reads the encoded binary string from `EncoderOutputFile.txt` and decodes it back into the original text.
- **Process**:
  1. **Initialization**:
     - Similar to the encoder, initializes values like `number_of_alphabet = 96` and `chunk_size`.
  2. **Reading the Encoded Data**:
     - Reads the length of the original input string and processes the encoded binary string in chunks.
  3. **Decoding Each Chunk**:
     - Converts the binary fractional code back to a decimal number.
     - Iteratively narrows down the range to determine the corresponding original symbols.
     - Updates the frequency and probability tables to stay synchronized with the encoder.
  4. **Final Output**:
     - Writes the final decoded string to `DecoderOutputFile.txt`.

### `decode` Function

- **Input Parameters**:
  - `codeWord`: The binary fractional code for a chunk of the original text.
  - `length`: The length of the original text chunk.
  - `number_of_alphabet`: Total number of symbols in the alphabet.
- **Working**:
  - Converts the binary fractional code into a decimal number.
  - Iteratively decodes each symbol by narrowing down the range based on the decimal value.
  - Reconstructs the original string chunk by chunk.

## Summary

This project demonstrates adaptive arithmetic coding, which is useful for lossless data compression. The adaptive nature allows for real-time adjustment of symbol probabilities, making it efficient even when symbol distributions are unknown. The project includes Python implementations of both an encoder and decoder, leveraging the `decimal` module for high-precision arithmetic. Additionally, it features chunk-based processing to handle large texts efficiently.

### Important Notes

- **Adaptive Nature**: The encoder and decoder both dynamically adjust to the data, ensuring synchronization without needing predefined probabilities.
- **Chunk Processing**: Handles large texts efficiently by processing the data in chunks.
