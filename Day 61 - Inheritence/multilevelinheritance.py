class GrandFather:
    def __init__(self, grandname):
        self.grandname = grandname

class Father(GrandFather):
    def __init__(self, fathername, grandname):
        self.fathername = fathername
        GrandFather.__init__(self,grandname)

class Son(Father):
    def __init__(self, sonname, fathername, grandname):
        self.sonname = sonname
        Father.__init__(self,fathername, grandname)

    def printName(self):
        print(f"Grandfather's Name: {self.grandname}")
        print(f"Father's Name: {self.fathername}")
        print(f"Son's Name: {self.sonname}")

s1 = Son("Ayyappa", "Chiddananda", "Prajwal")
s1.printName()