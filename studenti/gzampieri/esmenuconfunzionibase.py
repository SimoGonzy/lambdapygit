menu = {"caffe": 1, "cappuccino": 1.50, "the": 2, "acqua": 0.50}
totale = 0
passadmin = "1234"


def mostra_menu():
    print("\n--- MENU ---")
    for prodotto, prezzo in menu.items():
        print(f"{prodotto} - {prezzo:.2f} €")


# stampa menu iniziale
mostra_menu()

while True:
    scelta = input(
        "\nInserisci il prodotto da ordinare, 'menu' per vedere il menu, "
        "'2' per admin mode, 'stop' per terminare: "
    ).lower()

    if scelta == "stop":
        break

    elif scelta == "menu":
        mostra_menu()

    elif scelta == "2":
        password = input("Inserisci la password per entrare: ")
        if password == passadmin:
            print("Sei entrato nella sezione ADMIN MODE!")
            # esempio minimo admin: cambiare prezzo
            prodotto = input("Nome del prodotto da modificare: ").lower()
            if prodotto in menu:
                nuovo_prezzo = float(
                    input(f"Inserisci il nuovo prezzo per {prodotto}: ")
                )
                menu[prodotto] = nuovo_prezzo
                print(f"Prezzo di {prodotto} aggiornato a {nuovo_prezzo:.2f} €")
            else:
                print("Prodotto non trovato")
        else:
            print("Password errata!")

    elif scelta in menu:
        totale += menu[scelta]
        print(f"Aggiunto {scelta}. Totale attuale: {totale:.2f} €")

    else:
        print("Prodotto non presente nel menu")

print(f"\nTotale finale: {totale:.2f} €")
