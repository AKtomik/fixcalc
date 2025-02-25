class Fraction:
    def __init__(self, v):
        self.v = float(v)
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
        self.v /= gcd
        self.d /= gcd

    def __str__(self):
        return f"{int(self.v)}/{int(self.d)}"
def vr(r,t):
    if t==True :
        return r
    else :
        return Fraction(r)

print(Fraction(9.6328))