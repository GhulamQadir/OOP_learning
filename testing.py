# a = 5
## b = 5
# b = a
# print(a is b)
# print(b)
# b=9
# print(a)
# print(b)
# print(a is b)

import copy

a = [1, [2,1], 3, 4]
b = copy.copy(a)
# b[1] = [8]
# print(a)
# print(b)


b[1][1] = [8]
print(a)
print(b)
