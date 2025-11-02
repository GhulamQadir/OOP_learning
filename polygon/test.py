from triangle import Triangle, EquilateralTriangle, IsoscelesTriangle


def test():
    t = Triangle(2, 1, 2)
    t.area()

    eq = EquilateralTriangle(4)
    print(eq.perimeter())
    print(eq.area())

    isosceles = IsoscelesTriangle(4, 2)
    print(isosceles.perimeter())
    print(isosceles.area())


if __name__ == "__main__":
    test()
