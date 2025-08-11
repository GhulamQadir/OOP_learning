from point.point import Point
from math import sqrt


class Vector2d:
    def __init__(self, x, y):
        self.__coords = Point(x, y)
        self.__magnitude = 0

    @property
    def coords(self):
        return (self.__coords.x, self.__coords.y)

    @coords.setter
    def coords(self, new_coords):
        if isinstance(new_coords, Point):
            self.__coords = new_coords
        elif isinstance(new_coords, (tuple, list)) and len(new_coords) == 2:
            self.__coords = Point(new_coords[0], new_coords[1])
        else:
            raise TypeError(
                "Coordinates must be of type Point class or a tuple/list of length 2"
            )

    @property
    def magnitude(self):
        return round(sqrt(self.__coords.x**2 + self.__coords.y**2), 3)

    def __add__(self, other):
        if not isinstance(other, Vector2d):
            raise TypeError("Other operand must be of type Vector2d")
        new_vector = self.__coords + other.__coords
        return Vector2d(new_vector.x, new_vector.y)

    def __sub__(self, other):
        if not isinstance(other, Vector2d):
            raise TypeError("Other operand must be of type Vector2d")
        new_vector = self.__coords - other.__coords
        return Vector2d(new_vector.x, new_vector.y)

    def __str__(self):
        return f"Vector({self.__coords.x}, {self.__coords.y})"
