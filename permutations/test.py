from permutations import Permutations


def test():
    # Create a Permutations object with the initial string "catdog"
    a1 = Permutations("catdog")

    # Generate and print permutations for the first time (computed fresh)
    print(a1.permutations)

    # Print again (should use cached result, not recompute)
    print(a1.permutations)

    # Update the original text to a new string "potato"
    # This automatically resets permutations and recalculates unique characters
    a1.original_text = "potato"

    # Generate and print permutations of "potato" (computed fresh)
    print(a1.permutations)

    # Print again (should use cached result now)
    print(a1.permutations)

    # Print the unique characters extracted from "potato"
    print(a1.unique_characters)

    # Print the current value of the original input string
    print(a1.original_text)

    # Verify that all generated permutations are unique
    a1.verify_unique_permutations()

    # Print object representation (string format with permutations list)
    print(a1)


if __name__ == "__main__":
    test()
