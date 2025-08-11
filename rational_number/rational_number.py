class RationalNumber:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        if denominator == 0:
            raise TypeError("Denominator should not be zero")
        else:
            self.__denominator = denominator

        self.__simplified_fraction = 0

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, updated_denominator):
        self.__denominator = updated_denominator

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, updated_numerator):
        self.__numerator = updated_numerator

    @property
    def simplified_fraction(self):
        pass

    def __add__(self, other):
        numerator = (self.__numerator * other.denominator) + (
            self.__denominator * other.numerator
        )
        denominator = self.__denominator * other.denominator

        return RationalNumber(numerator, denominator)

    def __sub__(self, other):
        numerator = (self.__numerator * other.denominator) - (
            self.__denominator * other.numerator
        )
        denominator = self.__denominator * other.denominator

        return RationalNumber(numerator, denominator)

    def __mul__(self, other):
        numerator = self.__numerator * other.numerator
        denominator = self.__denominator * other.denominator

        return RationalNumber(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.__numerator * other.denominator
        denominator = self.__denominator * other.numerator

        return RationalNumber(numerator, denominator)

    def __str__(self):
        return f"{self.__numerator}/{self.denominator}"
