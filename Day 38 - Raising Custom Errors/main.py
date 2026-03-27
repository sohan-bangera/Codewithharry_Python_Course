a = input("Enter the value between 5 and 9:")
if (a == 'quit'):
    print()
elif(int(a) <5 or int(a) >9):
    raise ValueError("Value must be between 5 and 9")
    