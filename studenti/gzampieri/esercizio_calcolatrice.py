# creazione contenitore chiamato nuemro  e imput
numeri=[]

while true:

n=input("INSERICI QUANTI NUMERI VUOI COMPRENDERE")
if n.lower()== "stop"
break

numeri.append(float(n))
print("i numeri che hai inserito sono", numeri)

# calcola media,massimo,minimo


media=sum(numeri)/len(numeri)
massimo=max(numeri)
minimo=min(numeri)

print("la media e'", media)
print("il massimo e'", max)
print("il minimo e'", min)

#crea delle liste appunto pari e dispari per estarre numeri pari e dispari

pari=[x for x in numeri if int(x) % 2 == 0]
dispari=[x for x in numeri if int(x) % 2 != 0]

print("Numeri pari:", pari)
print("Numeri dispari:", dispari)

# per ordinare la lista e visualizzare la lista ordinata
ordinata = sorted(nuemri)
print("lista ordine crescente",ordinata)

sopra_media = [x for x in numeri if x > media]
print("Numeri sopra la media:", sopra_media)
