from functools import reduce

pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]
sommme = list(map(lambda x: x[0] + x[1], pairs))
print(sommme)


people = [
    {"name": "Mario", "age": 23},
    {"name": "Daghem", "age": 24},
    {"name": "Andrea", "age": 15},
]

magg = list(filter(lambda y: y["age"] >= 18, people))
print(list(map(lambda x: x["name"], magg)))
