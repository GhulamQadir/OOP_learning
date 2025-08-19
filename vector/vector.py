from functools import reduce
from math import sqrt


class Vector:
    def __init__(self, dimension):
        # Private list that stores the actual vector values.
        # By default, it's filled with zeros, e.g., Vector(3) → [0, 0, 0].
        self.__coords = [0] * dimension

    @property
    def coords(self):
        return self.__coords

    def __setitem__(self, index, value):
        # Allows assignment like v1[2] = 7.
        # This internally updates __coords at that index.
        if index < len(self):
            self.__coords[index] = value
        else:
            raise IndexError("The given index is out of range")

    def __getitem__(self, index):
        # Allows element access like v1[0].
        # This makes Vector objects behave like lists for indexing.
        if index < len(self):
            return self.__coords[index]
        else:
            raise IndexError("The given index is out of range")

    def __len__(self):
        # Returns the dimension (length) of the vector.
        # This enables using len(v1) instead of len(v1.__coords).
        return len(self.__coords)

    def _validate_instance_type(self, other_vector):
        # Ensure the other operand is also a Vector before doing operations.
        # This prevents adding Vector with int, list, etc.
        if not isinstance(other_vector, Vector):
            raise TypeError("Operand must be a Vector")

    def _validate_dimension(self, other_vector):
        # Ensure both vectors are of the same dimension.

        # We use len(self) instead of len(self.__coords)
        # because we defined __len__, so 'len(self)' is more flexible
        if len(other_vector) != len(self):
            raise ValueError("The dimensions must match for arithmetic operations")

    def __add__(self, other_vector):
        # Implements vector addition (v1 + v2).
        self._validate_instance_type(other_vector)  # check operand type
        self._validate_dimension(other_vector)  # check matching dimension
        new_vector = Vector(len(self))  # Create new zero vector of same length
        for i in range(len(self)):
            # Add each coordinate one by one.

            # Using self[i] here instead of self.__coords[i]
            # because self[i] automatically calls __getitem__,
            new_vector[i] = self[i] + other_vector[i]
        return new_vector

    def __sub__(self, other_vector):
        # Implements vector subtraction (v1 - v2).
        self._validate_instance_type(other_vector)
        self._validate_dimension(other_vector)
        new_vector = Vector(len(self))
        for i in range(len(self)):
            new_vector[i] = self[i] - other_vector[i]
        return new_vector

    def distance(self, other_vector):
        # Step 1: Compute squared differences using **list comprehension**
        # zip pairs elements from self.__coords and other_vector.coords
        # (y - x) ** 2 calculates the square of the difference for each pair
        squared_list = [
            (y - x) ** 2 for (x, y) in zip(self.__coords, other_vector.coords)
        ]

        # Step 2: Sum all squared differences
        sum_of_list = 0
        for element in squared_list:
            sum_of_list += element

        # Step 3: Take the square root to get distance
        final_distance = sqrt(sum_of_list)

        # Step 4: Round to 3 decimal places and return
        return round(final_distance, 3)

    def magnitude(self):
        # Step 1: Square each coordinate using list comprehension
        # List comprehension creates a new list with squares of all elements in self.__coords
        squared_list = [a**2 for a in self.__coords]

        # Step 2: Sum all squared values
        sum_of_list = 0
        for element in squared_list:
            sum_of_list += element

        # Step 3: Take square root of the sum to get the magnitude (Euclidean norm)
        final_magnitude = sqrt(sum_of_list)

        # Step 4: Round to 3 decimal places and return
        return round(final_magnitude, 3)

    def dot_product(self, other_vector):
        # Step 1: Multiply corresponding elements of the two vectors
        # - zip(self.__coords, other_vector.coords) pairs elements from both vectors
        # - List comprehension [a * b for a, b in ...] calculates the product of each pair
        products_list = [a * b for a, b in zip(self.__coords, other_vector.coords)]

        # Step 2: Sum all the products to get the dot product
        # - reduce(lambda x, y: x + y, products_list) adds elements of the list one by one
        # - The lambda function takes two numbers at a time and returns their sum
        sum_of_products = reduce(lambda x, y: x + y, products_list)
        return sum_of_products

    def __eq__(self, other_vector):
        # Equality operator (==). Returns True if all coordinates match.
        self._validate_instance_type(other_vector)
        return self.__coords == other_vector.coords

    def __ne__(self, other_vector):
        # Not-equal operator (!=).
        self._validate_instance_type(other_vector)
        return self.__coords != other_vector.coords

    def __str__(self):
        # Nicely formats the vector when printed.
        # str(self.__coords) → "[1, 2, 3]" → slice [1:-1] → "1, 2, 3"
        # Final → "(1, 2, 3)".
        return f"({str(self.__coords)[1:-1]})"


v1 = Vector(3)
v1[0] = 1
v1[1] = 2
v1[2] = 3
print(v1.magnitude())
v2 = Vector(3)
v2[0] = 2
v2[1] = 4
v2[2] = 1
distance = v2.distance(v1)
dot_product = v1.dot_product(v2)
print(dot_product)
