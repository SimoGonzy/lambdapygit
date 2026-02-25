"""
Esercizi sulle lambda: Livello 1 ⋆
• Scrivi una lambda function che, preso un numero, ne restiuisca
il quadrato;
• Scrivi una lambda function che, presi due numeri, ne restiuisca
la somma;
• Scrivi una lambda function che, prese due stringhe con un
nome e un cognome, restituisca la stringa con il nome completo
(es. «Mario» e «Rossi» → «Mario Rossi»).
• Scrivi una lambda function che, presa una stringa, restituisca
True se la stringa ha lunghezza pari, False altrimenti;
"""
import os
from functools import reduce

print((lambda x: x**2)(5))
print((lambda x, y: x + y)(2, 3))
print((lambda x, y: str(x) + " " + str(y))("Mario", "Rossi"))
print((lambda x: len(x) % 2 == 0)("Ciao"))

input()#pausa
os.system('clear')


"""
crivi una funzione apply_to_sum, che, presi una funzione fun e
due valori val1 e val2, applichi fun alla somma di val1 e val2
(cioè calcoli fun(val1 + val2));
• Scrivi una funzione apply_twice, che, presi una funzione fun e
un valore val, applichi fun a val due volte di seguito (cioè
calcoli fun(fun(val)));
• Scrivi una funzione incrementer, che, preso un numero n,
restituisca una funzione che, preso un altro numero x,
restituisca x + n;
"""
def apply_to_sum(fun: callable, val1: int, val2: int) -> int:
    return fun(val1 + val2)

print(apply_to_sum(lambda x: x + 2, 2, 3))

#fa 2 + 2 + 2
def apply_twice(fun: callable, val: int) -> int:
    return fun(fun(val))

print(apply_twice(lambda x: x + 2, 2))

def incrementer(n: int) -> callable:
    return lambda x: x + n

print(incrementer(2)(2))

input()#pausa
os.system('clear')
"""
Dato l’elenco nums = [10, 15, 20, 25, 30], estrai solo i
numeri maggiori di 20.
• Dato l’elenco words = ["ciao", "python", "lambda", "hi",
"fun"], ottieni la lista delle lunghezze di ogni parola.
• Dato l’elenco words = ["anna", "bob", "carla", "daniele",
"eve"], estrai solo le parole che iniziano con la lettera “a”.
• Dato l’elenco nums = [2, 3, 5, 7, 11], calcola il prodotto di
tutti i numeri.
"""
nums = [10, 15, 20, 25, 30]
print(list(filter(
    lambda x: x > 20,
    nums
)))

words = ["ciao", "python", "lambda", "hi", "fun"]
print(list(map(
    lambda x: len(x),
    words
)))

words = ["anna", "bob", "carla", "daniele", "eve", "antonio"]
print(list(filter(
    lambda x: x[0] == "a",
    words
)))

nums = [2, 3, 5, 7, 11]
print(reduce(
    lambda x, y: x * y,
    nums
))

input()#pausa
os.system('clear')

"""
Supponiamo di avere una lista di tuple
pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]
Usa la programmazione funzionale per ottenere la lista delle
somme di ogni coppia (i.e. [3, 7, 11, 15]).
Programmazione Funzio
"""
pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(list(map(
    lambda x: x[0] + x[1],
    pairs
)))

print(reduce(
    #     [] (1,2) -> [] + [y[0] + y[1]]
    # [3] + [7] = [3,7] + [11]
    # [3,7,11] + [15]
    lambda x, y: x + [y[0] + y[1]],
    pairs,
    []
))

"""
Supponiamo di avere una lista di dizionari che rappresentano
persone:
people = [
{"name": "Mario", "age": 23},
# ...
]
Usa la programmazione funzionale per estrarre i nominativi
delle persone maggiorenni
"""
people = [
{"name": "Mario", "age": 23},
{"name": "Luigi", "age": 17}]

print(list(map(
    lambda x: x["name"],
    filter(
        lambda x: x["age"] > 18,
        people
    )
)))
input()#pausa
os.system('clear')