n = int(input("Inserisci il numero: "))
quadrato=(lambda x: x * x)
print(quadrato(n))

n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))
somma = (lambda n1,n2: n1 + n2)
print(somma(n1,n2))

nome = input("Inserisci il nome: ")
cognome = input("Inserisci il cognome: ")
nome_completo = lambda nome, cognome: f"{nome} {cognome}"
print(nome_completo(nome, cognome))

st = input("Inserisci una stringa: ")
pari = (lambda st: len(st) % 2 == 0)
if pari(st) == True:
    print("Pari")
elif pari(st) == False:
    print("Dispari")
