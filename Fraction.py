class Fraction:
    def __init__(self, v):
        self.v = v
        self.d = 1
        self.simplify()

    def dénominateur(self):
        n = 0
        while self.v != int(self.v):
            self.v *= 10
            n += 1
        self.d = 10 ** n

    def pgcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def simplify(self):
        self.dénominateur()
        gcd = self.pgcd(self.v, self.d)
        self.v //= gcd
        self.d //= gcd

    def __str__(self):
        return f"{int(self.v)}/{int(self.d)}"

decimal_number = 0.75
fraction_converter = Fraction(decimal_number)
print(fraction_converter)
