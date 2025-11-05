from abc import ABC, abstractmethod


class ShapeInterface(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
