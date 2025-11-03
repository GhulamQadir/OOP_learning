from polygon import Polygon
from quadrilateral.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, a special type of rectangle where all sides are equal.
    """

    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        """Return a descriptive string for the square."""
        return f"Square with all sides equal to {self._length}"
