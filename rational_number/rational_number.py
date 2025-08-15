class RationalNumber:
    def __init__(self, numerator=0, denominator=1):
        """
        Initialize a RationalNumber in simplified form with a positive denominator.

        Args:
            numerator (int): The numerator of the rational number. Defaults to 0.
            denominator (int): The denominator of the rational number. Defaults to 1.

        Raises:
            ZeroDivisionError: If the denominator is zero.
        """
        # Ensure denominator is not zero
        self._validate_denominator(denominator)

        # Normalize signs so denominator is always positive
        numerator, denominator = self._normalize_signs(numerator, denominator)

        # Simplify the fraction and store as immutable private attributes
        self.__numerator, self.__denominator = self._simplified_fraction(
            numerator, denominator
        )

    # Read-only property for denominator
    @property
    def denominator(self):
        """Return the denominator of the rational number."""
        return self.__denominator

    # Read-only property for numerator
    @property
    def numerator(self):
        """Return the numerator of the rational number."""
        return self.__numerator

    def _normalize_signs(self, numerator, denominator):
        """
        Normalize signs so that the denominator is always positive.
        If the denominator is negative, multiply both numerator and denominator by -1.
        """
        if denominator < 0:
            denominator *= -1
            numerator *= -1
        return numerator, denominator

    def _validate_denominator(self, denominator):
        """
        Validate that the denominator is not zero.
        Raises:
            ZeroDivisionError: If the denominator is zero.
        """
        if denominator == 0:
            raise ZeroDivisionError("Denominator should not be zero")
        return denominator

    def _find_gcd(self, num1, num2):
        """
        Find the greatest common divisor (GCD) of two integers using a basic method.

        Args:
            num1 (int): First integer.
            num2 (int): Second integer.

        Returns:
            int: The greatest common divisor of num1 and num2.
        """
        num1 = abs(num1)
        num2 = abs(num2)

        smaller_num = num1
        greatest_common_divisor = 1

        # Identify smaller number
        if num1 > num2:
            smaller_num = num2

        # Directly return smaller number if it divides both
        if num1 % smaller_num == 0 and num2 % smaller_num == 0:
            greatest_common_divisor = smaller_num
            return greatest_common_divisor
        else:
            # Check divisors up to half of the smaller number
            half_of_small_num = smaller_num // 2
            for i in range(2, half_of_small_num + 1):
                if num1 % i == 0 and num2 % i == 0:
                    greatest_common_divisor = i

            return greatest_common_divisor

    def _simplified_fraction(self, numerator, denominator):
        """
        Simplify a fraction by dividing numerator and denominator by their GCD.
        Args:
            numerator (int): Fraction numerator.
            denominator (int): Fraction denominator.
        Returns:
            tuple: (simplified_numerator, simplified_denominator)
        """
        greatest_common_divisor = self._find_gcd(numerator, denominator)
        simplified_numerator = numerator // greatest_common_divisor
        simplified_denominator = denominator // greatest_common_divisor

        return simplified_numerator, simplified_denominator

    def __add__(self, other):
        """
        Add two RationalNumber objects and return the result as a new RationalNumber.
        """
        numerator = (self.__numerator * other.denominator) + (
            self.__denominator * other.numerator
        )
        denominator = self.__denominator * other.denominator

        return RationalNumber(numerator, denominator)

    def __sub__(self, other):
        """
        Subtract another RationalNumber from this one and return the result.
        """
        numerator = (self.__numerator * other.denominator) - (
            self.__denominator * other.numerator
        )
        denominator = self.__denominator * other.denominator

        return RationalNumber(numerator, denominator)

    def __mul__(self, other):
        """
        Multiply two RationalNumber objects and return the result.
        """
        numerator = self.__numerator * other.numerator
        denominator = self.__denominator * other.denominator

        return RationalNumber(numerator, denominator)

    def __truediv__(self, other):
        """
        Divide this RationalNumber by another and return the result.
        """
        numerator = self.__numerator * other.denominator
        denominator = self.__denominator * other.numerator

        return RationalNumber(numerator, denominator)

    def __str__(self):
        """
        Return string representation of the rational number in 'numerator/denominator' format.
        """
        return f"{self.__numerator}/{self.denominator}"
