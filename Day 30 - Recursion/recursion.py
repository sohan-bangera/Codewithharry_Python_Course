# Factorial of a given number
num = 4

def addNumbers(num):
    if(num == 0 or num == 1):
        return 1
    else:
        return num * addNumbers(num -1)
        
    
res = addNumbers(num)
print(res)

'''
4 * factorial(3)
4 * 3 * factorial(2)
4 * 3 * 2 * factorial(1)
4 * 3 * 2 * 1 => 24
'''

# Quick Quiz: Write a program to print the Fibonacci Sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

n = 5

def fibonacci(n):
    if(n <= 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) 
    
for i in range(n):
    print( fibonacci(i), end=" ")
