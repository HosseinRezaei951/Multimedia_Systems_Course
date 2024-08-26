def getIndex(symbol):
    decimal_in_Ascii = ord(symbol)
    if (decimal_in_Ascii == 10): # first index of array fo enter(or new line) ==> 10 (0):Count of symbols 1 
        return 0
    elif (31 < decimal_in_Ascii and decimal_in_Ascii < 126):  # ==> 32-125 (1-94):Count of symbols 94
        return decimal_in_Ascii - 31
    else: # last index of array for unknown things ==> ~ (95):Count of symbols 1 
        return 95

def getSymbol(index):
    if (index == 0):
        return chr(10)
    elif (0 < index and index < 95):  
        return chr(index + 31)
    else:
        return chr(126) # means: ~
