from typing import Callable


def apply_to_sum(func: Callable[[int], int], var1: int, var2: int) -> int:
    return func(var1 + var2)


print("1)", apply_to_sum(lambda x: x + 1, 3, 5))


def apply_twice(func: Callable[[int], int], var):
    return func(func(var))


print("2) " + str(apply_twice(lambda x: x + 1, 1)))


def increment(n: int):
    return lambda x: x + n


inc = increment(5)
print("3)", inc(10))
