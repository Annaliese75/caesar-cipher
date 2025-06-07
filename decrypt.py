# Caesar Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)
# Modified under BSD License Sarah Schaffer

def decrypt(cipher_txt, key):

# Every possible symbol that can be encrypted:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."&'

# Stores the encrypted/decrypted form of the message:
    translated = ""

    for symbol in cipher_txt:
    # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

        # Handle wrap-around, if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        cipher_txt = translated + symbol

# Return the output decrypted text to the main program

    return(cipher_txt)

