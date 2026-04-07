class Pokemon:
    def __init__(self, name, type_, health):
        self.name = name
        self.type = type_
        self.health = health

    def attack(self, other_pokemon, damage=10):
        other_pokemon.health -= damage
        print(f"{self.name} attacks {other_pokemon.name}! {other_pokemon.name}'s health is now {other_pokemon.health}")

    def dodge(self):
        print(f"{self.name} dodges the attack!")

    def evolve(self):
        print(f"{self.name} evolves!")  

    def __str__(self):
        return f"{self.name} ({self.type}) - Health: {self.health}"

# Create Pokémon objects
pikachu = Pokemon("Pikachu", "Electric", 70)
bulbasaur = Pokemon("Bulbasaur", "Grass", 100)
charizard = Pokemon("Charizard", "Fire", 100)

# Test methods
# pikachu.attack()
pikachu.attack(bulbasaur, 20)
bulbasaur.dodge()
charizard.evolve()        

class Item:
    def __init__(self, type_, size, used=False):
        self.type = type_
        self.size = size
        self.used = used

# class PokeBall(Item):
#     def __init__(self, type_="Normal", used=False):
#         super().__init__(type_, size=1, used=used)

class PokeBall(Item):
    def __init__(self, type_="Normal", used=False):
        super().__init__(type_, size=1, used=used)

    def throw(self, pokemon):
        if not self.used:
            print(f"{pokemon.name} is caught with the {self.type} PokeBall!")
            self.used = True
        else:
            print("This PokeBall has already been used.")

    def __str__(self):
        return f"{self.type} PokeBall (size {self.size}) - Used: {self.used}"        

ball = PokeBall()
ball.throw(pikachu)
ball.throw(bulbasaur)  # will show "already used"   
print(pikachu)         