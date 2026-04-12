class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        print("The calculation is for area")
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Calculation is for circle")
        super().area()
        return 3.14 * self.radius * self.radius 

rec = Shape(3,5)
print(rec.area())

cir = Circle(10)
print(cir.area())