num = int(input("Enter the number: "))

if(num < 0):
    print("The", num, "is negative")
elif(num >0):
    if(num<10):
        print("The",num,"is in between 1-10")
    elif(num>10 and num<50):
        print("The",num,"is in between 11-50")
    else:
        print("The",num,"is greater then 50")
else:
    print("The",num,"is zero")