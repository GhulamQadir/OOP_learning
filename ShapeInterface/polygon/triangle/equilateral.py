from polygon.triangle import Triangle
from math import sqrt


class EquilateralTriangle(Triangle):
    """
    Represents an equilateral triangle where all three sides are equal.

    Inherits from:
        Triangle

    Attributes:
        _sideA (float): Length of all three equal sides.
    """

    def __init__(self, side):
        super().__init__(side, side, side)

    def perimeter(self):
        """
        Calculates the perimeter of the equilateral triangle.
        Returns:
            float: The perimeter (3 × side), rounded to 3 decimal places.
        """
        super()._validate_triangle_sides()
        return super().perimeter()

    def area(self):
        """
        Calculates the area of the equilateral triangle.
        Formula:
            Area = (√3 / 4) × (side²)
        Returns:
            float: The area, rounded to 3 decimal places.
        """
        super()._validate_triangle_sides()
        return round(((sqrt(3) / 4) * (self._sideA**2)), 3)

    def __str__(self):
        """
        A description of the triangle with side length.
        """
        return f"Equilateral triangle with all sides equal to {self._sideA}"
