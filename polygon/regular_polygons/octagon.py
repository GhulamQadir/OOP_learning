from regular_polygons import Pentagon


class Octagon(Pentagon):
    """
    Represents a regular octagon (8 equal sides)
    Inherits from Pentagon class to reuse initialization and string method.
    """

    def __init__(self, side_length: int | float):
        super().__init__(side_length, n=8, shape="Octagon")
