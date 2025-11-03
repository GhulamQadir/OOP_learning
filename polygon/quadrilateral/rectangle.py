from polygon import Polygon


class Rectangle(Polygon):
    """
    Represents a rectangle, a quadrilateral with opposite sides equal and all angles 90 degrees.
    """

    def __init__(self, length, width):
        # Ensure both sides are positive
        self._length = super()._check_positive_side(length)
        self._width = super()._check_positive_side(width)

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        Formula: P = 2 × (length + width)
        """
        return round(2 * (self._length + self._width), 3)

    def area(self):
        """
        Calculate the area of the rectangle.
        Formula: A = length × width
        """
        return round(self._length * self._width, 3)

    def __str__(self):
        """Return a descriptive string for the rectangle."""
        return f"Rectangle with length {self._length} and width {self._width}"
