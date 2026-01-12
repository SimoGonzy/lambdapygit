
listanumeri = []

while True:
    valore = input(
        "inserisci i  numeri che vuoi inserire uno alla volta, (premi stop per uscire)"
    )
    if valore.lower() == "stop":
        break
    listanumeri.append(float(valore))

from collections import Counter  # importa Counter all'inizio del fil
massimo = max(listanumeri)
minimo = min(listanumeri)

print(f"il valore massimo della lista e': {massimo}")
print(f"il valore minimo della lista e' : {minimo} ")

pari = list(filter(lambda x: x % 2 == 0, listanumeri))
dispari = list(filter(lambda x: x % 2 != 0, listanumeri))

print("dispari", dispari)
print("pari", pari)

listaordinata = sorted(
    listanumeri
)  # con sorted ordina la lista e la restituisce ordinata
print("la lista ordinata è. ", listaordinata)

moda = from collections import Counter
conteggio = Counter(listanumeri)
media = sum(listanumeri)/len(listanumeri)


n_ord = sorted(listanumeri)
l = len(n_ord)
mediana = n_ord[l//2] if l % 2 == 1 else (n_ord[l//2 - 1] + n_ord[l//2]) / 2

sopralamedia = list(filter(lambda x: x > media, listanumeri))

print("media", media)
print("moda", moda)
print("mediana", mediana)
