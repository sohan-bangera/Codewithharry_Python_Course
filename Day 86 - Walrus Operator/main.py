a = True
print(a := False)

numbers = [1,2,3,4,5]

while(n := len(numbers)) >0:
    print(numbers.pop())
    print(numbers)

names = ["John", "Jane", "Jim"]

if (name := input("Enter a name: ")) in names:
    print(f"Hello, {name}!")
else:
    print("Name not found.")

# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)

# print(happy := True)

#without walrus operator
# foods = list()

# while True:
#     food = input("Enter the name of the food")
#     if food == 'quit':
#         break
#     foods.append(food)

# print(foods)

foods = list()

while (food := input("Enter the food you want to eat:")) != "quit":
    foods.append(food)
print(foods)