# Both of these classes are almost identical, the only difference is wording.
def cipherMessage():
    # Gets the words that the user wants to translate
    inputText = input("Enter your text to encode:\r\n")
    # Gets the bit shift 
    shifter = int(input("Enter how many places to shift:\r\n"))
    # Init text
    cipheredText = ""
    # Begin for loop for all words
    for char in inputText:
        position = ord(char)
        if 48 <= position <= 57:
            newPosition = (position - 48 + shifter) % 10 + 48
        elif 65 <= position <= 90:
            newPosition = (position - 65 + shifter) % 26 + 65
        elif 97 <= position <= 122:
            newPosition = (position - 97 + shifter) % 26 + 97
        else:
            newPosition = position
        cipheredText += chr(newPosition)

    print("Encoded Message (" + str(shifter) + " places): ")
    print(cipheredText)


def decipherMessage():
    inputText = input("Enter your text to decode:\r\n")
    shifter = int(input("Enter the secret shift number:\r\n"))

    decodedText = ""
    for char in inputText:
        position = ord(char)
        if 48 <= position <= 57:
            newPosition = (position - 48 - shifter) % 10 + 48
        elif 65 <= position <= 90:
            newPosition = (position - 65 - shifter) % 26 + 65
        elif 97 <= position <= 122:
            newPosition = (position - 97 - shifter) % 26 + 97
        else:
            newPosition = position
        decodedText += chr(newPosition)

    print("Decoded Message:")
    print(decodedText)


# Creates a loop until the user inputs the correct code.
userinput = ""
while userinput != "1" and userinput != "2":
    userinput = input("Enter 1 for Encode or 2 for Decode: ")
    if userinput != "1" and userinput != "2":
        print("You must type 1 or 2")

if userinput == "1":
    cipherMessage()
if userinput == "2":
    decipherMessage()
