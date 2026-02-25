import random

numero_segreto = random.randint(1, 100)

while True:
    tentativo = int(input("Indovina il numero (tra 1 e 10): "))

    if tentativo < numero_segreto:
        print("Troppo basso Riprova")
    elif tentativo > numero_segreto:
        print("Troppo alto  Riprova")
    else:
        print(" Hai indovinato")
        break
