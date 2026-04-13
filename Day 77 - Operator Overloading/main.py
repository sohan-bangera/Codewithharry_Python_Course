class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self,other):
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)

    def __str__(self):
        return f"i:{self.i}, j:{self.j}, k:{self.k}"

v1 = Vector(3,2,4)
print(v1)

v2 = Vector(13,12,14)
print(v2)

v3 = v1 + v2
print(v3)