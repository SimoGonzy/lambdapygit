from functools import reduce
from typing import Callable


def operazione(num: int, func: Callable[[int], int]) -> int:
    if num % 2 == 0:
        return func(num)
    return num


def square(num: int) -> int:
    return num**2


print(operazione(4, square))
# print(operazione(4, lambda num: num / 2))


def multiply(num: int) -> Callable[[int], int]:
    return lambda val: num * val


bytwo = multiply(2)
print(bytwo(5))

small_numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * x, small_numbers)))

print(list(filter(lambda x: x % 2 == 0, small_numbers)))

small_numbers2 = [1, 2, 3, 4, 5]
limit = 3
print(reduce(lambda sum, x: sum + x, small_numbers2))
print(reduce(lambda text, x: text + str(x) + " ", small_numbers, ""))
