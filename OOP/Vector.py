# 1.Create a class Vector, describing 3-dimentional

# vectors.

# 2.Implement as many special methods as possible.

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        # if isinstance(other, Vector):
        #     return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        # return NotImplemented
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        # if isinstance(other, Vector):
        #     return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        # return NotImplemented
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        # if isinstance(scalar, (int, float)):
        #     return Vector(self.x * scalar, self.y * scalar, self.z * scalar)
        # return NotImplemented
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Index out of range for Vector. Valid indices are 0, 1, and 2.")   
        
    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        else:
            raise IndexError("Index out of range for Vector. Valid indices are 0, 1, and 2.")    
    

vect1 = Vector(1, 2, 3)
vect2 = Vector(4, 5, 6)
print(vect1)  # Vector(1, 2, 3)
print(vect2)  # Vector(4, 5, 6)
vect3 = vect1 + vect2
print(vect3)  # Vector(5, 7, 9)
vect4 = vect1 - vect2
print(vect4)  # Vector(-3, -3, -3)
vect5 = vect1 * 2
print(vect5)  # Vector(2, 4, 6)
vect6 = 3 * vect2
print(vect6)  # Vector(12, 15, 18)
print(f"Magnitude of vect1: {vect1.magnitude()}")  # Magnitude of vect1: 3.7416573867739413
print(f"Magnitude of vect2: {vect2.magnitude()}")  # Magnitude of vect2: 8.774964387392123

vect1[1]  # This will raise an error since __getitem__ is not implemented

