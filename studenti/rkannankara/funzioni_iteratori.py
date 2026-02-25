from calendar import Calendar
from functools import reduce

from typing_extensions import Callable

# Livello 1
"""quadrato: Callable[[int], int] = lambda x: x**2
print(quadrato(5))

print((lambda x: x**2)(2))"""

"""somma: Callable[[int, int], int] = lambda x, y: x + y
print(somma(2, 3))"""

"""ncompleto: Callable[[str, str], str] = lambda nome, cognome: nome + " " + cognome
print(ncompleto("Andrea", "Contro"))"""

"""lunghezza: Callable[[str], bool] = lambda parola: len(parola) % 2 == 0
print(lunghezza("ciao"))
print(lunghezza("ITS"))
"""
# Livello 2

"""def quadrato(x: int) -> int:
    return x**2


def apply_to_sum(val1: int, val2: int, fun: Callable[[int], int]) -> int:
    return fun(val1 + val2)


print(apply_to_sum(1, 2, quadrato))"""


"""def quadrato(x: int) -> int:
    return x**2


def apply_twice(val: int, fun: Callable[[int], int]) -> int:
    return fun(fun(val))


print(apply_twice(2, quadrato))"""

"""
def incrementer(n):
    return lambda x: n + x


a = incrementer(5)
print(a(2))
"""

# Livello 3

"""nums = [10, 15, 20, 25, 30]
result: list[int] = list(filter(lambda x: x > 20, nums))

print(result)"""

"""words = ["ciao", "python", "lambda", "hi", "fun"]
result: list = list(map(lambda a: len(a), words))
print(result)"""

"""words = ["anna", "bob", "carla", "daniele", "eve", "andrea"]
result: list = list(filter(lambda x: x[0] == "a", words))
print(result)"""

"""nums = [2, 3, 5, 7, 11]
result: int = reduce(lambda x, y: x * y, nums)
print(result)"""

# Sfida Finale 1

"""pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]
result: list = list(map(lambda x: x[0] + x[1], pairs))
print(result)"""

# Sfida Finale 2

people = [{"name": "Mario", "age": 23}, {"name": "Andrea", "age": 17}]
result: list = list(filter(lambda x: x["age"] >= 18, people))
print(result)
