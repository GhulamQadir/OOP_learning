from polygon import Polygon
from polygon.point.point import Point
from math import pi, tan, isclose


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
            raise ValueError("Side length must be greater than zero")
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

    @classmethod
    def from_coordinates(
        cls,
        vertices: list[Point | tuple[float | int, float | int]],
        n=3,
        shape="Regular Polygon",
    ):
        if len(vertices) < n:
            raise ValueError(f"{shape} must have atleast {n} sides")
        formatted_vertices = [
            v if isinstance(v, Point) else Point(*v) for v in vertices
        ]
        distances = [
            cls.distance(
                formatted_vertices[i],
                formatted_vertices[(i + 1) % len(formatted_vertices)],
            )
            for i in range(len(formatted_vertices))
        ]

        for side in distances[1:]:
            if not round(distances[0], 3) == round(side, 3):
                raise ValueError(f"A {shape} must have all sides equal.")

        return cls(distances[0])

    def __str__(self):
        """Return a descriptive string of the polygon."""
        return f"RegularPolygon with number of sides = {self._num_of_sides} and sideLength = {self._side_length}"
