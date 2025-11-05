from polygon.regular_polygons import Pentagon


class Hexagon(Pentagon):
    """
    Represents a regular hexagon (6 equal sides)
    Inherits from Pentagon class to reuse initialization and string method.
    """

    def __init__(self, side_length: int | float):
        super().__init__(side_length, n=6, shape="Hexagon")

    @classmethod
    def from_coordinates(cls, vertices, n=5, shape="Hexagon"):
        return super().from_coordinates(vertices, n, shape)
