import random
import string


def encodingFun():
    # # input from the user
    message = input("Enter your message: ")

    # #random letters to generate
    ranDig = 3

    #intial random letters
    ran=""

    ranStart = ""
    ranEnd = ""
    finalEncodedWord =""

    # if len of name is less then 3
    if(len(message) <= 3):
        reversed = message[::-1]
        return reversed
    else:
        firstLetter = message[0]
        newName = message[1:]
        newName = newName + firstLetter
        for i in range(ranDig):
            ranStart = ranStart + random.choice(string.ascii_letters)
            ranEnd = ranEnd + random.choice(string.ascii_letters)
            finalEncodedWord = ranStart + newName + ranEnd
        reversed = finalEncodedWord[::-1]
        return reversed


def decodingFun(x):
    if(len(x)<=3):
        reversed = x[::-1]
        return reversed
    else:
        removeFirst = x[3:]
        removeLast = removeFirst[:-3]
        FLetter = removeLast[0]
        WFLetter = removeLast[1:]
        beforeReversed = WFLetter+FLetter
        reversed = beforeReversed[::-1]
        return reversed

encoded = encodingFun()
print(f"The encoded String is: {encoded}")


decoded = decodingFun(encoded)
print(f"The decoded String is: {decoded}")
