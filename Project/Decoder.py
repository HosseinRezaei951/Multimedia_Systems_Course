from decimal import Decimal, getcontext
import HashTable

def decode(codeWord, length, number_of_alphabet):
    getcontext().prec = length * 3

    # calculating decimal 
    code = codeWord
    fraction_decimal = Decimal(0)
    for i in range(len(codeWord)):
        if(code[i] == "1"):
            fraction_decimal += Decimal(pow(Decimal(2),-(i+1)))

    # initializing
    string = ""
    _value = Decimal(fraction_decimal)
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

    # initializing index to find symbol
    index = -1
    for i in range(length):

        # finding a symbol index and decoding decimal
        for i in range(number_of_alphabet):
            if(_value > symbols_ranges[i][0] and _value < symbols_ranges[i][1]):
                string += HashTable.getSymbol(i)
                index = i
                break
        
        # reading one symbol of string
        count_of_symbols += 1

        # updating low, high, range, value
        _low = Decimal(symbols_ranges[index][0])
        _high = Decimal(symbols_ranges[index][1])
        _range = Decimal(_high - _low)
        _value = Decimal(_value - _low)/Decimal(_range)        
        
        # updating the frequency of seened symbol
        symbols_frequencies[index] += 1
        
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

    return string


if __name__ == '__main__':

    number_of_alphabet = 96
    chunk_size = 100
    inputFile = open("Files/EncoderOutputFile.txt", "r")
    length = int(inputFile.readline()) 
    
    string = ""
    iterations = length // chunk_size

    for x in range(iterations):
        codeWord = inputFile.readline()
        string += decode(codeWord, chunk_size, number_of_alphabet)

    codeWord = inputFile.readline()
    string += decode(codeWord, length % chunk_size, number_of_alphabet)

    inputFile.close()
       
    outputFile = open("Files/DecoderOutputFile.txt", "w")
    outputFile.write(string)
    outputFile.close()