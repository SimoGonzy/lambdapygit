def apply_to_sum(var1,var2,fun):
    somma=fun(var1,var2)
    return somma
def apply_twice(var1,fun):
    quadrato=fun(fun(var1))
    return quadrato
def incrementer(n: int):
    return lambda x: x + n

def somma(var1,var2):return var1+var2

def quadrato(var1):return var1*var1



var1=int(input("Inserisci un numero"))
var2=int(input("Inserisci secondo numero"))
somma1=0
quadrato1=0
somma2=0

somma1=apply_to_sum(var1,var2,somma)
print(somma1)
quadrato1=apply_twice(var1,quadrato)
print(quadrato1)
somma2=incrementer(var1)
print(somma2)
inc5 = incrementer(5)
inc10 = incrementer(10)
    
print("inc5(3) =", inc5(3))     
print("inc5(10) =", inc5(10)) 




