"""s = lambda x: x * x
print(s(2))

y = lambda x, y: x + y
print(y(1, 2))

nome_cognome = lambda x, y: x + " " + y
print(nome_cognome("nome", "cognome"))

pari_dispari = lambda x: len(x) % 2 == 0
print(pari_dispari("Ciaoo"))"""

from typing import Callable

"""def apply_to_sum(fun: Callable[[int], int], val1: int, val2: int):
    print(fun(val1 + val2))

def apply_twice(fun: Callable[[int], int], val: int):
    print(fun(fun(val)))

def incrementer(n: int) -> Callable[[int], int]:
    return lambda num: n + num
"""

"""nums = [10, 15, 20, 25, 30]
def maggiori(nums: list[int]) -> list[int]:
    listamaggiori = []
    for x in nums:
        if x > 20:
            listamaggiori.append(x)
    return listamaggiori
print(maggiori(nums))
print(list(filter(lambda x: x > 20, nums)))

words = ["ciao", "python", "lambda", "hi", "fun"]
print(list(map(lambda x: len(x), words)))

words1 = ["anna", "bob", "carla", "daniele", "eve", "amario"]
print(list(filter(lambda x: x[0] == "a", words1)))

from functools import reduce
nums1 = [2, 3, 5, 7, 11]
print(int(reduce(lambda x, y: x * y, nums1)))"""

"""pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]
x = 0
def sommatore(fun: Callable[[int, int], int], lista_tuple: list[tuple]) -> list[int]:
    lista_somme: list[int] = []
    for x in lista_tuple:
        lista_somme.append(fun(x[0], x[1]))
    return lista_somme

print(sommatore(lambda x, y: x + y, pairs))
print(list(map(lambda x: x[0] + x[1], pairs)))"""

"""people = [
    {"name": "Mario", "age": 23},
    {"name": "Astolfo", "age": 3},
    {"name": "Carlo", "age": 942}
]

print(list(filter(lambda x: x["age"] >= 18, people)))"""