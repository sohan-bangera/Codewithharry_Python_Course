import time

# def usingWhile():
#     i = 0
#     while i<50000:
#         i = i+1
#         print(i)
#     pass

# def usingFor():
#     for i in range(50000):
#         print(i)
#     pass

# init = time.time()
# usingFor()
# forTime = time.time() - init

# init = time.time()
# usingWhile()
# whileTime = time.time() - init

# print(f"The for loop execution time is: {forTime}")
# print(f"The While loop execution time is: {whileTime}")

t = time.localtime()
print(t)
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)

print(4)
time.sleep(3)
print("This is printed after 3 seconds")

d = time.time()
print(d)