n = int(input("Quanti numeri vuoi inserire? "))

numeri_input = []


for i in range(n):
    num = int(input(f"Inserisci il numero {i + 1}: "))
    numeri_input.append(num)


print("La lista dei numeri inseriti è:", numeri_input)

# massimo e minimo
massimo = max(numeri_input)
minimo = min(numeri_input)
print(f"Massimo: {massimo}")
print(f"Minimo: {minimo}")

# numeri pari
numeri_pari: list[int] = [num for num in numeri_input if num % 2 == 0]
print(numeri_pari)

# numeri dispari
numeri_dispari: list[int] = [num for num in numeri_input if num % 2 == 1]
print(numeri_dispari)

# ordinamento della lista
numeri_input.sort()
print(f"Lista ordinata: {numeri_input}")

# calcolo media
somma_elementi = sum(numeri_input)
numero_elementi = len(numeri_input)
media = somma_elementi / numero_elementi
print(f"La media della lista è: {media}")

# calcolo moda
for num in numeri_input:
    frequenza = numeri_input.count(num)
    if frequenza > 1
    moda = num
    break
    else


# calcolo mediana
centro = numero_elementi // 2
if numero_elementi % 2 == 1:
    mediana = numeri_input[centro]
else:
    mediana = (numeri_input[centro - 1] + numeri_input[centro]) / 2
print(f"La mediana della lista è: {mediana}")

# Estrarre i numeri sopra la media
numeri_sopra_alla_media: list[float] = [num for num in numeri_input if num > media]
print(numeri_sopra_alla_media)
