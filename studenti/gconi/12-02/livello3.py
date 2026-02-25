from functools import reduce
from typing import Callable

nums = [10, 15, 20, 25, 30]
print(list(filter(lambda x: x > 20, nums)))

words = ["ciao", "python", "lambda", "hi", "fun"]
print(list(map(lambda x: len(x), words)))

words = ["anna", "bob", "carla", "daniele", "eve"]
print(list(filter(lambda x: x.find("a") == 0, words)))

nums = [2, 3, 5, 7, 11]
print(reduce(lambda x, y: x * y, nums))

pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(list(map(lambda x: x[0] + x[1], pairs)))

people = [
    {"name": "Mario", "age": 23},
    {"name": "Luigi", "age": 25},
    {"name": "Anna", "age": 30},
    {"name": "Giulia", "age": 19},
    {"name": "Francesco", "age": 27},
    {"name": "Elena", "age": 16},
    {"name": "Tommaso", "age": 14},
    {"name": "Sara", "age": 12},
]

print(list(map(lambda x: x["name"], filter(lambda x: x["age"] >= 18, people))))
a = list(filter(lambda x: x["age"] >= 18, people))
for i in range(len(a)):
    print(a[i]["name"])
