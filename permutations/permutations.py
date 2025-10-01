class Permutations:
    """
    Class to generate all possible arrangements (permutations) of a given set of characters
    and verify their uniqueness.

    Attributes:
        __original_text (str): The original string provided by the user.
        __unique_characters (list): Stores only the unique characters extracted from the input text.
        __permutations (list): Stores all generated permutations of the unique characters.
    """

    def __init__(self, original_text):
        """
        Initializes the class with the input text, validates it,
        extracts unique characters, and initializes an empty list for permutations.
        """
        self.__original_text = self._validate_input_text(original_text)
        self.__unique_characters = self._extract_unique_characters()
        self.__permutations = []

    def _validate_input_text(self, original_text):
        """
        Validates that the input text is not empty or just spaces.
        Args:
            original_text (str): The string provided by the user.
        Returns:
            str: A cleaned version of the input text (trimmed of spaces).
        - Raises: ValueError: If the input is empty or only contains whitespace.
        """
        clean_input = str(original_text).strip()
        if len(clean_input) < 1:
            raise ValueError("Input text cannot be blank or only spaces.")

        return clean_input

    def _extract_unique_characters(self):
        """
        Extracts unique characters from the input string without using Python's built-in 'set'.
        Returns:
            list: A list containing unique characters from the input text,
                  preserving their original order of appearance.
        """
        unique_chars = []
        for char in self.__original_text:
            already_checked = False
            for c in unique_chars:
                # Check if the character is already added to unique_chars
                if c == char:
                    already_checked = True
                    break

            # If not already in unique_chars, add it
            if not already_checked:
                for c in self.__original_text:
                    if c == char:
                        unique_chars.append(c)
                        break
        return unique_chars

    def factorial(self, n):
        """
        Computes the factorial of a non-negative integer n using recursion.
        Args:
            n (int): The number for which factorial will be calculated.
        Returns:
            int: Factorial of n (n!).

            - factorial(0) and factorial(1) both return 1.
            - If n < 0, returns None.
        """
        # n (int): Number to compute factorial for.
        if n == 0 or n == 1:
            return 1
        elif n < 0:
            return
        return n * self.factorial(n - 1)

    @property
    def original_text(self):
        """Getter for the original input text."""
        return self.__original_text

    @original_text.setter
    def original_text(self, updated_text):
        """
        Setter for updating the original input text.
        Args:
            updated_text (str): New input text to replace the old one.
        Effects:
            - Validates and stores the new text.
            - Resets previously generated permutations.
            - Updates the unique characters list.
        """
        self.__original_text = self._validate_input_text(updated_text)
        self.__permutations = []
        self.__unique_characters = self._extract_unique_characters()

    @property
    def unique_characters(self):
        """Getter for the list of unique characters from the input text."""
        return self.__unique_characters

    @property
    def permutations(self):
        """
        Getter for the list of permutations.
        Returns:
            list: All generated permutations of the unique characters.
        Notes:
            - If permutations have not yet been generated, they are computed.
            - Otherwise, the cached result is returned.
        """
        if self.__permutations == []:
            self.__permutations = self._generate_permutations()
        else:
            print("cached")  # Debugging: shows when cached result is reused
            pass
        return self.__permutations

    def _generate_permutations(self):
        """
        Generates all permutations of the unique characters.
        Process:
            1. Start with the first character as the initial permutation.
            2. For each subsequent character:
                - Insert it at every possible position in all current permutations.
                - Store the newly formed permutations in a temporary list.
            3. Update the main permutation list after processing each character.

        Returns:
            list: All possible permutations as strings.
        """
        permutations = [self.__unique_characters[0]]  # Start with the first char

        # Process each remaining character one by one
        for next_char in self.__unique_characters[1:]:
            updated_permutations = []  # Collect new permutations for this round

            for current_permutation in permutations:
                # Insert next_char at every possible position

                for i in range(len(current_permutation) + 1):
                    char_list = list(
                        current_permutation
                    )  # Convert string to list of characters
                    char_list.insert(i, next_char)  # Insert new character
                    new_permutation = "".join(char_list)  # Convert back to string
                    updated_permutations.append(
                        new_permutation
                    )  # Add to temporary list

            # Update the main permutations list after processing this character
            permutations = updated_permutations
        return permutations

    def verify_unique_permutations(self):
        """
        Verifies that all generated permutations are unique.
        Raises:
            ValueError: If duplicate permutations are detected.
        Notes:
            - Uses factorial to check expected count of unique permutations.
        """
        for current_permutation in self.__permutations:
            other_permutations = [
                remaining
                for remaining in self.__permutations
                if current_permutation != remaining
            ]
            expected_unique_count = self.factorial(len(self.__unique_characters))
            if expected_unique_count - 1 != len(other_permutations):
                raise ValueError("Duplicate permutations detected!")
        print("All generated permutations are unique!")

    def display(self):
        """Prints the list of generated permutations."""
        print(self.__permutations)

    def __str__(self):
        """
        Returns:
            str: Formatted string containing all permutations.
        """
        return f"All possible arrangements from the given string are:\n{self.__permutations}"
