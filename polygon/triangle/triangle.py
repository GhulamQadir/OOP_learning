from polygon import Polygon
from math import sqrt


class Triangle(Polygon):
    """
        Represents a general triangle defined by three side lengths.

    Inherits from:
        Polygon

    Attributes:
        _sideA (float): Length of the first side.
        _sideB (float): Length of the second side.
        _sideC (float): Length of the third side.
    """

    def __init__(self, sideA, sideB, sideC):
        self._sideA = self._check_positive_side(sideA)
        self._sideB = self._check_positive_side(sideB)
        self._sideC = self._check_positive_side(sideC)

    def _check_positive_side(self, side):
        """
        Ensures that a given side length is positive.
        Raises:
            ValueError: If the side is zero or negative.
        """

        if side <= 0:
            raise ValueError("Side length must be greater than zero.")
        return side

    def _validate_triangle_sides(self):
        """
        Validates the triangle inequality rule.

        The sum of any two sides must be greater than the third side.
        If violated, the triangle cannot exist geometrically.

        Raises:
            ValueError: If triangle inequality is not satisfied.
        """
        a = self._sideA + self._sideB
        b = self._sideB + self._sideC
        c = self._sideC + self._sideA
        if not (a > self._sideC and b > self._sideA and c > self._sideB):
            raise ValueError(
                "Triangle inequality violated: sum of any two sides must be greater than the third."
            )

    def perimeter(self):
        """
        Calculates the perimeter of the triangle.

        Returns:
            float: The perimeter, rounded to 3 decimal places.
        """
        self._validate_triangle_sides()
        return round((self._sideA + self._sideB + self._sideC), 3)

    def area(self):
        """
        Calculates the area of the triangle using Heron's formula.

        Formula:
            s = (a + b + c) / 2
            Area = √[s(s - a)(s - b)(s - c)]

        Returns:
            float: The area, rounded to 2 decimal places.
        """
        self._validate_triangle_sides()
        semi_perimeter = (self._sideA + self._sideB + self._sideC) / 2
        area = sqrt(
            semi_perimeter
            * (semi_perimeter - self._sideA)
            * (semi_perimeter - self._sideB)
            * (semi_perimeter - self._sideC)
        )
        return round(area, 2)

    def __str__(self):
        """
        A description of the triangle with side lengths.
        """
        return f"Triangle with sides {self._sideA}, {self._sideB}, and {self._sideC}"
