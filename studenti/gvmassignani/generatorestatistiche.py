lista = []


nome = print("Inserisci una serie di numeri separati: ")

while(True):
    numeri = input()
    if (numeri == "fine"):
        break
        
    lista.append(int(numeri))

#ordinare lista
lista.sort()
print(lista)

#massimo e minimo
massimo = max(lista)
minimo = min(lista)

print(f"Il numero massimo è: {massimo}")
print(f"Il numero minimo è: {minimo}")

#pari e dispari
numeri_pari: int = [lang for lang in lista if lang % 2 == 0] 
print(f"I numeri pari sono {numeri_pari}")

numeri_dispari: int = [lang for lang in lista if lang % 2 != 0]
print(f"I numeri dispari sono {numeri_dispari}")

#moda
posizione = 0
posizione_magg= 0
nuova_posiz = 0
m = len(lista) - 1

while(posizione <= m):
    count = lista.count(lista[posizione])
    if (count > posizione_magg):
        posizione_magg = count
        nuova_posiz = lista[posizione]
    posizione += count
print(f"La moda è: {lista[nuova_posiz]}")

#mediana
n = len(lista)
if n % 2 == 0:
    nm1 = (n // 2) -1
    nm2 = (n // 2) 
    mediana = lista[nm1] + lista[nm2]
    print(f"La mediana è: {mediana}")
else: 
    n % 2 != 0
    med = n // 2
    mediana = lista[med]
    print(f"La mediana è: {mediana}")


#media 
totale = sum(lista)
conteggio = len(lista)
media = int = totale/conteggio
print(f"La media è {media}")

#estrazione numeri
estrazione: int = [lang for lang in lista if lang > media] 
print(f"I numeri sopra la media sono {estrazione}")







