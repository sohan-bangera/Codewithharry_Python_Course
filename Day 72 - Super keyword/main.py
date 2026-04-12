class Parent:
    def parentMethod(self):
        print("This is a parent method")

class Child(Parent):
    def childMethod(self):
        print("This is a child method")
        super().parentMethod()

c = Child()
c.childMethod()
# c.parentMethod()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

sohan = Programmer("Sohan", 123, "Python")
print(sohan.name, sohan.id, sohan.lang)
        