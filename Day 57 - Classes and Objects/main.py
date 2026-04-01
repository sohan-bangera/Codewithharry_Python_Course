class Person:
    name = "Sohan"
    occupation = "Associate Software Engineer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
# a.name = "Shubham"
# a.occupation = "Accountant"
print(a.occupation)

a.info()