from vector.vector import Vector2d
from point.point import Point
from rational_number.rational_number import RationalNumber


def main():

    # vector1 = Vector2d(2, 3)
    # print(vector1.coords)
    # vector1.coords = Point(3, 4)
    # print(vector1.coords)
    # print(vector1)

    # vector2 = Vector2d(4, 5)

    # print(vector1 + vector2)
    # print(vector1 - vector2)

    # print(vector2.magnitude)

    rational1 = RationalNumber(2, 3)
    rational2 = RationalNumber(3, 6)
    print(rational1 + rational2)
    print(rational1 - rational2)
    print(rational1 * rational2)
    print(rational1 / rational2)


if __name__ == "__main__":
    main()
