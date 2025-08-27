class WordCounter:
    """
    WordCounter class is responsible for taking an input string,
    processing it into words, and counting how many times each
    word occurs in the string.

    Attributes:
        __input_text (str): The raw input text provided by the user.
        __frequency_dict (dict): Stores words as keys and their corresponding frequencies as values.
        __keys_list (list): Stores keys from the frequency dictionary for iteration.
        __iter_index (int): Tracks current index during iteration
    """

    def __init__(self, input_text):
        """
        Initialize the WordCounter object.
        Args:
            input_text (str): The string input from which words will be counted.
        """
        # Save the original input text
        self.__input_text = input_text

        # Initialize an empty dictionary to store word frequencies
        self.__frequency_dict = {}

        # Keeps track of the current position while iterating.
        # Starts at -1 so the first call to __next__() moves it to 0.
        self.__iter_index = -1

        # Stores the list of words (keys) from the frequency dictionary.
        self.__keys_list = []

    @property
    def input_text(self):
        """
        Returns the cleaned (stripped) input text.
        This removes leading and trailing whitespaces before returning.
        """
        return self.__input_text.strip()

    @input_text.setter
    def input_text(self, updated_text):
        """
        Updates the input text and clears previously stored frequencies.
        """
        self.__input_text = updated_text
        self._clear_frequencies()
        self._clear_keys()

    @property
    def frequency_dict(self):
        """
        Returns the dictionary containing words and their frequencies.
        This will be empty until `count_occurrences()` is called.
        """
        return self.__frequency_dict

    # ---------------------------
    # Helpers
    # ---------------------------
    def _clear_frequencies(self):
        """Clears the frequency dictionary."""
        self.__frequency_dict.clear()

    def _refresh_keys(self):
        """Refreshes the key list from the frequency dictionary."""
        self.__keys_list = list(self.__frequency_dict.keys())

    def _clear_keys(self):
        """Clears the key list."""
        self.__keys_list.clear()

    # ---------------------------
    # Dunder methods for dict-like behavior
    # ---------------------------
    def __getitem__(self, key):
        """Allows dictionary-style access: wc['word'] → frequency."""
        return self.__frequency_dict[key]

    def __contains__(self, key):
        """Allows `word in wc` syntax."""
        return key in self.__frequency_dict

    def __len__(self):
        """Returns number of unique words."""
        return len(self.__frequency_dict)

    # ---------------------------
    # Iteration protocol
    # ---------------------------
    def __iter__(self):
        """
        Reset index and return self as an iterator.
        Enables looping over the object.
        """
        self.__iter_index = -1
        return self

    def __next__(self):
        """
        Returns the next {word: frequency} pair in iteration.
        Raises StopIteration when all items are exhausted.
        """
        if self.__iter_index < len(self) - 1:
            self.__iter_index += 1
            key = self.__keys_list[self.__iter_index]
            return {key: self.__frequency_dict[key]}
        raise StopIteration("Words Limit Reached")

    # ---------------------------
    # Word counting
    # ---------------------------
    def count_occurrences(self):
        """
        Counts how many times each word appears in the input text.

        Process:
            1. Splits the input text into a list of words.
            2. Iterates through each word in the list.
            3. Skips the word if it has already been counted.
            4. Otherwise, counts how many times it occurs in the rest of the list.
            5. Updates the frequency dictionary with the word and its count.

        Returns:
            dict: A dictionary where keys are words and values are their frequencies.
        """
        # Split input text into a list of words, ignoring extra spaces
        split_input_to_list = self.__input_text.strip().split()

        # Outer loop: iterate over each word
        for i, word in enumerate(split_input_to_list):
            # Start counting the word (initially 1 for the current word itself)
            occurrence_count = 1

            # Skip this word if already counted and stored in dictionary
            if word in self.__frequency_dict:
                continue

            # Inner loop: check the rest of the list for matches
            for _, next_word in enumerate(split_input_to_list[i + 1 :]):
                if word == next_word:
                    occurrence_count += 1

            # Save the final count of the word in the dictionary
            self.__frequency_dict[word] = occurrence_count

        # refresh the keys for updation
        self._refresh_keys()
        return self.__frequency_dict

    def __str__(self):
        """
        Provides a user-friendly string representation of the object.
        Displays:
            - The original input text (stripped).
            - The frequency dictionary showing word occurrences.
        """
        return f"String Input: {self.__input_text.strip()}\nOccurences of words: {self.__frequency_dict}"
