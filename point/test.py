from point import Point


def test():
    # Create two Point objects with given coordinates
    p1 = Point(2, 3)
    p2 = Point(4, 5)

    # Access attributes using getters (property methods)
    # This will call the @property methods and print x of p1 and y of p2
    print(p1.x)
    print(p2.y)

    # Add two points using overloaded __add__ method
    # This creates a new Point whose x and y are sums of p1 and p2
    p3 = p1 + p2
    print(p3)

    # Modify x of p2 and y of p1 using property setters
    p2.x = 12  # p2 becomes (12, 5)
    p1.y = 8  # p1 becomes (2, 8)

    # Subtract two points using overloaded __sub__ method
    # This creates a new Point whose x and y are differences of p2 and p1
    p4 = p2 - p1
    print(p4)  # Expected: P(10, -3)


# Ensure test() only runs when this file is executed directly
if __name__ == "__main__":
    test()
