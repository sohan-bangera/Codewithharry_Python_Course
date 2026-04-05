class Father:
    def info(self):
        print("This is a father class")

class Son(Father):
    def info1(self):
        print("This is a Son class")

class Daughter(Father):
    def info2(self):
        print("This is a Daughter class")

s1 = Son()
d1 = Daughter()
s1.info()
s1.info1()

d1.info()
d1.info2()