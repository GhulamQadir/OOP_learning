from polygon import Polygon
from math import pi, tan


class RegularPolygon(Polygon):
    """
    Represents a regular polygon where all sides and all angles are equal.

    Attributes:
        _side_length (float): Length of each side (must be > 0)
        _num_of_sides (int): Number of sides (must be >= 3)

    Formulas:
        Perimeter: P = n * s
        Area: A = (n * s^2) / (4 * tan(pi / n))
            where n = number of sides, s = side length
    """

    def __init__(self, side: int | float, n: int) -> None:
        """
        Initialize a regular polygon with side length and number of sides.
        Performs validation for positive side length and minimum sides.
        """
        self._side_length = self._validate_side_length(side)
        self._num_of_sides = self._validate_num_of_sides(n)

    def _validate_num_of_sides(self, n):
        # Ensure the polygon has at least 3 sides
        if n < 3:
            raise ValueError(f"Regular Polygon must be of atleast 3 sides")
        return n

    def _validate_side_length(self, side_length):
        # Ensure the side length is positive
        if side_length <= 0:
            raise ValueError(
                "Invalid number of sides: {n}. A regular polygon must have at least 3 sides."
            )
        return side_length

    @property
    def perimeter(self):
        """
        Calculate and return the perimeter: P = n * s
        """
        return self._num_of_sides * self._side_length

    @property
    def area(self):
        """
        Calculate and return the area using:
        A = (n * s^2) / (4 * tan(pi / n))
        Rounds result to 3 decimal places for readability.
        """
        return round(
            (self._num_of_sides * (self._side_length**2))
            / (4 * tan(pi / self._num_of_sides)),
            3,
        )

    def __str__(self):
        """Return a descriptive string of the polygon."""
        return f"RegularPolygon with number of sides = {self._num_of_sides} and sideLength = {self._side_length}"
