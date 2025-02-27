def decode(text,shift_number):
    decoded_text = ""

    for char in text:
        if char.isalpha():
            charVal = ord(char) - shift_number

            if char.isupper() and charVal < ord("A"):
                charVal += 26

            elif char.islower() and charVal < ord("a"):
                charVal +=26

            newChar = chr(charVal)
            decoded_text += newChar

        else:
            decoded_text += char

    return decoded_text
