# Scrivi una funzione apply_to_sum, che, presi una funzione fun e
# due valori val1 e val2, applichi fun alla somma di val1 e val2
# (cioè calcoli fun(val1 + val2));
# • Scrivi una funzione apply_twice, che, presi una funzione fun e
# un valore val, applichi fun a val due volte di seguito (cioè
# calcoli fun(fun(val)));
# • Scrivi una funzione incrementer, che, preso un numero n,
# restituisca una funzione che, preso un altro numero x,
# restituisca x + n;

from typing import Callable


def apply_to_sum(fun: Callable[[int, int], int], val1: int, val2: int):
    return fun(val1, val2)


print(apply_to_sum(lambda x, y: x + y, 5, 6))


def apply_twice(fan: Callable[[int], int], val: int):
    return fan(fan(val))


print(apply_twice(lambda val: val**2, 2))


i = int(input("inserisci il primo numero "))


def incrementer(i):
    j = int(input("inserisci il secondo numero "))
    funzione = lambda i, j: i + j
    return funzione(i, j)


print(incrementer(i))
