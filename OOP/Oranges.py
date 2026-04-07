# 1.Create an Orange class that has one class variable named
# “count” used to track the number of oranges in existence.

# 2.All oranges should have a “weight” instance variable.

# 3.Create 3 different oranges. Make sure your “count” class
# variable tracks the count correctly.

# 4.Create a separate function (not bound to a class) to add
# the weight of each orange and get the result.

class Orange:
    count = 0 

    def __init__(self, weight):
        self.weight = weight 
        Orange.count += 1 

    def get_weight(self):
        return self.weight
    
    def __add__(self, other):
        return self.weight + other.weight
    
    def __del__(self):
        Orange.count -= 1
        

orange1 = Orange(150)
orange2 = Orange(200)
orange3 = Orange(250)

print(f"Number of oranges: {Orange.count}") 

def total_weight(*oranges):
    # total = sum(orange.weight for orange in oranges)
    total = 0
    for orange in oranges:
        total += orange.weight
    return total

total = total_weight(orange1, orange2, orange3)
print(f"Total weight of oranges: {total} grams") 

new_organge = orange1 + orange2
print(f"Combined weight of orange1 and orange2: {new_organge} grams")

del orange1

print(f"Number of oranges after deletion: {Orange.count}")

