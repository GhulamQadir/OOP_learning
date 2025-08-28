from random_utilities import RandomUtilities


def test():
    # Creating instance of RandomUtilities class
    r1 = RandomUtilities()

    # A sample list of programming languages to test shuffle and choice methods
    prog_languages = [
        "Java",
        "Python",
        "C",
        "C#",
        "Kotlin",
        "Rust",
        "R",
    ]

    ######## Shuffle Example #######
    # Shuffle the list of programming languages.
    # Expected: A new list with the same elements in random order.
    shuffled_list1 = r1.shuffle(prog_languages)
    print(shuffled_list1)

    # # Trying to shuffle a string instead of a list.
    # # Expected: TypeError (because shuffle only works with mutable sequences like lists).
    # shuffled_list1 = r1.shuffle("python")  # TypeError
    # print(shuffled_list1)

    ####### Choice Example  #######
    # Select a random element from a range (iterable of numbers from 0–9).
    random_element1 = r1.choice(range(10))  # range type
    print(random_element1)

    # Select a random element from a list (prog_languages).
    random_element2 = r1.choice(prog_languages)  # list type
    print(random_element2)

    # Select a random character from a string.
    # Example: could return 'O', 'b', or any other character from "Object-Oriented".
    random_element3 = r1.choice(("Object-Oriented"))  # string type
    print(random_element3)

    # Select a random element from a tuple.
    # Example: could return "Springboot" or "Java".
    random_element4 = r1.choice(("Springboot", "Java"))  # tuple type
    print(random_element4)

    # # Trying to select a random element from a dictionary (unsupported type).
    # # Expected: TypeError (since choice doesn’t support dictionaries).
    # random_element4 = r1.choice({"name": "abc"})  # TypeError
    # print(random_element4)


if __name__ == "__main__":
    test()
