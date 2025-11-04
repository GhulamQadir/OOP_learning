from triangle import Triangle, EquilateralTriangle, IsoscelesTriangle
from quadrilateral import Square, Rectangle
from regular_polygons import RegularPolygon, Pentagon, Hexagon, Octagon


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

    reg_polygon = RegularPolygon(5, 7)
    print(
        f"RegularPolygon --> Area: {reg_polygon.area}, Perimeter: {reg_polygon.perimeter}\n"
    )

    p = Pentagon(4)
    print(f"Pentagon --> Area: {p.area}, Perimeter: {p.perimeter}")
    print(p)

    h = Hexagon(7)
    print(f"\nHexagon --> Area: {h.area}, Perimeter: {h.perimeter}")
    print(h)

    o = Octagon(11)
    print(f"\nOctagon --> Area: {o.area}, Perimeter: {o.perimeter}")
    print(o)


if __name__ == "__main__":
    test()
