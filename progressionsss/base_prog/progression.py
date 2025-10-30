class Progression:
    def __init__(self, number_of_terms, start=0):
        self._current_val = start
        self._number_of_terms = number_of_terms
        self._current_term = 1

    def _advance(self):
        self._current_val += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_term > self._number_of_terms:
            raise StopIteration()
        else:
            current_val = self._current_val
            self._advance()
            self._current_term += 1
            return current_val

    def display_progression(self):
        print(" ".join(str(next(self)) for _ in range(self._number_of_terms)))
