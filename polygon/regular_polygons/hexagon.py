from regular_polygons import Pentagon


class Hexagon(Pentagon):
    """
    Represents a regular hexagon (6 equal sides)
    Inherits from Pentagon class to reuse initialization and string method.
    """

    def __init__(self, side_length: int | float):
        super().__init__(side_length, n=6, shape="Hexagon")
