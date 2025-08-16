from vector.vector import Vector2d
from point.point import Point
from rational_number.rational_number import RationalNumber


def main():
    # p1 = Point(2, 3)
    # p2 = Point(4, 5)
    # p3 = p1 + p2

    # vector1 = Vector2d(2, 3)
    # print(vector1.coords)
    # vector1.coords = Point(3, 4)
    # print(vector1.coords)
    # print(vector1)

    # vector2 = Vector2d(4, 5)

    # print(vector1 + vector2)
    # print(vector1 - vector2)

    # print(vector2.magnitude)

    rational1 = RationalNumber(2, -28)
    rational2 = RationalNumber(-6, 9)
    print(rational1)
    print(rational2)
    print(rational1 + rational2)
    print(rational1 - rational2)
    print(rational1 * rational2)
    print(rational1 / rational2)

    # parsing rational number as str
    rational3 = RationalNumber("2/6")
    rational4 = RationalNumber("1/3")
    print(rational3 == rational4)

    # parsing null constructor
    null_rational = RationalNumber()
    print(null_rational)

    # parsing list in rational number
    rational5 = RationalNumber([6, 18])
    print(rational5)

    # parsing tuple in rational number
    rational6 = RationalNumber((15, 40))
    print(rational6)


if __name__ == "__main__":
    main()
