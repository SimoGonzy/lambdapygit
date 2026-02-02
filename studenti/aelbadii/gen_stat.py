#//Scrivere un programma che chieda all’utente di inserire una serie
#di numeri e consenta successivamente di:
#• Calcolare massimo e minimo; +10exp
#• Estrarre i numeri pari o i numeri dispari; +10exp
#• Ordinare la lista; +10exp
#• Calcolare moda, media e mediana; +20exp
#• Estrarre i numeri sopra la media; +20exp
#Strutture Dati: Liste, Tuple e Dizionari - Python: da Zero a OOP - Riccardo Sacchetto, B.Sc.

numeri:list[int]=[]

quant=int(input("inserisci quanti numeri vuoi inserire nella lista"))
i:int=0
min:int=9999
max:int=0
rico:int=0
max_count:int=0
media:float=0
mediana:float=0

#riempo la lista
while(i<quant):
 n=int(input("Inserisci un numero"))
 numeri.append(n)
 i=i+1


#cerco max e min
for lang in numeri:
 if(lang<min):
  min=lang
 if(lang>max):
  max=lang
 print(f"Numero minimo: {min}\t" f"Numero massimo: {max}")

#faccio due liste per i pari e per i dispari e le stampo
numeri_pari: list[int] = [ num for num in numeri if num % 2 == 0 ]
print(f"I numeri pari sono {numeri_pari}")
numeri_dispari: list[int] = [ num for num in numeri if num % 2 == 1 ]
print(f"I numeri dispari sono {numeri_dispari}")

#ordino la lista grazie al bubble sort e la stampo ordinata
n = len(numeri)
for i in range(n-1):
  for j in range(n-i-1):
    if numeri[j] > numeri[j+1]:
      numeri[j], numeri[j+1] = numeri[j+1], numeri[j]
print(f"la lista ordinata :{numeri}")

#trovo le ricorrenze se ci sono
for lang in numeri:
 rico=0
 for n in numeri:
  if(n==lang):
   rico=rico+1 
   if rico >= max_count:
        max_count = rico
        moda = numeri[i]
if(max_count==1):
     print("Non ci sono ricorrenze significativi")
else:
    print("La moda è: ",moda)

#Calcolo la media e la stampo
for lang in numeri:
  media=media+lang
media=media/quant
print("La media è:", media)

#trovo la mediana 
if(quant%2==0):
  mediana=(numeri[quant//2]+numeri[(quant//2)-1])/2
elif(quant%2==1):
  mediana=numeri[quant//2]
print("La mediana è:", mediana)

#cerco i numeri sopra la media e gli stampo
print("I numeri sopra la media sono:")
for lang in numeri:
  if(lang>media):
    print(lang)
    





 