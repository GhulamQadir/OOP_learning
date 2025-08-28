from birthday_paradox import BirthdayParadox


def test():
    # Create a BirthdayParadox object with 5 people initially
    paradox1 = BirthdayParadox(5)

    # Test probability of shared birthdays for different group sizes
    # We loop from 5 people up to 100 people (step = 5)
    # For each group size, we run the simulation (default 1000 trials)
    # and print the probability of at least two people sharing a birthday
    people_counts = [i for i in range(5, 101, 5)]
    for count in people_counts:
        paradox1.people_count = count  # update group size
        percentage = paradox1.paradox_percentage()  # run simulation
        print(f"People Count: {count}, Percentage: {percentage}")

    # Create another BirthdayParadox object with 23 people
    paradox2 = BirthdayParadox(23)

    # Reduce the number of trials to 500 (faster, but less accurate)
    paradox2.testing_range = 500

    # Run the simulation for 23 people and print probability
    print(
        f"People Count: {paradox2.people_count}, Percentage: {paradox2.paradox_percentage()}"
    )

    # Print object summary (uses __str__ method in BirthdayParadox)
    print(paradox2)


if __name__ == "__main__":
    test()
