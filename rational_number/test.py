from rational_number import RationalNumber


def test():
    # Creating rational numbers with integer numerator and denominator
    rational1 = RationalNumber(2, -28)  # Should normalize signs and simplify to -1/14
    rational2 = RationalNumber(-6, 9)  # Should simplify to -2/3
    print(rational1)  # Expected: -1/14
    print(rational2)  # Expected: -2/3

    # Arithmetic operations on rational numbers
    print(rational1 + rational2)  # Tests __add__ operator
    print(rational1 - rational2)  # Tests __sub__ operator
    print(rational1 * rational2)  # Tests __mul__ operator
    print(rational1 / rational2)  # Tests __truediv__ operator

    # Parsing rational number from string
    rational3 = RationalNumber("2/6")  # Should simplify to 1/3
    rational4 = RationalNumber("1/3")  # Exactly equal to rational3
    print(rational3 == rational4)  # Expected: True (tests __eq__)

    # Null constructor (defaults to 0/1)
    null_rational = RationalNumber()
    print(null_rational)  # Expected: 0/1

    # Parsing rational number from list
    rational5 = RationalNumber([6, 18])  # Should simplify to 1/3
    print(rational5)  # Expected: 1/3

    # Parsing rational number from tuple
    rational6 = RationalNumber((15, 40))  # Should simplify to 3/8
    print(rational6)  # Expected: 3/8


if __name__ == "__main__":
    test()
