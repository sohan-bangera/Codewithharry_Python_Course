# Class Variable example

class MyClass:
    class_variable = 0 # class Variable
    
    def __init__(self):
        MyClass.class_variable += 1
        
    def print_class_variable(self):
        print(MyClass.class_variable)
        

obj1 = MyClass()
obj1.print_class_variable() # Output: 2
obj2 = MyClass()

obj2.print_class_variable() # Output: 2

# Instance Variable example
class MyClass:
    def __init__(self, name):
        self.name = name
        
    def print_name(self):
        print(self.name)

obj1 = MyClass("John")
obj2 = MyClass("Jane")

obj1.print_name() # Output: John
obj2.print_name() # Output: Jane