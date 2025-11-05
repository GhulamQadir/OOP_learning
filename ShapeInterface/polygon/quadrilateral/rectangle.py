from polygon.polygon import Polygon
from polygon.point.point import Point


class Rectangle(Polygon):
    """
    Represents a rectangle, a quadrilateral with opposite sides equal and all angles 90 degrees.
    """

    def __init__(self, length, width):
        # Ensure both sides are positive
        self._length = super()._check_positive_side(length)
        self._width = super()._check_positive_side(width)

    @property
    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        Formula: P = 2 × (length + width)
        """
        return round(2 * (self._length + self._width), 3)

    @property
    def area(self):
        """
        Calculate the area of the rectangle.
        Formula: A = length × width
        """
        return round(self._length * self._width, 3)

    @classmethod
    def from_coordinates(cls, vertices: list[Point | tuple[float | int, float | int]]):
        if len(vertices) < 4:
            raise ValueError("Quadrilateral must have atleast four sides")
        formatted_vertices = [
            v if isinstance(v, Point) else Point(*v) for v in vertices
        ]
        distances = (
            cls.distance(
                formatted_vertices[i],
                formatted_vertices[(i + 1) % len(formatted_vertices)],
            )
            for i in range(len(formatted_vertices))
        )

        ab, bc, cd, da = distances
        if not (ab == cd and bc == da):
            raise ValueError("Opposite sides should be equal")

        return cls(ab, bc)

    def __str__(self):
        """Return a descriptive string for the rectangle."""
        return f"Rectangle with length {self._length} and width {self._width}"
