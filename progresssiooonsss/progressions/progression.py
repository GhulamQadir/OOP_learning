class Progression:
    def __init__(self, n, start=0):
        self.__current_val = start
        self.__number_of_terms = n
        self.__current_term = 1

    @property
    def number_of_terms(self):
        return self.__number_of_terms

    @number_of_terms.setter
    def number_of_terms(self, n):
        self.__number_of_terms = n

    @property
    def current_val(self):
        return self.__current_val

    @current_val.setter
    def current_val(self, new_val):
        self.__current_val = new_val

    def _advance(self):
        self.__current_val += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_term > self.__number_of_terms:
            raise StopIteration()
        else:
            current_val = self.__current_val
            self._advance()
            self.__current_term += 1
            return current_val


# prog = Progression(4,2)
# print(next(prog))
# print(next(prog))
# print(next(prog))
# print(next(prog))
# print(next(prog))
