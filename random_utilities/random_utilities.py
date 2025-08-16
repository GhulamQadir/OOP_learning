from random import Random


class RandomUtilities:
    def __init__(self):
        # Step 1: Create a new Random instance.
        # This ensures that our class has its own independent random generator,
        # so it will not interfere with the global random module calls.
        self.r = Random()

    def shuffle(self, data: list):
        # Step 0: Validate input
        # Ensure the input is a list. If not, raise a TypeError.
        if not isinstance(data, list):
            raise TypeError("shuffle() expects a list as input")

        # Check if the list is empty. Shuffling an empty list makes no sense,
        # so raise an IndexError (similar to random.choice behavior).
        if len(data) == 0:
            raise IndexError("Cannot choose from an empty sequence")

        # Step 1: Create a new empty list with the same length as 'data'
        # This will store the shuffled result. Initially, it is filled with None.
        shuffled_list = [None] * len(data)

        # Step 2: Create a list of boolean flags, one for each index.
        # 'False' means the index is empty, 'True' means it is already filled.
        flags = [False] * len(data)

        # Step 3: Place each element of the original list at a random index
        for element in data:
            index_matched = (
                False  # This flag ensures we keep trying until an empty slot is found
            )
            while not index_matched:
                # Generate a random index between 0 and len(data)-1
                random_index = self.r.randint(0, len(data) - 1)

                # If this index is not filled yet, place the element here
                if flags[random_index] == False:
                    shuffled_list[random_index] = (
                        element  # Insert the element at this index
                    )

                    flags[random_index] = True  # Mark the index as filled
                    index_matched = True  # Exit the loop and move to next element
        return shuffled_list

    def choice(self, data):
        # Step 1: Validate input type.
        # The function only works with sequences: list, tuple, string, or range.
        # If the user passes anything else (like int, dict, or set), raise a TypeError.
        if not isinstance(data, (list, tuple, str, range)):
            raise TypeError("choice() expects a sequence (list, tuple, str, or range)")

        # Step 2: Check if the sequence is empty.
        # Choosing a random element from an empty sequence is impossible,
        # so we raise an IndexError to inform the user about this.
        if len(data) == 0:
            raise IndexError("Cannot choose from an empty sequence")

        # Step 3: Generate a random valid index.
        # randrange(len(data)) gives a random index between 0 and len(data)-1.
        random_index = self.r.randrange(len(data))

        # Step 4: Return the element at the chosen random index.
        return data[random_index]
