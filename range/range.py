class Range:
    def __init__(self, start, stop=None, step=1):
        """
        Custom implementation of Python's built-in range.
        Supports iteration, indexing, negative steps, and validation.
        """
        # Validate the inputs and calculate start, stop, length
        range_validation = self._validate_range(start, stop, step)

        # Save the validated values in private attributes
        self.__start = range_validation[0]  # First element in the sequence
        self.__stop = range_validation[1]  # Endpoint (exclusive)
        self.__step = step  # Step size (can be negative)
        self.__length = range_validation[2]  # Number of elements in the sequence
        self.__index = -1  # Internal counter for iteration

    def _validate_range(self, start, stop, step):
        """
        Validates the given arguments and computes the effective start, stop,
        and length of the sequence.

        Rules:
        - Step cannot be zero
        - If only one argument is provided → it becomes 'stop', and start defaults to 0
        - The direction of step must move towards stop
        - Length is calculated using integer arithmetic trick
        """

        local_start = start
        local_stop = stop
        local_length = 0

        # If only one argument is given, treat it as stop and set start = 0
        if stop is None:
            local_stop = start
            local_start = 0
            start, stop = local_start, local_stop

        # Ensure all inputs are integers (same as built-in range)
        if not all(isinstance(x, int) for x in (start, stop, step)):
            raise TypeError("The parameters of range must be of type int")

        # Step cannot be zero
        if step == 0:
            raise ValueError("Step cannot be zero")

        # Direction check:
        # Example: start=5, stop=10, step=-1 → invalid
        if (start > stop and step > 0) or (start < stop and step < 0):
            raise ValueError("Invalid range")

        # If start == stop → sequence is empty
        if start == stop:
            local_length = 0

        # Case 1: negative step, counting backwards
        elif start > stop and step < 0:
            local_length = (start - stop + abs(step) - 1) // abs(step)

        # Case 2: positive step, counting forwards
        else:
            local_length = (stop - start + step - 1) // step

        return local_start, local_stop, local_length

    # Properties to expose start, stop, and step
    @property
    def start(self):
        """Return the starting value of the range."""
        return self.__start

    @property
    def step(self):
        """Return the step value of the range."""
        return self.__step

    @property
    def stop(self):
        """Return the stopping value (exclusive) of the range."""
        return self.__stop

    # Length of the sequence
    def __len__(self):
        """Return the total number of elements in the range."""
        return self.__length

    # Indexing support
    def __getitem__(self, index):
        """
        Returns the element at the given index.
        Supports negative indexing like Python's range.
        """
        if index < 0:  # Adjust for negative indices
            index += len(self)
        if not (index >= 0 and index < len(self)):
            raise IndexError("Index out of range")

        return self.__start + (index * self.__step)

    # Iteration protocol
    def __iter__(self):
        """Return the iterator object (self)."""
        return self

    def __next__(self):
        """
        Returns the next element in the sequence.
        Raises StopIteration when the end is reached.
        """
        if self.__index < len(self) - 1:
            self.__index += 1
            return self.__start + (self.__index * self.__step)
        else:
            raise StopIteration("Limit Reached")

    # String representation
    def __str__(self):
        return f"Range({self.__start}, {self.__stop}, {self.__step})"


r1 = Range(10, 4, -3)
# print(r1[-3])
for i in r1:
    print(i)
