from vector.vector import Vector
from point.point import Point
from rational_number.rational_number import RationalNumber
from random_utilities.random_utilities import RandomUtilities
from range.range import Range


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
    # r1 = RandomUtilities()

    # prog_languages = [
    #     "Java",
    #     "Python",
    #     "C",
    #     "C#",
    #     "Kotlin",
    #     "Rust",
    #     "R",
    # ]

    # #### Shuffle Example ####
    # shuffled_list1 = r1.shuffle(prog_languages)
    # print(shuffled_list1)

    # shuffled_list1 = r1.shuffle("python") # TypeError
    # print(shuffled_list1)

    # #### Choice Example  ####
    # random_element1 = r1.choice(range(10))  # range type
    # print(random_element1)

    # random_element2 = r1.choice(prog_languages)  # list type
    # print(random_element2)

    # random_element3 = r1.choice(("Object-Oriented"))  # string type
    # print(random_element3)

    # random_element4 = r1.choice(("Springboot", "Java"))  # tuple type
    # print(random_element4)

    # random_element4 = r1.choice({"name":"abc"}) # TypeError
    # print(random_element4)

    ############## VECTOR ####################

    # Create a vector v1 with 3 dimensions
    v1 = Vector(3)

    # Set elements of v1
    v1[0] = 1  # Set first element to 1
    v1[1] = 2  # Set second element to 2
    v1[2] = 3  # Set third element to 3

    # Create another vector v2 with 3 dimensions
    v2 = Vector(3)

    # Set elements of v2
    v2[0] = 2  # Set first element to 2
    v2[1] = 4  # Set second element to 4
    v2[2] = 1  # Set third element to 1

    # Print magnitude (length) of vector v1
    print("Magnitude-->", v1.magnitude)

    # Print the unit vector (direction vector with magnitude = 1) of v1
    print("Unit Vector-->", v1.unit_vector)

    # Calculate and print distance between v2 and v1
    print("Distance-->", v2.distance(v1))

    # Calculate and print dot product of v1 and v2
    print("DotProduct-->", v1.dot_product(v2))

    # Calculate and print addition of vectors v2 + v1
    print("Addition-->", v2 + v1)

    # Calculate and print subtraction of vectors v1 - v2
    print("Subtraction-->", v1 - v2)

    # Access and print the second element of v1
    print("Access element-->", v1[1])

    # Update second element of v2
    v2[1] = 8

    # Check and print the updated second element of v2
    print("Check Updated element-->", v2[1])

    # Print the length (number of dimensions) of v2
    print("Length of vector", len(v2))

    ############ Range Class ####################
    ###### Built-in range class
    # r = range(2, 90, 4)
    # print(type(r))
    # print(r)
    # print(len(r))
    # print(r[8])

    # ###### Custom Range Class

    # # Create a Range object r1 starting at 2, stopping before 14, with a step of 5
    # r1 = Range(2, 14, 5)

    # # Print the number of elements in r1
    # print(len(r1))

    # # Print the string representation of r1
    # print(r1)

    # # Iterate over r1 and print each element
    # # Uses the Range iterator (__iter__ and __next__)
    # for i in r1:
    #     print(i)  # Expected output: 2, 7, 12

    # # Create another Range object r2 starting at 20, stopping before -5, with step -6
    # r2 = Range(20, -5, -6)

    # # Iterate over r2 and print each element
    # for i in r2:
    #     print(i)  # Expected output: 20, 14, 8, 2, -4

    # # Create a Range object r3 with a single argument (interpreted as stop=4, start=0, step=1)
    # r3 = Range(4)

    # # Manually create an iterator for r3
    # it = iter(r3)

    # # Use next() to get elements one by one from the iterator
    # # Each call to next() returns the next element in the range
    # print(next(it))  # Expected: 0
    # print(next(it))  # Expected: 1
    # print(next(it))  # Expected: 2
    # print(next(it))  # Expected: 3
    # print(next(it))  # Stop Iteration Error!


if __name__ == "__main__":
    main()
