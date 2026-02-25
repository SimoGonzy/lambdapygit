from functools import reduce
from typing import Callable

print((lambda x: x**2)(2))

somma: Callable[[int, int], int] = lambda x, y: x + y

print(somma(1, 2))

print((lambda nome, cognome: nome + " " + cognome)("Matteo", "Lovato"))

print((lambda stringa: len(stringa) % 2 == 0)("ciao"))


def apply_to_sum(fun: Callable[[int], int], val1: int, val2: int):
    return fun(val1 + val2)


print(apply_to_sum(lambda x: 2 * x, 5, 4))


def apply_twice(fun: Callable[[int], int], val: int):
    return fun(fun(val))


print(apply_twice(lambda x: x * 2, 3))


def incrementer(n: int) -> Callable[[int], int]:
    return lambda x: x + n


add_two = incrementer(2)

print(add_two(19))

print(incrementer(2)(19))

print("----------------------")

nums = [10, 15, 20, 25, 30]

print(list(filter(lambda x: x > 20, nums)))

words = ["ciao", "python", "lambda", "hi", "fun"]

print(list(map(lambda x: len(x), words)))

words2 = ["anna", "bob", "carla", "daniele", "eve"]

print(list(filter(lambda x: x[0] == "a", words2)))

nums2 = [2, 3, 5, 7, 11]

print(reduce(lambda temp, x: temp * x, nums2))

pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]

print(list(map(lambda x: x[0] + x[1], pairs)))

print(reduce(lambda temp, x: temp + [x[0] + x[1]], pairs, []))

people = [
    {"name": "Mario", "age": 23},
    {"name": "Matteo", "age": 27},
    {"name": "Luca", "age": 17},
    {"name": "Stefano", "age": 16},
    {"name": "PRova", "age": 18},
]

print(
    list(map(lambda x: x["name"], list(filter(lambda x: int(x["age"]) >= 18, people))))
)


def my_map(fun, list):
    temp = []
    for x in list:
        temp.append(fun(x))
    return temp


def my_filter(fun, list):
    temp = []
    for x in list:
        if fun(x):
            temp.append(x)
    return temp


def my_reduce(fun, list):
    val1 = list[0]
    list.remove(list[0])

    for x in list:
        val1 = fun(val1, x)
    return val1


print(my_map(lambda x: x * 2, [0, 1, 2, 3]))
print(my_filter(lambda x: x >= 2, [0, 1, 2, 3]))
print(my_reduce(lambda x, y: x * y, [1, 2, 3, 4]))
