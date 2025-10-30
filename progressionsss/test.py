from base_prog.progression import Progression
from arithmetic_prog.arithmetic_progression import ArithmeticProgression
from geometric_prog.geometric_progression import GeometricProgression

def test():
    p1 = Progression(5, 2)
    p1.display_progression()

    arith_prog = ArithmeticProgression(6, 4, 7)
    for t in arith_prog:
        print(t)
        
    p1 = GeometricProgression(4, 3, 5)
    p1.display_progression()

    
if __name__ == "__main__":
    test()
