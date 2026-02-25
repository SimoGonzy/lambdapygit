#funzione map e filter e reduce
from functools import reduce

small_numbers =[1, 2, 3, 4, 5]

print(list(map(
    lambda x: x * x,
    small_numbers
)))

print(list(filter(
    lambda x: x % 2 == 0,
    small_numbers
)))

limit = 3

print(list(filter(
    lambda x: x > limit,
    small_numbers
)))

print(reduce(
    lambda sum, x: sum + x,
    small_numbers
))

print(reduce(
    lambda text, x: text + str(x),
    small_numbers, ""
))