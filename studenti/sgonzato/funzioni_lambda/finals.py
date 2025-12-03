"""
Supponiamo di avere una lista di tuple
pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]
Usa la programmazione funzionale per ottenere la lista delle
somme di ogni coppia (i.e. [3, 7, 11, 15]).

Supponiamo di avere una lista di dizionari che rappresentano
persone:
people = [
{"name": "Mario", "age": 23},
# ...
]
Usa la programmazione funzionale per estrarre i nominativi
delle persone maggiorenni
"""

#1
pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]
somme = list(map(lambda x: x[0] + x[1], pairs))
print("1) Somme di ogni coppia: " + str(somme))

#2
people = [
    {"name": "Mario", "age": 23},
    {"name": "Luigi", "age": 17},
    {"name": "Anna", "age": 30},
    {"name": "Sara", "age": 15}
]

maggiorenni = list(map(
    lambda x: x["name"], filter(lambda x: x["age"] >= 18, people)
))

print("2) Nominativi delle persone maggiorenni: " + str(maggiorenni))