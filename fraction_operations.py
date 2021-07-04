import math

def gcd(m, n):
    while n % m != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n

def gcm(m, n):
    x = 1
    new_num = n
    while n % m != 0:
        new_num = n * x
        x = x + 1
        if new_num  % m == 0:
            n = new_num
            break

    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    
    def __str__(self):
        return str(self.num) + " / " + str(self.den)
    
    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
    
        return first_num == second_num
    
    
    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        if common == 0:
            common = 1
        return Fraction(new_num // common, new_den // common)

    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_dem = self.den * other_fraction.den
        return Fraction(new_num , new_dem)

    def __floordiv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        den_num = self.den * other_fraction.num
        common = gcd(new_num, den_num)
        if common == 0:
            common = 1
        return Fraction(new_num // common, den_num // common)

    def __sub__(self, other_fraction):
        if self.den != other_fraction.den:
            num_one = self.num
            num_two = other_fraction.num
            den_one = self.den
            den_two = other_fraction.den

            common = (gcm(den_one, den_two))

            factor_one = common / den_one
            factor_two = common / den_two
            num_one = factor_one * self.num
            num_two = factor_two * other_fraction.num

            num_one = num_one - num_two
            return Fraction(math.trunc(num_one), common)

    def __gt__(self, other_fraction):
        if self.den != other_fraction.den:
            num_one = self.num
            num_two = other_fraction.num
            den_one = self.den
            den_two = other_fraction.den
            
            common = (gcm(den_one, den_two))
            
            factor_one = common / den_one
            factor_two = common / den_two
            num_one = factor_one * self.num
            num_two = factor_two * other_fraction.num

            return(num_one > num_two)

    def __lt__(self, other_fraction):
        if self.den != other_fraction.den:
            num_one = self.num
            num_two = other_fraction.num
            den_one = self.den
            den_two = other_fraction.den
            
            common = (gcm(den_one, den_two))
            
            factor_one = common / den_one
            factor_two = common / den_two
            num_one = factor_one * self.num
            num_two = factor_two * other_fraction.num
            
            return(num_one < num_two)

f1 = Fraction(1, 3)
f2 = Fraction(1, 10)
# Prints out subtraction of two fractions
print(f1 - f2)

f1 = Fraction(1, 3)
f2 = Fraction(1, 10)

f2 = f1
#Prints out the new value for fraction 2
print(f2)

f1 = Fraction(1, 3)
f2 = Fraction(1, 10)
# Prints out the addition of the values
f3 = f2 + f1
print(f3)

f1 = Fraction(1, 3)
f2 = Fraction(1, 10)
# Prints out the multiplication of the values
print(f2 * f1)

f1 = Fraction(1, 3)
f2 = Fraction(1, 10)
#Divides the fractions
print(f1 // f2)

f1 = Fraction(1, 3)
f2 = Fraction(1, 10)
#Less than or greater than
print(f1 > f2)
print(f1 < f2)
