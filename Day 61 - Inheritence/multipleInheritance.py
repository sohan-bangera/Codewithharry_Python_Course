class C():
    def info(self):
        print("From C")


class b(C):
    def info(self):
        print("From B")

class A(C):
    def info(self):
        print("From A")




class D(b,A):
    def dinfo(self):
        print("From D")
a1 = D()
a1.info()
print(D.__mro__)