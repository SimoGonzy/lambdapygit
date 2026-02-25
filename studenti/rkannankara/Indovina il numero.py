def gioca():
    numero_segreto=7
    tentativi_massimi=3

    print("Indovina il numero")
    print("Il numero è compreso tra 0 e 10")

    for tentativo in range(1, tentativi_massimi +1)
        numero = int(input(f"Tentativo {tentativo}: "))

        if numero < numero_segreto:
            print("Basso!")
        elif numero > numero_segreto:
            print("Alto!")
        else:
             print("Corretto!")
             break
    else:
        print("Partita Terminata.")
        print(f"Il numero segreto era {numero_segreto}")


while True:
     gioca()
     if input("\nVuoi rigiocare? (s/n): ").lower() != 's':
        break
