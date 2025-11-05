from polygon import (
    Triangle,
    EquilateralTriangle,
    IsoscelesTriangle,
    Square,
    Rectangle,
    RegularPolygon,
    Pentagon,
    Hexagon,
    Octagon,
)

# from polygon import Square, Rectangle
# from polygon import RegularPolygon, Pentagon, Hexagon, Octagon


def test():
    # t = Triangle(2, 1, 2)
    # t.area()

    # eq = EquilateralTriangle(4)
    # print(eq.perimeter())
    # print(eq.area())

    # isosceles = IsoscelesTriangle(4, 2)
    # print(isosceles.perimeter())
    # print(isosceles.area())

    # sq = Square(5)
    # sq.area()
    # sq.perimeter()
    # print(sq)

    # rectangle = Rectangle(10, 12)
    # rectangle.area()
    # rectangle.perimeter()
    # print(rectangle)

    # reg_polygon = RegularPolygon(5, 7)
    # print(
    #     f"RegularPolygon --> Area: {reg_polygon.area}, Perimeter: {reg_polygon.perimeter}\n"
    # )

    # p = Pentagon(4)
    # print(f"Pentagon --> Area: {p.area}, Perimeter: {p.perimeter}")
    # print(p)

    # h = Hexagon(7)
    # print(f"\nHexagon --> Area: {h.area}, Perimeter: {h.perimeter}")
    # print(h)

    # o = Octagon(11)
    # print(f"\nOctagon --> Area: {o.area}, Perimeter: {o.perimeter}")
    # print(o)

    t = Triangle.from_coordinates([(2, 3), (4, 5), (7, 9)])
    print(f"({t._sideA}, {t._sideB}, {t._sideC})")
    print(t.area)
    print(t.perimeter)

    # rectangle = Rectangle.from_coordinates([(7, 8), (12, 3), (9, 9), (12, 19)]) # side length error
    rectangle = Rectangle.from_coordinates(
        [(0, 0), (4, 0), (4, 3), (0, 3)]  # A  # B  # C  # D
    )
    print(rectangle.area)
    print(rectangle.perimeter)

    square = Square.from_coordinates([(0, 0), (2, 0), (2, 2), (0, 2)])
    print(square.area)  # 4
    print(square.perimeter)  # 8

    # Pentagon (regular)
    pentagon_points = [
        (1.0000, 0.0000),
        (0.3090, 0.9511),
        (-0.8090, 0.5878),
        (-0.8090, -0.5878),
        (0.3090, -0.9511),
    ]

    # Hexagon (regular)
    hexagon_points = [
        (1, 0),
        (0.5, 0.8660),
        (-0.5, 0.8660),
        (-1, 0),
        (-0.5, -0.8660),
        (0.5, -0.8660),
    ]

    # Octagon (regular)
    octagon_points = [
        (0.9239, 0.3827),
        (0.3827, 0.9239),
        (-0.3827, 0.9239),
        (-0.9239, 0.3827),
        (-0.9239, -0.3827),
        (-0.3827, -0.9239),
        (0.3827, -0.9239),
        (0.9239, -0.3827),
    ]

    p = Pentagon.from_coordinates(pentagon_points)
    print("Pentagon →", p.area, p.perimeter)

    h = Hexagon.from_coordinates(hexagon_points)
    print("Hexagon →", h.area, h.perimeter)

    o = Octagon.from_coordinates(octagon_points)
    print("Octagon →", o.area, o.perimeter)


if __name__ == "__main__":
    test()
