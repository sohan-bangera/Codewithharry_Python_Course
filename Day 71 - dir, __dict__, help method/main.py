X = [1,2,3]
print(dir(X))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"The name is {self.name} and the age is {self.age}")

p = Person("Sohan", "24")
print(p.__dict__)
print(dir(p))

class Dog:
    """Represents a dog with a name and age."""
    def bark(self):
        """Makes the dog bark."""
        print("Woof!")

help(Dog)
# Outputs: Represents a dog with a name and age.