class Animal:
    def __init__(self, species):
        self.species = species

    def move(self):
        print(f"{self.species} is moving")

class Mammal(Animal):
    pass

class Bird(Animal):
    def move(self):
        self.fly()

    def fly(self):
        print(f"{self.species} is flying!")

class Duck(Bird):
    def fly(self):
        print(f"{self.species} is swimming and flying!")

class Sparrow(Bird):
    def fly(self):
        print(f"{self.species} is hopping and flying!")

class Rocket():
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is flying to space!")

class Fish(Animal):
    def move(self):
        self.swim()

    def swim(self):
        print(f"{self.species} is swimming!")

class Dolphin(Fish, Mammal):
    def move(self):
        self.swim()
        print(f"{self.species} is also a mammal, so it can do other things too!")                


animals = [Mammal("Lion"), Bird("Eagle"), Duck("Mallard"), Sparrow("House Sparrow"), Rocket("Falcon 9"), Fish("Goldfish"), Dolphin("Flipper")]
for animal in animals:
        animal.move()