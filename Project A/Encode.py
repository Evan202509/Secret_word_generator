
def encode(text, shift_number):
    newWord = ""

    for char in text:
        if char.isalpha():
            charVal = ord(char)+shift_number

            if char.isupper() and charVal>90 or char.islower() and charVal>122:
                charVal-=26

            newChar = chr(charVal)
            newWord += newChar

        else:
            newWord +=char



    return(newWord)

