from functools import reduce

n=int(input("Inserisci il numero"))
n1=int(input("Inserisci il secondo numero"))
#nome=(input("Insersici il tuo nome"))
#cognome=(input("Inserisci il tuo cognome"))
quadrato=(lambda n: n*n)
print(quadrato(n))
somma=(lambda n,n1:n+n1)
print(somma(n,n1))

nome_completo=reduce(lambda x,y: x + y,["Isacco","Pretto"])
print(nome_completo)

pari=(lambda nome_completo:len(nome_completo) % 2==0)
if(pari(nome_completo)==True):
    print("Pari")
else:
    print("Dispari")

