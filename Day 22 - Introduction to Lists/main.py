list = [2,3,4,5,6,7,8,9,10,11,12]
print(list)

marks=  [12,130,14]
print(marks[1])

if 13 in marks:
    print("Yes")
else:
    print("No")

if "SO" in "SOHAN":
    print("Yes")

# first 0 is start, seocnd -1 is the end, and 2 is jump index,
#it skips the second values like, 2,4,6,8,0 (it skips 3,5,7,9)
print(list[0:-1:2])

lst = [i*i for i in list if i%2==0]
print(lst)


'''
Here the syntax is like:
variable_name = [(expression)(for loop)(if condition)]
variable_name = [Expression(item) for item in iterable if condition]
'''
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
leet = [item for item in names if len(item)>4]
print(leet)

