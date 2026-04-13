class FlyBehavior:
    def move(self, species):
        print(f"{species} is flying.")

class SwimBehavior:
    def move(self, species):
        print(f"{species} is swimming.")

class WaddleBehavior:
    def move(self, species):
        print(f"{species} is waddling.")

class HopBehavior:
    def move(self, species):
        print(f"{species} is hopping.")  

class WalkBehavior:
    def move(self, species):
        print(f"{species} is walking.")

class RunBehavior:
    def move(self, species):
        print(f"{species} is running.")  

class RompBehavior:
    def move(self, species):
        print(f"{species} is romping around.")      
                              

class Animal:
    def __init__(self, species, movements:list):
        self.species = species
        self._movements = movements

    def move(self):
        for movement in self._movements:
            movement.move(self.species)


class Duck(Animal):
    def __init__(self):
        super().__init__(
            species="Duck",
            movements=[FlyBehavior(), SwimBehavior(), WaddleBehavior()]
        )

class Sparrow(Animal):
    def __init__(self):
        super().__init__(
            species="Sparrow",
            movements=[FlyBehavior(), HopBehavior()]
        )

class Dog(Animal):
    def __init__(self):
        super().__init__(
            species="Dog",
            movements=[WalkBehavior(), RunBehavior(), RompBehavior(), SwimBehavior()]
        )                

animals = [Duck(), Sparrow(), Dog()]
for animal in animals:
    animal.move()
    print()        