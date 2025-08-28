from vector import Vector

def test():
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
    
    # printing vector using __str__ method
    print(v2)



if __name__ == "__main__":
    test()
