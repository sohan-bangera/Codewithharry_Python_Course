class Employee:
    company = "Apple"

    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Sohan"
e1.show()
e1.changeCompany("Google")
e1.show()
# Employee.company = "SohanCOm"
print(Employee.company)