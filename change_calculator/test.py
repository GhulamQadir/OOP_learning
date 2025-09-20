from change_calc import ChangeCalculator


def test():
    # Create an instance of ChangeCalculator with charged amount 3000 and given amount 5057
    c1 = ChangeCalculator(3000, 5057)

    # Get the calculated change as a dictionary from the 'change' property
    change = c1.change

    print(change)  # Print the raw dictionary showing denomination breakdown

    # Print the ChangeCalculator object using its __str__ method,
    # which shows charged amount, given amount, and the formatted change string.
    print(c1)

    # Display the change in a human-readable format
    c1.display_change()

    # Update the charged amount to 600 using the setter
    c1.amount_charged = 600

    # Displays the updated change
    c1.display_change()

    # Uncommenting this block will raise an error because the given amount is negative
    # c2 = ChangeCalculator(3000, -5058)
    # change = c2.change
    # c2.display_change()


if __name__ == "__main__":
    test()
