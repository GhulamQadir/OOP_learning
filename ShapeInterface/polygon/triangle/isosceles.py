from polygon.triangle import Triangle
from math import sqrt


class IsoscelesTriangle(Triangle):
    """
    Represents an isosceles triangle (two equal sides and one base).

    Inherits from:
        Triangle

    Attributes:
        _sideA (float): Length of the two equal sides (legs).
        __base (float): Length of the base side.
    """

    def __init__(self, legs, base):
        super().__init__(legs, legs, base)
        self.__base = super()._check_positive_side(base)

    def _validate_triangle_sides(self):
        """
        Validates the isosceles triangle inequality.
        Rule:
            Sum of the two equal sides must be greater than the base.
        Raises:
            ValueError: If the sides do not satisfy the inequality.
        """
        if not (2 * self._sideA) > self.__base:
            raise ValueError(
                "Invalid isosceles triangle: sum of two equal sides must be greater than the base."
            )

    def perimeter(self):
        """
        Calculates the perimeter of the isosceles triangle.
        Returns:
            float: The perimeter, rounded to 3 decimal places.
        """
        self._validate_triangle_sides()
        return round(((2 * self._sideA) + self.__base), 3)

    def area(self):
        """
        Calculates the area of the isosceles triangle.
        Formula:
            height = √(leg² - (base² / 4))
            Area = (base × height) / 2
        Returns:
            float: The area, rounded to 3 decimal places.
        """
        self._validate_triangle_sides()
        height = sqrt((self._sideA**2) - ((self.__base**2) / 4))
        return round(((self.__base * height) / 2), 3)

    def __str__(self):
        """
        A description with equal side and base lengths.
        """
        return (
            f"Isosceles Triangle with equal sides {self._sideA} and base {self.__base}"
        )
