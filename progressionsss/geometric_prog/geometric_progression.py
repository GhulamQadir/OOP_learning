from base_prog.progression import Progression


class GeometricProgression(Progression):
    def __init__(self, n, common_ratio, start):
        super().__init__(n, start)
        self.__common_ratio = common_ratio

    def _advance(self):
        self._current_val *= self.__common_ratio
