from range import Range


def test():
    # Create a Range object r1 starting at 2, stopping before 14, with a step of 5
    r1 = Range(2, 14, 5)

    # Print the number of elements in r1
    print(len(r1))

    # Print the string representation of r1
    print(r1)

    # Iterate over r1 and print each element
    # Uses the Range iterator (__iter__ and __next__)
    for i in r1:
        print(i)  # Expected output: 2, 7, 12

    # Create another Range object r2 starting at 20, stopping before -5, with step -6
    r2 = Range(20, -5, -6)

    # Iterate over r2 and print each element
    for i in r2:
        print(i)  # Expected output: 20, 14, 8, 2, -4

    # Create a Range object r3 with a single argument (interpreted as stop=4, start=0, step=1)
    r3 = Range(4)

    # Manually create an iterator for r3
    it = iter(r3)

    # Use next() to get elements one by one from the iterator
    # Each call to next() returns the next element in the range
    print(next(it))  # Expected: 0
    print(next(it))  # Expected: 1
    print(next(it))  # Expected: 2
    print(next(it))  # Expected: 3
    # print(next(it))  # Stop Iteration Error!


if __name__ == "__main__":
    test()
