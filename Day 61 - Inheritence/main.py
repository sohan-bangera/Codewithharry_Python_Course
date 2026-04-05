class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee id: {self.id} is {self.name}")

class Programmer(Employee):
    def showLang(self):
        print("The default lang is Python")


class newProg(Programmer):
    def showInfo(self):
        print("I am a new programmer!")
e = newProg("Sohan", "21")
e.showDetails()
e.showLang()
e.showInfo()
        
print(newProg.__mro__)