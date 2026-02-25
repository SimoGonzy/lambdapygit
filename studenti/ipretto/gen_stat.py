quant = int(input("Quanti numeri vuoi inserire?: "))
i:int = 0
numeri: list[int] = []

while(i < quant):
    n = int(input("Inserisci il numero: "))
    numeri.append(n)
    i = i+1

n_min:int = 9999
n_max:int = 0
for lang in numeri:
    if(lang < n_min):
        n_min = lang
    if(lang > n_max):
        n_max = lang

print(f"Numero minore: {n_min}" " " f"Numero maggiore: {n_max}")

numeri_pari: list[int] = [num for num in numeri if num % 2 == 0]
numeri_dispari: list[int] = [num for num in numeri if num % 2 == 1]
print(f"Numeri pari: {numeri_pari}")
print(f"Numeri dispari: {numeri_dispari}")

"""n = len(numeri)
for i in range(n-1):
  for j in range(n-i-1):
    if numeri[j] > numeri[j+1]:
      numeri[j], numeri[j+1] = numeri[j+1], numeri[j]"""
numeri.sort()

print(f"Lista ordinata: {numeri}")

mediana: float

if quant % 2 == 1:
    indice_centrale: int = quant // 2
    mediana = numeri[indice_centrale]
    print(f"La mediana è: {mediana}")
    
else:
    
    n1: int = numeri[quant // 2]
    n2: int = numeri[(quant // 2) - 1]        
    ris: float = (n1 + n2) / 2     
    print(f"La mediana è: {ris}")

somma:float = 0
for num in numeri:   
   somma = somma+num

media:float = somma/quant
print(f"La media è {media}")

print("Numeri maggiori della media: ")
for num in numeri:
   if(num>media):
    print(num)
