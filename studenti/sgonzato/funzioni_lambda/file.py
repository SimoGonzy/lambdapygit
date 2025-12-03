from typing import Callable

def operazione(num: int, func: Callable[[int], int]) -> int:
    if num % 2 == 0:
        return func(num)
    return num

def square(num: int) -> int:
    return num ** 2

print(operazione(4, lambda num: num ** 2))


small_numbers = [1,2,3,4,5]
limit = 3

print(list(map(
    lambda x: x * x,
    small_numbers 
)))

print(list(filter(
    lambda x: x > limit,
    small_numbers 
)))