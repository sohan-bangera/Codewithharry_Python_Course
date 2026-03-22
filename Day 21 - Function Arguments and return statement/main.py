# default arguments
def average(a=9,b=1):
    print("The average is", (a+b)/2)

average(1,5)

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

# Keyword arguments
name(fname = "Amy", lname ="bane")

# required Arguments
average(2,3)


# variable-length arguments
def averageOfManyNumbers(*nums):
    print(nums)
    sum = 0
    for i in nums:
        sum = sum+i
    print("The average is:", sum/len(nums))

averageOfManyNumbers(1,2,3,4,5,6,7,8)

# single * means it is stored as tuple
def example(*enusm):
    sum = 0
    for i in enusm:
        sum = sum + i
    print("The average of nums is:", sum/len(enusm))

# double *  means it is stored as dictonary
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

