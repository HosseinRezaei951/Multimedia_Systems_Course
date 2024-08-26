from decimal import Decimal, getcontext
import HashTable

def encode(string, length, number_of_alphabet):
    getcontext().prec = length * 3
    
    # initializing 
    codeWord = ""
    _low = Decimal(0)
    _high = Decimal(1)
    _range = Decimal(_high - _low)
    count_of_symbols = Decimal(number_of_alphabet)

    # initializing symbols frequencies
    symbols_frequencies = [Decimal(1) for i in range(number_of_alphabet)]
    
    # initializing symbols probabilities
    symbols_probabilities = [Decimal(1)/Decimal(count_of_symbols) for i in range(number_of_alphabet)]

    # initializing symbols ranges
    symbols_ranges = []
    _start_of_range = Decimal(0)
    _end_of_range = Decimal(0)
    for i in range(number_of_alphabet):
        _end_of_range = _start_of_range+(_range*Decimal(symbols_probabilities[i]))
        symbols_ranges.append([Decimal(_start_of_range), Decimal(_end_of_range)])
        _start_of_range = _end_of_range

    # initializing index to start reading string
    index = 0
    while (index != length):

        # reading one symbol of string
        count_of_symbols += 1
        
        # updating low, high, range 
        _low = _low + (_range * Decimal(symbols_ranges[HashTable.getIndex(string[index])][0]))
        _high = _low + (_range * Decimal(symbols_probabilities[HashTable.getIndex(string[index])]))
        _range = Decimal(_high - _low)

        # updating the frequency of seened symbol
        symbols_frequencies[HashTable.getIndex(string[index])] += 1

        # updating symbols probabilities
        for i in range(number_of_alphabet):
            symbols_probabilities[i] = symbols_frequencies[i]/count_of_symbols
            
        # updating symbols ranges
        _start_of_range = 0
        _end_of_range = 0
        for i in range(number_of_alphabet):
            _end_of_range = _start_of_range + symbols_probabilities[i]
            symbols_ranges[i]= [_start_of_range, _end_of_range]
            _start_of_range = _end_of_range

        # updating index to read next symbol
        index += 1
        
    # initializing output a code so that low <= code < high
    code = Decimal(0)
    fraction_decimal = Decimal(1)
   
    # calculating binary fractional codeword
    while(code < _low):
        fraction_decimal /= Decimal(2)

        if(code + fraction_decimal >= _high):
            codeWord+='0'
        else:
            code += fraction_decimal
            codeWord+='1'
    
    return codeWord


if __name__ == '__main__':

    number_of_alphabet = 96
    chunk_size = 100
    inputFile = open("Files/EncoderInputFile.txt", "r")
    inputString = inputFile.read()
    inputFile.close()
    
    output = ""
    outputFile = open("Files/EncoderOutputFile.txt", "w")
    output += str(len(inputString))

    iterations = len(inputString) // chunk_size
    start = 0
    while(start < len(inputString)):
        output += "\n"
        sentence = inputString[start:min(len(inputString),start + chunk_size)]
        output += encode(sentence, len(sentence), number_of_alphabet)
        start += chunk_size
        
    outputString = outputFile.write(output)
    outputFile.close()
    
    