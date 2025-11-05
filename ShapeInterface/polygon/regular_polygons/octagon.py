from polygon.regular_polygons import Pentagon


class Octagon(Pentagon):
    """
    Represents a regular octagon (8 equal sides)
    Inherits from Pentagon class to reuse initialization and string method.
    """

    def __init__(self, side_length: int | float):
        super().__init__(side_length, n=8, shape="Octagon")

    @classmethod
    def from_coordinates(cls, vertices, n=8, shape="Octagon"):
        return super().from_coordinates(vertices, n, shape)
