"""scrivi una lambda function che, preso un numero, ne restiuisca
il quadrato;
• Scrivi una lambda function che, presi due numeri, ne restiuisca
la somma;
• Scrivi una lambda function che, prese due stringhe con un
nome e un cognome, restituisca la stringa con il nome completo
(es. «Mario» e «Rossi» → «Mario Rossi»).
• Scrivi una lambda function che, presa una stringa, restituisca
True se la stringa ha lunghezza pari, False altrimenti;"""
from typing import Callable 
from functools import reduce

print( (lambda x : x * x )(2))
print ((lambda x , y: x + y)(2,5))
print ((lambda nome, cognome : nome + " "+ cognome)("Daghem", "Fanton"))
print((lambda stringa : len(stringa) % 2==0)("Daghem"))
"""Scrivi una funzione apply_to_sum, che, presi una funzione fun e
due valori val1 e val2, applichi fun alla somma di val1 e val2
(cioè calcoli fun(val1 + val2));
• Scrivi una funzione apply_twice, che, presi una funzione fun e
un valore val, applichi fun a val due volte di seguito (cioè
calcoli fun(fun(val)));
• Scrivi una funzione incrementer, che, preso un numero n,
restituisca una funzione che, preso un altro numero x,
restituisca x + n;"""
def apply_to_sum (fun : Callable[[int, int], int],val , val2 ):
    return fun(val, val2)
print(apply_to_sum(lambda x , y: x + y, 2, 5))
def apply_twice (fun : Callable[[int, int], int], val):
    return fun(fun(val))
print(apply_twice(lambda x : x * x, 2))

def incrementer( n):
    x = int(input("Inserisci un numero"))
    funzione = lambda x, n: x + n
    return funzione(x,n)

#print(incrementer(6))

"""Dato l’elenco nums = [10, 15, 20, 25, 30], estrai solo i
numeri maggiori di 20.
• Dato l’elenco words = ["ciao", "python", "lambda", "hi",
"fun"], ottieni la lista delle lunghezze di ogni parola.
• Dato l’elenco words = ["anna", "bob", "carla", "daniele",
"eve"], estrai solo le parole che iniziano con la lettera “a”.
• Dato l’elenco nums = [2, 3, 5, 7, 11], calcola il prodotto di
tutti i numeri"""
nums : list = [10, 15, 20, 25, 30]
print(list(filter(lambda x:x > 20, nums)))
words : list = ["ciao", "python", "lambda", "hi","fun"]
print(list(map(lambda x: len(x), words)))
words2 : list = ["anna", "bob", "carla", "daniele","eve"]
print(list(filter(lambda x : x[0]=="a", words2)))
nums2 : list = [2, 3, 5, 7, 11]
print(reduce(lambda x, y: x * y, nums2))


"""supponiamo di avere una lista di tuple
pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]
Usa la programmazione funzionale per ottenere la lista delle
somme di ogni coppia (i.e. [3, 7, 11, 15])."""
pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]
somme = list(map(lambda x: x[0] + x[1], pairs))
print(somme)
"""upponiamo di avere una lista di dizionari che rappresentano
persone:
people = [
{"name": "Mario", "age": 23},
# ...
]
Usa la programmazione funzionale per estrarre i nominativi
delle persone maggiorenni."""

peaple = [
    {'nome': 'Alice', 'age': 30},
    {'nome': 'Bob', 'age': 25},
    {'nome': 'Charlie', 'age': 35},
    {'nome': 'Diana', 'age': 28},
    {'nome': 'Eva', 'age': 16},       # Minorenne
    {'nome': 'Frank', 'age': 10},     # Minorenne
    {'nome': 'Grace', 'age': 17}      # Minorenne
]
maggiorenni = list(filter(lambda x: x['age']>18, peaple))

print(list(map(lambda x: x["nome"], maggiorenni)))