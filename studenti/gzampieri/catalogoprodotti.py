catalogo = {
    "Coca Cola": {"prezzo": 1.50, "categoria": "bevande"},
    "Iphone 15": {"prezzo": 1200, "categoria": "tecnologia"},
}


def mostra_prodotti():
    print("Il catalogo completo è formato da:")
    for nome, dati in catalogo.items():
        print(f"NOME: {nome}, PREZZO: {dati['prezzo']}, CATEGORIA: {dati['categoria']}")


def aggiungi_prodotto():
    nome = input("Inserisci il nuovo prodotto: ")
    if nome in catalogo:
        print("Il prodotto è già presente.")
    else:
        prezzo = float(input("Inserisci il prezzo: "))
        categoria = input("Inserisci la categoria: ")
        catalogo[nome] = {"prezzo": prezzo, "categoria": categoria}
        print(f"Prodotto '{nome}' aggiunto con successo!")


def cerca_prodotto():
    nome = input("Inserisci il nome del prodotto da cercare: ")
    if nome in catalogo:
        dati = catalogo[nome]
        print(f"Trovato! PREZZO: {dati['prezzo']}, CATEGORIA: {dati['categoria']}")
    else:
        print("Prodotto non trovato.")


def rimuovi_prodotto():
    nome = input("Inserisci il nome del prodotto da rimuovere: ")
    if nome in catalogo:
        catalogo.pop(nome)
        print(f"Prodotto '{nome}' rimosso con successo!")
    else:
        print("Prodotto non trovato.")


def filtra_categoria():
    categoria = input("Inserisci la categoria da cercare: ")
    trovati = False
    for nome, dati in catalogo.items():
        if dati["categoria"] == categoria:
            print(
                f"NOME: {nome}, PREZZO: {dati['prezzo']}, CATEGORIA: {dati['categoria']}"
            )
            trovati = True
    if not trovati:
        print("Nessun prodotto trovato per questa categoria.")


def filtra_prezzo():
    prezzo = float(input("Inserisci il prezzo da cercare: "))
    trovati = False
    for nome, dati in catalogo.items():
        if dati["prezzo"] == prezzo:
            print(
                f"NOME: {nome}, PREZZO: {dati['prezzo']}, CATEGORIA: {dati['categoria']}"
            )
            trovati = True
    if not trovati:
        print("Nessun prodotto ha questo prezzo.")


def filtraprodottopiucostoso():
    if not catalogo:
        print("Il catalogo è vuoto.")
        return

    # inizializza con un valore minimo
    nome_max = None
    prezzo_max = -1

    for nome, dati in catalogo.items():
        if dati["prezzo"] > prezzo_max:
            prezzo_max = dati["prezzo"]
            nome_max = nome

    print(f"Il prodotto più costoso è '{nome_max}' con prezzo {prezzo_max}€")


while True:
    print("\n--- MENU ---")
    print("1 - Mostra catalogo")
    print("2 - Aggiungi un prodotto")
    print("3 - Cerca un prodotto")
    print("4 - Cancella un prodotto")
    print("5 - Filtra per categoria")
    print("6 - Filtra per prezzo")
    print("stop - Uscire")

    scelta = input("Inserisci l'operazione: ")

    if scelta == "stop":
        print("Programma terminato.")
        break

    elif scelta == "1":
        mostra_prodotti()

    elif scelta == "2":
        aggiungi_prodotto()

    elif scelta == "3":
        cerca_prodotto()

    elif scelta == "4":
        rimuovi_prodotto()

    elif scelta == "5":
        filtra_categoria()

    elif scelta == "6":
        filtra_prezzo()

    else:
        print("Scelta non valida. Riprova.")
