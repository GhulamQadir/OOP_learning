import math

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        self.__x = new_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        self.__y = new_y

    def calculate_distance(self, other_point):
        x = (other_point.__x - self.__x) ** 2
        y = (other_point.__y - self.__y) ** 2
        distance = math.sqrt(x + y)
        return round(distance, 3)

    def __add__(self, other_point):
        x = self.__x + other_point.__x
        y = self.__y + other_point.__y
        return Point(x, y)

    def __sub__(self, other_point):
        x = self.__x - other_point.__x
        y = self.__y - other_point.__y
        return Point(x, y)

    def __str__(self):
        return f"P({self.__x}, {self.__y})"
