def apply_to_sum(fun, val1, val2):
    somma=fun(val1, val2)
    return somma

def apply_twice(fun, val1):
    quadrato = fun(val1)
    return quadrato

def incrementer(val1):
    return lambda val2: val2 + val1

def somma(val1,val2): return val1 + val2

def quadrato(val1): return val1 * val1

val1 = int(input("Inserisci il primo numero: "))
val2 = int(input("Inserisci il secondo numero: "))

somma1 = apply_to_sum(somma, val1, val2)
print(somma1)
quadrato1 = apply_twice(quadrato, val1)
print(quadrato1)

add_tre = incrementer(3)
print(f"3 + 7 = {add_tre(7)}")

