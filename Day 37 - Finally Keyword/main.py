def fun1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        while(i == 0):
            break
        return 0
    except:
        print("Enter the valid index")
        return 1
    finally:
        print("This executes regardless of error or not")

x = fun1()

print(x)
'''
finally executes regardless of the try except executes or error shows up
anther importance of the finally keyword is that inside function
when we try to return a value and if we use only print statement then
print statement wont run but if the finally keyword is used then
it will run even if a value is returned.
'''