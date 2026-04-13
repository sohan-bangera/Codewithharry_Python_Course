class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def info(self):
        print(f"The name of {self.species} is {self.name}")
        
    def make_sound(self):
        print(f"{self.name} which is {self.species} makes Sound")

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Cat")
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} which is {self.species} makes sound")

a = Animal("Dog", "Dobberman")

c = Cat("Pinky", "Persian")

a.make_sound()
c.make_sound()
a.info()
c.info()