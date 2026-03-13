numbers = [1, 2, 3, 4, 5, 6]
squares = list(map(lambda x: x * x, numbers))
print(squares)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# ==============================================================
from functools import reduce
result = reduce(lambda x, y: x * y, numbers)

print(result)