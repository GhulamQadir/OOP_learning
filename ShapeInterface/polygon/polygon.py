from shape_interface import ShapeInterface
from math import sqrt


class Polygon(ShapeInterface):
    """
    Abstract base class representing a general polygon.

    A polygon is a closed geometric figure made up of straight sides.
    This class defines the common structure that all specific polygon
    types (like Triangle, Rectangle, Square, etc.) should follow.

    Every polygon must be able to:
      - Calculate its area
      - Calculate its perimeter
    Subclasses that inherit from Polygon must implement these abstract methods.
    """

    def area(self):
        pass

    def perimeter(self):
        pass

    @staticmethod
    def distance(p1, p2):
        return sqrt((p2._x - p1._x) ** 2 + (p2._y - p1._y) ** 2)

    def _check_positive_side(self, side):
        """
        Ensures that a given side length is positive.
        Raises:
            ValueError: If the side is zero or negative.
        """
        if side <= 0:
            raise ValueError("Side length must be greater than zero.")
        return side
