from functools import reduce


small_numbers = [1, 2, 3, 4, 5]
limit = 3

print(reduce(
    lambda text, x: text + str(x) + " ",
    small_numbers, ""
))
