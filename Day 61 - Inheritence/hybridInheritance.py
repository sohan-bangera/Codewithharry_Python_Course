class School:
    def Info(self):
        print("This is a school function")

class Teacher1(School):
    def Info1(self):
        print("This is a Teacher 1 function")

class Teacher2(School):
    def Info2(self):
        print("This is a Teacher 2 function")

class Student(Teacher1, Teacher2):
    def Info3(self):
        print("This is a student function")

s1 = Student()
s1.Info3()
s1.Info2()
s1.Info1()
s1.Info()