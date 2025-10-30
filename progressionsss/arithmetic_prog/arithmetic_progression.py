from base_prog.progression import Progression


class ArithmeticProgression(Progression):
    def __init__(self, n, common_difference=1, start=0):
        super().__init__(n, start)
        self.__common_difference = common_difference

    def _advance(self):
        self._current_val += self.__common_difference
