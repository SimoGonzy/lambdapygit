from typing import Callable

'''
quadrato= lambda x: x * 2
print(quadrato(5))
'''
'''
quadrato: Callable[[int], int] = lambda x: x * 2
print(quadrato(5))
'''

'''
add = lambda x, y: x + y
print(add(3, 2))

nome = lambda x, y: x + " " + y
print(nome("Giovanni", "Mattino"))

ugual = lambda x: len(x) % 2 == 0
print(ugual("Giovanni"))
'''
'''
apply_to_sum: Callable[[int, int], int] = lambda x, y: x + y
print(apply_to_sum(5, 4))
'''

'''
def apply_to_sum(fun: Callable[[int], int], val1: int, val2: int):
    print(fun(val1 + val2))


def apply_twice(fun: Callable[[int], int], val: int):
    print(fun(fun(val)))


def incrementer(n) -> Callable[[int], int]: 
    return lambda x: n + x

 
var = incrementer(3)
print(var(7))
'''

'''
nums = [10, 15, 20, 25, 30]

maggiori: list[int] = list(filter(
    lambda x: x > 20,
    nums        
    ))

print(maggiori)

print(list(filter(lambda x: x > 20, nums)))
'''

'''
words = ["ciao", "python", "lambda", "hi",
"fun"]

print(list(map(lambda x: len(x), words)))
'''

'''
words = ["anna", "bob", "carla", "daniele",
"eve"]
print(list(filter(lambda x: x[0] == "a", words)))
'''

'''
from functools import reduce

nums = [2, 3, 5, 7, 11]

print(int(reduce(lambda sum, x: sum * x, nums)))
'''

'''
pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]

print(list(map(
        lambda x: x[0] + x[1], pairs
        )))

'''

'''
people = [
    {"name": "Gigio", "age": 22},
    {"name": "Mario", "age": 10},
    {"name": "Toni", "age": 18},
    {"name": "Fulvio", "age": 9},
]

print(list(filter(lambda x: x["age"] >= 18, people)))

'''
