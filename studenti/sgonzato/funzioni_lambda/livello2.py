from typing import Callable

"""
Scrivi una funzione apply_to_sum, che, presi una funzione fun e
due valori val1 e val2, applichi fun alla somma di val1 e val2
(cioè calcoli fun(val1 + val2));
• Scrivi una funzione apply_twice, che, presi una funzione fun e
un valore val, applichi fun a val due volte di seguito (cioè
calcoli fun(fun(val)));
• Scrivi una funzione incrementer, che, preso un numero n,
restituisca una funzione che, preso un altro numero x,
restituisca x + n;
"""

#1
def apply_to_sum(fun: Callable[[int], int], val1: int, val2: int) -> int:
    return fun(val1 + val2)

print("1) " , apply_to_sum(lambda x: x+1, 3, 5))

#2
def apply_twice(fun: Callable[[int], int], val: int) -> int:
    return fun(fun(val))

print("2) " + str(apply_twice(lambda x: x + 1, 1)))

#3
def incrementer(n: int):
    return lambda x: x + n

inc = incrementer(5)
print("3) " + str(inc(10)))