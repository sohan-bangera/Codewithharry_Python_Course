import threading
import time
from concurrent.futures import ThreadPoolExecutor

#Indicates some task being done
def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

def main():
    # Normal code 
    # func(4)
    # func(2)
    # func(1)

    #Same code using Threads
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])

    t1.start()
    t2.start()
    t3.start()

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func, 3)
        # future2 = executor.submit(func, 2)
        # future3 = executor.submit(func, 4)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l = [3,2,4,1,5,6,6]
        results = executor.map(func, l)
        for result in results:
            print(result)


poolingDemo()

