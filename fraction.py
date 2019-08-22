import math

class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        elif denominator == 0:
            if numerator < 0:
                numerator = -1
            elif numerator == 0:
                raise ZeroDivisionError()
            else:
                numerator = 1
        
        gcd_value = math.gcd(int(numerator), int(denominator))
        numerator /= gcd_value
        denominator /= gcd_value

        self.numerator = numerator
        self.denominator = denominator
            

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        new_numerator = self.numerator*frac.denominator + self.denominator*frac.numerator
        new_denominator = self.denominator*frac.denominator
        gcd_value = math.gcd(int(new_numerator), int(new_denominator))
        new_numerator /= gcd_value
        new_denominator /= gcd_value
        return Fraction(new_numerator, new_denominator)

        
    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        gcd_value1 = math.gcd(int(self.numerator), int(self.denominator))
        self.numerator /= gcd_value1
        self.denominator /= gcd_value1
        gcd_value2 = math.gcd(int(frac.numerator), int(frac.denominator))
        frac.numerator /= gcd_value2
        frac.denominator /= gcd_value2
        return self.numerator == frac.numerator and self.denominator == frac.denominator
    
    def __mul__(self, frac):
        """Return the product of two fractions as a new fraction.
           Use the standard formula  a/b * c/d = (a*c)/(b*d)
        """
        new_numerator = self.numerator*frac.numerator
        new_denominator = self.denominator*frac.denominator
        gcd_value = math.gcd(int(new_numerator), int(new_denominator))
        new_numerator /= gcd_value
        new_denominator /= gcd_value
        return Fraction(new_numerator, new_denominator)
    
    
