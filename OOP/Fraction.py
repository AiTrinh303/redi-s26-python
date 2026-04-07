# 1.Create a class Fraction

# 2.Implement as many special methods as possible.

import math

class Fraction:
    def __init__(self, num, denom):
        if denom == 0:
            raise ValueError("Denominator cannot be zero.")
        # Reduce the fraction to its simplest form
        gcd = math.gcd(num, denom)
        self.num = num // gcd
        self.denom = denom // gcd

    def __str__(self):
        return f"{self.num}/{self.denom}"
    def __repr__(self):
        return f"Fraction({self.num}, {self.denom})"
    
    # def __new__(self,*params):
    #     print("Creating a new Fraction instance...")
    #     return super().__new__(Fraction)
    

    def __add__(self, other):
        return Fraction(self.num * other.denom + other.num * self.denom, self.denom * other.denom)
    def __sub__(self, other):
        return Fraction(self.num * other.denom - other.num * self.denom, self.denom * other.denom)
    def __mul__(self, other):
        return Fraction(self.num * other.num, self.denom * other.denom)
    def __truediv__(self, other):
        return Fraction(self.num * other.denom, self.denom * other.num)
    def __eq__(self, other):
        return self.num * other.denom == other.num * self.denom
    def __lt__(self, other):
        return self.num * other.denom < other.num * self.denom
    def __le__(self, other):
        return self.num * other.denom <= other.num * self.denom
    def __gt__(self, other):
        return self.num * other.denom > other.num * self.denom
    def __ge__(self, other):
        return self.num * other.denom >= other.num * self.denom
    def __neg__(self):
        return Fraction(-self.num, self.denom)
    def __abs__(self):
        return Fraction(abs(self.num), abs(self.denom))
    def __float__(self):
        return self.num / self.denom
    def __int__(self):
        return self.num // self.denom
    def __pow__(self, power):
        return Fraction(self.num ** power, self.denom ** power)
    
# i want  2/6 to be equal to 1/3


frac1 = Fraction(1, 2)
print(frac1)  # Output: 1/2
print(repr(frac1))  # Output: Fraction(1, 2)
frac2 = Fraction(3, 4)  
print(frac1 + frac2)  # Output: 10/8
print(frac1 - frac2)  # Output: -2/8
print(frac1 * frac2)  # Output: 3/8
print(frac1 / frac2)  # Output: 4/6
print(frac1 == frac2)  # Output: False
print(frac1 < frac2)  # Output: True
print(frac1 <= frac2)  # Output: True
print(frac1 > frac2)  # Output: False
print(frac1 >= frac2)  # Output: False
print(-frac1)  # Output: -1/2
print(abs(-frac1))  # Output: 1/2
print(float(frac1))  # Output: 0.5
print(int(frac1))  # Output: 0
print(frac1 ** 2)  # Output: 1/4


