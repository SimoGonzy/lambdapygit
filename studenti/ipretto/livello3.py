from functools import reduce

nums = [10, 15, 20, 25, 30]

maggiori_20: list[int] = list(filter(
    lambda x: x > 20,
    nums
))

print(maggiori_20)

words = ["ciao", "python", "lambda", "hi", "fun"]

lunghezza_parole: list[str] = list(map(
    lambda x: len(x),
    words
))

print(lunghezza_parole)

words = ["anna", "bob", "carla", "daniele", "eve"]

inziale_a: list[str] = list(filter(
    lambda x: x[0] == 'a',
    words
))

print(inziale_a)

nums = [2, 3, 5, 7, 11]

prodotto: int = reduce(
    lambda x, y: x * y,
    nums
)

print(prodotto)