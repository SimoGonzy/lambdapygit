lista = []

n = int(input("Quanti numeri vuoi inserire? "))

for i in range(n):
    numero = int(input("Inserisci un numero: "))
    lista.append(numero)

somma = sum(lista)
massimo = max(lista)
minimo = min(lista)
media = somma / len(lista)

listanpari = []
for num in lista:
    if num % 2:
        listanpari.append(num)


"per ordinare la listta sia in oprine crescente che decrescente si usa sort"
"decrecente"
lista.sort(reverse=True)
"crescente"
lista.sort(reverse=False)

"verificare se elenento è presente in una lista"
numdacercare = int(input("inserisci il numero da cercare nella lista"))
if numdacercare in lista:
    print("il numero è presente in lista")
else:
    print("NUEMRO NON ORESENTE IN LISTA")


print(f"la lista è formata da : ", lista)
print(f"la somma della lista è : ", somma)
print(f"il numero massimo della lista è : ", massimo)
print(f"il numero minimo della lista è : ", minimo)
print(f"la media della lista è : ", media)
print(f"nueri pari cioè divisibili per due", listanpari)
