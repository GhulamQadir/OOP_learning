from vector.vector import Vector2d
from point.point import Point
from rational_number.rational_number import RationalNumber
from random_utilities.random_utilities import RandomUtilities


def main():
    ########### Point Class ############
    # p1 = Point(2, 3)
    # p2 = Point(4, 5)
    # p3 = p1 + p2

    ############# 2D Vector Class ############
    # vector1 = Vector2d(2, 3)
    # print(vector1.coords)
    # vector1.coords = Point(3, 4)
    # print(vector1.coords)
    # print(vector1)

    # vector2 = Vector2d(4, 5)

    # print(vector1 + vector2)
    # print(vector1 - vector2)

    # print(vector2.magnitude)

    ############ Rational Number Class ##############
    # rational1 = RationalNumber(2, -28)
    # rational2 = RationalNumber(-6, 9)
    # print(rational1)
    # print(rational2)
    # print(rational1 + rational2)
    # print(rational1 - rational2)
    # print(rational1 * rational2)
    # print(rational1 / rational2)

    # # parsing rational number as str
    # rational3 = RationalNumber("2/6")
    # rational4 = RationalNumber("1/3")
    # print(rational3 == rational4)

    # # parsing null constructor
    # null_rational = RationalNumber()
    # print(null_rational)

    # # parsing list in rational number
    # rational5 = RationalNumber([6, 18])
    # print(rational5)

    # # parsing tuple in rational number
    # rational6 = RationalNumber((15, 40))
    # print(rational6)

    ################## Random Utilities Class ###############
    r1 = RandomUtilities()

    prog_languages = [
        "Java",
        "Python",
        "C",
        "C#",
        "Kotlin",
        "Rust",
        "R",
    ]

    #### Shuffle Example ####
    shuffled_list1 = r1.shuffle(prog_languages)
    print(shuffled_list1)

    # shuffled_list1 = r1.shuffle("python") # TypeError
    # print(shuffled_list1)

    #### Choice Example  ####
    random_element1 = r1.choice(range(10))  # range type
    print(random_element1)

    random_element2 = r1.choice(prog_languages)  # list type
    print(random_element2)

    random_element3 = r1.choice(("Object-Oriented"))  # string type
    print(random_element3)

    random_element4 = r1.choice(("Springboot", "Java"))  # tuple type
    print(random_element4)

    # random_element4 = r1.choice({"name":"abc"}) # TypeError
    # print(random_element4)


if __name__ == "__main__":
    main()
