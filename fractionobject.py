#fractionobject
class Fraction(object):
    def __init__(self, num, denom):
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom  = denom
    def __str__(self):
        #Used when print() is called, returns a string representation 
        return str(self.num) + "/" + str(self.denom)
    def __add__(self, other):
        #returns a Fraction object equal to the sum of two parameters
        top = self.num * other.denom + self.denom * other.num
        bottom = self.denom * other.num
        return Fraction(top, bottom)
    def __sub__(self, other):
        #returns a Fraction object equal to the difference between two parameters
        top = self.num * other.denom - self.denom * other.num
        bottom = self.denom * other.denom
        return Fraction(top, bottom)
    def __float__(self):
        #returns a float.
        return self.num / self.denom
    def inverse(self):
        #returns the inverse of the Fraction object
        return Fraction(self.denom, self.num)

a = Fraction(1,4)
b = Fraction(3,4)
c = a + b
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))