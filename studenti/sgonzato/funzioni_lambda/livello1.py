from typing import Callable

"""
Scrivi una lambda function che, preso un numero, ne restiuisca
il quadrato;
• Scrivi una lambda function che, presi due numeri, ne restiuisca
la somma;
• Scrivi una lambda function che, prese due stringhe con un
nome e un cognome, restituisca la stringa con il nome completo
(es. «Mario» e «Rossi» → «Mario Rossi»).
• Scrivi una lambda function che, presa una stringa, restituisca
True se la stringa ha lunghezza pari, False altrimenti;
"""

#1
a = lambda x: x**2
x = int(input("1) Inserisci un numero: "))
print(a(x))

#2
stringa = lambda s1, s2: str(s1) + " " + str(s2)
nome = input("\n2) Inserisci il nome: ")
cognome = input("\n Inserisci il cognome: ")
print(stringa(nome, cognome))

#3
pari = lambda s1: len(s1) % 2 == 0
str = input("\n3) Inserisci una stringa: ")
print(pari(str))