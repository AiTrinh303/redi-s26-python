import math

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def getRadius(self):
        return self.radius

    def getArea(self):
        return math.pi * self.radius ** 2

circle1 = Circle(5, "red")
print(circle1.getRadius())  # Output: 5
print(circle1.getArea())    # Output: 78.53981633974483