import math

class Fraction:
    def __init__(self, n, m):
        self.numerator = n        
        if(m == 0):
            raise ValueError("Denominator can't be 0")
        self.denominator = m

    
    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def simplify(self):
        g = math.gcd(self.numerator, self.denominator)
        self.numerator /= g
        self.denominator //= g



f1 = Fraction(5, 10)
print(f1)
f1.simplify()
print(f1)