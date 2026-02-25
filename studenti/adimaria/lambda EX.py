"""Livello 1"""

quadrato = lambda x: x ** x

somma = lambda x, y: x + y

nome_completo = lambda nome, cognome: f"{nome} {cognome}"

e_pari= lambda s: len(s) % 2 == 0

"""Livello 2"""

def apply_to_sum(fun, val1, val2):
    return fun(val1 + val2)

def apply_twice(fun, val):
     return fun(fun(val))

def incrementer(n):
    def inner_function(x):
         return x + n
    return inner_function

"""Livello 3"""

filtro_piu_di_venti = list(filter(lambda x: x > 20, nums))

lunghezza_elementi_lista = list(map(lambda word: len(word), words))

filtro_comincia_con_a = list(filter(lambda word: word.startswith('a'), words))