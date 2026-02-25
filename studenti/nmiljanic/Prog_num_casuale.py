import random

num = random.randint(1, 10)
numero = 0

while numero != num:
    numero = int(input("Inserisci un numero: "))
    if numero < num:
        print("Troppo basso")
    elif numero > num:
        print("Troppo alto")
    else:
        print("Giusto!")
