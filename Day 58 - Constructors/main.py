# class Person:
#     name = "Sohan"
#     occ = "Developer"

#     def info(self):
#         print(f"{self.name} is a {self.occ}")

# a = Person()
# a.name = "Sakshi"
# a.occ = "QA"
# a.info()

#Using Constructor

class Person:
    def __init__(self):
        print("HI")

    def __init__(self, name="Deault Name", occ="Deafult Occ"):
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")
a = Person("Sohan", "Developer")
b = Person("Sakshi", "QA")
c = Person()

a.info()
b.info()
c.info()