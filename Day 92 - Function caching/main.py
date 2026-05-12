from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

fx(10)
print("done for 10")
fx(4)
print("Done for 4")
fx(3)
print("Done for 3")

# When it tries to print the below content,
# it will automatically prints without waiting 5 sec as
# the values are already saved in cache
fx(10)
print("done for 10")
fx(4)
print("Done for 4")
fx(3)
print("Done for 3")



@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(20))
# Output: 6765