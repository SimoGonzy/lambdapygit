catalogo = {
    "Coca Cola": {"prezzo": 1.50, "categoria": "bevande"},
    "Iphone 15": {"prezzo": 1200, "categoria": "tecnologia"},
}

while True:
    print("\n--- MENU ---")
    print("1 - Mostra catalogo")
    print("2 - Aggiungi un prodotto")
    print("3 - Cerca un prodotto")
    print("4 - Cancella un prodotto")
    print("5 - Filtra prodotti")
    print("6 - Prodotto più costoso/economico")
    print("stop - Uscire")

    scelta = input("Inserisci l'operazione da effettuare: ")

    if scelta == "stop":
        print("Programma terminato.")
        break

    # 1 - Mostra catalogo
    if scelta == "1":
        for nome, dati in catalogo.items():
            print(
                f"{nome} - Prezzo: {dati['prezzo']} € - Categoria: {dati['categoria']}"
            )

    # 2 - Aggiungi prodotto
    elif scelta == "2":
        nome = input("Inserisci il nome del prodotto: ")
        prezzo = float(input("Inserisci il prezzo: "))
        categoria = input("Inserisci la categoria: ")
        catalogo[nome] = {"prezzo": prezzo, "categoria": categoria}
        print(f"Hai aggiunto {nome}.")

    # 3 - Cerca prodotto
    elif scelta == "3":
        nome = input("Inserisci il nome del prodotto da cercare: ")
        if nome in catalogo:
            p = catalogo[nome]
            print("Prodotto trovato:")
            print("Nome:", nome)
            print("Prezzo:", p["prezzo"])
            print("Categoria:", p["categoria"])
        else:
            print("Prodotto non trovato.")

    # 4 - Cancella prodotto
    elif scelta == "4":
        prod = input("Inserisci il prodotto da cancellare: ")
        if prod in catalogo:
            catalogo.pop(prod)
            print(f"Hai rimosso {prod}.")
        else:
            print("Prodotto non trovato.")

    # 5 - FILTRI PER PREZZO O CATEGORIA
    elif scelta == "5":
        print("a) Filtra per categoria")
        print("b) Filtra per prezzo massimo")
        print("c) Filtra per prezzo minimo")

        filtro = input("Scegli un'opzione: ")

        if filtro == "a":
            cat = input("Inserisci la categoria: ")
            trovati = [n for n, d in catalogo.items() if d["categoria"] == cat]
            if trovati:
                print("Prodotti trovati:", trovati)
            else:
                print("Nessun prodotto in questa categoria.")

        elif filtro == "b":
            maxp = float(input("Inserisci il prezzo massimo: "))
            trovati = [n for n, d in catalogo.items() if d["prezzo"] <= maxp]
            if trovati:
                print("Prodotti con prezzo <= al massimo:", trovati)
            else:
                print("Nessun prodotto sotto questo prezzo.")

        elif filtro == "c":
            minp = float(input("Inserisci il prezzo minimo: "))
            trovati = [n for n, d in catalogo.items() if d["prezzo"] >= minp]
            if trovati:
                print("Prodotti con prezzo >= al minimo:", trovati)
            else:
                print("Nessun prodotto sopra questo prezzo.")

    # 6 - PRODOTTO PIÙ COSTOSO / PIÙ ECONOMICO
    elif scelta == "6":
        if catalogo:
            # più costoso
            max_prod = max(catalogo.items(), key=lambda x: x[1]["prezzo"])
            # più economico
            min_prod = min(catalogo.items(), key=lambda x: x[1]["prezzo"])

            print(f"Prodotto più costoso: {max_prod[0]} - {max_prod[1]['prezzo']}€")
            print(f"Prodotto più economico: {min_prod[0]} - {min_prod[1]['prezzo']}€")
        else:
            print("Catalogo vuoto.")
    else:
        print("Scelta non valida.")
