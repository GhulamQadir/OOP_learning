from progression import Progression


class ArithmeticProgression(Progression):
    def __init__(self, n, common_diff=1, start=0):
        super().__init__(n, start)
        self.__common_diff = common_diff
        self.__current_term = 1

    def _advance(self):
        self.current_val += self.__common_diff

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_term > self.number_of_terms:
            raise StopIteration()
        else:
            current_val = self.current_val
            self._advance()
            self.__current_term += 1
            return current_val


arith_prog = ArithmeticProgression(5, 3, 7)

print(next(arith_prog))
print(next(arith_prog))
print(next(arith_prog))
print(next(arith_prog))
print(next(arith_prog))
print(next(arith_prog))
