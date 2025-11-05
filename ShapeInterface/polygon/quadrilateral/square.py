from polygon import Polygon
from polygon.quadrilateral.rectangle import Rectangle
from polygon.point.point import Point


class Square(Rectangle):
    """
    Represents a square, a special type of rectangle where all sides are equal.
    """

    def __init__(self, side):
        super().__init__(side, side)

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
        if not (ab == bc and ab == cd and ab == da):
            raise ValueError("All sides of a square must be equal")

        return cls(ab)

    def __str__(self):
        """Return a descriptive string for the square."""
        return f"Square with all sides equal to {self._length}"
