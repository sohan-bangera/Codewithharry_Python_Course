#public

class Employee:
    def __init__(self):
        self.name = "Sohan"

a = Employee()
print(a.name)

#private

class Student:
    def __init__(self):
        self.__name = "Sohan"

a1 = Student()
# print(a1.__name) # Cannot be accessed directly
#This can be accessed by putting _Classname
print(a1._Student__name)
print(a1.__dir__())

#protected
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())