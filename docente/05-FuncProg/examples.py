# 05 - Programmazione Funzionale e Iteratori
# Esempi tratti dalla dispensa


from typing import Callable
from functools import reduce


# Esempio 1: Definizione e utilizzo di una lambda function
# In questo esempio definiamo una lambda function che calcola il perimetro
# di un rettangolo dato la lunghezza e la larghezza. La lambda function viene
# assegnata alla variabile 'perimeter' e poi utilizzata per calcolare il
# perimetro di un rettangolo con lunghezza 5 e larghezza 10.

perimeter: Callable[[int, int], int] = lambda length, width: 2 * (length + width)
print(perimeter(5, 10))  # → 30


# Esempio 2: Utilizzo immediato di una lambda function
# Qui mostriamo come utilizzare una lambda function senza assegnarla
# a una variabile. La lambda function viene definita e chiamata
# immediatamente per calcolare il perimetro di un rettangolo
# con lunghezza 5 e larghezza 10.

print((lambda length, width: 2 * (length + width))(5, 10))


# Esempio 3: Funzioni di ordine superiore (funzionali)
# In questo esempio definiamo due funzioni, 'quadrato' e 'cubo',
# che calcolano rispettivamente il quadrato e il cubo di un numero.
# La funzione 'risultati_oltre_20' accetta una lista di numeri
# e una funzione come argomenti. Essa applica la funzione a ciascun
# numero pari nella lista e restituisce una nuova lista contenente
# solo i risultati maggiori di 20.

def quadrato(val: int) -> int:
    return val * val

def cubo(val: int) -> int:
    return val * val * val

def risultati_oltre_20(
    numbers: list[int],
    func: Callable[[int], int]
) -> list[int]:
    result: list[int] = []
    for x in numbers:
        if x % 2 == 0:
            y: int = func(x)
            if y > 20:
                result.append(y)
    return result

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(risultati_oltre_20(numbers, quadrato))
print(risultati_oltre_20(numbers, cubo))

print(risultati_oltre_20(
    numbers,
    lambda val: val * val
))
print(risultati_oltre_20(
    numbers,
    lambda val: val * val * val
))


# Esempio 4: Utilizzo di map() con una lambda function
# In questo esempio utilizziamo la funzione built-in 'map()' per
# applicare una lambda function che calcola il quadrato di un numero
# a ciascun elemento di una lista di numeri. Il risultato viene convertito
# in una lista e stampato.

small_numbers: list[int] = [1, 2, 3, 4, 5]
squared_numbers: list[int] = list(map(
    lambda x: x * x,
    small_numbers
))
print(squared_numbers)


# Esempio 5: Utilizzo di filter() con una lambda function
# Qui utilizziamo la funzione built-in 'filter()' per filtrare
# una lista di numeri, mantenendo solo quelli pari. La lambda function
# verifica se un numero è pari controllando se il resto della divisione
# per 2 è uguale a zero. Il risultato viene convertito in una lista
# e stampato.

even_numbers: list[int] = list(filter(
    lambda x: x % 2 == 0,
    numbers
))
print(even_numbers)


# Esempio 6: Utilizzo di reduce() con una lambda function
# In questo esempio utilizziamo la funzione 'reduce()' dal modulo
# 'functools' (vedi import in cima al file) per calcolare la somma
# di tutti gli elementi in una lista di numeri.

total: int = reduce(
    lambda x, y: x + y,
    small_numbers
)
print(total)
