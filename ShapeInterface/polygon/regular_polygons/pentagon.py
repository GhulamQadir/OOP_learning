from polygon.regular_polygons import RegularPolygon


class Pentagon(RegularPolygon):
    """
    Represents a regular pentagon (5 equal sides).
    Can also be used as a base class for other regular polygons
    by passing a different number of sides.
    """

    def __init__(self, side_length: int | float, n=5, shape="Pentagon"):
        """
        side_length (float): Length of each side
        n (int): Number of sides, default=5
        shape (str): Name of the polygon for descriptive output
        """

        super().__init__(side_length, n)
        self.__shape = shape

    @classmethod
    def from_coordinates(cls, vertices, n=5, shape="Pentagon"):
        return super().from_coordinates(vertices, n, shape)

    def __str__(self):
        """Return descriptive string including shape, side length, area, and perimeter."""
        return f"{self.__shape} with sideLength = {self._side_length}, area = {self.area}, and perimeter = {self.perimeter}"
