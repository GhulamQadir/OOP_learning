class Range:
    def __init__(self, start, stop=None, step=1):
        # ---- Basic argument validation ----
        if step == 0:
            # A zero step would cause an infinite loop / undefined progression.
            raise ValueError("Step cannot be zero")

        if stop == None:
            self.__stop = start

        if (start > stop and step > 0) or (stop > start and step < 0):
            raise IndexError("Invalid range")

        # Starts at -1 so that the first call to __next__() moves it to index 0.
        self.__index = -1
        self.__start = start
        self.__step = step
        self.__stop = stop

        self.__length = (stop - start + step - 1) // step

        if start > stop and step < 0:
            self.__length = (start - stop - step - 1) // step

        if start == stop:
            self.__length = 0

    @property
    def start(self):
        return self.__start

    @property
    def step(self):
        return self.__step

    @property
    def stop(self):
        return self.__stop

    def __len__(self):
        return self.__length

    def __getitem__(self, index):
        if index < 0:
            index += len(self)

        if not (index >= 0 and index < len(self)):
            raise IndexError("Index out of range")

        return self.__start + (index * self.__step)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < len(self) - 1:
            self.__index += 1
            return self.__start + (self.__index * self.__step)
        else:
            raise StopIteration("Limit Reached")

    def __str__(self):
        return f"Range({self.__start}, {self.__stop}, {self.__step})"


r1 = Range(1, 10, 3)
for i in r1:
    print(i)
