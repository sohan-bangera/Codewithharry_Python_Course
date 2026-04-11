# This will import the OS so that we can use it in the program
import os

# creating a function with the name rename so that when we run this it will execute
def rename():
    #Path stores the actual path where the files reside
    path = r"C:\Users\ASUS\OneDrive\Desktop\Python\Day 68 - Exercise 7 Clear the Clutter\Clutter"

    # this is used to increment the file name below in the for loop
    a =1

    # Files will store the actual path which is being used in for loop
    files = os.listdir(path)

    for file in files:
        # This will have old path
        old_path = os.path.join(path, file)
        # This will have new path
        new_path = os.path.join(path, f"{a}.png")

        #This will rename the old path with the new path
        os.rename(old_path, new_path)
        a+=1

#Below line is calling the function rename
rename()