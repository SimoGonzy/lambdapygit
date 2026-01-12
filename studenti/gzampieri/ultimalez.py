punto = 0
continua = "si"

while continua == "si":
    importo = int(input("Inserisci importo: "))

    valore_manopola = importo % 100

    print(f"Il puntatore della manopola è su: {valore_manopola}")

    if valore_manopola == 0:
        punto += 1
        print("Hai guadagnato 1 punto!")
    else:
        print("Nessun punto assegnato.")

    continua = input("Vuoi inserire un altro importo? digita si: ")

print(f"Punteggio totale: {punto}")
