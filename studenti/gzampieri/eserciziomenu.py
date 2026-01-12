menu = {"caffe": 2, "panino": 3, "the": 1.50}

# Stampa il menu
for prodotto, prezzo in menu.items():
    print(f"Il menu è composto da {prodotto}: {prezzo}€")

totale = 0

# Ciclo per gli ordini
while True:
    scelta = input(
        "Inserisci il prodotto che vuoi prendere (digita 'stop' per fermare): "
    )
    if scelta == "stop":
        break
    if scelta in menu:
        totale += menu[scelta]  # aggiunge il prezzo al totale
        print(f"Hai aggiunto {scelta}. Totale provvisorio: {totale}€")
    else:
        print("Prodotto non presente nel menu.")

# Stampa totale finale
print(f"Il totale da pagare è: {totale}€")
