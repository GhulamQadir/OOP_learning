class ChangeCalculator:
    """
    A class to calculate the change that needs to be returned
    when a customer gives more money than the charged amount.

    The class uses available currency denominations (notes/coins)
    to provide a breakdown of how the change should be given
    in the least number of units possible.
    """

    def __init__(self, charged_amount, given_amount):
        """
        Initialize the ChangeCalculator with charged and given amounts.

        Parameters:
        charged_amount (int): The total cost of the product/service.
        given_amount   (int): The amount of money provided by the customer.
        """

        # Validate and store the charged and given amounts as private variables
        self.__amount_charged = self._charged_amount_validator(
            charged_amount, given_amount
        )
        self.__amount_given = self._given_amount_validator(given_amount, charged_amount)

        # Available currency denominations (notes and coins) in descending order
        self.__denominations = (5000, 1000, 500, 100, 50, 20, 10, 5, 2, 1)

    # getter for denominations
    @property
    def denominations(self):
        return self.__denominations

    # Getter and Setter for charged amount
    @property
    def amount_charged(self):
        """Return the charged amount."""
        return self.__amount_charged

    @amount_charged.setter
    def amount_charged(self, new_charged_amount):
        """Validate and update the charged amount."""
        self.__amount_charged = self._charged_amount_validator(
            new_charged_amount, self.__amount_given
        )

    # Getter and Setter for given amount
    @property
    def amount_given(self):
        """Return the given amount."""
        return self.__amount_given

    @amount_given.setter
    def amount_given(self, new_given_amount):
        """Validate and update the given amount."""
        self.__amount_given = self._given_amount_validator(
            new_given_amount, self.__amount_charged
        )

    def _charged_amount_validator(self, charged_amount, given_amount):
        """
        Validate the charged amount.
        Raises:
            TypeError: If charged_amount is not an integer.
            ValueError: If charged_amount is negative or greater than given_amount.
        """
        # Raise an error if the charged_amount is not an integer
        if not isinstance(charged_amount, int):
            raise TypeError("charged_amount must be an integer (whole rupee value).")

        # Raise an error if the charged_amount is greater than the given_amount
        # because the customer cannot give less than the charged amount
        if charged_amount > given_amount:
            raise ValueError("charged_amount cannot be greater than given_amount")

        # Raise an error if the charged_amount is negative
        # as the cost of a product/service cannot be negative
        if charged_amount < 0:
            raise ValueError("charged_amount must be non-negative integer value.")

        # If all checks pass, return the validated charged_amount
        return charged_amount

    def _given_amount_validator(self, given_amount, charged_amount):
        """
        Validate the given amount.
        Raises:
            TypeError: If given_amount is not an integer.
            ValueError: If given_amount is negative.
        """
        if not isinstance(given_amount, int):
            raise TypeError("given_amount must be an integer (whole rupee value).")

        if given_amount < charged_amount:
            raise ValueError("given_amount cannot be less than charged_amount")

        return given_amount

    # Change Calculation Property
    @property
    def change(self):
        """
        Calculate the change breakdown in terms of available denominations.

        Returns:
        dict: A dictionary where the keys are denominations
              and the values are the count of each denomination used.
        """
        # Total change to return
        remaining_change = self.__amount_given - self.__amount_charged

        # Dictionary to store the breakdown of change
        change_breakdown = {}

        # Iterate through each denomination
        for denomination in self.__denominations:
            # If no change left, exit early
            if remaining_change < 1:
                break

            # Find how many notes/coins of this denomination can be used
            num_of_units = remaining_change // denomination

            # Add only if this denomination is used
            if num_of_units > 0:
                change_breakdown[denomination] = num_of_units

                # Update remaining change
                remaining_change %= denomination
        return change_breakdown

    def _get_punctuation(self, current_index, keys_length):
        """
        Return a separator: comma if more items follow, else period.
        """
        # If not the last item, use a comma, otherwise a full stop
        if current_index < keys_length - 1:
            return ","
        return "."

    def _format_denomination(self, denomination, quantity):
        """
        Format a denomination into 'note' or 'coin' with its count.
        """
        # Notes are 10 or above, coins are less than 10
        phrase = f" {quantity} note/s of {denomination}"
        if denomination < 10:
            phrase = f" {quantity} coin/s of {denomination}"
        return phrase

    def _format_change_string(self):
        # Store the change breakdown in a local variable to avoid
        # recalculating the property multiple times
        change = self.change

        # Convert dict keys to tuple so we can check positions with .index()
        keys_sequence = tuple(change.keys())

        # Start building the output sentence
        message = "You have"
        for denomination, quantity in change.items():
            # Add formatted denomination (note/coin + count)
            message += self._format_denomination(denomination, quantity)

            # Add proper punctuation depending on position
            current_index = keys_sequence.index(denomination)
            message += self._get_punctuation(current_index, len(keys_sequence))

        return message

    def display_change(self):
        """
        Print a human-readable sentence of the change.
        """
        print(self._format_change_string())

    def __str__(self):
        """
        Return a formatted string representation of the ChangeCalculator object,
        including charged amount, given amount, and detailed change breakdown.
        """
        return (
            f"Charged Amount: {self.__amount_charged}\n"
            f"Given Amount: {self.__amount_given}\n"
            f"Cash Back: {self._format_change_string()}"
        )
