from abc import ABC, abstractmethod


class Polygon(ABC):
    """
    Abstract base class representing a general polygon.

    A polygon is a closed geometric figure made up of straight sides.
    This class defines the common structure that all specific polygon
    types (like Triangle, Rectangle, Square, etc.) should follow.

    Every polygon must be able to:
      - Calculate its area
      - Calculate its perimeter
    Subclasses that inherit from Polygon must implement these abstract methods.
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
