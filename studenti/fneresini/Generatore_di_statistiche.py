con = True
mylist = []
i = 0
mylistmoda = []
maggiore = 0
somma = 0
media = 0
mediana = 0.0
mylistmaggioremedia = []

print("Inserisci un numero e premi INVIO")
print("Per uscire scrivi 'f' e premi INVIO")

while(True):
    numero = input()
    if (numero == "f"):
        break
    mylist.append(int(numero))

"""#calcola massimo
mylist.sort(key=int, reverse=True)
print(mylist[0])

#calcola minimo
mylist.sort(key=int, reverse=False)
print(mylist[0])

#estrai pari
mylistpari = [num for num in range(0, len(mylist)) if num % 2 == 0]
print(mylistpari)

#estrai dispari
mylistdispari = [num for num in range(0, len(mylist)) if num % 2 != 0]
print(mylistdispari)

#ordina lista
mylist.sort(key=int, reverse=True)
mylist.sort(key=int, reverse=False)

#calcola moda
for i in range(len(mylist)):
    if(mylist.count(mylist[i]) > maggiore):
        maggiore = mylist.count(mylist[i])
        mylistmoda = [maggiore, mylist[i]]
print(mylistmoda[1])

#calcola media
for i in range(len(mylist)):
    somma = somma + mylist[i]
media = somma / len(mylist)
print(media)

#calcola mediana
sorted(mylist, key = int, reverse = False)
if (len(mylist) % 2) == False:
    #media valore in mezzo
    centros = int(((len(mylist) - 1) / 2))
    centrod = int((len(mylist) / 2))
    mediana = (mylist[centros] + mylist[centrod]) / 2
    print(mediana)
    print("pari")
else:
    #valori in mezzo
    ciao = len(mylist)
    centro = int(ciao / 2)
    print(mylist[centro])
    print("dispari")

#estrai numeri sopra la media
for i in range(len(mylist)):
    somma = somma + mylist[i]
media = somma / len(mylist)

for i in range(len(mylist)):
    if mylist[i] > media:
        mylistmaggioremedia.append(mylist[i])
print(mylistmaggioremedia)"""