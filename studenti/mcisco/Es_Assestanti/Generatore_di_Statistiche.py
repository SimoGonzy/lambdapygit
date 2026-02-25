"""Generatore di Statistiche
Scrivere un programma che chieda all’utente di inserire una serie
di numeri e consenta successivamente di:
• Calcolare massimo e minimo; +10exp
• Estrarre i numeri pari o i numeri dispari; +10exp
• Ordinare la lista; +10exp
• Calcolare moda, media e mediana; +20exp
• Estrarre i numeri sopra la media; 
"""


import os

#inizializzo la lista vuota per i numeri dell'utente
numeri_utente = []
w = True


os.system('clear')
print("Generatore di Statistiche\n")

while w:
    n = input("Inserisci un numero: ")
    numeri_utente.append(float(n))

    continua = input("Vuoi inserire un altro numero? (s/n): ")  
    if(continua.lower() != 's'):
        w = False
        os.system('clear')
#end while
    
# Calcolo massimo e minimo
massimo = max(numeri_utente)
minimo = min(numeri_utente)
print(f"Massimo: {massimo}\n")
print(f"Minimo: {minimo}\n")

# Estrazione numeri pari e dispari
numeri_pari = [num for num in numeri_utente if num % 2 == 0]    #numeri pari
numeri_dispari = [num for num in numeri_utente if num % 2 != 0]  #numeri dispari
print(f"Numeri Pari: {numeri_pari}\n")
print(f"Numeri Dispari: {numeri_dispari}\n") 

# Ordinamento della lista
numeri_ordinati = sorted(numeri_utente) #ordina in modo crescente
print(f"Numeri Ordinati: {numeri_ordinati}\n")

# Calcolo moda
#prende sola la prima moda che trova 
for num in numeri_ordinati:

    frequenza = numeri_ordinati.count(num) #conta quante volte num appare nella lista

    if frequenza > 1:
        moda = num
        break
    else:
        moda = "Nessuna moda"
print(f"Moda: {moda}\n")

# Calcolo media
media = sum(numeri_utente) / len(numeri_utente)
print(f"Media: {media}\n")

# Calcolo mediana
n = len(numeri_ordinati)
if n % 2 == 0:
    mediana = (numeri_ordinati[(n//2) - 1] + numeri_ordinati[n//2]) / 2   #  // divisione che restituisce un intero quindi tronca i decimali
else:
    mediana = numeri_ordinati[n//2] 
print(f"Mediana: {mediana}\n")

# Estrazione numeri sopra la media
numeri_sopra_media = [num for num in numeri_utente if num > media]
print(f"Numeri sopra la media: {numeri_sopra_media}\n")


